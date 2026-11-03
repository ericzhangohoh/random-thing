# A06 independent argument and prose attack r01

Status: bounded pre-revision critique complete. This reviews the existing Markdown, not the forthcoming LaTeX or PDF. The reviewer did not author or edit the target. No model was refitted. Numerical accuracy, fonts and rendering are outside this pass.

## Targets and authority

Line references refer to `paper/manuscript-complete-r03.md`.

| Read-only target | SHA-256 |
|---|---|
| paper/manuscript-complete-r03.md | 76c9b3de561214a0bd970c17afe95335f0559e31c8f35950dbea345177fe1616 |
| control/accepted-claims-g3-r01.json | 2b4056fba13ce75f8ebce73a8872fa391da19872e95eda6d43ac762267ab32d4 |
| models/interpretation-r02.md | a1403117e038695aaebb2e3539e8994337225ab48cd803d3e70c6be4f298a2b0 |

G3 governs accepted claim scope. The interpretation's older pending-status language does not override G3. The planned `paper/latex-r01` was not reviewed.

## Overall finding

The report gives appropriately bounded answers. Its principal weakness is an argument that often reads like audit safeguards: methods specify what was done more reliably than why, and results repeatedly turn into lists of prohibited interpretations. The rewrite should strengthen explanatory links and consolidate cautions, while preserving material limits. Natural cadence means sentences and paragraphs shaped by purpose, not arbitrary length targets, deliberate errors, invented findings or concealed AI use.

## Findings

### A06-01 — P1: a fixed design is not a justified design

Evidence: lines 113, 119 and 125 define D/Q/E. Line 139 lists origins, horizon, MAE and tie order. Line 201 states the sequential rule. These are reproducible instructions, but do not fully explain the choice. “Prespecified” explains retaining a rule after assessment, not its intrinsic quality.

Repair: explain that the forms contrast constant absolute growth, constant acceleration and constant proportional growth with few parameters. Distinguish the ten-year drift window and origin schedule as declared choices from choices demonstrated optimal. Explain MAE's role as average absolute error in the measured units and that pooling weights forecast pairs equally, not independent experimental replications. Explain that sequential selection assesses the downstream consequence of the selected concentration rule rather than searching for the lowest temperature error. Do not invent an optimization study or historical author motivation.

Acceptance: a reader can explain the intended comparison and its untested design choices before the scores. Preserve D-development versus Q-final and T1-D selection versus lower-error T1-Q comparator. No model or selector changes.

### A06-02 — P1: the abstract compresses too many jobs into one paragraph

Evidence: line 21 combines selection, baseline performance, comparator performance, three dates, baseline definition, crossing semantics, sensitivity and noncausality. Line 23 adds horizon, envelope, 2031 and probability qualifications. The hierarchy is difficult despite valid individual statements.

Repair: move through the annual historical check, concentration comparison, temperature result, then tested horizon and principal failure. Keep the baseline in the date sentence. Give the association finding its own sentence. Define the error reference in ordinary language when reporting its 2016 miss. Keep annual/March, CO2/CO2-equivalent, D/Q and T1-Q distinctions intelligible instead of listing labels. One compact horizon statement can govern the distant projections.

Acceptance: the abstract answers the problem directly without requiring readers to decode “selected sequential temperature path,” “central-path” and “historical-error envelope” together. Numerical values and all material C01–C13 qualifications remain intact.

### A06-03 — P2: repeated caution replaces explanation

Evidence: negative lists recur at lines 167, 171, 174, 220–223, 263, 279, 293 and 296. Line 265 (“We keep it beside the principal temperature forecast, including in the summary and article”) describes editorial placement, not a result.

Repair: keep local qualifications where detached reading creates ambiguity, especially CO2-equivalent, 1951–1980, annual/March, noncausality and historical-reference status. Develop the general extrapolation argument once: short tests cannot establish century-scale accuracy, and actual form/window sensitivity shows distant answers changing. Remove statements about where the writer will put information. Preserve the 2016 miss in the summary, body and article as required.

Acceptance: each caution resolves a specific ambiguity or adds a distinct reason. Repeated paragraphs do not simply restate “not guaranteed/not probability/not causal.” Explain positively what the tests establish: relative errors for declared rules in stated historical windows.

### A06-04 — P2: paragraph functions repeat mechanically

Evidence: model paragraphs often follow “define rule, then warning” and result paragraphs “state number, then deny wider claim.” Lines 239–243 give three qualification-heavy paragraphs. Lines 341, 343 and 345 repeat bold command plus short explanation. “Page…” headings and “Claims: C…” expose production scaffolding.

Repair: organize by scientific purpose. A method paragraph can develop assumption, consequence and test. A result paragraph can compare outcomes. A discussion paragraph can connect a weakness to observed sensitivity. Use short sentences for decisive answers and longer ones where dependence needs explanation. Convert concluding commands into a connected argument. Keep claim bindings in companion metadata and use conventional numbered sections, not fixed page-sized arguments.

Acceptance: adjacent paragraphs do not continually repeat claim-plus-disclaimer. Transitions explain dependencies. The body reads as a scientific argument while a separate claim map preserves auditability. Do not impose arbitrary sentence-length metrics.

### A06-05 — P1: disclose evaluation exposure where scores are interpreted

Evidence: lines 139–153 explain fixed selection and final assessment. Prior project-wide score exposure is disclosed only at line 391. The main method does not claim blindness, but its chronology can suggest greater independence than the project supports.

Repair: add a brief methods statement that the local run retained declared selection order while another reviewer had previously exposed final scores. This is a later historical assessment, not a globally blind holdout. Keep full details and AI disclosure in end matter. Do not conflate prior score exposure with feeding realized future CO2 to the temperature model, which the stated scoring procedure excludes.

Acceptance: the main validation discussion makes this limitation findable. No fresh/unseen/blind holdout claim. Preserve unchanged selection and forecast-input discipline accurately.

### A06-06 — P2: conclusion inventories rather than synthesizes

Evidence: lines 329–337 repeat question mappings and 341–347 give general recommendations. Ranking reversal and changed crossing years offer a stronger shared argument. “No guaranteed reliable-through date” in line 337 answers an extreme claim but says less about useful evidence than the body.

Repair: connect the results. A declared selector supports an honest historical comparison, but neither its winner nor the later winner establishes distant superiority. The miss and shifting dates justify revisiting assumptions. Historical tests furnish limited comparative evidence at one to ten years without identifying a universal expiry date. Keep direct dates with baseline and conditional meaning. Do not replace answers with generalized uncertainty.

Acceptance: the conclusion provides synthesis supported by C07/C11–C13. It neither oversells distant dates nor implies that historical testing has no evidential value. Policy implications remain within C17.

## Compact writer rubric

1. Answer with the supported result and necessary unit/baseline.
2. Explain why the comparison addresses the question. Label declared choices honestly.
3. Connect interpretation to a specific contrast, table, figure or sensitivity result.
4. Place scope limits where the particular wrong inference arises. Consolidate repeated general cautions.
5. Shape sentence and paragraph length by function. Read adjacent paragraphs for repeated scaffolding.
6. Conclude with a supported implication rather than a table inventory or unsupported advice.
7. Preserve annual/March, CO2/CO2-equivalent, 1951–1980, D-development/Q-final, sequential T1-D/T1-Q comparator, 2016 miss, noncausality, exposure and AI disclosure.

## New sentence-review requirement and disposition

The user now requires every sentence to receive multiple independent reviews, with at most three semicolons total across ASCII and fullwidth forms, aiming for zero. This initial report does not satisfy or claim that later sentence acceptance. The follow-up must bind to completed TeX and a sentence register and produce a per-sentence ledger containing ID, checked dimensions, verdict, and issue/repair where applicable. Include all actual sentences in summary, body, captions, notes, article, disclosure and references. Classify non-sentence labels separately. Count both semicolon characters in the complete rendered paper text, including bibliography and captions, and distinguish unavoidable TeX syntax from visible punctuation.

Request focused revision for P1 findings and connected prose repairs for P2 findings. No scientific rerun or blanket subjective replacement is requested. No LaTeX or PDF acceptance is claimed.
