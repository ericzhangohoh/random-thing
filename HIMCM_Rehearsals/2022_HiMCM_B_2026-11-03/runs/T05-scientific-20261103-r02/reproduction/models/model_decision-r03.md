# Model decisions r03 — preserved selector, narrowed claims and crossing contract

T06/modeler; 2026-11-03. Read framing/specification/interface/experiment r02 and unchanged assumptions r01. Independent adversarial scores are exposed; no accepted primary-run result is asserted. Original equations, splits and selector remain unchanged.

## G1 recommendation

Adopt the supplied-vintage, annual, common-year interpretation and complete every official subquestion. Distinguish Mauna Loa from a global spatial sample, anomaly from absolute temperature, annual from March, and CO2 from CO2-equivalent. T01 source evidence supports these distinctions; coordinator must record accepted source hashes. Preserve the requested 685-ppm pure-CO2 exercise even though it cannot validate the source's different greenhouse-gas quantity. Alternative: reconstruct March observations from an external series. That changes the supplied-data task and vintage and is unnecessary for this bounded rehearsal.

## G2 recommendation

Retain the previously released deterministic architecture below. Proposed r02 changes require independent review of interpretation and crossing-status semantics, followed by G2 r02 coordinator release. Freeze model selection on pre-2012 development forecasts before final assessment. This proposes an experiment; it does not preselect Q, E or D. G1/G2 disposition is DELEGATED_PRACTICE_DECISION under intake, recorded by coordinator, not a fabricated human approval.

| Decision | Requirement and representation | Why it is a serious choice | Discriminating evidence and limitation |
|---|---|---|---|
| D01: recent drift baseline D | R02–R04; latest level plus recent ten-year average growth | Transparent recent-growth comparator with no distant-history weighting; endpoint noise can matter | Common-origin MAE/RMSE versus Q/E, origin/horizon consistency; extrapolation fixes absolute growth |
| D02: quadratic Q | R02–R04; concentration has constant absolute acceleration | Allows changing growth at one extra coefficient and explains curvature directly | Temporal errors and turning-point/positivity checks; unbounded curvature can dominate 2100 |
| D03: exponential E | R02–R04; constant proportional concentration growth | Different long-run structure from constant growth/acceleration, positive by construction | Original-ppm temporal errors; constant percentage growth of total stock is an empirical assumption, not carbon-cycle mechanics |
| D04: temporal development and final segment | R04,R07; repeated origins with 1–10-year predictions, then final-segment assessment under the unchanged frozen rule | Matches forecasting information order and separates selection from assessment | Freeze receipt and leakage audit; overlapping folds are dependent and supplied vintage is not real-time historical vintage |
| D05: time baseline T0 | R05,R07; linear anomaly trend | Compares CO2 linkage with the specified linear-time baseline | Same origins/targets and anomaly-unit errors; omits climate mechanisms |
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

## D09 — response to A01/A02 evidence (post-assessment amendment)

Accept A01's narrow R04 objection: precommitment protects selection integrity but cannot convert a pooled-development winner into a universally most accurate model. Independent probes report D selected in pooled development, Q better in final CO2 MAE and at three origins, and leave-one-origin-out instability. These are adversarial results pending primary reconciliation, not primary publication numbers. Preserve D if the unchanged selector reproduces it; report the final challenger and lack of stable uniform superiority.

The selected temperature model belongs to the specified sequential design; it is not necessarily the lowest-MAE path among all T1 alternatives. A02's limited omitted time comparators did not overturn T1-D but do not prove unique predictive information from CO2. Do not add their exploratory candidates to the frozen set. Preserve the algebraic fact that T1-E is linear in future time and all slopes are descriptive.

Retain the historical-error envelope definition but require explicit misses and observed errors. A01's T1-D 2016 miss is a counterexample to a guaranteed error bound, not a reason to resize it using final data. The 2031 endpoint is the maximum tested-horizon display cutoff, not an accuracy certification. The repair adds rank/envelope reporting, not a new calibrated uncertainty method.

## D10 — crossing event versus domain validity

Accept computation's proposed distinction. An established first annual crossing on a contiguous valid prefix remains CROSSED even if a later segment fails. Full-domain validity and first-invalid year/reason are separate mandatory outputs. Failure before or at an apparent crossing yields INVALID_PATH; later valid re-entry does not erase that gap. A valid already-above origin has its own status. This removes implementation ambiguity without changing model equations, forecast values or tested-horizon definition. Source/metric/model selections remain frozen; branch tests and independent re-review are required.

## Exposure and release conditions

A01 numerical use of final2012–2021 precedes primary T05 receipt. This author has read those outcomes; no global holdout-unseen claim may be made. Local primary ordering still tests implementation of the original pre-exposure selector. New rank-stability summaries are explicitly post-assessment diagnostics; future model redesign would require new validation. Primary claims remain pending numerical reconciliation and independent acceptance. No source-table edit, winner switch or fictional gate approval is part of r02.
