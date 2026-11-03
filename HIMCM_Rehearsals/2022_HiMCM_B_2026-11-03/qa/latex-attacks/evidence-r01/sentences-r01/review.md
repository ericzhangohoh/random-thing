# A07 full sentence evidence review, first candidate

Verdict: REPAIRS REQUIRED for two wording issues, affecting three registered records. All 311 records were read individually and have explicit evidence or rationale. 308 pass for their stated scope. The 54 separately inventoried equations, tables, headings, plot-label groups and furniture items were also assessed. No numerical mismatch was found in the reported results. This is not final artifact acceptance because the repairs need exact-version recheck.

## Exact reviewed candidate

- `paper/latex-r01/manuscript-r02.tex`, SHA-256 `f9f60adb63996ae83d2bffeec43e4e3b9e04cc10d9e85cbd1c3f452db8bed35b`.
- `paper/latex-r01/build-r02/manuscript-r02.pdf`, SHA-256 `c0e4a245b2b5013effbd7fcca5262db2114ab5b48e3162b5a7482707e2137e8e`.
- `paper/latex-r01/sentence-register-r03.json`, SHA-256 `80e9e581927f4483cf99a3038dea6fb387ba9a903edec7b9b36cd69b8e940e7e`.

The review is A07's new independent factual, numerical and evidentiary pass, not a relabeling of an earlier numerical review. The source, records and actual evidence were read in this turn. Existing accepted scientific outputs remain the numerical basis. No original artifact, selector or Git state was changed.

## A07-F01: retain the single-vintage backtest qualification

Affected records: VAL01.01 and APP01.02. TEM03.01 shares the same historical-training context.

The reported origin years and year cutoffs are correct. However, the revision says that forecasts use observations “available” at the origins without retaining the known vintage limitation. Neither the entire TeX source nor its sentence register contains a single-vintage qualification. `research/data-quality-r01.md` explicitly explains that the tests use one supplied vintage and cannot prove what was known at each earlier date. The original model decision also explicitly distinguishes supplied vintage from real-time historical vintage.

Required repair: add a clear qualification near VAL01, such as “These backtests use the single supplied data vintage, rather than the data versions available at each historical date.” APP01.02 may then describe correct year cutoffs without implying a historically reconstructed release vintage. Alternatively replace its availability wording with “observations dated no later than their origin.” Both details can be stated together. This changes interpretation only and requires no scientific rerun.

## A07-F02: avoid an unperformed logistic-identification conclusion

Affected record: APP02.05.

“A logistic capacity is not identified by the rising record” is stronger than the provided evidence. The model decision uses similar rationale, but no logistic fit or identifiability assessment was performed. A monotonically rising segment alone does not mathematically establish structural non-identifiability. The actual data fields do support the narrower statement that the exercise does not establish a physically justified saturation capacity and omits inputs needed by physical carbon-cycle or energy-balance models.

Required repair: use “The supplied record does not establish a physically justified saturation capacity, and a physical carbon-cycle or energy-balance model would require additional inputs.” Equivalent cautious wording is acceptable. This requires no new candidate model or fit.

## Numerical and interpretation checks

Every numerical prose claim and each of the 12 tabular environments was checked against actual primary files. This includes endpoint arithmetic and ranking, all three CO2 model forms, production coefficients, fit samples and diagnostics, all forecast comparisons, crossing years and previous/current boundary values, all temperature comparator scores, association statistics, horizon evidence, the 2016 envelope miss, sensitivity values, and producer execution/reproduction counts.

The accompanying independent computation reconstructs all 14 overall development/final model metrics from predicted minus observed rather than trusting stored metric labels. It also checks the 2050/2100 model spreads, 10/10 and 9/10 containment, the sole 2016 miss, all nine actual finite/nondecreasing paths, and strict threshold bracketing. The displayed values agree. These are review checks of fixed outputs, not new model fitting or new validation.

C18's target-year loss diagnostic is correctly scoped in VAL06 and DIS04.03. It uses the same 50 tasks and 30 years, explicitly says post-assessment and different loss, retains D, and makes no inference of significance or future superiority. Both original and alternative objectives are correctly described. The source does not repeat A05's earlier horizon-weight ambiguity.

The report consistently distinguishes station concentration from global temperature, annual means from March and monthly May, CO2 from CO2-equivalent, 1951–1980 anomalies from pre-industrial/Paris levels, descriptive association from causation, deterministic crossings from realized/persistent warming, historical envelopes from probability intervals, and local execution order from a globally blind holdout.

## Independent omission and artifact checks

An independently written balanced-brace scan finds exactly 92 actual `p`/`txt` prose blocks in the TeX body. Their IDs and exact TeX match the registry. Joining each block's registered records recovers its whole display text. The remaining source was saved and manually inspected. It contains only the separately reviewed equations, tables, figures, titles/headings, bibliography control, TOC, headers/footers, labels and layout commands. No unregistered substantive sentence, footnote or note was found.

Independent Poppler extraction finds 15 pages and zero combined ASCII/fullwidth semicolons. All 311 records reconcile with the PDF after normalization. Two sentences cross page boundaries: VAL06.03 across pages 6–7 and APP02.04 across pages 12–13. Their exact continuations were inspected after removing only the repeated header and page number. This is not an omission.

`pdffonts` confirms embedded Times New Roman regular/bold/italic for text and Times-compatible NewTX/Termes mathematical fonts. The TeX references local system fonts and the figure code sets Times New Roman. This corroborates the typography disclosure but is not a full page-by-page visual-quality certification, which remains a separate reviewer task. No font installation or redistribution occurred.

## Review artifacts

- `sentence-ledger.json` and `sentence-ledger.md`: all 311 exact record texts, text hashes, source lines, evidence keys, distinct rationales, verdicts and repairs.
- `manual-assessments.txt`: individually authored judgments used to package the ledger. They are not automatically inferred PASS labels.
- `non-sentence-ledger.json`: 54 individually reviewed content items, including every equation/table and plot-label group.
- `evidence-sources.json`: exact source-file SHA-256 bindings for each evidence key.
- `coverage-and-hashes.json`: independent source/PDF coverage, semicolon counts and 30 accepted-evidence hash checks.
- `independent-numeric-checks.json`: recomputed fixed-output quantities.
- `pdf-text.txt`, `pdf-fonts.txt` and `independent-source-residue.txt`: independent extraction and omission-inspection evidence.
- `package-review.py`: packaging and bounded verification code, with no production model import or refitting.

Next step is author repair followed by A07 inspection of changed sentences and surrounding contexts against new pinned TeX/PDF/register bytes. The original ledger is preserved and must not be represented as acceptance of an unseen later revision.
