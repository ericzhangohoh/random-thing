# Model interfaces r02

Owner modeler, T06. Proposed r02 boundary/reporting amendment; requires independent review and coordinator release. All original r01 bytes remain preserved. Numerical meaning is normative; computation may use CSV/JSON or equivalent tables but must preserve these fields and meanings. No producer/consumer may silently reinterpret units or available time. A consumer receipt must name exact accepted versions and hashes before consequential use.

## I01 — admitted workbook to model-ready observations

Producer T01 domain-data; consumer computation. Source: immutable admitted `inputs/2022_HiMCM_Data.xlsx`, exact path/hash from T01 manifest (verify before use). Sheets/ranges: `CO2 Data Set 1!A2:B64`, 63 rows 1959–2021; `Temps Data Set 2!A2:B65`, 64 rows 1958–2021. Read sheet/header names exactly from admitted dictionary if workbook naming differs. Values are supplied-vintage annual concentration and annual global anomaly; no unit conversion or source update.

Model-ready columns: `year:int`, `co2_ppm:float`, `temp_anomaly_c:float`. Temperature-only 1958 is retained in its source table; common table has exactly 63 joined years 1959–2021. Require finite values, unique contiguous years and positive CO2. Include source path/hash, ranges, extraction version, dictionary hash and baseline metadata in manifest. Missing/duplicated/reinterpreted fields fail rather than impute. Root must release accepted T01 before computation.

## I02 — observations to temporal fits and forecast scores

Producer computation/data; consumer computation/modeling. For origin o, permitted predictors/targets used in fitting have `year<=o`. Reference C_ref is the supplied 1959 value, a fixed positive unit scale known at every origin. It remains fixed even in last-30-year sensitivity; changing the log reference only shifts the intercept, not predictions.

Forecast-score rows: `phase` (development/final), `target` (co2/temp), `model_id` (D/Q/E/T0/T1-D/T1-Q/T1-E), `origin_year`, `train_start`, `train_end`, `n_train`, `target_year`, `horizon`, `observed`, `predicted`, `error=predicted-observed`, `unit`, `status`. Require target_year=origin_year+horizon and train_end<=origin_year. Each CO2 candidate has 50 development pairs and 10 final pairs, including failed pairs with status. Do not confuse repeated target years from different origins with duplicate records.

Parameters: model ID, origin, coefficient names/values, input hashes, training years/n, fit method, rank and status. Data-derived preprocessing is fit only on training observations. D's declared window is structural and is not selected using held-out scores.

## I03 — forecast CO2 to temperature forecast

Producer M02; consumer M05. Input: `model_id`, `origin`, `year`, `co2_ppm`, `status`; annual future years and Mauna Loa ppm. Consumer: `T1(t|o)=alpha_o+beta_o*log(C_hat(t|o)/C_ref)` degrees C relative to 1951–1980, with coefficients fitted through o. The future concentration is a predicted indicator, not an observed or causally controlled input.

No feedback, lag adjustment, monthly-to-annual conversion, concentration-to-emission conversion or CO2-equivalent conversion exists. Nonpositive/nonfinite/missing CO2 returns `INVALID_UPSTREAM_PATH` and blocks dependent temperatures. Preserve producer identity and uncertainty/path flags. End-to-end validation uses predicted future CO2 even when actual values happen to be in the workbook.

## I04 — development scores to frozen decisions

Producer computation/experiments; consumers reviewer/coordinator and final-assessment routine. Required receipt: source/spec/config hashes, explicit model and temperature candidate lists, fixed origins/horizons, eligibility, development metrics, selected CO2 ID and selected T ID, timestamp/order receipt and status `FROZEN_BEFORE_FINAL_ASSESSMENT`. A final-assessment routine must load that saved receipt rather than recalculate selection from final scores. A01 already evaluated final scores before primary execution; this receipt proves local ordering for the unchanged original rules, not project-wide unseen-data status. The receipt is immutable once final outputs are generated.

M03's selected temperature alternatives are T0 versus T1 driven by the selected CO2 rule. Other T1 paths are scenario/comparator evidence, not a larger undeclared temperature hyperparameter search. Source/fitting changes invalidate receipt and all dependent results. Once final targets were evaluated, any new selection is explicitly post-holdout development, not untouched assessment.

## I05 — final forecasts to thresholds and uncertainty

Forecast rows: `fit_window` (full/last30), `target`, `model_id`, `origin=2021`, `year`, `value`, `unit`, `status`, `interpretation=conditional_central_path`. Annual display forecasts run 2022–2100; threshold computation may evaluate through 2300. Keep required 2050/2100 rows even when invalid, with missing numeric value and reason; never fabricate values.

Threshold rows: `target`, `model_id`, `fit_window`, `threshold`, `unit`, `origin`, `search_end=2300`, nullable `first_year`, `status`, `value_at_year`, `value_previous_year`, nullable `monotone_flag`, `monotonicity_end_year`, and `beyond_tested_horizon`. Additional mandatory r02 fields:

| Field | Meaning |
|---|---|
| `search_domain_valid:boolean` | Every required target/upstream annual value is valid on inclusive [origin,2300]. This can be false even when status is CROSSED. |
| `valid_through_year:int or null` | Last year of contiguous valid prefix from origin; 2300 if all valid, null if origin invalid. |
| `invalid_from_year:int or null` | First invalid year in inclusive domain; null if none. |
| `invalid_reason:string or null` | First failure: `NONPOSITIVE_CO2`, `NONFINITE_CO2`, `NONFINITE_TARGET`, `MISSING_REQUIRED_VALUE`, `EVALUATION_ERROR` or an equivalently explicit recorded reason. |
| `monotonicity_end_year:int or null` | End of prefix on which monotone_flag was computed; do not imply monotonicity beyond invalidity. |

Validity: CO2 must be finite and positive; T1 requires its CO2 producer finite/positive plus finite anomaly; T0 requires finite anomaly. Negative anomalies are valid. Check required upstream validity before testing a threshold at the same year. A missing/nonfinite value is not silently skipped or replaced. Stop first-passage inference at first invalidity even if the function later becomes valid again; continue domain validity inspection to preserve the earliest warning.

Status precedence: invalid origin -> `INVALID_PATH`; valid origin already at/above H -> `AT_OR_BEFORE_ORIGIN`; valid below-threshold origin and a crossing within the contiguous valid prefix -> `CROSSED`; no such crossing but any invalidity -> `INVALID_PATH`; otherwise -> `NO_CROSSING_THROUGH_2300`. Only CROSSED has a non-null first_year. With CROSSED, retain boundary values at t and t-1; `beyond_tested_horizon` means first_year>2031. For other statuses it is null. `monotone_flag` is true iff the valid prefix with at least two values is nondecreasing within 1e-9, false if it decreases somewhere, null if fewer than two valid values exist.

A later invalid segment does not undo an established first annual crossing. It does require `search_domain_valid=false`, exact invalid year/reason and an adjacent warning in display/prose. Thus CROSSED is an event status, not certification of the full path. Conversely, an invalid prefix makes a later apparent crossing inadmissible. Fully valid no-crossing through2300 is distinct from inability to establish crossing because the path failed. Optional analytic later roots are separate fields and cannot override invalid-prefix status.

Crossing comparisons use unrounded values and equality tolerance; no rounded display drives threshold selection. Writer must render later-invalid warnings, not drop them because a numeric first_year exists. See M06 r02 synthetic tests for all precedence branches.

Error envelope rows: `target`, `selected_model_id`, `horizon` 1–10, `radius`, `unit`, `development_origin_count=5`, `label=historical_max_error_envelope`; final containment is a separate assessment field. Future envelope rows end in 2031. Structural spread and last30 sensitivity are separately identified and have no probability/coverage label. No iid-standard-error confidence band is substituted.

## I06 — results to writer and reviewer

Provide identifiable tables for ten-year arithmetic; CO2 comparison; temperature comparison; selected-rule/final receipt; 2050/2100/crossings; relationship diagnostics; horizon errors/envelopes; sensitivity; fit/path validity. Every table cites its run ID and data/spec hashes. Relationship rows include variable/transform, period, n, correlation/slope/R-squared where defined, detrending order and noncausal interpretation.

Writer may round or format but cannot refit, change thresholds or select winners. Reviewer independently recomputes at least decade arithmetic, one forecast, one score and one crossing boundary from the preserved inputs/code. Summary, body and article must use the same accepted tables and retain annual/March, CO2/CO2-equivalent, baseline and extrapolation distinctions.

## Failure and invalidation

Missing dependency: explicit blocked artifact, not guessed conversion. Failed calculation: preserve status/log and create a new run for repair. Accepted bytes remain retrievable after replacement. Changed source rows/definitions invalidate I01 onward; changed equations/splits invalidate I02 onward; plot-only changes require display review unless values/transformations also change. Modeler requests repairs through owner handoffs; does not edit computation results.

## I07 — r02 mandatory interpretation diagnostics

Report original pooled-development selected IDs separately from final-score winners. Add `rank_stability` rows for per-origin CO2 winner/count and leave-one-origin-out pooled winner; fields identify omitted origin, candidate scores, diagnostic winner and `introduced_after_assessment=true`. These summaries do not alter selection. Preserve every declared T1 comparison and identify the eligible sequential pair T0/T1-selected-CO2 so a better ineligible comparator is not hidden.

Envelope-assessment rows must retain actual year/horizon, absolute error, radius, containment and excess `max(0,abs(error)-radius)`. Observed counts are descriptive; no inferred probability or calibrated “reliable through2031” field is permitted. Any primary/adversarial disagreement requires investigation before claim release. Every narrative claim distinguishes sample/metric/model scope and future uncertainty.
