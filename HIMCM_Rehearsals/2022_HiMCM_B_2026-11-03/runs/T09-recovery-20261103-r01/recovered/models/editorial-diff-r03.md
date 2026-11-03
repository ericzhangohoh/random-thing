# T06 editorial follow-up r03

Scope: two residual “untouched” labels only, plus document-title revision identifiers. No equations, data, split, selector, test, output-schema or scientific claim-rule changes. This is not new scientific development.

The E04 heading now describes computational final assessment under unchanged frozen rules. D04 similarly names final-segment assessment under the unchanged frozen rule. Existing A01 exposure caveats remain intact: no project-wide unseen-final-data claim is made. These documents replace only their r02 counterparts; model_spec-r02, model_interface-r02, framing-r02, assumptions-r01 and all test artifacts remain unchanged.

Checks executed: exact reversible replacement assertion for both files; all 11 closed r02 artifact hashes match their original inventory; no mathematical tests rerun. Root/reviewer should perform diff-only recheck before gate release. No other model document, toy result, control, QA, data, code or Git artifact was edited.

Exact unified diff:

```diff
--- experiment_plan-r02.md
+++ experiment_plan-r03.md
@@ -1,4 +1,4 @@
-# Experiment plan r02 — original frozen experiment with disclosed reporting/boundary repairs
+# Experiment plan r03 — original frozen experiment with disclosed reporting/boundary repairs
 
 T06/modeler; deterministic bounded work. Model specification r02 preserves original r01 equations/splits/selector and clarifies boundary/reporting contracts. The original plan predates fits; this revision follows A01 final-score exposure and does not claim a fresh unseen holdout. Existing E00–E07 phases are retained with the explicit amendments below; accepted primary results remain pending.
 
@@ -28,7 +28,7 @@
 
 Persist a selection receipt before final evaluation with source/spec/code/config hashes, candidate lists, chosen IDs and development scores. Save development-only output and freeze receipt even if one command later orchestrates final assessment. Prefer distinct development/final commands so sequence is inspectable.
 
-## E04 — untouched final assessment
+## E04 — computational final assessment under unchanged frozen rules
 
 Prerequisite: existing freeze receipt. Fit the frozen forms at origin 2011; predict 2012–2021 once without intermediate refitting. Score all declared comparators, highlighting the frozen choices. Expected 10 rows per candidate. Final errors cannot alter selection, detrending order, window, thresholds, envelope construction or fitting method. Report any final ranking reversal and any lack of advantage over the baseline.
 
--- model_decision-r02.md
+++ model_decision-r03.md
@@ -1,4 +1,4 @@
-# Model decisions r02 — preserved selector, narrowed claims and crossing contract
+# Model decisions r03 — preserved selector, narrowed claims and crossing contract
 
 T06/modeler; 2026-11-03. Read framing/specification/interface/experiment r02 and unchanged assumptions r01. Independent adversarial scores are exposed; no accepted primary-run result is asserted. Original equations, splits and selector remain unchanged.
 
@@ -15,7 +15,7 @@
 | D01: recent drift baseline D | R02–R04; latest level plus recent ten-year average growth | Transparent recent-growth comparator with no distant-history weighting; endpoint noise can matter | Common-origin MAE/RMSE versus Q/E, origin/horizon consistency; extrapolation fixes absolute growth |
 | D02: quadratic Q | R02–R04; concentration has constant absolute acceleration | Allows changing growth at one extra coefficient and explains curvature directly | Temporal errors and turning-point/positivity checks; unbounded curvature can dominate 2100 |
 | D03: exponential E | R02–R04; constant proportional concentration growth | Different long-run structure from constant growth/acceleration, positive by construction | Original-ppm temporal errors; constant percentage growth of total stock is an empirical assumption, not carbon-cycle mechanics |
-| D04: temporal development and final segment | R04,R07; repeated origins with 1–10-year predictions, then one untouched segment | Matches forecasting information order and separates selection from assessment | Freeze receipt and leakage audit; overlapping folds are dependent and supplied vintage is not real-time historical vintage |
+| D04: temporal development and final segment | R04,R07; repeated origins with 1–10-year predictions, then final-segment assessment under the unchanged frozen rule | Matches forecasting information order and separates selection from assessment | Freeze receipt and leakage audit; overlapping folds are dependent and supplied vintage is not real-time historical vintage |
 | D05: time baseline T0 | R05,R07; linear anomaly trend | Compares CO2 linkage with the specified linear-time baseline | Same origins/targets and anomaly-unit errors; omits climate mechanisms |
 | D06: log-CO2 T1 | R05–R07; each proportional CO2 change associates with equal modeled anomaly change | Parsimonious transform permits extrapolating the required relationship | Full pipeline comparison uses predicted future CO2; beta is association, not identified sensitivity |
 | D07: shared trends and differences | R06; detrended correlations and first-difference association | Exposes level correlation's dependence on common trends | Compare raw/linear-detrended/quadratic-detrended/difference results; none is a causal identification design |
```
