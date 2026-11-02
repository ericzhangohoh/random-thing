#!/usr/bin/env python3
"""Exhaustive mathematical verification of a synthetic teaching fixture only.

Standard library only. No Claude session, real booking, empirical validation,
or target-scale solver is exercised. Run from any directory; default artifacts
are next to this file. The manifest hashes the exact input, source and result.
"""

import argparse
import hashlib
import itertools
import json
import platform
import sys
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def instance(data, scenario):
    chosen_ids = scenario.get("request_ids")
    requests = [r for r in data["requests_in_booking_order"]
                if chosen_ids is None or r["id"] in chosen_ids]
    return {
        "requests": requests,
        "camps": data["camps"],
        "length": data["river_length_miles"],
        "limit": scenario.get("daily_limit_miles", data["daily_limit_miles"]),
        "horizon": data["horizon_days"],
        "closed": {tuple(slot) for slot in scenario.get("closed_slots", [])},
        "quota": scenario.get("minimum_long_accepted", 0),
    }


def routes_for(request, inst):
    """Enumerate every strictly downstream camp sequence of the required length."""
    n = request["trip_days"] - 1
    routes = []
    ordered_camps = sorted(inst["camps"], key=lambda c: c["position_miles"])
    for camps in itertools.combinations(ordered_camps, n):
        positions = [0] + [c["position_miles"] for c in camps] + [inst["length"]]
        if any(not 0 < b - a <= inst["limit"] for a, b in zip(positions, positions[1:])):
            continue
        slots = tuple((c["id"], request["launch_day"] + k) for k, c in enumerate(camps))
        if any(slot in inst["closed"] for slot in slots):
            continue
        routes.append(slots)
    # Prefer even daily progress, then alphabetical camp IDs. This is only
    # the baseline's route tie-breaker, not a new optimization objective.
    positions_by_id = {c["id"]: c["position_miles"] for c in inst["camps"]}
    ideal = inst["length"] / request["trip_days"]
    def route_key(route):
        positions = [0] + [positions_by_id[c] for c, _ in route] + [inst["length"]]
        return (sum((b - a - ideal) ** 2 for a, b in zip(positions, positions[1:])), route)
    return sorted(routes, key=route_key)


def verify(schedule, inst):
    """Inspect output directly; do not call the generator or trust its feasibility."""
    issues, used = [], set()
    requests = {r["id"]: r for r in inst["requests"]}
    positions = {c["id"]: c["position_miles"] for c in inst["camps"]}
    for rid, route in schedule.items():
        if rid not in requests:
            issues.append(f"Unknown request: {rid}")
            continue
        request = requests[rid]
        expected_nights = list(range(request["launch_day"],
                                     request["launch_day"] + request["trip_days"] - 1))
        if [night for _, night in route] != expected_nights:
            issues.append(f"Wrong night sequence: {rid}")
        if request["launch_day"] < 1 or request["launch_day"] + request["trip_days"] - 1 > inst["horizon"]:
            issues.append(f"Outside horizon: {rid}")
        track = [0]
        for camp, night in route:
            slot = (camp, night)
            if camp not in positions:
                issues.append(f"Unknown camp: {rid}/{camp}")
                continue
            track.append(positions[camp])
            if slot in used:
                issues.append(f"Double booking: {camp}/{night}")
            if slot in inst["closed"]:
                issues.append(f"Closed slot: {rid}/{camp}/{night}")
            used.add(slot)
        track.append(inst["length"])
        for k, (start, end) in enumerate(zip(track, track[1:]), 1):
            if end <= start or end - start > inst["limit"]:
                issues.append(f"Invalid travel leg: {rid}/{k}/{end-start}")
    long_count = sum(requests[rid]["service_class"] == "long" for rid in schedule if rid in requests)
    if long_count < inst["quota"]:
        issues.append("Long-trip service quota not met")
    return issues


def baseline(inst, paths):
    """Offline first-booked-first-served insertion, with whole-trip reservation."""
    schedule, used = {}, set()
    for request in inst["requests"]:
        for path in paths[request["id"]]:
            if used.isdisjoint(path):
                schedule[request["id"]] = path
                used.update(path)
                break
    return schedule


def exhaustive(inst, paths):
    """Enumerate all accept/reject and itinerary combinations, not a heuristic."""
    ids = [r["id"] for r in inst["requests"]]
    best, best_key, explored, feasible = None, None, 0, 0
    for choices in itertools.product(*[[None] + paths[rid] for rid in ids]):
        explored += 1
        schedule = {rid: path for rid, path in zip(ids, choices) if path is not None}
        slots = [slot for path in schedule.values() for slot in path]
        if len(slots) != len(set(slots)):
            continue
        long_count = sum(r["service_class"] == "long" for r in inst["requests"] if r["id"] in schedule)
        if long_count < inst["quota"]:
            continue
        feasible += 1
        # Only count is the scientific objective. Equal-count solutions retain
        # earlier requests, solely to make the printed witness deterministic.
        key = (len(schedule), tuple(rid in schedule for rid in ids))
        if best_key is None or key > best_key:
            best, best_key = schedule, key
    return best, explored, feasible


def describe(schedule, inst):
    if schedule is None:
        return {"status": "INFEASIBLE", "accepted_groups": None}
    issues = verify(schedule, inst)
    accepted = [r for r in inst["requests"] if r["id"] in schedule]
    result = {
        "status": "FEASIBLE" if not issues else "INVALID",
        "accepted_groups": len(accepted),
        "rejected_groups": len(inst["requests"]) - len(accepted),
        "occupied_campsite_nights": sum(len(p) for p in schedule.values()),
        "accepted_mean_trip_days": sum(r["trip_days"] for r in accepted) / len(accepted) if accepted else None,
        "class_counts": {},
        "schedule": schedule,
        "verification_issues": issues,
    }
    for category in ("long", "short"):
        submitted = sum(r["service_class"] == category for r in inst["requests"])
        served = sum(r["service_class"] == category for r in accepted)
        result["class_counts"][category] = {"requested": submitted, "accepted": served, "rejected": submitted - served}
    assert result["accepted_groups"] + result["rejected_groups"] == len(inst["requests"])
    return result


def run(data):
    rows, by_id = [], {}
    for scenario in data["scenarios"]:
        inst = instance(data, scenario)
        paths = {r["id"]: routes_for(r, inst) for r in inst["requests"]}
        greedy = baseline(inst, paths)
        best, explored, feasible = exhaustive(inst, paths)
        row = {
            "scenario_id": scenario["id"],
            "candidate_path_counts": {rid: len(options) for rid, options in paths.items()},
            "assignments_enumerated": explored,
            "feasible_assignments": feasible,
            "baseline": describe(greedy, inst),
            "exact": describe(best, inst),
        }
        rows.append(row)
        by_id[scenario["id"]] = row
        assert row["exact"]["status"] != "INVALID", row
        assert row["baseline"]["status"] == "FEASIBLE", row
    # This fixture is deliberately malformed: its final leg is too long.
    # It checks that QA covers the exit, not just entry and intermediate legs.
    exit_fixture = {"S1": (("A", 1),)}
    limit_59_inst = instance(data, {"daily_limit_miles": 59})
    invalid_exit_issues = verify(exit_fixture, limit_59_inst)
    assert "Invalid travel leg: S1/2/60" in invalid_exit_issues
    closed_inst = instance(data, {"closed_slots": [["B", 2]]})
    fixed_plan = by_id["base"]["exact"]["schedule"]
    closure_issues = verify(fixed_plan, closed_inst)
    assert closure_issues, "A fixed plan using the closed slot must be flagged"
    return {
        "classification": "EXECUTED_SYNTHETIC_TOY_VERIFICATION_ONLY",
        "objective": "Maximize accepted groups; equal optima use booking order only as a deterministic tie-breaker",
        "scenarios": rows,
        "negative_checks": {
            "overlong_final_leg_at_limit_59": invalid_exit_issues,
            "fixed_base_plan_under_closure": closure_issues,
        },
        "limitations": [
            "No empirical observations or real contest output.",
            "No target-scale performance or stochastic reliability evidence.",
            "No actual Claude session or multi-agent runtime is tested.",
            "Closure reoptimization assumes information is known before admission.",
            "An in-transit interruption has no modeled rescue or fallback policy."
        ],
    }


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=here / "inputs.json")
    parser.add_argument("--output", type=Path, default=here)
    args = parser.parse_args()
    data = json.loads(args.inputs.read_text())
    result = run(data)
    args.output.mkdir(parents=True, exist_ok=True)
    result_path = args.output / "results.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    manifest = {
        "classification": result["classification"],
        "default_example_command_from_library_root": "python3 examples/approach_demo/run_demo.py",
        "actual_invocation": {
            "argv": [sys.executable] + sys.argv,
            "working_directory": str(Path.cwd()),
            "resolved_input": str(args.inputs.resolve()),
            "resolved_output": str(args.output.resolve()),
        },
        "runtime": {
            "implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "calculation_status": "COMPLETED_SUCCESSFULLY",
        },
        "dependencies": "Python 3 standard library only",
        "files": {
            "inputs.json": digest(args.inputs),
            "run_demo.py": digest(Path(__file__).resolve()),
            "results.json": digest(result_path),
        },
        "hash_algorithm": "SHA-256",
        "hash_meaning": "Artifact identity only; hashes do not prove mathematical correctness",
    }
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    for row in result["scenarios"]:
        print(f"{row['scenario_id']}: baseline={row['baseline']['accepted_groups']}, exact={row['exact']['accepted_groups']}, enumerated={row['assignments_enumerated']}")


if __name__ == "__main__":
    main()
