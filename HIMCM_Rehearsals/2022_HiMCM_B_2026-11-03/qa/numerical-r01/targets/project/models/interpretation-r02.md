# T12 primary-result interpretation r02

**Current binding:** repaired T05 scientific run r03 and closed producer handoff r05 have been consumed. Direct comparison of all 35 outputs found identical scientific fields; only enumerated provenance and explicit unchanged-selector metadata differ. Independent A03/T10 acceptance and G3 remain pending; this author does not self-approve the repairs or claims.

Status: proposed for independent T10 review and G3; not self-accepted. Authority: closed run `T05-scientific-20261103-r03`, manifest SHA-256 `7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00`; closed T05 computation-r05 receipt consumed, SHA-256 `ca0853e2b5433f1ed79fe9ccc5332150bb31dcb80e0a16ffdcca2761f48c2006`. Table names below mean this run's `outputs/` files. Exact paths, hashes, filters and columns are in `claim-evidence-r02.json`. No refitting or model change occurs here.

## 1a — historical increase

In the supplied annual series, the 2004 ten-year increase is **not strictly largest**. The 1994–2004 change is 377.70−358.96=18.74 ppm (1.874 ppm/year), while the prior 1993–2003 interval gives 375.98−357.21=18.77 ppm (1.877 ppm/year). Thus 2004 ranks second among 36 available intervals ending 1969–2004; its margin against the prior maximum is −0.03 ppm. This small arithmetic difference is not a claim of statistical or physical significance. [C01: ten_year_changes.csv; ten_year_comparison.json.]

The statement's March wording conflicts with its annual observations/source. This calculation cannot adjudicate the actual March claim or all periods before the supplied coverage. Say “not largest in the supplied annual series,” never “March 2004 was disproved.” [C02: T01 data-quality finding 1 and source register S03–S05.]

The opening May-2022 claim is separately supported by NOAA's June 2022 release: monthly means 420.99 ppm (NOAA) and 420.78 ppm (Scripps), consistent with rounded 421 ppm. It is a monthly Mauna Loa observation excluded from fitting. [C03: source register S06.]

## 1b — fitted paths

Let x=(year−1959)/10. Production refits through 2021 give these display equations; retain full stored coefficients for calculations:

- D: C=416.45+2.46(year−2021), in ppm: constant recent absolute growth.
- Q: C=315.521509+8.057027x+1.303764x²: constant absolute acceleration.
- E: C=315.98 exp(−0.019627123+0.044917135x): constant proportional growth.

D uses the 2011–2021 endpoints; Q/E use all 63 years 1959–2021. These are contrasting conditional continuations, not physical carbon-cycle mechanisms. Q/E describe the whole historical curve; D is a recent-growth benchmark. [C05: production_coefficients.csv, full CO2 rows.]

Q/E full-history residual RMSEs are 0.720/2.888 ppm, with lag-one residual correlations 0.814/0.979, indicating persistent residual patterns. D's 0.301-ppm fit RMSE covers only 11 points and cannot be ranked against 63-point fit errors as if the samples matched. Temporal errors, not in-sample fit, select the primary rule. [C15: production_fit_diagnostics.csv.]

## 1c — concentrations and first 685-ppm years

| CO2 path |2050 ppm|Gap from 685 in2050, ppm|2100 ppm|First annual central-path year at least 685 ppm|
|---|---:|---:|---:|---:|
|D, development-selected|487.79|−197.21|610.79|2131|
|Q|496.81|−188.19|688.33|2100|
|E|466.29|−218.71|583.70|2136|

None reaches 685 ppm by2050. These are **conditional long extrapolations**, not validated long-term forecasts or probability statements. Raw boundary checks: D has 684.59 in2130 then 687.05 in2131; Q has 683.85754 in2099 then 688.32682 in2100; E has 683.06729 in2135 then 686.14233 in2136. [C06: forecast_summary.csv and thresholds.csv, fit_window=full, target=co2.]

OECD's source value is685 ppm **CO2-equivalent** for greenhouse gases under a conditional baseline; CO2-only source values are about 530 ppm in2050 and 780 ppm in2100. The required pure-CO2 exercise neither validates nor falsifies that different quantity. Source scenario numbers are not fitting targets or model-quality scores. [C04: T01 S07, data-quality finding 4.]

## 1d — accuracy is scope-specific

|CO2 rule|Development MAE, ppm|Final 2012–2021 MAE, ppm|Final RMSE, ppm|
|---|---:|---:|---:|
|D|1.48122|2.14450|2.52491|
|Q|1.75903|1.39841|1.64292|
|E|3.78876|8.24177|8.58429|

**Q is most accurate of the three on the later 2012–2021 assessment. D remains the prespecified pooled-development selection. Neither is established as uniformly most accurate or most accurate in the future.** Preserve the original selector rather than switching after assessment exposure. [C07: development/final_metrics.csv where grouping=overall; selection_frozen.json.]

Q wins three origins (1981, 1996, 2001), D two (1986, 1991). Omitting 1986 or1991 changes the pooled diagnostic winner to Q; omitting other origins retains D. Those additional rank summaries were introduced after adversarial assessment, not made selection criteria. D underpredicts every final CO2 observation and its ten-year error is −4.07 ppm. [C07: rank_stability.csv; final_forecasts.csv.]

## 2a — temperature forecasts and thresholds

The time baseline is T0=−0.170257937+0.168183564x. The full-period association is T=−0.100573219+3.776119820 log(C/315.98), with T in degrees C above 1951–1980. Each T1 pipeline substitutes forecast future C, never actual future C in its score. [C05: production_coefficients.csv.]

|Temperature path|Development MAE, C|Final MAE, C|Eligible for original sequential selection?|
|---|---:|---:|---|
|T0|0.100011|0.124803|Yes|
|T1-D|0.087214|0.093147|Yes; selected|
|T1-Q|0.083687|0.090526|Comparator only|
|T1-E|0.095634|0.121659|Comparator only|

T1-D improves on the specified full-history linear-time baseline on both periods. T1-Q has slightly lower errors across all declared paths, so T1-D is the **selected sequential pipeline**, not the lowest-error model among every temperature comparator. This does not establish unique predictive information from CO2 beyond all representations of time. [C08: metrics, comparison_ranks.csv and frozen eligibility.]

|Conditional annual path|1.25 C year|1.50 C year|2.00 C year|2050 anomaly, C|2100 anomaly, C|
|---|---:|---:|---:|---:|---:|
|T1-D, selected|2036|2048|2076|1.54|2.39|
|T0, time baseline|2044|2059|2089|1.36|2.20|
|T1-Q|2035|2046|2067|1.61|2.84|
|T1-E|2043|2058|2088|1.37|2.22|

These are first integer annual **central-path** crossings against 1951–1980, not first realized warm years, sustained climate crossings or Paris/pre-industrial dates. All lie beyond the ten-year tested horizon from 2021. Dates use raw values: T0's 2088 anomaly is 1.999310 C, below 2 despite rounding to 2.00; first crossing is 2089. [C09: full temperature rows of thresholds.csv and forecast_summary.csv.]

## 2b — relationship since 1959

The two supplied indicators have a strong positive level association, which weakens after removing common trends or examining annual changes.

|Diagnostic|Period/n|Correlation|
|---|---|---:|
|CO2 concentration and anomaly|1959–2021 /63|0.961318|
|log(C/315.98) and anomaly|1959–2021 /63|0.960366|
|Linear-time-detrended log CO2 and anomaly|1959–2021 /63|0.551057|
|Quadratic-time-detrended log CO2 and anomaly|1959–2021 /63|0.491659|
|First differences of log CO2 and anomaly|1960–2021 /62|0.355269|

The level log-CO2 regression has descriptive R²=0.922302. This does not mean CO2 caused 92.2% of warming. Trend removal and differencing change the question and remove low-frequency information; weaker correlation neither disproves physical effects nor identifies them. These series omit forcings, lags and other drivers and pair a station indicator with a global index. No causal parameter or equilibrium climate sensitivity is estimated. The stored 2.61741-C fitted doubling contrast is descriptive only and need not be foregrounded. T1-E is algebraically a straight line in future time, despite different calibration from T0. [C10: relationship_diagnostics.csv; current model spec M04/M08.]

These are full 1959–2021 primary diagnostics. Do not accidentally substitute A02's exploratory through 2011 correlations, which address a different period.

## 2c — extension, tested horizons and reliability limits

The linked extension is already shown for D/Q/E in the temperature table. By2100 its three associated anomalies span 2.21685–2.83946 C; adding the time baseline gives 2.20113–2.83946 C. The CO2 paths span 583.70–688.33 ppm, a104.63-ppm spread, versus 30.52 ppm in2050. These are model-form sensitivities, not confidence bounds or equally probable scenarios. [C13: forecast_summary.csv; structural_sensitivity.csv.]

Historical tests evaluate horizons 1–10 years, with five development origins per horizon. The following final absolute errors refer to forecasts made in2011 and evaluated in2012/2016/2021; they are not observed errors in2022/2026/2031.

|Horizon, years|CO2 development MAE, ppm|CO2 final absolute error, ppm|T1-D development MAE, C|T1-D final absolute error, C|
|---|---:|---:|---:|---:|
|1|0.36420|0.15700|0.093956|0.062471|
|5|1.12300|2.29500|0.084078|0.222292|
|10|2.28000|4.07000|0.053046|0.039622|

Applying the same maximum horizon from 2021 ends the plotted historical-error reference in2031. **2031 is not a validated reliability date.** The tests provide limited conditional evidence within these horizons, not a universal guarantee even for the next decade, and no validation of2050/2100 or later crossing years. There are 50 development origin-target pairs but only 30 distinct target years; overlapping folds and ten final observations are not independent trials. [C11: horizon_evidence.csv; development_forecasts.csv; spec split.]

The selected D empirical envelope contains all 10 final CO2 observations, while T1-D contains 9 of10. In2016, T1-D predicts 0.787708 C versus observed 1.01 C: absolute error 0.222292 C exceeds the fixed 0.197125-C radius by0.025167 C. The miss remains visible and radii are not enlarged after assessment. These containment counts do not estimate a future coverage probability. [C12: historical_error_envelopes.csv; final_forecasts.csv.]

The last 30-observation sensitivity (1992–2021) leaves D unchanged by construction because it still uses the last ten-year change. That is not proof that the whole framework is insensitive to training history. Refitting the temperature association raises its 2050/2100 anomalies from 1.53904/2.38817 to1.64488/2.59910 C and moves threshold dates from 2036/2048/2076 to2033/2044/2068—3, 4 and 8 years earlier. This is sensitivity, not a new chosen model or probability interval. [C13: window_sensitivity.csv; last 30 coefficients.]

Every actual full and declared last 30 path is numerically valid and nondecreasing over 2021–2300; every reported threshold is beyond 2031, with no observed historical exceedance of the requested levels. This verifies the declared calculation domain and crossing statuses, not climate credibility through 2300. Synthetic failure tests, not these all-valid paths, exercise the revised invalid-prefix/later-invalid branches. [C14: path_diagnostics.csv; thresholds.csv; T05 receipt.]

## 3 — implications and required nontechnical deliverable

The article should say what was checked, distinguish source quantities, report conditional projections and show why exact future dates are not established. Recommendations justified here are to preserve consistent measurement definitions/vintages, keep monitoring and reassess forecast errors, compare scenario assumptions, and use emissions/forcing/response evidence before evaluating interventions. These data do not quantify how a particular policy changes CO2, temperature or a crossing date. Proposed summary/article text and forbidden claims are in claim_proposals-r02.md. [C17.]

## Evidence status and unresolved release work

The closed primary run reproduces the attack's consequential findings: CO2 ranking reversal/instability, stronger T1-Q comparator and 2016 envelope miss. The response is narrower claims and transparent comparisons; equations and selector remain unchanged. Source ambiguity is handled by annual/March and CO2-equivalent distinctions. Boundary ambiguity is resolved by explicit status fields, with no actual primary-path invalidity to hide. No new numerical discrepancy was found in author table/receipt checks; independent T10 acceptance remains pending. [C16; C07–C14.]

Primary receipts show local development selection persisted before final scoring and unchanged-rule production refit. A01 had already exposed final scores across agents, so the project cannot claim a globally unseen or blind holdout. The run reports 44 implementation tests and byte-identical reproduction of 32 numerical outputs from 88 recovered dependencies; those are execution/reproducibility evidence, not proof of scientific truth. T05 r05 is the producer receipt for these statements. No final PDF/page-count or G3 acceptance is implied. [C16.]

## r02 binding check

This revision preserves the r01 scientific wording, values, selector and all 17 claim limits while binding tables/columns/hashes to repaired run r03. The author directly compared every output: CSV differences are only run_id; scientific JSON values match; receipt differences are timestamps, code/config/run identifiers, hash chains and the explicit record of the unchanged selector. No numerical field was excluded. New execution totals are 44 test methods and 88 recovered dependencies, with 32 reproduced numerical files; these are producer execution evidence, not new scientific findings.

The selected-ID guard and direct nonpositive-failure counting are substantive execution-contract repairs, even though ordinary result-file differences are provenance and unchanged-selector metadata. This author did not rerun the attacks or refit models. The new packet remains proposed pending independent repair/numerical/claim acceptance and G3. Original r01 documents and run r02 remain preserved.
