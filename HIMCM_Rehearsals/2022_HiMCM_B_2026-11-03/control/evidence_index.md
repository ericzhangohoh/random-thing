# Accepted evidence index

Current science: G3-r01, repaired primary T05-scientific-20261103-r03. Full row selectors, columns, values, SHA-256 and limits: [accepted claim register](accepted-claims-g3-r01.json). [Writing input identities](accepted-writing-inputs-r01.json).

| Claim | Requirements | Scope | Evidence files |
|---|---|---|---|
| C01 | R01 | The supplied annual 2004 ten-year rise is18.74 ppm versus prior maximum 18.77 ppm ending 2003;2004 ranks second. | `ten_year_changes.csv`, `ten_year_comparison.json` |
| C02 | R01, R10 | The supplied annual series cannot directly test the March-specific assertion or all earlier history. | `research/data-quality-r01.md` |
| C03 | R08 | Source-reported May 2022 monthly means support rounded 421 ppm. | `research/source-register-r01.md` |
| C04 | R03, R08 | The cited OECD 685 ppm denotes CO2-equivalent, whereas this exercise computes pure CO2 paths. | `research/source-register-r01.md` |
| C05 | R02, R05 | D/Q/E and T0/T1 use the declared equations and fitted parameters through 2021. | `production_coefficients.csv` |
| C06 | R03 | D/Q/E give 2050=487.79/496.81/466.29 ppm, 2100=610.79/688.33/583.70, 685 crossings 2131/2100/2136. | `forecast_summary.csv`, `thresholds.csv` |
| C07 | R04 | D is pooled-development selection; Q has best final CO2 score; origin ranks are unstable. | `development_metrics.csv`, `final_metrics.csv`, `rank_stability.csv`, `selection_frozen.json` |
| C08 | R05, R07 | Selected sequential T1-D beats the specified T0 baseline, while T1-Q is a slightly better declared comparator. | `development_metrics.csv`, `final_metrics.csv`, `selection_frozen.json` |
| C09 | R05 | Selected T1-D central-path thresholds occur in2036/2048/2076; alternate paths give different years. | `thresholds.csv`, `forecast_summary.csv` |
| C10 | R06 | Level association is strong but lower after detrending/differencing. | `relationship_diagnostics.csv` |
| C11 | R07 | Tests cover horizons 1–10;2031 is only the corresponding display cutoff from 2021. | `horizon_evidence.csv`, `development_forecasts.csv` |
| C12 | R07 | The selected temperature historical envelope misses 2016 by0.025167 C beyond its radius. | `historical_error_envelopes.csv`, `final_forecasts.csv` |
| C13 | R03, R05, R07 | Form and window changes materially alter distant levels/dates. | `structural_sensitivity.csv`, `window_sensitivity.csv` |
| C14 | R05, R07 | Actual calculated paths are valid/nondecreasing in the declared annual domain and crossing boundaries are satisfied. | `path_diagnostics.csv`, `thresholds.csv` |
| C15 | R02, R07 | Residual patterns and unequal baseline fit windows limit naive fit comparisons and independent-error claims. | `production_fit_diagnostics.csv` |
| C16 | R10, R11 | Local execution retained original selection order and reproducible evidence, while A01 already exposed final scores. | `selection_frozen.json`, `final_assessment_receipt.json`, `handoffs/T05/computation-r05.md` |
| C17 | R08 | Use consistent measurements, monitor forecast errors and assess multiple scenarios; intervention effects need additional evidence. | `reasoned implication` |

Paper locations and final PDF hash will be added at delivery. Scientific acceptance does not imply rendered-export or external-submission acceptance.

## Accepted PDF delivery, 2026-11-04 Australia/Sydney

Exact acceptance: [delivery-acceptance-r01.json](delivery-acceptance-r01.json). [Final16-page paper](../paper/exports/2022_HiMCM_B_practice-complete-r03.pdf); [T11 all-page review](../qa/pdf-review-r00/review.md); [A04 claim attacks](../qa/adversarial_paper/r01/review.md); [T13 recovery review](../qa/recovery-review-r01/review.md).

- PDF page 1: C01, C02, C04, C06, C07, C08, C09, C10, C11, C12, C13, C17.
- PDF page 2: C05, C16.
- PDF page 3: C02, C03, C04, C05.
- PDF page 4: C01, C02.
- PDF page 5: C05, C15.
- PDF page 6: C07, C11, C16.
- PDF page 7: C04, C06, C13, C14.
- PDF page 8: C05, C08, C10.
- PDF page 9: C09, C13, C14.
- PDF page 10: C10.
- PDF page 11: C11, C12.
- PDF page 12: C11, C12, C13, C17.
- PDF page 13: C05, C13, C14, C15.
- PDF page 14: C01, C02, C04, C06, C07, C08, C09, C10, C11, C12, C13, C17.
- PDF page 15: C01, C02, C03, C04, C06, C07, C08, C09, C10, C11, C12, C13, C17.
- PDF page 16: C16.
