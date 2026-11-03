# Model decisions r01 — proposed architecture, not selected empirical winner

T02/modeler; 2026-11-03. Read with framing, mathematical specification, experiment plan, assumptions and interface r01. No historical forecast score has been calculated by this role.

## G1 recommendation

Adopt the supplied-vintage, annual, common-year interpretation and complete every official subquestion. Distinguish Mauna Loa from a global spatial sample, anomaly from absolute temperature, annual from March, and CO2 from CO2-equivalent. T01 source evidence supports these distinctions; coordinator must record accepted source hashes. Preserve the requested 685-ppm pure-CO2 exercise even though it cannot validate the source's different greenhouse-gas quantity. Alternative: reconstruct March observations from an external series. That changes the supplied-data task and vintage and is unnecessary for this bounded rehearsal.

## G2 recommendation

Adopt the deterministic architecture below, subject to independent specification review and exact toy self-checks. Freeze model selection on pre-2012 development forecasts before final assessment. This proposes an experiment; it does not preselect Q, E or D. G1/G2 disposition is DELEGATED_PRACTICE_DECISION under intake, recorded by coordinator, not a fabricated human approval.

| Decision | Requirement and representation | Why it is a serious choice | Discriminating evidence and limitation |
|---|---|---|---|
| D01: recent drift baseline D | R02–R04; latest level plus recent ten-year average growth | Transparent recent-growth comparator with no distant-history weighting; endpoint noise can matter | Common-origin MAE/RMSE versus Q/E, origin/horizon consistency; extrapolation fixes absolute growth |
| D02: quadratic Q | R02–R04; concentration has constant absolute acceleration | Allows changing growth at one extra coefficient and explains curvature directly | Temporal errors and turning-point/positivity checks; unbounded curvature can dominate 2100 |
| D03: exponential E | R02–R04; constant proportional concentration growth | Different long-run structure from constant growth/acceleration, positive by construction | Original-ppm temporal errors; constant percentage growth of total stock is an empirical assumption, not carbon-cycle mechanics |
| D04: temporal development and final segment | R04,R07; repeated origins with 1–10-year predictions, then one untouched segment | Matches forecasting information order and separates selection from assessment | Freeze receipt and leakage audit; overlapping folds are dependent and supplied vintage is not real-time historical vintage |
| D05: time baseline T0 | R05,R07; linear anomaly trend | Tests whether CO2 linkage improves prediction beyond time | Same origins/targets and anomaly-unit errors; omits climate mechanisms |
| D06: log-CO2 T1 | R05–R07; each proportional CO2 change associates with equal modeled anomaly change | Parsimonious transform permits extrapolating the required relationship | Full pipeline comparison uses predicted future CO2; beta is association, not identified sensitivity |
| D07: shared trends and differences | R06; detrended correlations and first-difference association | Exposes level correlation's dependence on common trends | Compare raw/linear-detrended/quadratic-detrended/difference results; none is a causal identification design |
| D08: empirical error envelope plus sensitivity | R03–R07; historical errors, alternative forms, last-30-year fits | Shows observed uncertainty sources without pretending a long forecast distribution is known | Final envelope misses and forecast/crossing spread; no guaranteed coverage or exhaustive uncertainty |

## Alternatives deferred or rejected for stated reasons

High-degree polynomials add unstable extrapolation without enough independent long-horizon evidence. Logistic growth introduces a saturation capacity not identified by this supplied increasing segment. A carbon-cycle/energy-balance model would require emissions, sinks, forcings, heat-response inputs and externally supported calibration beyond the admitted two series. Large machine-learning searches, large Monte Carlo samples and elaborate causal methods do not supply the missing information. These choices are excluded for task/evidence reasons, not because simple models are universally superior.

A level correlation alone is insufficient for a causal claim. Differencing alone is also insufficient to dismiss long-run physical effects. Both remain descriptive diagnostics alongside a time-only forecast benchmark. Model choices are conditional on this task and sample, not borrowed from historical award papers.

## What can overturn the recommendation

Source incompatibility, inability to reproduce admitted rows, leakage, unidentified or rank-deficient coefficients, invalid required log inputs, nonfinite paths, failed exact examples, or implementation ambiguity returns the affected component for revision before dependent claims. Poor final validation need not invalidate the arithmetic but does invalidate claims of confirmed superiority. If an alternate wins only the final table, report the reversal without silently replacing the frozen primary model. No match to 685 ppm is used as evidence of model quality.

## Decision log to be completed by downstream owners

At architecture stage: coordinator records G1/G2 exact versions and independent verdict; modeler does not fill in acceptance.

At experiment stage: computation writes selected IDs with development scores and hashes before evaluating the final segment. Coordinator/reviewer assess the resulting scope. At G3, accepted claims cite actual result tables, uncertainty and source semantics. The decision remains pending until those artifacts exist; no result or winner is invented here.
