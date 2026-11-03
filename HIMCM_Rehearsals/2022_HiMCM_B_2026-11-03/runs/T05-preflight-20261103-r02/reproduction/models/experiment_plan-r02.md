# Experiment plan r02 — original frozen experiment with disclosed reporting/boundary repairs

T06/modeler; deterministic bounded work. Model specification r02 preserves original r01 equations/splits/selector and clarifies boundary/reporting contracts. The original plan predates fits; this revision follows A01 final-score exposure and does not claim a fresh unseen holdout. Existing E00–E07 phases are retained with the explicit amendments below; accepted primary results remain pending.

## E00 — exact modeler toy self-check, before G2 architecture release

Use synthetic values only. Tests: ten-year endpoint arithmetic/tie; drift recovery; exact quadratic and log-linear exponential recovery; first integer threshold crossing versus fractional root; subthreshold/no-crossing and already-above statuses; positive-log domain; time-baseline and log-CO2 temperature coefficient recovery; invariance to log reference scale. Execute and retain exact script plus JSON. This is modeler self-check evidence, not validation of computation's later implementation and not independent review. Computation must implement its own tests; reviewer independently checks pinned artifacts.

## E01 — data preparation and contract audit

Prerequisite: coordinator releases accepted T01 input/dictionary and specification hashes. Independently read exact workbook sheets and ranges, preserve supplied vintage, verify 63/64 row counts, unique consecutive years, finite values, positive CO2, valid negative temperature anomalies and 63-row year join. Assert the first joined pair is both from 1959, not temperature 1958. Check rows match original supplied values within reader tolerance 1e-10 without changing source bytes. Explicitly reject an injected duplicate year, missing year or positional-join mismatch in isolated test fixtures. No repair to source data.

Output: processed tables, preparation script/config/log, hash manifest and status. Failure blocks model fitting. Acceptance: expected rows/units/years, provenance and no imputation/external observations.

## E02 — independently implement equations and boundary tests

Implement M01–M07 and own verification tests. Use modeler synthetic formulas as test cases, but do not label reuse an independent numerical review. Verify units, coefficient recovery, positive-log enforcement, tie handling, threshold boundary/equality, non-crossing and invalid-path statuses. Add a nonmonotone toy path to ensure first passage is not confused with a later endpoint. Confirm a duplicated/missing year fails loudly. Compare direct evaluation with returned parameters for at least one forecast. No historical conclusion yet.

Output: versioned code, self-check log/status and exact executed command. Failed tests return to owner before larger computation; preserve failed log/run rather than rewriting it as successful.

## E03 — historical arithmetic and development comparison

Calculate every M01 interval independently of T01's audit. Do not merely copy its answer. Fit D/Q/E at origins 1981,1986,1991,1996,2001 using only data through the origin; forecast horizons 1–10. Fit T0 and T1-D/Q/E analogously. Expected development count: 50 rows per candidate, including failed-status rows.

Metrics: MAE/RMSE/bias, per-origin and per-horizon errors. Selection: CO2 minimum development MAE; then T0 versus T1 driven by that chosen CO2, using temperature development MAE. Numerical ties follow model-spec. Report rankings/near ties and failures without inventing significance or independence. Store parameters and exact predictions so scores can be recomputed.

Leakage test: after fitting at a chosen origin, modify only later fixture values and verify that this origin's coefficients/predictions stay unchanged. Ensure temperature forecast changes when the CO2 forecast input changes, not when merely the held-out observed CO2 field changes. The development targets may affect development selection by design; they must not affect any fold's fitted predictions.

Persist a selection receipt before final evaluation with source/spec/code/config hashes, candidate lists, chosen IDs and development scores. Save development-only output and freeze receipt even if one command later orchestrates final assessment. Prefer distinct development/final commands so sequence is inspectable.

## E04 — untouched final assessment

Prerequisite: existing freeze receipt. Fit the frozen forms at origin 2011; predict 2012–2021 once without intermediate refitting. Score all declared comparators, highlighting the frozen choices. Expected 10 rows per candidate. Final errors cannot alter selection, detrending order, window, thresholds, envelope construction or fitting method. Report any final ranking reversal and any lack of advantage over the baseline.

Form historical maximum-error radii only from E03 errors; check final containment without adjustment. Preserve all misses and final metrics. If a bug is discovered, new code and a new run may repair the implementation, but record that the holdout was already observed; do not claim a new untouched scientific selection.

## E05 — production paths and descriptive relationship

After E04, refit unchanged forms on common supplied years through 2021. Produce D/Q/E annual paths through 2100, 2050/2100 concentrations/gaps, and 685-ppm first passages through 2300. Produce T0 and T1 driven by D/Q/E, selected-rule threshold years and association extensions. Mark invalid/nonmonotone paths. Check each crossing boundary from unrounded values and retain the previous year.

Compute M04 levels, linear/quadratic detrending and first-difference diagnostics on paired 1959–2021 data. Report n, period, transform, units and descriptive status; no causal p-values. Plotting consumers must not refit from tables.

Output horizon evidence at h=1,5,10 plus full h=1–10 records. Label future periods through 2031 as at most historically assessed short horizons; 2050/2100 and later crossings are conditional extrapolations, never validated long-term predictions.

## E06 — predefined sensitivity and scientific challenge

Refit selected forms on 1992–2021 as in M07. Compare full/last30 predictions and threshold years; do not select a new primary winner from this comparison. Show full-model structural paths as separate scenarios, not a weighted ensemble or probability band. Check CO2 positivity, polynomial turning points, exponential overflow and linked temperature input validity over display/search domains. Record residual mean, RMSE and lag-1 correlation as descriptive fit diagnostics; they do not drive undeclared model additions.

Minimum claim-challenging outcomes: a baseline may win; model ranks may reverse across origins/horizons or final holdout; linked temperature may not improve over time; detrending may weaken level association; extrapolation forms/windows may yield different threshold years. The paper must be able to report each outcome honestly. No result is suppressed to protect the proposed architecture.

## E07 — independent review and release

Fresh reviewer consumes pinned source/spec/run/code, independently recalculates ten-year comparison, at least one prediction/score and crossing boundary, audits temporal availability and source semantics, and challenges unsupported claim strength. Coordinator integrates only accepted versions. Writer receives accepted tables and immutable run IDs, then reviewer examines actual PDF, required sections, article/page limits and numerical consistency. Modeler addresses feedback in new revisions within owned paths.

## Required run evidence and scope limits

Computation owns code and runs; retain command/config, environment, source/spec/code hashes, stdout/stderr, exact input snapshots or recoverable inventories, model outputs, freeze receipt, status and reproduction instructions. Successful command exit does not establish scientific validity. No Monte Carlo, exhaustive hyperparameter search, external data fitting, policy-effect simulation or historical solution borrowing is authorized by this plan. Report executed checks separately from inspections and planned future checks.

## E08 — r02 amendments and checks after adversarial exposure

Before release, independently review full spec/interface r02 and T06 author response. Add all M06 precedence cases to computation tests: valid crossing/later-invalid, before-cross invalidity, invalid-at-hit, invalid origin, valid-above origin/later-invalid, resumed validity after a gap, all-valid bounded non-crossing and negative valid anomaly. Confirm raw first-year values agree with unchanged original r01 ordinary cases; r02 differences are statuses/warnings for formerly ambiguous failures.

From original development error tables add per-origin winner/count and leave-one-origin-out pooled CO2 ranks, explicitly tagged `introduced_after_assessment=true`. They are descriptive challenge diagnostics, never a new selector. Report final ranking reversal, error signs and every envelope miss. Show all T1 comparator scores while identifying the eligible sequential pair. Reconcile A01/A02 probes against primary outputs and explain any discrepancy; do not copy numbers or suppress failures.

Preserve original r01 artifacts and all prior runs. New r02 implementation/tests/output fields require new code/run versions and review. Unchanged source ingestion does not need rerun. If an r01 primary run already exists, preserve it and add a new r02 run; if none exists, implement directly against independently released r02. A01 exposure remains recorded regardless of local execution order. Do not rerun QA reviewers' scripts into their closed output directories.
