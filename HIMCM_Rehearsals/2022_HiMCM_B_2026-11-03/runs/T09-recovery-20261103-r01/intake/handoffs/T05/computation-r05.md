# T05 computation repair handoff r05

Owner/session: `/root/rehearsal_computation`. Status: CLOSED_EXECUTION_CANDIDATE; independent A03 recheck and T10 scientific identity/equivalence acceptance remain pending. This handoff atomically replaces no prior closed handoff. It routes the new r03 code/run after the confirmed F01/F02 defects; all earlier r02 source/run/output bytes remain intact.

Accepted task: `control/repair-request-A03-r01.md`, A03 `qa/adversarial_implementation/r02/review.md` and `handoffs/A03/independent-reviewer-r02.md`. Exact consumed identities are retained in `code/qa/repair-intake-r01.md` and the new manifest snapshot. The unchanged G2 release is `control/accepted-inputs-g2-r02.json`: framing/spec/interface r02, decision/experiment plan r03, assumptions r01. All23 released identities were verified before execution. No equations, split dates, selector ordering/tolerance, empirical envelopes, original observations or model core were changed. The model module remains climate_models_r02.py, hash6dad80e8ee59c28c37829a4034d2a6534ede4865411f94d3bcca03a41afc7bd0.

## Repairs and executed counterexamples

A03-F01: `Analysis.load_frozen` now validates semantic receipt fields against hash-verified development forecasts and metrics before either final or production writes. It checks the complete declared origin/model/horizon grid and development chronology, recomputes overall MAE/RMSE/bias and validity counts from the frozen forecast evidence, verifies those values against the hashed metrics, and derives the original D/E/Q tie ordering and sequential T0-versus-T1(selectedCO2) choice. Candidate sets, eligibility, scores, selected IDs, development bounds and explicit selector metadata must match. It never uses final errors for this validation. A new receipt field documents the existing selector; it does not alter it.

Executed synthetic before/after evidence uses the actual preserved analysis_r02 and new analysis_r03 implementations. With only D→Q and T1-D→T1-Q receipt IDs changed, r02 accepts and writes COMPLETED/selection_changed=false; r03 rejects with Frozen selection semantic mismatch before any final_* output. Both keep development CSV hashes unchanged. Fourteen independent field mutations cover selected IDs, sequential eligible pair, eligibility, development MAE, candidate sets, both tie orders, tie tolerance, score rule, origins, horizons and final-target-use flag. Rehashed but inconsistent development metrics are also rejected by reconciliation with forecast errors. Production rejects an inconsistent receipt before production_* writes. An unchanged receipt completes all stages and retains its original hash. These are executed synthetic regression findings, not claims that the original historical r02 run selected wrong models.

A03-F02: path diagnostics count direct NONPOSITIVE_CO2 statuses before the prefix is marked invalid, instead of counting values after they have become null. The schema now explicitly defines this as a count of direct failures over evaluated prefix years, including the first invalid year, excluding later unevaluated invalid suffix years and other causes. Synthetic D=-1 at2023 yields null/NONPOSITIVE_CO2 and invalid_count278 in full and last30 windows. The preserved r02 reports nonpositive_co2_count0; repaired r03 reports1. An additional invalid2024 does not produce a second direct count after the invalid prefix. Zero also counts1; injected NONFINITE_PREDICTION and MISSING_PREDICTION each count0 while keeping the invalid suffix. Valid ordinary paths count0.

Evidence: `code/qa/test_repair_r03.py`, retained and executed before historical fitting and again from recovered files; complete commands, exit statuses and unittest output are in the closed execution.log. This is owner regression validation; A03 will repeat independently. The earlier author-arranged preflight remains separately identified in preflight-review-r01.md and is not independent final acceptance.

## Closed execution and retention

Command (cwdPROJECT_ROOT):

```text
/Users/ericzhang/.venvs/default/bin/python3 code/experiments/run_analysis_r03.py --project-root /Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03 --run-id T05-scientific-20261103-r03
```

Run status `SUCCEEDED`, exit0; UTC2026-11-03T12:25:19.715749+00:00 to2026-11-03T12:25:24.423808+00:00; elapsed4.708056s. Exact interpreter/package versions and single-thread environment are recorded in environment.json and requirements.txt. Solver: numpy.linalg.lstsq/SVD, all executed regressions full rank; no iterative solver or stochastic seed.

The retained run is `runs/T05-scientific-20261103-r03`. It contains88 exact retained dependencies, including source/data/spec/config bytes, repair request/review/handoff, previous closed manifest and all35 previous outputs used for equivalence. Original XLSX reingestion reproduced admitted year-keyed CSVs. The 9 ingestion,28 model and7 repair tests (44 unittest methods; extra mutation subcases inside repair tests) passed before historical fits and again from isolated recovery. Twelve postrun checks passed.

Distinct development, final and production subprocesses ran in order. Selection was saved at2026-11-03T12:25:22.289937+00:00; final began at12:25:22.405546+00:00 and loaded that saved receipt. The project-wide A01 prior final-score exposure remains explicitly true. No clean unseen-holdout or retuned-selection claim is made.

Actual inventory retrieval populated an unused isolated-recovery directory and verified every artifact hash. Its own test suites and all three stage commands then ran from that recovered CWD. All32 non-timestamp numerical output files reproduced byte-for-byte; frozen selection semantics matched after removing only the fresh timestamp. Three receipts necessarily differ in timestamps and dependent receipt hashes. Python/package versions are recorded; package binaries are not bundled. Reusing the run ID remains prohibited by mkdir(exist_ok=False).

## r02 equivalence and unchanged scientific results

`equivalence-r02.json` compares all35 output files to the exact closed r02 manifest and outputs, first verifying their hashes. Every scientific field is identical. All CSVs and traced scientific JSONs differ only in run_id. numerical_checks.json is byte-identical. Receipt differences are new code/config/run identities, timestamps, dependent CSV/receipt hashes, and the explicit unchanged selection_rule metadata. No numerical field is excluded. The isolated rerun independently executes the same comparator against recovered baseline bytes. The wrapper reverified all original r02 source/output hashes and the closed manifest after execution; they remain unchanged.

Frozen models remain D then T1-D. Development MAE: D1.48122ppm versus Q1.7590314104ppm; T1-D0.08721371947°C versus T0.10001082429°C. Final MAE: Q1.3984076719ppm beats selected D2.1445ppm; T1-D0.09314657142°C. The T1-D2016 historical envelope miss remains excess0.02516695643°C, with9/10 contained; no envelope widening or probability interpretation. CO2 origin wins D2/Q3, and leave-one-origin-out winner reversals remain diagnostic only. Selected full2050/2100: D487.79/610.79ppm; T1-D1.53904090838/2.38817023529°C anomaly versus1951–1980. D685 crossing2131; selected temperature1.25/1.5/2 crossings2036/2048/2076. All comparator results, coefficients, sensitivities, status fields and source-definition caveats are unchanged from r04, now bound to r03 outputs.

The full35-file output inventory and exact hashes are in manifest.json. Use r03/outputs forecast_summary.csv, thresholds.csv, production_forecasts.csv, threshold_search_paths.csv, path_diagnostics.csv; development/final metrics and forecasts; all three phases' coefficients/residuals/fit_diagnostics; historical/production_error_envelopes.csv; rank_stability.csv/comparison_ranks.csv; window_sensitivity.csv/structural_sensitivity.csv; relationship_diagnostics.csv/relationship_series.csv; ten_year_changes.csv/ten_year_comparison.json; and numerical_checks.json. output_schema-r03.json defines every table and unit. Candidate interpretation must retain annual-versus-March,685CO2-equivalent-versus-pureCO2,1951–1980baseline, descriptive association, no probability interval and long extrapolation cautions.

## Exact review targets

- `runs/T05-scientific-20261103-r03/manifest.json`: `7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00`
- `runs/T05-scientific-20261103-r03/execution.log`: `db695a2987721ca1c61d55ced4466f52ecb21fa60c9ba96adaec707e0c5b1e98`
- `runs/T05-scientific-20261103-r03/equivalence-r02.json`: `a400da6c70b22085a9bfebde759002cc90af92f8486bd0e53bb78d4f3368c005`
- `runs/T05-scientific-20261103-r03/reproduction-check.json`: `ff7b01ba7b889e55fcd0a12ac7b24f50750c8ec9faa2395104dc55ec69dd3904`
- `runs/T05-scientific-20261103-r03/isolated-recovery/retrieval-receipt.json`: `20b2a1fe03ef262720b792e7f66d148956380d09d07f3df4b6aa23e83de7b153`
- `code/experiments/analysis_r03.py`: `be8feb6fbe65170c3414a9cc7cfd76d0cca55a81cdbd035ce10a9982261f6558`
- `code/experiments/run_analysis_r03.py`: `a8fe542653b9f00f7b75ef426e817111975a8a07edfcdbab06c073ccdd4e24e1`
- `code/qa/test_models_r03.py`: `894f61966c9cc06c098a710ddf2d76039f51b8d1392be8e0f1339650d7f9cf70`
- `code/qa/test_repair_r03.py`: `bcb8df803a9b5158b53bd9257aa91d9aa4ed2c6cdc48f7c7dbd47bd0f354d5fa`
- `code/qa/compare_scientific_r03.py`: `f928cc4a2c6a33e96308287aa1357bf82c64770e7e5bf4665c4d07ec2a8b14cc`

Downstream action: A03 repeats the exact changed failure attacks against retained r03 targets; T10 verifies identities/chronology and numerical equivalence. M/W must refresh bindings to the accepted repaired release after those decisions. No scientific acceptance, final PDF status or new external observation is asserted here.
