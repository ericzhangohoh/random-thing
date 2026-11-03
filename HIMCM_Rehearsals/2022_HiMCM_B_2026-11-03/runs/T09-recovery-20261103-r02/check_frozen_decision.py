"""Recalculate the declared selector from recovered development rows only.

No original analysis/model module is imported. This supplements recovery
identity checks; it does not independently validate forecast mathematics.
"""
import csv
import hashlib
import json
import math
from pathlib import Path

run = Path(__file__).resolve().parent
outputs = run / "outputs"
with (outputs / "development_forecasts.csv").open() as f:
    rows = list(csv.DictReader(f))
receipt = json.loads((outputs / "selection_frozen.json").read_text())
scores = {}
ids = ["D", "Q", "E", "T0", "T1-D", "T1-Q", "T1-E"]
expected = {(origin, horizon) for origin in (1981, 1986, 1991, 1996, 2001)
            for horizon in range(1, 11)}
for model in ids:
    selected = [r for r in rows if r["model_id"] == model]
    assert len(selected) == 50
    assert {(int(r["origin_year"]), int(r["horizon"])) for r in selected} == expected
    assert all(r["phase"] == "development" and int(r["target_year"]) <= 2011 for r in selected)
    assert all(int(r["target_year"]) == int(r["origin_year"]) + int(r["horizon"]) for r in selected)
    assert all(int(r["train_end"]) <= int(r["origin_year"]) for r in selected)
    assert all(r["status"] == "OK" for r in selected)
    errors = [float(r["predicted"]) - float(r["observed"]) for r in selected]
    assert all(abs(error - float(row["error"])) <= 1e-12 for error, row in zip(errors, selected))
    scores[model] = math.fsum(abs(e) for e in errors) / len(errors)
    assert math.isclose(scores[model], receipt["development_mae"][model], rel_tol=0, abs_tol=1e-12)

def select(ordered):
    minimum = min(scores[mid] for mid in ordered)
    return next(mid for mid in ordered if scores[mid] <= minimum + 1e-12)

co2 = select(["D", "E", "Q"])
temperature_candidates = ["T0", "T1-" + co2]
temperature = select(temperature_candidates)
assert co2 == receipt["selected_co2_id"]
assert temperature == receipt["selected_temperature_id"]
assert temperature_candidates == receipt["temperature_selection_candidates"]
assert receipt["selection_rule"] == {"score": "pooled_development_mae", "co2_tie_order": ["D", "E", "Q"],
    "temperature_tie_order": temperature_candidates, "absolute_tie_tolerance": 1e-12}
result = {"status": "EXECUTED_SELECTOR_CHECK_MATCHES", "specification": "recovered/models/model_spec-r02.md sections M03/M05",
    "input": "outputs/development_forecasts.csv", "input_sha256": hashlib.sha256((outputs / "development_forecasts.csv").read_bytes()).hexdigest(),
    "model_count": len(ids), "forecast_rows": len(rows), "pooled_mae_recalculated": scores,
    "selected_co2_id": co2, "selected_temperature_id": temperature,
    "read_final_forecast_or_metric_files": False, "comparison_tolerance": 1e-12,
    "scope": "Recalculation of the unchanged selection rule from reproduced development predictions, not fresh validation of the scientific model."}
with (run / "decision_recalculation.json").open("x") as f:
    json.dump(result, f, indent=2); f.write("\n")
print(json.dumps(result, indent=2))
