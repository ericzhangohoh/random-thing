# Carbon dioxide and temperature: what the supplied record can support

Complete candidate r01

## Page 1: Carbon dioxide and temperature

Claims: C01, C02, C04, C06, C07, C08, C09, C10, C11, C12, C13, C17

Using the supplied annual Mauna Loa CO<sub>2</sub> and global temperature records through 2021, we evaluate historical claims, compare forecast rules and examine how concentration and temperature move together. The ten-year concentration rise ending in 2004 is <b>18.74 ppm</b>, slightly below <b>18.77 ppm</b> ending in 2003. This small arithmetic difference does not establish physical significance, and annual observations cannot settle the statement's March-specific claim.

We compare recent drift (D), quadratic growth (Q) and exponential growth (E) using fixed chronological development forecasts. D minimizes pooled development error, but <b>Q has lower CO<sub>2</sub> error on the later 2012-2021 assessment</b>. Rankings also vary across origins. We retain the prespecified selection and conclude that no uniformly best future model is established.

| Conditional CO2 path | 2050 (ppm) | 2100 (ppm) | First 685-ppm year |
| --- | --- | --- | --- |
| D - selected | 487.79 | 610.79 | 2131 |
| Q | 496.81 | 688.33 | 2100 |
| E | 466.29 | 583.70 | 2136 |

None reaches this pure-CO<sub>2</sub> threshold by 2050. OECD's cited 685 ppm instead measures greenhouse gases as CO<sub>2</sub>-equivalent, so the calculations do not test the same quantity. [6]

The selected sequential temperature path, T1-D, improves on the specified linear-time baseline, although T1-Q has slightly lower errors. T1-D reaches anomalies of <b>1.25, 1.50 and 2.00 degrees C above 1951-1980 in 2036, 2048 and 2076</b>. These are conditional annual central-path crossings, not realized, sustained or Paris-target dates. Alternative models and fitting windows change them. Strong level association weakens after detrending and differencing; it does not identify causation.

Backtests cover at most ten years, and the selected temperature historical-error envelope <b>misses 2016</b>. Thus 2031 is only the corresponding display cutoff, not a validated reliability date. Neither historical envelopes nor model spread provide probability bounds for distant forecasts.

We recommend consistent measurement definitions, continued monitoring, repeated error assessment and comparison of alternative assumptions. Estimating intervention effects requires additional emissions, forcing and response evidence.

## Page 2: A connected answer to the problem

Claims: C05, C16

| Section | Page |
| --- | --- |
| Summary Sheet | 1 |
| Contents and problem approach | 2 |
| 1. Data and source definitions | 3 |
| 2. The 2004 ten-year claim | 4 |
| 3. Concentration models and historical fit | 5 |
| 4. Model comparison and accuracy | 6 |
| 5. Concentration projections and crossings | 7 |
| 6. Temperature model and comparison | 8 |
| 7. Temperature paths and threshold dates | 9 |
| 8. CO2-temperature association | 10 |
| 9. Historical error envelopes and their miss | 11 |
| 10. Horizon evidence and window sensitivity | 12 |
| 11. Strengths, limitations and calculation validity | 13 |
| 12. Direct answers and recommendations | 14 |
| Article for Scientific Today | 15 |
| References and practice/AI disclosure | 16 |

### Approach and scope

The question has three linked tasks: check concentration claims, model the concentration-temperature relationship, and explain the implications to a public audience. We reconcile definitions, then compare simple continuations with chronological forecast tests. Concentration outputs become inputs to the linked temperature extension. [1]

All fitted observations come from the supplied historical workbook. Dates answer the mathematical exercise under explicit continuation assumptions, not an emissions-driven climate model. Tables and figures use the reviewed scientific run; exact evidence bindings and reproducible sources accompany this practice report.

## Page 3: Compare like quantities first

Claims: C02, C03, C04, C05

The supplied workbook is the sole numerical input. Its two sheets contain 63 annual CO<sub>2</sub> observations and 64 annual temperature anomalies. Admission checked every stored cell, printed tables and year keys; no missing values or years, duplicates or nonnumeric observations were found. We preserve the supplied vintage through 2021 rather than substitute revised live data. [1,2]

| Series | Definition and unit | Coverage |
| --- | --- | --- |
| CO2 | Annual dry-air mole fraction at Mauna Loa, Hawaii; ppm | 1959-2021 |
| Temperature | Global land-ocean anomaly; degrees C relative to 1951-1980 | 1958-2021 |
| Joint sample | Inner join on calendar year; 63 matched observations | 1959-2021 |

The temperature-only 1958 observation is retained in its source table but excluded from the common modeling sample. A positional join would mismatch years. Negative anomalies are valid. Mauna Loa is an atmospheric indicator, while temperature is a global index; their spatial definitions differ. NASA's index combines land-air and sea-surface temperature anomalies. [2,5]

### Annual observations do not become March observations

The statement's March caption conflicts with its annual-mean source and supplied values. We interpret the modeling series as annual. It can answer the supported annual comparison but cannot directly verify or disprove a March-specific record or claims about all earlier history. [1,3]

### May 2022 and the OECD benchmark

NOAA's June 2022 release gives May monthly means of 420.99 ppm (NOAA) and 420.78 ppm (Scripps), supporting rounded 421 ppm. This monthly Mauna Loa context is excluded from fitting and validation. [4]

OECD's approximately 685 ppm in 2050 denotes greenhouse gases in CO<sub>2</sub>-equivalent under a conditional baseline. Its separate CO<sub>2</sub>-only levels are approximately 530 ppm in 2050 and 780 ppm in 2100. We retain the requested pure-CO<sub>2</sub> exercise without presenting a mismatch as a test of OECD's different quantity. [6]

> **Temperature baseline**
> The 1.25, 1.50 and 2.00 degree thresholds are above the 1951-1980 mean. No pre-industrial conversion is made; these are not Paris-target dates. [1,5]

## Page 4: The annual 2004 rise was not the largest

Claims: C01, C02

A ten-year interval contains ten elapsed years, so we compare endpoints rather than count ten listed observations. The increase and annualized rate are

Delta<sub>10,t</sub> = C<sub>t</sub> - C<sub>t-10</sub>;     g<sub>10,t</sub> = Delta<sub>10,t</sub>/10.

![<b>Figure 1.</b> All supported ten-year annual changes ending 1969-2004. The two latest windows are nearly equal. Source: accepted ten_year_changes table; observations [2].](/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/figures/F01-r01.png)

| Interval | Endpoint calculation (ppm) | Increase (ppm) | Average (ppm/year) |
| --- | --- | --- | --- |
| 1993-2003 | 375.98 - 357.21 | 18.77 | 1.877 |
| 1994-2004 | 377.70 - 358.96 | 18.74 | 1.874 |

The 2004 window ranks second among the 36 supported intervals ending 1969-2004. Its increase is 0.03 ppm below the earlier maximum ending in 2003. Therefore we do not agree that 2004 is strictly largest <b>in the supplied annual series</b>.

> **What this answer does not establish**
> The 0.03-ppm margin is arithmetic, not evidence of a physically significant difference. Annual data do not settle the actual March assertion, and the supplied coverage cannot test every earlier historical period.

## Page 5: Three concentration continuations

Claims: C05, C15

Write x = (year - 1959)/10 and C<sub>ref</sub> = 315.98 ppm. One x-unit is a decade. Only observations available through each origin enter estimation. Least squares uses a stable SVD solution; full precision is retained for forecasts and crossings. Display coefficients are rounded.

### D: continue recent absolute growth

C<sub>D</sub>(t|2021) = 416.45 + 2.46(t - 2021).

D anchors at the latest concentration and uses average annual growth between 2011 and 2021. Generally, s<sub>o</sub> = (C<sub>o</sub> - C<sub>o-10</sub>)/10 and C<sub>D</sub>(t|o) = C<sub>o</sub> + s<sub>o</sub>(t-o). It is a recent-growth forecast baseline, not an explanation fitted to the whole history.

### Q: continue constant absolute acceleration

C<sub>Q</sub>(t) = 315.521509 + 8.057027x + 1.303764x<super>2</super>.

Q fits concentration to 1, x and x squared. Its quadratic coefficient is not constrained to force acceleration. Turning points and nonpositive extrapolated concentrations must remain visible.

### E: continue constant proportional growth

C<sub>E</sub>(t) = 315.98 exp(-0.019627123 + 0.044917135x).

E fits log(C/C<sub>ref</sub>) to a linear trend. Its fit loss is in log units, but predictive comparisons use ppm. No lognormal error model or mean correction is assumed. Q and E use all 63 years for the production refit.

| Path | Fit years | n | Fit RMSE (ppm) | Lag-one residual r |
| --- | --- | --- | --- | --- |
| D | 2011-2021 | 11 | 0.301 | 0.015 |
| Q | 1959-2021 | 63 | 0.720 | 0.814 |
| E | 1959-2021 | 63 | 2.888 | 0.979 |

Q follows the historical curve more closely than E, but both retain persistent residual patterns. D's smaller fit error covers only 11 observations and cannot be ranked against 63-point errors as if the samples matched. Forecast errors, not this fit table, determine selection.

## Page 6: A selected rule is not a universal winner

Claims: C07, C11, C16

Development origins are 1981, 1986, 1991, 1996 and 2001, each at horizons 1-10. The 50 overlapping origin-target pairs end no later than 2011. Selection minimizes pooled mean absolute error (MAE); RMSE and signed bias describe further behavior. Numerical ties follow D, E, Q.

MAE = mean(|prediction - observation|);     RMSE = sqrt(mean(error<super>2</super>)).

![<b>Figure 2.</b> The later assessment reverses the D-versus-Q ranking. Final predictions originate in 2011 and target 2012-2021 without intermediate refitting. Units are ppm.](/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/figures/F02-r01.png)

| CO2 rule | Development MAE | Final MAE | Final RMSE |
| --- | --- | --- | --- |
| D | 1.48122 | 2.14450 | 2.52491 |
| Q | 1.75903 | 1.39841 | 1.64292 |
| E | 3.78876 | 8.24177 | 8.58429 |

<b>Q is most accurate of these three on the later 2012-2021 assessment. D remains the prespecified pooled-development choice.</b> Q wins three development origins; D wins two. Omitting either 1986 or 1991 changes the pooled diagnostic winner to Q. These post-assessment stability summaries do not replace the original selector.

D underpredicts every final CO<sub>2</sub> observation, with a ten-year error of -4.07 ppm. No uniform superiority or known future winner is established. A separate production step refits unchanged forms through 2021; matching the benchmark is never a selection criterion.

## Page 7: Concentration projections depend on the rule

Claims: C04, C06, C13, C14

![<b>Figure 3.</b> Observations end in 2021; colored lines are full-window conditional extensions. The reference is the requested pure-CO2 threshold, not OECD CO2-equivalent.](/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/figures/F03-r01.png)

| Path | 2050 ppm | 2050 minus 685 | 2100 ppm | First 685 year |
| --- | --- | --- | --- | --- |
| D | 487.79 | -197.21 | 610.79 | 2131 |
| Q | 496.81 | -188.19 | 688.33 | 2100 |
| E | 466.29 | -218.71 | 583.70 | 2136 |

<b>None reaches 685 ppm by 2050.</b> Q first reaches it in 2100, D in 2131 and E in 2136. These are first integer annual central-path crossings under the fitted continuation, not forecasts validated at those dates.

| Path | Previous-year value (ppm) | Crossing-year value (ppm) |
| --- | --- | --- |
| D | 684.59000 | 687.05000 |
| Q | 683.85754 | 688.32682 |
| E | 683.06729 | 686.14233 |

The spread grows from 30.52 ppm in 2050 to 104.63 ppm in 2100. Divergence reflects the absolute-growth, acceleration and proportional-growth assumptions. It is sensitivity across these models, not a probability interval or bound on all plausible futures.

> **Source and horizon caution**
> OECD reports a different quantity, CO2-equivalent. [6] Tests of at most ten-year forecasts cannot validate these distant values. Numerical digits reproduce model arithmetic, not future measurement precision.

## Page 8: Forecast concentration enters the temperature model

Claims: C05, C08, C10

Temperature T is an anomaly in degrees C relative to 1951-1980. We compare a linear-time baseline with a descriptive log-concentration relationship over the same paired training years. Production coefficients through 2021 give

T0(t) = -0.170257937 + 0.168183564x,

T1(C) = -0.100573219 + 3.776119820 log(C/315.98).

T0 measures what this specified full-history linear trend predicts. T1 associates equal proportional concentration changes with equal changes in fitted anomaly. Its slope is not identified climate sensitivity or a causal policy-effect coefficient.

### Validate the entire linked forecast

At origin o, T1's coefficients use observed paired data through o. Future temperature substitutes <b>forecast</b> C from D, Q or E; realized future concentration never enters its score. Temperature error therefore includes upstream concentration error. An invalid path cannot be rescued with future observations.

T1-m(t|o) = alpha<sub>o</sub> + beta<sub>o</sub> log(C<sub>m</sub>(t|o)/C<sub>ref</sub>).

| Temperature path | Development MAE (C) | Final MAE (C) | Original selection role |
| --- | --- | --- | --- |
| T0 | 0.100011 | 0.124803 | Eligible |
| T1-D | 0.087214 | 0.093147 | Selected |
| T1-Q | 0.083687 | 0.090526 | Comparator |
| T1-E | 0.095634 | 0.121659 | Comparator |

The sequential rule first selects D, then compares T0 with T1-D. T1-D wins that eligible comparison. <b>T1-Q has slightly lower errors among all declared comparators.</b> We retain this fact rather than call the selected pipeline a global minimum.

T1-D improves on the specified linear-time baseline in both periods. This does not establish unique CO<sub>2</sub> information beyond every representation of time. Substituting exponential E into T1 gives alpha + beta a + beta b x: a straight line in future time despite different calibration.

## Page 9: Temperature dates are conditional annual crossings

Claims: C09, C13, C14

![<b>Figure 4.</b> Full-window extensions and observed anomalies relative to 1951-1980. Markers label selected T1-D crossings. Every threshold date is beyond the ten-year tested horizon from 2021.](/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/figures/F04-r01.png)

| Path | 1.25 C year | 1.50 C year | 2.00 C year | 2050 C | 2100 C |
| --- | --- | --- | --- | --- | --- |
| T1-D (selected) | 2036 | 2048 | 2076 | 1.54 | 2.39 |
| T0 | 2044 | 2059 | 2089 | 1.36 | 2.20 |
| T1-Q | 2035 | 2046 | 2067 | 1.61 | 2.84 |
| T1-E | 2043 | 2058 | 2088 | 1.37 | 2.22 |

The direct answer for selected T1-D is <b>2036, 2048 and 2076</b>. Alternative concentration assumptions move the linked dates; T0 gives 2044, 2059 and 2089. The last two columns are anomalies, not absolute temperatures.

A crossing is the first integer year after 2021 whose unrounded central-path value reaches the threshold, searched through 2300. It is not the first realized warm year or the start of sustained warming. T0 in 2088 is 1.999310 C, which displays as 2.00 but is below 2; its crossing is correctly 2089.

> **No change of baseline or certainty**
> These dates refer to the 1951-1980 mean, not pre-industrial warming or Paris targets. They are conditional arithmetic, not probability quantiles, established deadlines or validated century-scale forecasts.

## Page 10: A strong association is not causal identification

Claims: C10

![<b>Figure 5.</b> Left: levels with the accepted log-concentration fitted curve. Right: accepted annual changes. The panels answer different descriptive questions; neither establishes causation.](/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/figures/F05-r01.png)

| Diagnostic | Years | n | Correlation |
| --- | --- | --- | --- |
| CO2 level versus anomaly | 1959-2021 | 63 | 0.961318 |
| Log-CO2 level versus anomaly | 1959-2021 | 63 | 0.960366 |
| After linear time detrending | 1959-2021 | 63 | 0.551057 |
| After quadratic time detrending | 1959-2021 | 63 | 0.491659 |
| Annual changes in log-CO2/anomaly | 1960-2021 | 62 | 0.355269 |

The indicators rise together strongly at level. The log-concentration fit has descriptive R-squared 0.922302. This does <b>not</b> mean CO<sub>2</sub> caused 92.2% of warming. Removing separate linear or quadratic time trends weakens the association; annual changes weaken it further.

Detrending and differencing change the question and remove low-frequency information. Weaker correlations neither disprove a physical greenhouse mechanism nor identify its magnitude. Omitted forcings, response delays, serial dependence and the station/global spatial mismatch prevent these two series from isolating cause.

These are the primary 1959-2021 diagnostics (1960-2021 for changes), not earlier exploratory values from a shorter period. We report descriptive relationships without independent-observation p-values or a causal climate-sensitivity interpretation.

## Page 11: The historical envelope misses a later temperature observation

Claims: C11, C12

For the selected pipeline at horizon h, take the largest absolute development error across all five origins and all horizons j no greater than h. This gives a nondecreasing historical error reference:

B<sub>h</sub> = max |error<sub>o,j</sub>|, over development origins o and 1 &lt;= j &lt;= h.

![<b>Figure 6.</b> Fixed development-derived envelopes assessed on forecasts from 2011. The selected temperature path misses 2016. Shading is a historical-error reference, not a calibrated confidence or prediction interval.](/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/figures/F06-r01.png)

| 2016 T1-D assessment | Anomaly/error (C) |
| --- | --- |
| Predicted anomaly | 0.787708 |
| Observed anomaly | 1.010000 |
| Absolute error | 0.222292 |
| Historical radius at horizon 5 | 0.197125 |
| Excess beyond radius | 0.025167 |

D's reference contains all ten later CO<sub>2</sub> observations; T1-D contains nine of ten later temperatures. We retain the 2016 miss and do not enlarge the radius afterward. Ten temporally related checks are not independent trials, and 9/10 containment does not estimate 90% future coverage.

The miss directly contradicts a guaranteed-bound interpretation. We keep it beside the principal temperature forecast, including in the summary and article.

## Page 12: How far can the model be trusted?

Claims: C11, C12, C13, C17

The tests cover only horizons one to ten years, with five development origins per horizon. The final errors below belong to predictions made in 2011 and checked against 2012, 2016 and 2021. They are not measured errors in 2022, 2026 or 2031.

| Horizon | D dev. MAE (ppm) | D final abs. error (ppm) | T1-D dev. MAE (C) | T1-D final abs. error (C) |
| --- | --- | --- | --- | --- |
| 1 | 0.36420 | 0.15700 | 0.093956 | 0.062471 |
| 5 | 1.12300 | 2.29500 | 0.084078 | 0.222292 |
| 10 | 2.28000 | 4.07000 | 0.053046 | 0.039622 |

From 2021, the same ten-year maximum ends in 2031. <b>This is a tested-horizon display cutoff, not a validated reliability date.</b> There are 50 development pairs but only 30 distinct target years. Dependence and the small final sample limit generalization. No accuracy tolerance supplied by the question identifies a universal reliable-through year.

### Sensitivity to the fitting window

The predeclared sensitivity refits selected forms on 1992-2021. D is unchanged because its last-ten-year rule is unchanged; this does not establish robustness of the whole linked framework. The refitted T1-D association changes:

| Selected T1-D quantity | Full history | Last 30 observations |
| --- | --- | --- |
| 2050 anomaly (C) | 1.53904 | 1.64488 |
| 2100 anomaly (C) | 2.38817 | 2.59910 |
| 1.25 C first year | 2036 | 2033 |
| 1.50 C first year | 2048 | 2044 |
| 2.00 C first year | 2076 | 2068 |

Dates move 3, 4 and 8 years earlier. This is not a new chosen model, confidence interval or retuned selector. Form changes also matter: linked 2100 anomalies span 2.21685-2.83946 C; adding T0 gives 2.20113-2.83946 C.

> **Practical reliability answer**
> Use short-horizon errors as limited conditional evidence and reassess as observations arrive. All 2050/2100 values and distant crossings depend on continuation assumptions; neither this sample nor the envelopes establishes a guaranteed reliable horizon.

## Page 13: Strengths, limits and validity checks

Claims: C05, C13, C14, C15

### What the architecture does well

The models are transparent, use few parameters and represent distinct continuation assumptions. Evaluation respects information available at each origin. Linked temperature scores include concentration forecast error. A fixed selector, explicit alternatives, residual diagnostics and adverse results make the answer inspectable rather than dependent on a single fitted curve.

| Assumption or design choice | Consequence for interpretation |
| --- | --- |
| Recent growth persists (D) | Endpoint growth can be unrepresentative; later errors expose underprediction. |
| Constant acceleration (Q) | Curvature can dominate distant behavior; a better later score does not certify 2100. |
| Proportional stock growth (E) | An empirical continuation, not an emissions/sink mechanism. |
| Static log-CO2 association (T1) | Omits lags and other drivers; coefficient is descriptive, not causal. |
| Retrospective supplied vintage | Tests do not recreate the exact data vintage available to historical forecasters. |
| Overlapping test origins | No independent-trial or calibrated probability interpretation. |

### Mathematical validity is narrower than credibility

All actual full and declared last-30 paths are finite, valid and nondecreasing over the annual search domain 2021-2300. Reported crossings satisfy unrounded boundaries; the supplied history never exceeds the requested levels. These facts establish calculation status, not climate credibility through 2300.

First-passage inference uses only the contiguous valid prefix from the origin. A crossing before later invalidity is retained with a warning; invalidity before crossing blocks a date. Already-above-origin and valid non-crossing-through-2300 cases have different statuses. No later valid segment bridges an invalid gap.

### Why not simply add complexity?

High-degree curves add extrapolation flexibility without long-horizon evidence. A logistic capacity is not identified by this rising record. Physical carbon-cycle and energy-balance models need emissions, sinks, forcing and response inputs absent from the two supplied series. These justify a bounded exercise, not an exhaustive-model claim.

## Page 14: Conclusions and conditional recommendations

Claims: C01, C02, C04, C06, C07, C08, C09, C10, C11, C12, C13, C17

| Question | Answer within the available evidence |
| --- | --- |
| 1.a | 2004 is second among supplied annual windows: 18.74 versus 18.77 ppm. The March-specific assertion remains untested. |
| 1.b | D, Q and E represent recent growth, constant acceleration and proportional growth; fitted forms and limitations are in Section 3. |
| 1.c | All are below 685 ppm in 2050. D/Q/E give 2100 values 610.79/688.33/583.70 ppm and first annual crossings 2131/2100/2136. |
| 1.d | Q has the lowest later 2012-2021 error; D remains the development selection. No uniformly best future rule is established. |
| 2.a | Selected T1-D reaches 1.25/1.50/2.00 C above 1951-1980 in 2036/2048/2076, conditional on continuation. |
| 2.b | Strong level association weakens after trend removal and differencing; it does not identify causation. |
| 2.c | All linked extensions are given. Tests cover at most ten years, include a 2016 miss and establish no guaranteed reliable-through date. |

### Use the findings without overstating them

<b>Keep measurements comparable.</b> Preserve the annual/monthly distinction, temperature baseline, data vintage and CO<sub>2</sub>-equivalent definition before interpreting a quoted number.

<b>Monitor performance and compare assumptions.</b> Preserve the chosen rule for an honest assessment, track later errors and show competing paths. Ranking reversals and envelope misses should prompt reassessment, not disappear.

<b>Use more evidence for intervention decisions.</b> Planning can compare conclusions under different assumptions. Quantifying a policy's effect requires emissions, forcings, sinks and response dynamics that these two records do not identify.

These recommendations follow from definition conflicts, ranking instability and extrapolation sensitivity. We do not estimate a specific intervention's benefit or assign probabilities to distant scenarios.

## Page 15: Climate numbers need more than a date

Claims: C01, C02, C03, C04, C06, C07, C08, C09, C10, C11, C12, C13, C17

A concentration figure can be accurate yet answer the wrong question. We examined the records supplied through 2021 for a mathematical modeling exercise, beginning with what each number measures.

The supplied CO<sub>2</sub> values are annual Mauna Loa averages, despite the question's reference to March. Their ten-year rise ending in 2004 was 18.74 parts per million, slightly below 18.77 ppm ending in 2003. That small difference does not settle the separate March claim. NOAA's source supports about 421 ppm for the monthly average in May 2022; this later observation was not used to fit our models. [1-4]

Three simple extensions of past concentration changes produce roughly <b>466-497 ppm in 2050</b> and <b>584-688 ppm in 2100</b>. None reaches 685 ppm by 2050. This does not refute OECD: its cited figure combines greenhouse gases as CO<sub>2</sub>-equivalent, rather than measuring CO<sub>2</sub> alone. [6]

The model changes the answer. A recent-growth rule performed best in our planned development comparison, but a quadratic curve performed better on the later 2012-2021 assessment. Neither has demonstrated universal superiority. We retain the original selection rather than choose again after seeing those errors.

Our selected temperature path, driven by recent-growth CO<sub>2</sub>, reaches <b>1.25, 1.50 and 2.00 degrees C above the 1951-1980 average in 2036, 2048 and 2076</b>. Driving the same relationship with the quadratic concentration path gives slightly smaller errors. Other models and fitting periods move the dates. These are conditional paths, not established deadlines, sustained warming dates or Paris targets. The observed association also does not isolate cause.

Tests extend only ten years ahead, and the temperature error reference <b>missed 2016</b>. They establish no guaranteed reliability date or probability for a century-scale projection.

The useful response is continued measurement, consistent definitions and regular comparison of forecasts with observations. Planning should examine several assumptions. Evaluating interventions additionally requires evidence on emissions, other climate drivers and response delays; these two records cannot quantify policy benefits.

## Page 16: Sources and reproducible practice

Claims: C16

[1] COMAP. 2022 HiMCM Problem B: CO2 and Global Warming. Official four-page statement supplied in the local archive, 2022. Requirements p. 1; delivery rules p. 2; data and source notes pp. 3-4.

[2] COMAP. 2022_HiMCM_Data.xlsx. Supplied CO2 Data Set 1 and Temps Data Set 2, 2022 vintage. Sole numerical modeling input. Admission records and source hashes are retained with this practice project.

[3] NOAA Global Monitoring Laboratory / Scripps. Trends in atmospheric carbon dioxide: data definitions, annual and monthly Mauna Loa series. Definition snapshots inspected 3 November 2026; current observations excluded from modeling. <link href='https://gml.noaa.gov/ccgg/trends/data.html' color='#176A73'>gml.noaa.gov/ccgg/trends/data.html</link>

[4] NOAA. Carbon dioxide now more than 50% higher than pre-industrial levels. 3 June 2022. Monthly May concentration/site context only. <link href='https://www.noaa.gov/news-release/carbon-dioxide-now-more-than-50-higher-than-pre-industrial-levels' color='#176A73'>NOAA news release</link>

[5] NASA Goddard Institute for Space Studies. GISTEMP frequently asked questions: anomaly baseline and land-ocean temperature index. Definition snapshot inspected 3 November 2026. <link href='https://data.giss.nasa.gov/gistemp/faq/' color='#176A73'>data.giss.nasa.gov/gistemp/faq/</link>

[6] OECD. OECD Environmental Outlook to 2050: The Consequences of Inaction. OECD Publishing, 2012. Chapter 3, especially printed p. 83, and baseline definition. Primary report text inspected; selected evidence retained as labeled excerpt/paraphrase rather than an original downloaded PDF. <link href='https://www.oecd.org/content/dam/oecd/en/publications/reports/2012/03/oecd-environmental-outlook-to-2050_g1g14e69/9789264122246-en.pdf' color='#176A73'>Official OECD report</link>

### Practice and AI use

This is a retrospective exercise, not a live entry or external submission. Codex collaboration sessions carried out coordination, source/data admission, modeling, computation, writing/visuals and independent review, with some roles operating sequentially. The user delegated reversible practice decisions to the coordinator; no human checkpoint response or Claude Code execution is invented.

The companion project retains source/model versions, commands, fixed outputs and claim bindings. Scientific run T05-scientific-20261103-r03 supplies this report. Independent numerical review accepted this run and scoped claims. Plots and tables read accepted outputs without refitting. Writer rendering checks are author self-checks, not independent PDF acceptance.

### Evaluation exposure and repairs

Candidate forms and the selector were fixed before adversarial final-score exposure. An adversarial reviewer nevertheless examined 2012-2021 scores before the primary selection receipt. The primary run retained local selection-before-assessment order, but the project has no globally unseen or blind holdout. Later interpretation and implementation safeguards are post-exposure repairs, not a fresh evaluation.

Earlier failed artifacts and repaired versions are retained. The producer reports 44 implementation tests and byte-identical reproduction of 32 numerical outputs from 88 recovered dependencies; these are execution evidence, not proof of future accuracy. Separate recovery and final PDF review have their own acceptance records; this report does not claim their completion in advance.
