# Carbon dioxide and temperature: what the supplied record can support

DRAFT / PENDING RESULTS | Phase A - r02

## Page 1: Carbon dioxide and temperature

SUMMARY SHEET - DRAFT

What the supplied record can support

> **PENDING_EVIDENCE: export checkpoint only**
> This is a methods and layout draft, not a completed scientific solution. Primary forecast results, threshold dates and final recommendations have not been released. The draft demonstrates the actual PDF export and preserves the boundaries required for later results.

The task asks whether a reported ten-year CO<sub>2</sub> increase was unprecedented, how different mathematical models extend atmospheric concentration, and how concentration relates to global land-ocean temperature. We organize the answer around what each comparison can establish, rather than treating a good historical fit as proof of a distant forecast. [1]

The supplied workbook is the sole modeling input. It contains annual Mauna Loa CO<sub>2</sub> observations and a global temperature anomaly series through 2021. The temperature reference period is 1951-1980. Source checking separates annual observations from the statement's March wording, and the requested 685-ppm pure-CO<sub>2</sub> exercise from OECD's different CO<sub>2</sub>-equivalent quantity. [1-6]

Three concentration paths represent recent constant growth, constant acceleration and constant proportional growth. A time-only temperature baseline is compared with a log-CO<sub>2</sub> relationship driven by forecast concentration. The comparison uses fixed chronological origins and assesses the complete linked forecast, including its concentration error.

### Findings to be inserted after scientific release

- The annual ten-year comparison, with its March-specific limitation.
- Every concentration candidate's 2050 and 2100 values and first 685-ppm crossing.
- Selected-rule and final-period rankings, including instability and competing temperature paths.
- Temperature threshold dates, relationship diagnostics, observed envelope misses and conditional recommendations.

The final summary will distinguish the rule selected on development errors, the best score on the later assessment and unknown future accuracy. Dates from an extrapolated central path will not be described as guaranteed outcomes or as pre-industrial warming thresholds.

## Page 2: Contents and draft status

NAVIGATION

| Section | Page |
| --- | --- |
| Summary Sheet - draft | 1 |
| Contents and draft status | 2 |
| 1. Data, definitions and source claims | 3 |
| 2. CO2 models and the ten-year comparison | 4 |
| 3. Temporal comparison and evaluation exposure | 5 |
| 4. Temperature, association and reliability | 6 |
| 5. Required result slots and article boundary | 7 |
| References and practice disclosure | 8 |

### What is complete at this checkpoint

The source definitions and original model equations have been released for this rehearsal. This draft provides the data interpretation, mathematical representations, evaluation design and reporting safeguards. All primary numerical conclusions remain pending; no independent adversary's probe result is substituted for a reviewed production result.

### What remains before a complete solution

The next revision must consume the exact accepted production run, revised model interpretation and independent numerical review. It must add the complete forecast and threshold tables, figures, direct answers, one-page article and a result-bearing summary. The intended finished report is approximately 14-18 readable pages, with every page counted toward the official maximum of 25. [1]

> **Evidence status**
> PENDING_EVIDENCE labels identify unfinished claims. They are intentionally visible in this checkpoint and must be resolved before a final candidate is released. Page numbers in this contents table refer only to this eight-page draft.

### Reading conventions

C denotes annual Mauna Loa CO<sub>2</sub> concentration in ppm. T denotes the annual global temperature anomaly in degrees Celsius above the 1951-1980 mean. An origin is the last available training year; horizon h predicts h years after that origin. A model path is a mathematical continuation under stated assumptions, not a policy scenario with calibrated emissions or climate dynamics.

## Page 3: Measure the same quantity before comparing claims

1 / DATA AND SOURCE INTERPRETATION

We preserve the supplied 2022-vintage workbook rather than replace its observations with revised live records. The admission audit inspected both sheets, all stored cells and the complete printed tables. It found no missing years, duplicate years or missing numerical values. Values in the printed statement and workbook agree at the supplied precision. [1,2]

| Series | Meaning | Coverage | Rows |
| --- | --- | --- | --- |
| CO2 | Mauna Loa annual dry-air mole fraction, ppm | 1959-2021 | 63 |
| Temperature | Global land-ocean anomaly, degrees C above 1951-1980 | 1958-2021 | 64 |
| Joint sample | Inner join on calendar year | 1959-2021 | 63 |

The extra temperature year is retained in its source table but is outside the common modeling sample. Joining by row position would pair different years. Negative temperature anomalies are valid observations, not missing-data codes. Mauna Loa is an atmospheric indicator, whereas temperature is a global index; the pairing is not a common spatial sample. [2,5]

### Annual versus March

The problem's CO<sub>2</sub> caption refers to March, but its cited file is an annual-mean series and the supplied values match that annual interpretation. We therefore answer the supported annual ten-year comparison. It cannot directly verify or disprove a March-specific record, nor describe periods before the supplied coverage. [1-3]

### Two further source distinctions

NOAA's June 2022 release reports May monthly means of 420.99 ppm (NOAA) and 420.78 ppm (Scripps), supporting the statement's rounded 421 ppm. These are monthly Mauna Loa observations, not a 2022 annual global mean, and are excluded from fitting and validation. [4]

OECD's approximately 685 ppm in 2050 is a greenhouse-gas concentration in CO<sub>2</sub>-equivalent under a conditional baseline. It is not the same as 685 ppm of CO<sub>2</sub> alone. We retain the problem's requested pure-CO<sub>2</sub> crossing calculation while avoiding the false claim that a mismatch would refute OECD's different quantity. [6]

> **Keep the temperature baseline fixed**
> Every requested 1.25, 1.50 and 2.00 degree threshold is measured above 1951-1980. These dates must not be relabeled as Paris targets or warming above a pre-industrial baseline. [1,5]

## Page 4: Three contrasting continuation assumptions

2 / CONCENTRATION METHODS

For year t, write x<sub>t</sub> = (t - 1959)/10 so one unit of x is a decade. Let C<sub>ref</sub> be the supplied 1959 concentration, known at every evaluation origin. All fitted parameters use observations available through origin o. Least squares uses a stable QR/SVD method; failed or nonfinite fits remain explicit failures.

### The ten-year claim

Delta<sub>10,t</sub> = C<sub>t</sub> - C<sub>t-10</sub>;     g<sub>10,t</sub> = Delta<sub>10,t</sub>/10

Delta is the increase over ten elapsed years in ppm; g is average annual growth in ppm/year. Compare the window ending in 2004 with every earlier supported window ending from 1969 through 2003. Record all ties and the margin, rather than checking only a favorable comparison. PENDING_EVIDENCE: the reviewed arithmetic and direct answer belong here.

### D: recent ten-year drift

s<sub>o</sub> = (C<sub>o</sub> - C<sub>o-10</sub>)/10;     C<sub>D</sub>(t|o) = C<sub>o</sub> + s<sub>o</sub>(t-o)

D anchors at the latest observation and continues its recent average absolute growth. It is an interpretable forecast baseline, not an all-history fitted explanation. Its endpoint dependence and constant future growth are limitations to evaluate.

### Q: quadratic concentration

C<sub>t</sub> = a + b x<sub>t</sub> + c x<sub>t</sub><super>2</super> + e<sub>t</sub>

Q represents constant absolute acceleration. The quadratic coefficient is not constrained to force an increase. Turning points, decreasing segments and nonpositive predictions must be flagged; a nonpositive concentration cannot enter a logarithmic temperature model.

### E: exponential concentration

log(C<sub>t</sub>/C<sub>ref</sub>) = a + b x<sub>t</sub> + u<sub>t</sub>;     C<sub>E</sub>(t|o) = C<sub>ref</sub> exp(a + b x<sub>t</sub>)

E represents constant proportional growth of total concentration. It is fitted in log units but evaluated in the common ppm unit. No lognormal error distribution or mean correction is assumed. These are compact empirical alternatives, not calibrated carbon-cycle models.

Every candidate retains its requested 2050 and 2100 values and first 685-ppm crossing/status, regardless of selection. Matching the benchmark is never a model-selection criterion. PENDING_EVIDENCE: all-candidate result table.

## Page 5: Selection, later assessment and future accuracy

3 / EVALUATION DESIGN

Forecast evaluation must respect information order. At each origin, fit on years at or before that origin and predict the next ten annual observations without using their realized values. Fixed development origins are 1981, 1986, 1991, 1996 and 2001. Their final target is 2011. The resulting 50 origin-target pairs overlap and are not 50 independent replications.

MAE = mean(|prediction - observation|);     RMSE = sqrt(mean(error<super>2</super>))

Mean absolute error in ppm selects the concentration rule; RMSE, bias and errors by origin and horizon describe its weaknesses. The numerical tie order is D, E, Q. A saved selection receipt precedes the primary program's final assessment. The selected model is a decision under this rule, not a claim of universal superiority.

| Stage | Information allowed | Purpose |
| --- | --- | --- |
| Development | Training through each fixed origin; targets no later than 2011 | Compare candidates and freeze rules |
| Final assessment | Fit through 2011; predict 2012-2021 without refitting | Assess frozen rules and declared comparators |
| Production refit | Unchanged forms fitted through 2021 | Generate conditional future paths |

### The actual exposure history

The complete official table was visible from intake. In addition, an independent adversarial review computed final-period scores before the primary program's selection receipt was produced. Consequently, this rehearsal is not globally blind. The candidate forms and original selector were specified before that exposure; later interpretation and failure-handling clarifications are recorded as post-exposure changes.

The primary run must still preserve its own selection-before-assessment order. That local execution order cannot erase cross-agent exposure. Any new model, window or selector informed by the final scores would be further development, not a fresh test. The final report must separate the development-selected rule, best later-period score and unknown future accuracy.

> **A ranking reversal must remain visible**
> PENDING_EVIDENCE: insert the accepted primary development/final scores and origin-stability diagnostics. Adversarial probes have motivated this reporting requirement; their numerical outputs are not promoted into this draft's main findings. Do not switch the primary winner after seeing the later assessment.

## Page 6: A linked forecast is more than a fitted association

4 / TEMPERATURE AND RELIABILITY

The time-only baseline T0 fits the annual anomaly to x. The linked model T1 fits the anomaly to z = log(C/C<sub>ref</sub>) over the same paired training years. This compares a specific full-history linear-time baseline with a specified log-concentration representation; it does not identify unique predictive information beyond every possible function of time.

T0: T<sub>t</sub> = alpha<sub>0</sub> + delta x<sub>t</sub> + error

T1: T<sub>t</sub> = alpha + beta log(C<sub>t</sub>/C<sub>ref</sub>) + error

Future T1 values use forecast CO<sub>2</sub> from D, Q or E, never realized future concentration. Thus its evaluation includes upstream concentration error. After concentration selection, temperature selection compares T0 with the linked path driven by that selected concentration rule. The other linked paths remain declared comparators; the sequential choice need not have the smallest error among every temperature path.

### Relationship diagnostics

On matched years since 1959, report concentration/anomaly and log-concentration/anomaly correlations, the fitted relationship and descriptive R-squared. Remove separate linear time trends from both variables, repeat with quadratic trends, and examine first differences. These checks probe shared trends and short-run co-movement. They neither identify a causal CO<sub>2</sub> effect nor prove that a physical greenhouse mechanism is absent. The fitted doubling contrast is not an estimate of equilibrium climate sensitivity.

### What a threshold year means

Search annual central-path values after 2021 through 2300 for the first year at or above each requested threshold. A first annual crossing differs from a fractional root, an observed weather excursion or sustained warming. Already-above-origin, invalid-path and no-crossing-through-2300 outcomes remain distinct. Failure-status precedence is awaiting release of the revised specification; no crossing calculation is performed by this draft.

### Historical errors, not probabilistic guarantees

B<sub>h</sub> = max |error<sub>o,j</sub>| over development origins o and 1 <= j <= h

The nondecreasing B<sub>h</sub> is a historical maximum-error reference, not a confidence interval. Assess final-period misses without resizing it. Any displayed future envelope ends at 2031 because ten years is the maximum tested horizon, not because accuracy is established through that date. Alternative model paths and last-30-year fits show sensitivity, not probability bounds. PENDING_EVIDENCE: errors, actual misses and sensitivity results.

## Page 7: Required answers remain visible

5 / PENDING SCIENTIFIC CONTENT

The final solution must answer the following questions directly. Each row is an evidence dependency, not a claim that an unfinished calculation succeeded. Values will come from immutable, reviewed production tables and the accepted modeler's interpretation.

| Question | Required content | Checkpoint status |
| --- | --- | --- |
| 1.a | 2004 annual ten-year change, strongest earlier interval, margin and March limitation | PENDING_EVIDENCE |
| 1.b | D/Q/E calibrated parameters, historical fit and future paths | PENDING_EVIDENCE |
| 1.c | Every candidate: 2050/2100 ppm, benchmark comparison, first 685-ppm crossing/status | PENDING_EVIDENCE |
| 1.d | Frozen selection, final-period comparison, origin instability and bounded accuracy claim | PENDING_EVIDENCE |
| 2.a | Selected temperature path and 1.25, 1.50, 2.00 degree threshold outcomes | PENDING_EVIDENCE |
| 2.b | Level, detrended and differenced association diagnostics since 1959 | PENDING_EVIDENCE |
| 2.c | All linked extensions; tested-horizon errors, actual envelope misses and limitations | PENDING_EVIDENCE |
| 3 | One-page nontechnical article with consistent findings and recommendations | PENDING_EVIDENCE |

### Article boundary: Scientific Today

The article will receive its own page in the complete report. It should explain the strongest accepted findings, why model paths disagree, and what the dates do and do not mean. The annual/March distinction, CO<sub>2</sub>-equivalent correction, fixed temperature baseline and limits exposed by the later assessment must survive simplification.

PENDING_EVIDENCE: no completed article or policy recommendation is asserted in this checkpoint. Conditional recommendations must follow the accepted results; a statistical extension alone does not establish the effect or optimality of a particular climate policy.

> **Release boundary**
> This export is suitable for layout and method review only. It cannot substitute for numerical review, a completed article, a final scientific gate or an accepted solution.

## Page 8: Sources and how this practice was produced

REFERENCES AND DISCLOSURE

[1] COMAP. 2022 HiMCM Problem B: CO2 and Global Warming. Official four-page statement supplied in the local archive, 2022. Requirements p. 1; delivery rules p. 2; data and source notes pp. 3-4.

[2] COMAP. 2022_HiMCM_Data.xlsx. Supplied CO2 Data Set 1 and Temps Data Set 2, 2022 vintage. Sole numerical modeling input. Admission records and source hashes are retained with this practice project.

[3] NOAA Global Monitoring Laboratory / Scripps. Trends in atmospheric carbon dioxide: data definitions, annual and monthly Mauna Loa series. Definition snapshots inspected 3 November 2026; current observations excluded from modeling. <link href='https://gml.noaa.gov/ccgg/trends/data.html' color='#176A73'>gml.noaa.gov/ccgg/trends/data.html</link>

[4] NOAA. Carbon dioxide now more than 50% higher than pre-industrial levels. 3 June 2022. Monthly May concentration/site context only. <link href='https://www.noaa.gov/news-release/carbon-dioxide-now-more-than-50-higher-than-pre-industrial-levels' color='#176A73'>NOAA news release</link>

[5] NASA Goddard Institute for Space Studies. GISTEMP frequently asked questions: anomaly baseline and land-ocean temperature index. Definition snapshot inspected 3 November 2026. <link href='https://data.giss.nasa.gov/gistemp/faq/' color='#176A73'>data.giss.nasa.gov/gistemp/faq/</link>

[6] OECD. OECD Environmental Outlook to 2050: The Consequences of Inaction. OECD Publishing, 2012. Chapter 3, especially printed p. 83, and baseline definition. Primary report text inspected; selected evidence retained as labeled excerpt/paraphrase rather than an original downloaded PDF. <link href='https://www.oecd.org/content/dam/oecd/en/publications/reports/2012/03/oecd-environmental-outlook-to-2050_g1g14e69/9789264122246-en.pdf' color='#176A73'>Official OECD report</link>

### Retrospective practice and AI use

This is a retrospective exercise using the 2022 problem, not a live contest entry or submission. Work is conducted through Codex collaboration sessions with separate logical roles for coordination, source/data admission, modeling, computation, writing/visuals and independent review. Some roles operate sequentially. No execution by Claude Code or actual human checkpoint approval is claimed.

The user delegated reversible practice decisions to the coordinator. Source admission and the initial methods have undergone scoped independent review. Adversarial reviewers challenged model selection, structure and interpretation. Their final-period exposure is disclosed in Section 3. Writer export and layout checks are author self-checks, not independent acceptance.

> **Status at this export**
> Data/method draft only. Primary numerical results, final scientific review and the completed article are pending. The final disclosure will be updated from the actual activity record and will not claim checks or repairs that did not occur.
