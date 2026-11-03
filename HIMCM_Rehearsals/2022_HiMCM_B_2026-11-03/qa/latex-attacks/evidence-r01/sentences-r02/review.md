# A07 exact revised-candidate evidence review

Verdict: ACCEPTED FOR EXACT REVISED TEXT AND EVIDENCE SCOPE. All 314 registered records have a complete evidence ledger. Both A07 findings are closed, with no outstanding factual or numerical repair. This acceptance applies to the pinned candidate below and does not replace independent visual/layout QA or authorize automatic acceptance of later bytes.

## Exact candidate and provenance

- `paper/latex-r01/manuscript-r03.tex`, SHA-256 `2c86588b978e271eaafae26f89a4adada724316981586051f5566d509c610685`.
- `paper/latex-r01/build-r03/manuscript-r03.pdf`, SHA-256 `4b9457da90c3b7a91343a0570fe1072a5bd5f7ff52aa36ecae10d80b687c3ff4`.
- `paper/latex-r01/sentence-register-r04.json`, SHA-256 `ef5ac7a999d90934b0e686cc0b36c80f6a69d6686f105f9c7431537b64c73f33`.
- `paper/latex-r01/sentence-delta-r03.json`, SHA-256 `b7c46ade1e8d4cc6fc549906ce23d50749fa4c840dbf3cc2b9f1cc30703ccf72`.

The complete first review is preserved in `../sentences-r01/`. The new ledger records its exact review/ledger hashes and original target identities. It carries forward 295 judgments only after exact sentence-text equality and verified unchanged evidence bindings. The 16 changed and three added records were actually read afresh together with their complete paragraphs and surrounding argument. The reviewer independently derived this delta from the old and new registers, checked it against the full TeX diff, and verified that the author's delta contains exactly the same changes and no removed IDs.

## Repairs closed

A07-F01 is closed by DAT07.01–02, which explicitly says that retrospective tests truncate one supplied vintage by observation year and do not reconstruct historical releases. VAL01.01, TEM03.01 and APP01.02 now consistently describe workbook observation dates rather than implying actual real-time availability. The new paragraph sits directly after the source/sample description, so its qualification governs the subsequent backtest discussion.

A07-F02 is closed by APP02.05. The statement now concerns a physically justified saturation capacity not established by these data. It no longer claims that a rising segment proves logistic-parameter non-identifiability. The missing inputs for physical carbon-cycle and energy-balance models remain correctly qualified. No new model fit or unreviewed numerical result is introduced.

All other edits are supported clarifications. The summary distinguishes the prespecified selection rule from the model it selects. Temperature dates are explicitly conditional crossings. The 2016 miss and the 2031 display cutoff are separated. The temperature comparison correctly identifies selected sequential T1-D and lower-error declared comparator T1-Q. The relationship discussion now sends detrending readers to Table 8 and level/change readers to Figure 5. Sensitivity still changes neither selection nor probabilistic interpretation. Path-validity wording describes the existing accepted status logic and actual valid paths.

## Unchanged numerical evidence and non-prose content

Every actual equation/align environment and every tabular environment is byte-for-byte unchanged within the TeX source. The counts are eight equation environments, one align environment containing two equations, and 12 tables. Scientific output files and all prior evidence bindings still match their reviewed hashes. Prior independent numeric checks therefore remain applicable without repeating an unchanged model run.

C18's five VAL06 records and DIS04.03 are exact-text unchanged. Their correct post-assessment loss-sensitivity interpretation, same 50 tasks/30 years and unchanged D selection remain intact. The revised artifact introduces no new numerical or causal claim.

The complete non-sentence ledger covers all 54 entries. F05's legend is the only changed non-prose text: “Accepted log-CO2 fit” becomes “Fitted log-CO2 curve.” Its actual PDF text was independently extracted. The rendering-code diff changes only that label and versioned output/register filenames. No data selection, calculation or coordinates change. F01–F04 and F06 are byte-identical under their new filenames. F05 retains the correct level and change axes and corresponding correlation labels. The new legend accurately names the fitted curve without internal acceptance terminology.

## Independent coverage and PDF checks

An independent source scan finds 93 prose macros and matches all exact block bodies against the register. Registered sentences join to the full block text. The TeX diff and residual source inspection reveal no unregistered substantive prose, footnote or note. All 314 records reconcile with independently extracted PDF text.

Five records cross page boundaries and were inspected with their actual continuations: DEC01.03 on pages 3–4, VAL01.02 on pages 5–6, VAL05.05 on pages 6–7, PRO03.04 on pages 7–8 and APP02.04 on pages 12–13. Removing only repeated headers and page numbers establishes full matches. These are pagination breaks, not omissions.

The exact PDF has 15 pages and zero combined ASCII/fullwidth semicolons. The exact TeX also has zero. Font extraction continues to show embedded Times New Roman regular/bold/italic with NewTX/Termes mathematical families, consistent with the disclosure. This review does not claim a complete visual inspection of every page.

## Final review package

`sentence-ledger.json` and `sentence-ledger.md` contain all 314 exact record texts, hashes, updated source lines, evidence keys, rationales, PASS verdicts and original-review provenance. Each entry identifies either exact-text carry-forward or a new manual text/context review. `manual-delta-assessments.txt` preserves the 19 fresh judgments.

`non-sentence-ledger.json` covers all 54 additional items. `evidence-sources.json` binds the current TeX/figure evidence and unchanged scientific sources to exact hashes. `delta-coverage-and-hashes.json` records independent delta, source/PDF coverage, unchanged equations/tables/C18, figure hashes and punctuation checks. Independent PDF text, font extraction and F05 text are retained alongside the packaging script.

All A07 factual/evidence review work is complete for these exact bytes. No original artifact edits, scientific selector changes, Git operations or installations occurred.
