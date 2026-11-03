# A07 independent evidence verdict on weighting sensitivity

Verdict: PASS WITH INTERPRETATION CLARIFICATION, limited to the diagnostic below. The equal-pair and equal-target-year scores, sample counts and ranking reversal are independently reproduced. No revised LaTeX sentence, PDF rendering or font is accepted by this bounded review. A full per-sentence ledger is still pending receipt of the revised source and sentence register.

## Exact evidence and independent method

The primary source is `runs/T05-scientific-20261103-r03/outputs/development_forecasts.csv`, SHA-256 `d82a891af936cbe2865e99c90d3495df3b91311f8dadd5756a245ddfbb29ede4`. All rows for `phase=development`, `target=co2`, and models D, Q and E are included. Each row is status OK and measured in ppm. Every expected origin–horizon key occurs exactly once per model, and `target_year=origin_year+horizon` holds throughout.

A07 wrote `verify-weighting-r01.py` independently. It uses Python standard-library CSV and 50-digit Decimal arithmetic, reconstructing each absolute error from the exported `predicted` and `observed` columns. It does not import or execute A05's script or production code. It then groups those errors by target year and averages within each group before averaging the 30 group means. A separate inverse-multiplicity weighted sum crosschecks the result. Reconstructed errors agree with the stored binary-float error field within ordinary serialization precision, and original pooled scores agree with the frozen selection receipt within 1e-12 ppm. This distinction explains immaterial last-decimal differences in the JSON evidence.

`weighting-verification-r01.json` contains exact SHA-256 identities for every source used, complete year multiplicities, all scores, and induced origin/horizon weights. `weighting-row-evidence-r01.csv` preserves all 150 evaluated CO2 rows, their reconstructed absolute errors, grouping counts and both weights. All pinned inputs were verified unchanged at the end of the computation.

## Formula and exact sample structure

Each model contributes five origins, 1981, 1986, 1991, 1996 and 2001, with ten horizons, 1 through 10, for 50 forecast tasks. There are 30 distinct target years, 1982 through 2011 inclusive. Years 1982–1986 and 2007–2011 each occur once, giving ten single-occurrence years. Years 1987–2006 each occur twice, giving twenty double-occurrence years. Thus 10×1+20×2=50 forecast tasks per model.

For absolute error a(o,h) and the n(y) forecasts targeting year y, the original score is L_pairs = sum a(o,h) / 50. The diagnostic is L_years = sum_y [sum_(o+h=y) a(o,h) / n(y)] / 30. Consequently a single-occurrence row receives diagnostic weight 1/30 and a double-occurrence row receives weight 1/60. All rows originally receive weight 1/50. The diagnostic averages absolute errors, rather than averaging predictions first and then taking an absolute error.

| Loss, ppm | D | Q | E | Lowest |
|---|---:|---:|---:|---|
| Equal origin–horizon tasks | 1.4812200000 | 1.7590314104 | 3.7887582225 | D |
| Equal distinct target years | 1.6103500000 | 1.5228424486 | 3.9444846702 | Q |

D's pooled advantage over Q is 0.2778114104 ppm. Q's target-year-weighted advantage over D is 0.0875075514 ppm. These reproduce the A05 claims at their displayed precision.

## Interpretation and one wording clarification

The original objective is coherent for a study valuing each origin–horizon forecasting task equally. Two forecasts of the same target year use different information sets and horizons. Their inclusion is intentional repeated forecast evaluation, not erroneous duplication. This descriptive loss needs no claim that its 50 errors are independent, although independence would matter for inferential claims. The original specification explicitly acknowledges overlapping targets.

The alternative loss evaluates a different aggregation objective. It does not supply new targets, new validation, a new untouched holdout or evidence of statistical significance. It does not establish future superiority and does not automatically authorize model reselection. The original D selection and sequential temperature-selection design remain unchanged. Because the diagnostic was introduced after assessment exposure, text must explicitly identify it as post-assessment weighting sensitivity.

One A05 phrase needs clarification if reused: calendar weighting does not change the marginal weights of individual horizons in this particular balanced design. Every horizon still has total weight 1/10. It does change origin totals from 1/5 each to 1/4 at origins 1981 and 2001 and 1/6 at origins 1986, 1991 and 1996. It also changes joint origin–horizon weights and calendar-regime weights. Prefer “changes origin and calendar-regime weights” over “changes horizon/regime weights” unless the joint weighting distinction is made explicit. This does not affect A05's numerical result or the defensibility of the original objective.

Recommended report wording, requiring no semicolons:

> Pooled MAE gives equal weight to all 50 origin–horizon forecast tasks, so the 20 target years represented twice receive twice the total weight of the ten years represented once. A post-assessment diagnostic first averages absolute errors within each of the 30 target years and then weights those years equally. It favors Q at 1.52284 ppm over D at 1.61035 ppm, demonstrating sensitivity to the loss weights. The original D selection remains unchanged.

## Scope boundary

This review independently verifies A05-1 only. It does not verify the secondary temperature-error decomposition in A05-2, recalculate the source regressions, revalidate the accepted scientific run, or audit every sentence of the forthcoming LaTeX source. It does not edit the primary selector, accepted-claims register or original artifacts. The original accepted-claims register supplies context and remains separately hash-pinned.
