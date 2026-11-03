# Evidence outline - 2022 HiMCM B - r01

Status: T03 planning artifact, awaiting coordinator acceptance. All scientific results are `PENDING_EVIDENCE`. Numbers below specify the official question's years, thresholds or limits, or this proposed page allocation; they are not computed findings.

Audience: technical modeling readers and, separately, readers of *Scientific Today*. Deliverable: a polished English retrospective practice report. The target is 14-18 pages; the detailed allocation below is 17 pages, within the hard maximum of 25. No separate cover page, fabricated team-control number or live-contest status is planned.

## Inputs and interpretation boundaries

The complete official statement was read by text extraction and visual inspection of all four rendered pages: `/Users/ericzhang/Desktop/himcm/HIMCM_备赛资料/02_历年真题/2022/2022_HiMCM_Problem_B.pdf`, SHA-256 `fb9000006eb0402d24c4e810a0e6d4cd69f26f94181a48adbfe9c795d6669ece`. Question numbering is on page 1; delivery rules are on page 2; CO2 and temperature tables/metadata are on pages 3 and 4. The working requirement version is `control/requirements-r00.md`.

Prepare a concise definitions and source-misstatement box near the start:

- The CO2 caption says March averages, but the linked source names an annual-mean series. The final interpretation must cite domain-data's accepted admission record. Until then the month-specific interpretation remains `PENDING_EVIDENCE`.
- The coordinator relayed a provisional domain-data finding that OECD's 685 ppm refers to CO2-equivalent, not pure CO2. The report should distinguish that source quantity from the exercise's requested 685-ppm pure-CO2 crossing. This is a planning dependency, not an independently verified writer claim; bind it to the accepted domain-data source before publication.
- Temperature is an anomaly relative to 1951-1980, not absolute temperature or a pre-industrial anomaly. The joint analysis uses matched years since 1959, as required.
- Intake fixes the fitting/validation cutoff at the supplied observations through 2021. The introductory May 2022 value is context, not permission to add later data.
- A long-horizon model extension is conditional on its assumptions. Historical fit, held-out accuracy, association and causation are distinct claims.

These distinctions must survive simplification in the summary and article. The XLSX was not consumed by T03; its admitted definitions and numerical contents are dependencies for later work.

## Page budget

| Planned pages | Section | Allocation | Reader's question |
|---|---|---:|---|
| 1 | Summary Sheet | 1 | What are the main answers, the reasons to trust them and the material limits? Write last. |
| 2 | Contents | 1 | Where is each required answer? Use final page numbers. |
| 3-4 | 1. Scope, data and conventions | 2 | What do the observations measure, which claims are testable and how do the modules connect? |
| 5 | 2. The 2004 ten-year claim | 1 | Was this the largest earlier supported ten-year change? |
| 6-8 | 3. CO2 models, comparison and forecasts | 3 | How do multiple candidates perform, and how does each answer every forecast question? |
| 9-10 | 4. Temperature trajectory and threshold dates | 2 | How does the anomaly evolve, and when are the requested levels first crossed? |
| 11-12 | 5. CO2-temperature relationship and extension | 2 | What association exists since 1959, and what does its future extension mean? |
| 13 | 6. Reliability, sensitivity and limitations | 1 | Which checks support the conclusions and where does extrapolation outrun evidence? |
| 14 | 7. Direct answers and conditional recommendations | 1 | What is the concise response to each question and what follows from it? |
| 15 | Article for Scientific Today | 1 | What should a nontechnical reader understand and do with the findings? |
| 16-17 | References; retrospective practice and AI disclosure | 2 | What supports the work, and how was it produced? |

This is an allocation, not a length target to fill. Aim for 14-18 readable pages; up to eight pages remain under the hard limit if accepted evidence or layout needs them. All front matter, references, disclosure and any later appendix count. Keep the summary and article on explicit one-page boundaries. Cut repetition before shrinking fonts or dropping required answers.

## Requirement-to-evidence map

W01-W11 are writing dependencies, not accepted claim IDs. Later each slot must identify accepted source/model/run versions, exact tables/columns, units, scenario, time definition and review. The coordinator owns the official evidence index.

| Slot / requirement | Official location and answer | Evidence needed | Planned location | Status |
|---|---|---|---|---|
| W01 / R01 | 1.a: compare the 2004 ten-year increase with every earlier supported period and explain agreement/disagreement | Admitted annual/monthly definition; accepted ten-year formula; complete eligible-window table; 2004 row and prior maximum; coverage limitation | Section 2, summary, answer ledger; article if consequential | `PENDING_EVIDENCE` |
| W02 / R02 | 1.b: fit more than one CO2 model to describe history and project the future | Accepted candidate equations, parameter units, assumptions, calibration window, fitted parameters/values and residuals | Section 3.1, Figure F02 | `PENDING_EVIDENCE` |
| W03 / R03 | 1.c: every candidate's 2100 value, comparison of 2050 with 685 ppm, and first 685-ppm crossing or no crossing | All-candidate forecast/crossing table, model IDs, units, threshold convention, numerical status and benchmark qualification | Section 3.3, Table T03, summary | `PENDING_EVIDENCE` |
| W04 / R04 | 1.d: most accurate model and reasons within a declared scope | Time-ordered validation design, common held-out targets, error table/metric, leakage check, selection and limits | Section 3.2, Table T02, summary | `PENDING_EVIDENCE` |
| W05 / R05 | 2.a: temperature model; first years at 1.25, 1.50 and 2 degrees C above 1951-1980 | Accepted specification/parameters, validation, trajectory, threshold table/convention, uncertainty or its stated absence | Section 4, Figure F03, Table T04, summary/article | `PENDING_EVIDENCE` |
| W06 / R06 | 2.b: analyze/explain CO2-temperature relationship since 1959 or justify absence | Matched-year sample, accepted relationship, diagnostics for shared trends/residual structure, association/causation limits | Section 5.1, Figure F04 | `PENDING_EVIDENCE` |
| W07 / R07 | 2.c: extend joint model; state supported horizon and concerns for both variables | CO2-to-temperature interface, joint scenarios, horizon-dependent hindcasts, reliability criterion, sensitivity/model disagreement and uncertainty interpretation | Section 5.2, Section 6, Figure F05 | `PENDING_EVIDENCE` |
| W08 / R08 | 3: nontechnical article for Scientific Today, one page maximum | Accepted W01-W07 claims and conditional recommendations, with definitions and limitations preserved | Article, planned page 15 | `PENDING_EVIDENCE` |
| W09 / R09 | Page 2: PDF at most 25 pages with summary, contents, solution, article and references | Actual exported file/page count, all-page rendered inspection, content checks and independent PDF review | Entire PDF and production receipt | `PENDING_EVIDENCE` |
| W10 / R10 | Intake: honest retrospective practice/AI disclosure | Actual role/activity record, source/model provenance, review scope and delegated-practice dispositions | Scope note and closing disclosure | `PENDING_EVIDENCE` |
| W11 / R11 | Intake: operational collaboration/recovery evidence | Actual acknowledgments, receipts, independent review, rejected error/repair, upstream invalidation, restart and recoverable runs | Brief reproducibility/disclosure paragraph; full records remain outside PDF | `PENDING_EVIDENCE` |

R11 is a rehearsal verification requirement, not an extra scientific question in the 2022 statement. Preserve its project records without filling the report with internal task logs or implying an unperformed test occurred.

## Section-level argument

### Summary Sheet

State the problem and data boundary, why the selected methods earned use, direct historical answer, forecast comparison, temperature threshold outcomes, relationship and supported horizon, then a conditional recommendation with material limitations. Reconcile every number against accepted tables. The summary must stand alone but need not repeat every coefficient. `PENDING_EVIDENCE`.

### 1. Scope, data and conventions

Restate the questions; introduce the definitions/misstatement box; identify admitted entities, units, time coverage, temperature baseline and data-quality checks. Define notation beside its first use. Include only adopted assumptions with their consequences. Explain how CO2 outputs feed the joint extension without implying a causal proof. Avoid reprinting raw data. `PENDING_EVIDENCE`.

### 2. The 2004 ten-year claim

Give the accepted window definition and eligible coverage. Distinguish ten-year total change from average annual change if both are used. Present the 2004 result, strongest earlier comparison and direct conclusion under the admitted data definition. Do not extend the claim to all earlier history or to a particular month unsupported by the input. `PENDING_EVIDENCE`.

### 3. CO2 models and forecasts

Explain each candidate's representation and limits, with equations and units. Separate historical fit from predictive evaluation. Use the accepted common chronological validation to justify the preferred candidate's scope of accuracy. Put every candidate's 2050 concentration, relation to 685 ppm, 2100 concentration and first crossing/status in one table. Distinguish the requested exercise threshold from the verified OECD source quantity. Treat distant projections as conditional extrapolations. `PENDING_EVIDENCE`.

### 4. Temperature model and threshold dates

Explain the accepted model, input window and validation. Label every temperature as an anomaly above 1951-1980. Show the trajectory and all three threshold results. Specify continuous versus integer year, fitted mean versus annual observation, and first crossing if paths are nonmonotone. Use accepted uncertainty only; do not invent intervals or silently call a mean confidence band a prediction interval. `PENDING_EVIDENCE`.

### 5. Relationship and joint extension

Explain the matched sample since 1959, functional relationship and accepted checks for shared trends and residual dependence. Keep association distinct from causal attribution. Show the accepted CO2-to-temperature module connection without hidden refitting by visualization code. Separate requested future extension from the horizon actually supported by validation. `PENDING_EVIDENCE`.

### 6. Reliability and limitations

Report relevant accepted sensitivity and diagnostic evidence, not generic robustness claims. Address tested horizons, candidate disagreement, data definitions, baseline, residual structure and omitted drivers to the extent supported. Distinguish data, parameter and scenario/model uncertainty if quantified. A reliable-horizon claim requires its criterion and tested horizons; otherwise state that a defensible long-term reliability bound was not established. `PENDING_EVIDENCE`.

### 7. Direct answers and conditional recommendations

Provide a compact answer ledger keyed to 1.a-1.d and 2.a-2.c. Tie recommendations to accepted results and state what would change them. Avoid implying statistical extrapolation selects a detailed climate policy. `PENDING_EVIDENCE`.

### Article for Scientific Today

Use a headline and accessible prose: main accepted finding, why future curves differ, what the temperature baseline means and why projected dates are conditional. Retain the annual/March and CO2/CO2-equivalent distinction in concise language when consequential. Avoid equations, unexplained acronyms and internal process detail. Keep recommendations and material qualifications consistent with the body. Verify the actual one-page boundary. `PENDING_EVIDENCE`.

### References and disclosure

Cite the official statement/workbook, source definitions actually checked and methods actually used; do not reproduce unread references as if consulted. State the data vintage. The disclosure must describe actual Codex collaboration, six logical roles used in sequence where appropriate, actual independent-review scope, retrospective practice and delegated decisions. Never claim actual Claude runtime use, fabricated human gate approvals or live-contest submission. Final wording depends on the completed activity record. `PENDING_EVIDENCE`.

## Planned visual/table register

Specifications only; no plotted values or visualization code exist in T03. Drop a redundant visual rather than fill a quota.

| ID | Reader question | Display | Accepted binding needed |
|---|---|---|---|
| F01 | Was 2004 a ten-year record? | Changes by window ending year, highlighted target/prior maximum; explicit ppm or ppm/year | W01 window table and definition |
| F02 | How do CO2 candidates fit and diverge? | Clearly separated observed/forecast spans, candidate IDs, cutoff and benchmark; optional aligned panels | W02-W04 fitted/forecast table, model/run IDs, benchmark caveat |
| F03 | When are temperature levels crossed? | Anomaly path, forecast boundary, labeled thresholds and supported uncertainty | W05 trajectory and interval meaning |
| F04 | What supports the relationship beyond common trends? | Relationship display and only analysis-supported diagnostic panel | W06 matched observations/diagnostics |
| F05 | What horizon/scenario variation is supported? | Horizon error curve and/or joint scenario comparison, without implying 2100 validation | W07 hindcasts/joint projections |
| T01 | What do data and assumptions mean? | Compact admitted definitions and consequential assumptions | Dictionary and adopted assumptions |
| T02 | Why prefer a CO2 model? | Candidates, common validation metric/units/window and chosen model | W04 comparison |
| T03 | How does every candidate answer 1.c? | Model, 2050 ppm, relation to 685, 2100 ppm, first crossing/status, caveat | W03 forecasts/crossings |
| T04 | What are the temperature threshold outcomes? | Threshold, model/scenario, first year/status, uncertainty definition/limit | W05 thresholds |

Later bind each item to exact paths, hashes, columns, units, transformations and captions. Plotting may format and round accepted outputs but may not refit, redefine thresholds, alter rankings or silently omit results. Distinguish zero, no crossing, missing and numerical failure.

## Dependencies before later writing

1. Coordinator routes accepted requirements and recorded G1/G2 dispositions; writer acknowledges exact versions in its next handoff.
2. Domain-data supplies admitted workbook/data definitions, resolves source discrepancies and provides actually verified bibliography entries.
3. Modeler supplies accepted equations, assumptions, symbols, interface, selection metric, threshold convention and reliability interpretation.
4. Computation supplies immutable validated result tables and reproducible run records with units/schema. Writer does not fit models or edit results.
5. Reviewer and coordinator release scientific claims via the accepted evidence index and G3 disposition. Until then these remain slots, not findings.
6. Writer binds prose/figures to accepted evidence, writes summary/article last, exports and requests independent PDF review under the next task.

Any upstream data, equation, metric or result revision invalidates dependent captions, tables, prose, summary and article until reconciled. Preserve prior accepted versions and identify affected slots in a new handoff.
