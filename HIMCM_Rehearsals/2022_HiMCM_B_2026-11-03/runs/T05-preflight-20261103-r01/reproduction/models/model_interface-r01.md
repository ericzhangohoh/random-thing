# Model interfaces r01

Owner modeler, T02. Numerical meaning is normative; computation may use CSV/JSON or equivalent tables but must preserve these fields and meanings. No producer/consumer may silently reinterpret units or available time. A consumer receipt must name exact accepted versions and hashes before consequential use.

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

Producer computation/experiments; consumers reviewer/coordinator and final-assessment routine. Required receipt: source/spec/config hashes, explicit model and temperature candidate lists, fixed origins/horizons, eligibility, development metrics, selected CO2 ID and selected T ID, timestamp/order receipt and status `FROZEN_BEFORE_FINAL_ASSESSMENT`. A final-assessment routine must load that saved receipt rather than recalculate selection from final scores. The receipt is immutable once final outputs are generated.

M03's selected temperature alternatives are T0 versus T1 driven by the selected CO2 rule. Other T1 paths are scenario/comparator evidence, not a larger undeclared temperature hyperparameter search. Source/fitting changes invalidate receipt and all dependent results. Once final targets were evaluated, any new selection is explicitly post-holdout development, not untouched assessment.

## I05 — final forecasts to thresholds and uncertainty

Forecast rows: `fit_window` (full/last30), `target`, `model_id`, `origin=2021`, `year`, `value`, `unit`, `status`, `interpretation=conditional_central_path`. Annual display forecasts run 2022–2100; threshold computation may evaluate through 2300. Keep required 2050/2100 rows even when invalid, with missing numeric value and reason; never fabricate values.

Threshold rows: `target`, `model_id`, `fit_window`, `threshold`, `unit`, `origin`, `search_end=2300`, nullable `first_year`, `status`, `value_at_year`, `value_previous_year`, `monotone_flag`, `beyond_tested_horizon`. Allowed status: `CROSSED`, `AT_OR_BEFORE_ORIGIN`, `NO_CROSSING_THROUGH_2300`, `INVALID_PATH`. Crossing comparisons use raw values, not rounded displays. An optional analytic later root is a separate field, never silently substituted for the bounded status.

Error envelope rows: `target`, `selected_model_id`, `horizon` 1–10, `radius`, `unit`, `development_origin_count=5`, `label=historical_max_error_envelope`; final containment is a separate assessment field. Future envelope rows end in 2031. Structural spread and last30 sensitivity are separately identified and have no probability/coverage label. No iid-standard-error confidence band is substituted.

## I06 — results to writer and reviewer

Provide identifiable tables for ten-year arithmetic; CO2 comparison; temperature comparison; selected-rule/final receipt; 2050/2100/crossings; relationship diagnostics; horizon errors/envelopes; sensitivity; fit/path validity. Every table cites its run ID and data/spec hashes. Relationship rows include variable/transform, period, n, correlation/slope/R-squared where defined, detrending order and noncausal interpretation.

Writer may round or format but cannot refit, change thresholds or select winners. Reviewer independently recomputes at least decade arithmetic, one forecast, one score and one crossing boundary from the preserved inputs/code. Summary, body and article must use the same accepted tables and retain annual/March, CO2/CO2-equivalent, baseline and extrapolation distinctions.

## Failure and invalidation

Missing dependency: explicit blocked artifact, not guessed conversion. Failed calculation: preserve status/log and create a new run for repair. Accepted bytes remain retrievable after replacement. Changed source rows/definitions invalidate I01 onward; changed equations/splits invalidate I02 onward; plot-only changes require display review unless values/transformations also change. Modeler requests repairs through owner handoffs; does not edit computation results.
