"""T09 file-based reproduction and copied-fixture integrity probes.

Writes only beneath this previously created T09 directory. The input tree is
read-only. This is execution evidence awaiting independent review, not a
scientific acceptance decision.
"""
from datetime import datetime, timezone
import copy
import csv
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

RUN = Path(__file__).resolve().parent
PROJECT = RUN.parents[1]
PRIMARY = PROJECT / "runs/T05-scientific-20261103-r03"
EXPECTED_MANIFEST = "7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00"
PINNED = RUN / "intake/runs/T05-scientific-20261103-r03/manifest.json"
PYTHON = "/Users/ericzhang/.venvs/default/bin/python3"
RECOVERED = RUN / "recovered"
REFERENCE = RUN / "reference/outputs"
OUTPUT = RUN / "outputs"
COMMANDS = []
ENV = os.environ.copy()
ENV.update(PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="1",
           OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", TMPDIR=str(RUN / "tmp"))


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as f:
        json.dump(value, f, indent=2, allow_nan=False)
        f.write("\n")


def run_command(label, argv, cwd, reject=None):
    index = len(COMMANDS) + 1
    base = RUN / "commands" / f"{index:02d}-{label}"
    record = {"label": label, "argv": [str(x) for x in argv],
              "working_directory": str(cwd), "started_at": now(),
              "environment_overrides": {k: ENV[k] for k in
                  ("PYTHONDONTWRITEBYTECODE", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "TMPDIR")},
              "timeout_seconds": 60, "expected_rejection_substring": reject}
    result = subprocess.run(record["argv"], cwd=cwd, env=ENV, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
    base.with_suffix(".stdout.txt").write_text(result.stdout)
    base.with_suffix(".stderr.txt").write_text(result.stderr)
    record.update(finished_at=now(), exit_code=result.returncode,
                  stdout_path=str(base.with_suffix(".stdout.txt").relative_to(RUN)),
                  stderr_path=str(base.with_suffix(".stderr.txt").relative_to(RUN)))
    if reject is None:
        record["expected_outcome_observed"] = result.returncode == 0
    else:
        record["expected_outcome_observed"] = result.returncode != 0 and reject in result.stderr + result.stdout
    save(base.with_suffix(".json"), record)
    COMMANDS.append(record)
    assert record["expected_outcome_observed"], (label, record, result.stderr)
    return record


def copy_verified(source, target, expected):
    assert sha(source) == expected, ("Source changed", str(source))
    target.parent.mkdir(parents=True, exist_ok=True)
    assert not target.exists()
    shutil.copyfile(source, target)
    assert sha(target) == expected


def verify_originals(manifest):
    checks = [{"path": str(PRIMARY / "manifest.json"), "sha256": sha(PRIMARY / "manifest.json"),
               "expected_sha256": EXPECTED_MANIFEST}]
    for item in manifest["retained_artifacts"]:
        path = PROJECT / item["retained_path"]
        checks.append({"path": str(path), "sha256": sha(path), "expected_sha256": item["sha256"]})
    for item in manifest["outputs"]:
        path = PROJECT / item["path"]
        checks.append({"path": str(path), "sha256": sha(path), "expected_sha256": item["sha256"]})
    handoff = PROJECT / "handoffs/T05/computation-r05.md"
    checks.append({"path": str(handoff), "sha256": sha(handoff),
                   "expected_sha256": "ca0853e2b5433f1ed79fe9ccc5332150bb31dcb80e0a16ffdcca2761f48c2006"})
    assert all(row["sha256"] == row["expected_sha256"] for row in checks)
    return checks


def phase(which, output):
    return [PYTHON, RECOVERED / "code/experiments/analysis_r03.py", "--phase", which,
            "--snapshot", RECOVERED, "--output-dir", output, "--config", RECOVERED / "config.json"]


def compare_outputs(actual_dir):
    exceptions = {"selection_frozen.json", "final_assessment_receipt.json", "production_receipt.json"}
    expected_names = {p.name for p in REFERENCE.iterdir()}
    actual_names = {p.name for p in actual_dir.iterdir()}
    assert actual_names == expected_names, (expected_names - actual_names, actual_names - expected_names)
    rows = []
    for name in sorted(expected_names - exceptions):
        actual, expected = sha(actual_dir / name), sha(REFERENCE / name)
        rows.append({"file": name, "expected_sha256": expected, "actual_sha256": actual,
                     "bitwise_equal": actual == expected})
    assert all(row["bitwise_equal"] for row in rows)
    exclusions = {
        "selection_frozen.json": ["frozen_at"],
        "final_assessment_receipt.json": ["started_at", "finished_at", "selection_frozen_at", "loaded_selection_sha256"],
        "production_receipt.json": ["finished_at", "loaded_selection_sha256", "final_assessment_sha256"],
    }
    receipts = {}
    for name, keys in exclusions.items():
        original = json.loads((REFERENCE / name).read_text())
        produced = json.loads((actual_dir / name).read_text())
        old_fields = {k: v for k, v in original.items() if k not in keys}
        new_fields = {k: v for k, v in produced.items() if k not in keys}
        assert old_fields == new_fields, ("Receipt scientific fields changed", name)
        receipts[name] = {"excluded_provenance_fields": keys, "all_other_fields_exactly_equal": True}
    selection = json.loads((actual_dir / "selection_frozen.json").read_text())
    final = json.loads((actual_dir / "final_assessment_receipt.json").read_text())
    production = json.loads((actual_dir / "production_receipt.json").read_text())
    assert final["loaded_selection_sha256"] == sha(actual_dir / "selection_frozen.json")
    assert final["selection_frozen_at"] == selection["frozen_at"]
    assert final["final_forecasts_sha256"] == sha(actual_dir / "final_forecasts.csv")
    assert final["final_metrics_sha256"] == sha(actual_dir / "final_metrics.csv")
    assert production["loaded_selection_sha256"] == sha(actual_dir / "selection_frozen.json")
    assert production["final_assessment_sha256"] == sha(actual_dir / "final_assessment_receipt.json")
    assert selection["frozen_at"] <= final["started_at"] <= final["finished_at"] <= production["finished_at"]
    assert final["selection_changed"] is False
    assert final["selected_co2_id"] == selection["selected_co2_id"]
    assert final["selected_temperature_id"] == selection["selected_temperature_id"]
    checks = json.loads((actual_dir / "numerical_checks.json").read_text())
    assert all(row["pass"] for row in checks["checks"])
    return {"numeric_files": rows, "numeric_bitwise_count": len(rows), "receipt_checks": receipts,
            "current_receipt_hash_links_verified": True, "local_chronology_verified": True,
            "selected_co2_id": selection["selected_co2_id"],
            "selected_temperature_id": selection["selected_temperature_id"],
            "selection_rule": selection["selection_rule"],
            "final_targets_used_for_selection": selection["final_targets_used_for_selection"],
            "project_final_scores_previously_exposed_by_A01": selection["project_final_scores_previously_exposed_by_A01"],
            "postrun_checks_passed": len(checks["checks"]),
            "meaning": "Executed reproduction, not independent scientific acceptance or a global blindness claim."}


def main():
    started = now()
    assert sys.executable == PYTHON, (sys.executable, PYTHON)
    assert sha(PINNED) == EXPECTED_MANIFEST
    manifest = json.loads(PINNED.read_text())
    originals_before = verify_originals(manifest)
    save(RUN / "original_hashes_before.json", originals_before)
    environment = {"python": sys.version, "executable": sys.executable, "packages": {},
                   "invocation": [sys.executable, *sys.argv], "cwd": str(Path.cwd())}
    for name, version in manifest["environment"]["packages"].items():
        importlib.import_module(name)
        actual = importlib.metadata.version(name)
        environment["packages"][name] = actual
        assert actual == version, (name, actual, version)
    assert sys.version == manifest["environment"]["python"]
    environment["recorded_environment_matches"] = True
    save(RUN / "environment_preflight.json", environment)
    retrieve_path = PRIMARY / "reproduction/code/qa/retrieve_retained_r01.py"
    record = next(i for i in manifest["retained_artifacts"] if i["used_path"] == "code/qa/retrieve_retained_r01.py")
    assert sha(retrieve_path) == record["sha256"]
    run_command("recover-retained", [PYTHON, retrieve_path, "--project-root", PROJECT,
                 "--manifest", PINNED, "--destination", RECOVERED], RUN)
    release = json.loads((RECOVERED / "control/accepted-inputs-g2-r02.json").read_text())
    released_checks = []
    for path, expected in release["sha256"].items():
        actual = sha(RECOVERED / path)
        assert actual == expected, path
        released_checks.append({"path": path, "expected_sha256": expected, "actual_sha256": actual})
    save(RUN / "released_dependencies_verified.json", released_checks)
    for item in manifest["outputs"]:
        copy_verified(PROJECT / item["path"], REFERENCE / Path(item["path"]).name, item["sha256"])
    for script in ("test_ingestion_r01.py", "test_models_r03.py", "test_repair_r03.py"):
        run_command(script.removesuffix(".py"), [PYTHON, RECOVERED / "code/qa" / script], RECOVERED)
    run_command("workbook-reingestion", [PYTHON, RECOVERED / "code/data/ingest_r01.py",
                "--input", RECOVERED / "inputs/2022_HiMCM_Data.xlsx", "--config",
                RECOVERED / "code/data/ingestion_config-r01.json", "--output-dir", RUN / "input-reaudit"], RECOVERED)
    ingestion_checks = []
    for name in ("co2-r01.csv", "temperature-r01.csv", "joined-r01.csv"):
        expected, actual = sha(RECOVERED / "data/processed" / name), sha(RUN / "input-reaudit" / name)
        assert actual == expected
        ingestion_checks.append({"file": name, "expected_sha256": expected, "actual_sha256": actual})
    save(RUN / "reingestion_comparison.json", ingestion_checks)
    for which in ("development", "final", "production"):
        run_command("reproduce-" + which, phase(which, OUTPUT), RECOVERED)
    comparison = compare_outputs(OUTPUT)
    save(RUN / "output_comparison.json", comparison)

    # Operational fixtures only: a deliberately altered copy keeps the original
    # expected identity, and the existing retained-byte retriever must reject it.
    probes = RUN / "probes"
    stale = probes / "tampered-dependency-v01"
    source = RECOVERED / "data/processed/joined-r01.csv"
    copied = stale / "repository-copy/fixture/joined-r01.csv"
    copy_verified(source, copied, sha(source))
    with copied.open(newline="") as f:
        reader = csv.DictReader(f)
        fieldnames, rows = reader.fieldnames, list(reader)
    before_value = rows[0]["co2_ppm"]
    rows[0]["co2_ppm"] = str(float(before_value) + 1.0)
    with copied.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)
    fixture_manifest = {"classification": "OPERATIONAL_TAMPER_FIXTURE_NOT_OFFICIAL_OBSERVATIONS",
        "retained_artifacts": [{"kind": "copied_test_dependency", "used_path": "data/processed/joined-r01.csv",
        "retained_path": "fixture/joined-r01.csv", "retrieval_method": "retained_file", "sha256": sha(source)}]}
    save(stale / "manifest.json", fixture_manifest)
    stale_receipt = run_command("reject-tampered-dependency", [PYTHON, RECOVERED / "code/qa/retrieve_retained_r01.py",
        "--project-root", stale / "repository-copy", "--manifest", stale / "manifest.json", "--destination", stale / "retrieval-attempt"],
        stale, reject="Recovered artifact hash mismatch: data/processed/joined-r01.csv")
    assert not (stale / "retrieval-attempt/retrieval-receipt.json").exists()
    corrected = probes / "valid-dependency-v02"
    copy_verified(source, corrected / "repository-copy/fixture/joined-r01.csv", sha(source))
    valid_manifest = copy.deepcopy(fixture_manifest)
    valid_manifest["classification"] = "OPERATIONAL_RECOVERED_VALID_COPY"
    save(corrected / "manifest.json", valid_manifest)
    run_command("recover-valid-dependency", [PYTHON, RECOVERED / "code/qa/retrieve_retained_r01.py",
        "--project-root", corrected / "repository-copy", "--manifest", corrected / "manifest.json",
        "--destination", corrected / "retrieved"], corrected)
    assert sha(corrected / "retrieved/data/processed/joined-r01.csv") == sha(source)

    # Wrong frozen-output reference: use genuine development bytes, replace only
    # the expected metrics digest in a COPY, and call the retained final stage.
    wrong = probes / "wrong-output-reference-v01/outputs"
    development_files = [p for p in OUTPUT.iterdir() if p.name.startswith("development_")] + [OUTPUT / "selection_frozen.json"]
    for path in development_files:
        copy_verified(path, wrong / path.name, sha(path))
    freeze = json.loads((wrong / "selection_frozen.json").read_text())
    real_reference = freeze["development_metrics_sha256"]
    freeze["development_metrics_sha256"] = "0" * 64
    (wrong / "selection_frozen.json").write_text(json.dumps(freeze, indent=2) + "\n")
    run_command("reject-wrong-output-reference", phase("final", wrong), RECOVERED,
                reject="Development evidence changed after freeze")
    assert not list(wrong.glob("final_*")), "Rejected reference must not produce final-stage evidence"
    valid_outputs = probes / "valid-output-reference-v02/outputs"
    for path in development_files:
        copy_verified(path, valid_outputs / path.name, sha(path))
    for which in ("final", "production"):
        run_command("recover-valid-reference-" + which, phase(which, valid_outputs), RECOVERED)
    valid_comparison = compare_outputs(valid_outputs)
    save(probes / "valid-output-reference-v02/comparison.json", valid_comparison)
    save(RUN / "stale_probe_receipt.json", {
        "classification": "EXECUTED_OPERATIONAL_FIXTURES_ONLY",
        "tampered_dependency": {"fixture": str(copied.relative_to(RUN)), "original_expected_sha256": sha(source),
            "tampered_sha256": sha(copied), "changed_column": "co2_ppm", "changed_row": 0,
            "original_value": before_value, "fixture_value": rows[0]["co2_ppm"],
            "actual_verifier_exit": stale_receipt["exit_code"], "no_success_receipt_created": True,
            "versioned_valid_copy_recovered": str((corrected / "retrieved").relative_to(RUN))},
        "wrong_output_reference": {"fixture": str((wrong / "selection_frozen.json").relative_to(RUN)),
            "reference_field": "development_metrics_sha256", "valid_reference": real_reference,
            "wrong_reference": "0" * 64, "actual_final_stage_rejected": True, "no_final_outputs_created": True,
            "versioned_valid_copy": str(valid_outputs.relative_to(RUN)), "valid_pipeline_reproduced": True},
        "meaning": "Demonstrates two concrete integrity rejections and valid recovery, not tamper-proof security or scientific acceptance."})
    originals_after = verify_originals(manifest)
    assert originals_after == originals_before
    save(RUN / "original_hashes_after.json", originals_after)
    save(RUN / "execution_report.json", {
        "task": "T09", "session": "/root/early_mcm_continue", "started_at": started, "finished_at": now(),
        "status": "EXECUTED_CHECKS_COMPLETE_PENDING_INDEPENDENT_REVIEW",
        "primary_manifest_sha256": EXPECTED_MANIFEST, "retained_artifacts_recovered": len(manifest["retained_artifacts"]),
        "released_artifacts_verified": len(released_checks), "declared_outputs": len(manifest["outputs"]),
        "numeric_files_bitwise_equal": comparison["numeric_bitwise_count"],
        "timestamped_receipts_all_other_fields_equal": 3, "original_artifacts_unchanged": len(originals_after),
        "source_of_commands": "Closed run manifest, producer handoff, retained wrapper and execution log; no agent supplied numerical answers.",
        "execution_choice": "Execute retained ingestion/tests/stage commands in recovered CWD; do not invoke the T05 wrapper that snapshots current files.",
        "logical_scientific_run_id": manifest["run_id"],
        "physical_recovery_directory": str(RUN),
        "run_id_note": "Retained config preserves original logical ID to enable exact output comparison; T09 execution provenance is recorded here separately.",
        "commands": COMMANDS,
        "selected_decisions": {"co2": comparison["selected_co2_id"], "temperature": comparison["selected_temperature_id"]},
        "limitations": ["Existing previously uninvolved agent, not an empty new thread.",
            "Original mathematical reasoning is not independently revalidated by reproducing the same code.",
            "Original final-score exposure remains disclosed; no global blindness claim.",
            "No Claude-native runtime, contest submission, installation, Git operation or biological research.",
            "Copied-fixture checks are operational integrity checks, not OS permission enforcement.",
            "Independent reviewer and coordinator disposition required before calling recovery accepted."]})
    print(json.dumps({"status": "EXECUTED_CHECKS_COMPLETE_PENDING_INDEPENDENT_REVIEW", "recovered": 88,
                      "bitwise_outputs": comparison["numeric_bitwise_count"], "receipt_semantics": 3,
                      "selected": [comparison["selected_co2_id"], comparison["selected_temperature_id"]],
                      "commands_executed": len(COMMANDS)}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except BaseException:
        failure = RUN / "driver_failure.txt"
        with failure.open("x") as f:
            traceback.print_exc(file=f)
        raise
