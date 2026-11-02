"""Independent finite-fixture checks; does not import the demonstration code."""
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEMO = ROOT / "examples" / "approach_demo"
OUT = Path(__file__).resolve().parent
data = json.loads((DEMO / "inputs.json").read_text())
reported = json.loads((DEMO / "results.json").read_text())
expected = {"base": (3, 4), "long_service_quota": (3, 3),
            "limit_59": (1, 1), "limit_30": (1, 1), "limit_29": (0, 0),
            "known_closure": (3, 3), "zero_demand": (0, 0), "all_slots_closed": (0, 0)}
positions = {c["id"]: c["position_miles"] for c in data["camps"]}
receipts = []


def valid_route(request, route, limit, closed):
    days = request["trip_days"]
    start = request["launch_day"]
    if start < 1 or start + days - 1 > data["horizon_days"]:
        return False
    if len(route) != days - 1:
        return False
    previous = 0
    for offset, (camp, night) in enumerate(route):
        if camp not in positions or night != start + offset or (camp, night) in closed:
            return False
        distance = positions[camp] - previous
        if distance <= 0 or distance > limit:
            return False
        previous = positions[camp]
    return 0 < data["river_length_miles"] - previous <= limit


for scenario in data["scenarios"]:
    sid = scenario["id"]
    chosen = scenario.get("request_ids")
    requests = [r for r in data["requests_in_booking_order"]
                if chosen is None or r["id"] in chosen]
    limit = scenario.get("daily_limit_miles", data["daily_limit_miles"])
    closed = set(map(tuple, scenario.get("closed_slots", [])))
    quota = scenario.get("minimum_long_accepted", 0)
    choices = []
    for request in requests:
        # Product permits repeated/reverse camp sequences; validation rejects them.
        candidates = [tuple((camp, request["launch_day"] + j)
                            for j, camp in enumerate(sequence))
                      for sequence in itertools.product(positions, repeat=request["trip_days"] - 1)]
        choices.append([None] + [route for route in candidates
                                if valid_route(request, route, limit, closed)])
    accepted_counts = []
    for combination in itertools.product(*choices):
        slots = [slot for route in combination if route is not None for slot in route]
        if len(slots) != len(set(slots)):
            continue
        long_count = sum(request["service_class"] == "long"
                         for request, route in zip(requests, combination) if route is not None)
        if long_count < quota:
            continue
        accepted_counts.append(sum(route is not None for route in combination))
    optimum = max(accepted_counts) if accepted_counts else None
    row = next(r for r in reported["scenarios"] if r["scenario_id"] == sid)
    assert optimum == expected[sid][1] == row["exact"]["accepted_groups"]
    assert len(accepted_counts) == row["feasible_assignments"]
    assert (row["baseline"]["accepted_groups"], row["exact"]["accepted_groups"]) == expected[sid]
    lookup = {r["id"]: r for r in requests}
    for strategy in ("baseline", "exact"):
        plan = row[strategy]["schedule"]
        assert set(plan).issubset(lookup)
        slots = []
        for rid, raw_route in plan.items():
            route = tuple(map(tuple, raw_route))
            assert valid_route(lookup[rid], route, limit, closed), (sid, strategy, rid)
            slots.extend(route)
        assert len(slots) == len(set(slots))
        assert sum(lookup[r]["service_class"] == "long" for r in plan) >= quota
        assert row[strategy]["occupied_campsite_nights"] == len(slots)
        assert row[strategy]["accepted_groups"] == len(plan)
        assert row[strategy]["accepted_groups"] + row[strategy]["rejected_groups"] == len(requests)
        for category, counts in row[strategy]["class_counts"].items():
            assert counts["requested"] == sum(r["service_class"] == category for r in requests)
            assert counts["accepted"] == sum(lookup[r]["service_class"] == category for r in plan)
            assert counts["rejected"] == counts["requested"] - counts["accepted"]
        average = sum(lookup[r]["trip_days"] for r in plan) / len(plan) if plan else None
        assert row[strategy]["accepted_mean_trip_days"] == average
    receipts.append({"scenario": sid, "independent_optimum": optimum,
                     "independent_feasible_assignments": len(accepted_counts), "status": "PASS"})

manifest = json.loads((DEMO / "manifest.json").read_text())
for name, claimed in manifest["files"].items():
    assert hashlib.sha256((DEMO / name).read_bytes()).hexdigest() == claimed, name

receipt = {"scope": "Eight supplied synthetic scenarios; independent generation/enumeration and output feasibility",
           "source_files": {name: hashlib.sha256((DEMO / name).read_bytes()).hexdigest()
                            for name in ("inputs.json", "run_demo.py", "results.json", "manifest.json")},
           "checks": receipts, "status": "PASS"}
(OUT / "independent_results.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
