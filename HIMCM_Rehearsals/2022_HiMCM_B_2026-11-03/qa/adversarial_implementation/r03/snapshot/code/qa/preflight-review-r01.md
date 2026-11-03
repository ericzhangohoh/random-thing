# Author-arranged implementation preflight r01

Reviewer agent/session: `/root/rehearsal_computation/implementation_preflight`, spawned by computation after G2r01, before any historical execution of this implementation. Read-only static comparison against released M00–M07 and I01–I06. The reviewer did not edit code or compute historical forecasts. This is author-arranged preflight, not final independent scientific acceptance.

Consolidated actual reviewer response: no ordinary-path equation or split/selection leakage bug found. Four concrete implementation defects identified before execution:

1. `predict_temperature` propagated producer overflow as NONFINITE_PREDICTION instead of INVALID_UPSTREAM_PATH. Repaired with explicit producer-error translation. Test `test_upstream_overflow_status_is_translated` uses an overflowing synthetic E producer and asserts the required status.
2. Failure outputs could trigger TypeError in abs(error), envelope arithmetic, last30 subtraction and int(train_end). Repaired with null-preserving arithmetic and guarded training checks. Test `test_failed_fold_rows_and_metrics_preserve_nulls` injects seven failed synthetic fits and verifies70 explicit failure rows and null metrics. Null never becomes zero.
3. Production trusted the final receipt without verifying final_forecasts/final_metrics bytes. Repaired with `verify_final_tables` at production entry. Test `test_final_table_tamper_blocks_production_consumption` verifies original fixture hashes then mutates a fixture CSV and requires rejection.
4. Forecast-summary rows dropped failure reasons. Repaired by copying the source reason alongside status and null value.

Before-behavior evidence above is static source inspection, not an executed historical failure. After-behavior evidence is the named synthetic tests and subsequent run log. No fabricated failed scientific run or acceptance is claimed.

Reviewer also confirmed: D/E/Q tie order; temperature selection only T0 versus T1(selectedCO2); all7 full paths; last30 sensitivity only for selected forms; last30 T1 refits both association and producer while keeping1959 reference; D retains ten-year rule; ten-year prior maximum and competition rank match M01. No alternative form or tuning change requested or adopted.

M06 later-invalid-path semantics remain separately owned by modeler and coordinator; preflight does not approve that normative clarification.
