# A05 independent model attack: canonical corrected review r02

**Verdict: ACCEPTED_FOR_SCOPE, with one new advisory sensitivity result independently verified by A07 and this reviewer’s corrected weighting interpretation.** No new blocking or consequential incorrect claim was established in the original manuscript/specification. This does not accept the forthcoming LaTeX text or its rendering. The architecture remains defensible for the bounded empirical exercise if its existing qualifications survive revision.

Reviewer: `/root/latex_model_attack`, a new independent reviewer for this phase, not A01/A02/A04 renamed. Prior reviews were read to distinguish repaired issues from new evidence, not treated as correctness proof. Only owned `qa/latex-attacks/model-r01/` and `handoffs/A05/` were written. No original edits, Git operations, installation, external source retrieval, or new primary fit occurred.

## Exact targets and scope

`target-hashes-r01.json` pins 21 exact original source/review/result identities. Principal targets:

- Manuscript `paper/manuscript-complete-r03.md`: `76c9b3de561214a0bd970c17afe95335f0559e31c8f35950dbea345177fe1616`.
- Specification `models/model_spec-r02.md`: `ba81a65550193a8775f2275224329d6bad339191ffccf4cf33c9a1094ea1c796`.
- Scientific manifest: `7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00`.
- Original PDF: `27182592954ee011e2c9f94b7c9a86465b3be44e3fba94d7ab1e3e3c3ef39573`. Its bytes were hashed; this reviewer did not render or visually inspect the PDF.

Inspected the specification, relevant decisions/experiment wording, accepted interpretation/claims, original manuscript text and prior structure/validation/numerical/paper reviews. Executed `python3 qa/latex-attacks/model-r01/probe-r01.py`, using Python standard-library CSV/math/aggregation, not production model imports. It independently recomputes pooled and diagnostic losses, decomposes 180 linked-temperature error rows, and verifies pinned inputs remain unchanged. `probe-results-r01.json` and `decomposition-r01.csv` preserve results. A separate direct inverse-multiplicity weighted sum reproduced the diagnostic at tolerance 1e-14 and checked 50 pairs/30 target years per model. No original-data regression, new model, boundary solver, source web verification or full implementation audit was performed.

## A05-1: target-year weighting reverses the development ranking

**Classification: advisory extension of disclosed rank instability, not a duplicate-data bug or selector error.** The original paper correctly states that 50 overlapping pairs comprise 30 target years and denies independence. Their loss-weighting consequence is less explicit: target years 1987–2006 each enter twice, while 1982–1986 and 2007–2011 each enter once.

Exact input: `runs/T05-scientific-20261103-r03/outputs/development_forecasts.csv`, SHA-256 `d82a891af936cbe2865e99c90d3495df3b91311f8dadd5756a245ddfbb29ede4`; use rows for each of D/Q/E, fields `origin_year`, `target_year`, `horizon`, `error`. Each model has exactly 50 rows, with 30 distinct target years and the same multiplicity distribution: 20 years with two rows and 10 with one. No rows are omitted.

Let `A_y = (1/n_y) sum_{o: o+h=y} |error_(o,h)|`, where `n_y` is that target year's forecast count. The post-assessment diagnostic is `L_calendar = (1/30) sum_y A_y`: average absolute error per target year, then mean across the 30 target years. This differs from the declared `L_pairs = (1/50) sum_(o,h) |error_(o,h)|`.

| Development MAE, ppm | D | Q | E | Lowest |
|---|---:|---:|---:|---|
| Declared equal origin–target pair weight | 1.4812200000 | 1.7590314104 | 3.7887582225 | D |
| Diagnostic equal target-year weight | 1.6103500000 | 1.5228424486 | 3.9444846702 | Q |

**Importance:** the selected label depends on the precise forecast loss. Central overlapping calendar regimes receive twice the total weight of edge regimes under pair pooling. The declared 0.277811-ppm D advantage becomes a 0.087508-ppm Q advantage under this diagnostic. Neither difference has a significance, independence or future-superiority interpretation.

**Strongest defense:** equal forecast-task weighting is a coherent stated objective when each origin–horizon forecast counts equally. The two forecasts for a year have different information sets/horizons, so they are not duplicate observations erroneously introduced by a join. Calendar weighting answers a different question and changes origin, calendar-regime and joint origin–horizon weights. In this balanced design, each marginal horizon weight remains exactly 1/10. Origin weights change from 1/5 each to 1/4 for 1981 and 2001 and 1/6 for 1986, 1991 and 1996. It is not a uniquely correct replacement objective. The original paper already calls D the prespecified pooled-development choice and denies uniform superiority; the new result strengthens that limitation without invalidating it.

**Minimal honest improvement, proposed bounded text:** “Pooled MAE gives equal weight to all 50 origin–horizon forecast tasks, so the 20 target years represented twice receive twice the total weight of the ten years represented once. A post-assessment diagnostic first averages absolute errors within each of the 30 target years and then weights those years equally. It favors Q at 1.52284 ppm over D at 1.61035 ppm, demonstrating sensitivity to the loss weights. The original D selection remains unchanged.” If space is constrained, retain the qualitative weighting explanation and keep the numerical diagnostic in supporting evidence.

**Recheck criterion:** A07 has independently verified the pinned CSV, formula, count distribution and all three scores. Any adopted manuscript text still needs to retain the post-assessment diagnostic label and exact scope. D must remain the original selection. Do not call this fresh validation, a predeclared comparison, or an automatically accepted G3 claim. No primary production rerun is requested.

## A05-2: composed error and calibration drift

For every linked forecast, independently checked the identity

`e_T = [alpha_o + beta_o log(C_observed/C_ref) - T_observed] + beta_o log(C_forecast/C_observed)`.

The first bracket is the fitted association's error using realized concentration; the second is upstream forecast error propagated through the log link. Realized concentration is used only for this ex-post algebraic diagnostic, never as an operational forecast or eligible comparator. All 180 identities passed absolute tolerance 1e-12.

For selected T1-D, development mean error -0.037439°C decomposes into -0.028011°C association error and -0.009428°C upstream contribution. Final mean error -0.058386°C decomposes into -0.039227°C and -0.019159°C. These mean errors reinforce each other, so the attack that T1-D's mean error is hidden by systematic cancellation is not sustained. Local cancellation reduces absolute error in 15/50 development and 4/10 final rows. T1-Q's development upstream contribution +0.015416°C offsets part of the common negative association bias, illustrating why lowest CO2 MAE need not minimize temperature MAE. The original sequential-selection disclosure and end-to-end scoring already handle that distinction.

Stored beta varies across development origins (3.009519–3.706168); final beta is 3.646341, 2021 full beta 3.776120, and last30 beta 4.243437. These dependent refit differences do not prove a structural break. The original paper already reports resulting threshold-window sensitivity. **Disposition:** no consequential new defect; no mandatory repair. Preserve static-association/window caveats and avoid promising that improved CO2 forecasts alone validate temperature predictions. This secondary diagnostic need not be added to the paper.

## Other attacks and defenses

| Challenge | Evidence and disposition | Minimal repair/recheck |
|---|---|---|
| Selector versus distant outputs | h=1–10 loss does not validate 2050/2100 or threshold dates, and the paper says so. D remains best development CO2 model for h=1–3, h=8–10 and h=10 subsets; Q remains best on those final subsets. | No new defect. Preserve loss/horizon labels and conditional extrapolation. Long-horizon evaluation is future work, not permission to switch after exposure. |
| Deployment versus backtest | Final scores are explicitly a single 2011 issuance without intermediate refitting; production is a separate 2021 refit. Reassessment as observations arrive is a recommendation, not a tested annual updating algorithm. Vintage limitation is stated. | No false operational claim found. Optional clarification: scores measure fixed-origin multi-step forecasts, not a continuously updated service. |
| Time-baseline fairness | T0/T1 use the same paired years and targets; the claim is expressly relative to specified full-history linear T0. T1-E's future-time linear equivalence is disclosed. | No new defect. Preserve comparator-specific/noncausal wording; no arbitrary candidate enlargement is required. |
| Dependent uncertainty | Historical maximum radius is not called probabilistic; 2016 miss and 50-pair/30-year dependence remain explicit. | Preserve those limits; do not infer 90% coverage or add independence-based standard errors. |
| Source/benchmark inference | Annual/March, station/global, CO2/CO2-equivalent and monthly May definitions are distinguished. Accepted source interpretation was inspected; source retrieval was not independently repeated. | No model inference defect found. Do not turn OECD mismatch into a model-accuracy score or tune to it. |
| Threshold validity | Central annual path, raw-value crossing, 1951–1980 baseline, valid-prefix semantics and extrapolation limitations are explicit. | No overlooked claim defect established. Boundary implementation was not rerun in this pass. Preserve non-realized/non-persistent interpretation. |

## Handoff

The strongest new result is objective sensitivity to calendar-year weights. It adds useful evidence without proving the declared objective erroneous. A07 has independently verified A05-1. Root owns acceptance of any new C18 post-assessment diagnostic claim. No primary selector change is justified by this report. Later revised-text recheck is required; this report does not transfer acceptance automatically to new LaTeX/PDF bytes or certify fonts.

## r02 correction and independent recheck

This revision supersedes r01 only as the canonical A05 interpretation and preserves r01 unchanged. A07 correctly identified an error in r01’s claim that horizon weights change indirectly. The diagnostic changes joint origin–horizon weights, but the marginal weights of individual horizons do not change in this particular design. The incorrect phrase is removed above. No diagnostic score or model-selection result changes.

Read `qa/latex-attacks/evidence-r01/weighting-review-r01.md`. Independently executed `python3 qa/latex-attacks/model-r01/check-marginals-r02.py`, which reconstructs exact rational weights from the original accepted CSV using `fractions.Fraction` without importing A07’s code or the A05 r01 probe. It verifies for D, Q and E that all ten horizon totals remain 1/10, while origin totals become 1/4, 1/6, 1/6, 1/6, 1/4 in chronological order. The original marginal weights were 1/10 per horizon and 1/5 per origin. Diagnostic joint-task weights are 1/30 or 1/60, replacing 1/50. Full exact weights are retained in `marginal-weights-r02.json`. This is an interpretation correction to the post-assessment diagnostic, not new forecast validation.

A07’s independent acceptance covers A05-1’s scores/counts and clarified meaning. It does not accept the secondary decomposition, forthcoming LaTeX sentences, rendering or fonts. Root may register only the bounded post-assessment C18 claim, with the original D selection unchanged. The proposed adopted text above contains no semicolon.
