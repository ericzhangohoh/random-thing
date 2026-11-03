# T16 canonical independent final LaTeX artifact review

**ACCEPTED_FOR_SCOPE.** Reviewer /root/rehearsal_reviewer. Open blocking, consequential and editorial defects: **0 / 0 / 0**. No author repair requested. Acceptance is for the exact final LaTeX source, compiled PDF, complete sentence-review binding and artifact reproduction described below. It does not extend to future revisions, live competition submission or new scientific validation.

## Exact accepted artifacts

- `paper/latex-r01/manuscript-r05.tex`: SHA-256 `1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55`.
- `paper/latex-r01/build-r05/manuscript-r05.pdf`: SHA-256 `2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac`.
- `paper/latex-r01/sentence-register-r06.json`: SHA-256 `2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c`.
- Closed writer receipt `handoffs/T15/writer-visuals-r02.md`: SHA-256 `788a1d3690c484a7a56728f4814b1480ad84cf93e791e5d47aebcbd2d7d401c4`.
- `paper/latex-r01/author-receipt-r05.json`: SHA-256 `852a2ed6006e5b257de2839d402959065783d8a4e94931ee3a5ccd9e374b8a93`.

The 75-file `target-inventory.json` retains exact source/PDF/register/build guidance, author evidence, figures, all three closed reviewer packages and their immediate prior ledgers, C18 evidence and relevant accepted claims. All targets were rehashed unchanged before closure. Root's final-link/Git work is outside this review.

## Independent rebuild and mechanical evidence

I read the current README and source preamble, then executed the recorded XeLaTeX command three times from `paper/latex-r01`, changing only the output directory to the owned `qa/latex-pdf-review-r01/rebuild/`. All three passes exited0. Exact arguments, CWD and exits are in `rebuild/commands.json`, with full pass logs. The final independently generated log has no warnings, overfull/underfull boxes, missing-character or undefined-reference messages. Its resolved contents file is byte-identical to the author's final contents file.

Both PDFs have16 pages. Independent Poppler layout extraction is exactly identical between released and rebuilt PDF, including page boundaries. I separately rendered both at scale1500. All16 corresponding PNG files are SHA-256-identical, as recorded in `render-comparison.json`. This establishes identical observed text/pagination/rendering with the installed environment. It is not a claim of binary PDF identity, which can vary with compilation metadata.

`verify.py` executed **1,785 checks**, retained in `checks.json`: source/author bindings, all three314-record ledger identities and verdicts, provenance hashes where recorded,93 exact prose blocks, final PDF sentence presence, page counts, punctuation, current primary output/C18 identities, fonts, grayscale and rebuild content. An initial extraction-filter check removed a reference line containing the running-header phrase. The filter was narrowed to the complete running-header line and all314 records then reconciled. No manuscript repair was involved. PyMuPDF was unavailable, so installed pdfplumber supplied font-character inspection without installing packages.

## Fonts, punctuation and visual style

The source uses actual installed Times New Roman regular/bold/italic files through fontspec and compiles with XeLaTeX. Independently generated `pdffonts.txt` confirms embedded TimesNewRomanPSMT, TimesNewRomanPS-BoldMT and TimesNewRomanPS-ItalicMT, with Times-compatible NewTX/TeX Gyre Termes mathematical fonts. Every page has actual TNR text. Each of the six imported vector figure PDFs independently reports embedded Times New Roman label text, documented in `figure-*-fonts.txt`. There is no Latin Modern, DejaVu or Helvetica fallback. Mathematics uses the separately disclosed compatible family rather than being mislabeled as TNR glyphs. The source references locally installed font files and does not bundle them.

Both actual PDF extraction and complete TeX contain **0 ASCII semicolons and 0 fullwidth semicolons**, satisfying the combined limit of at most3. Figure text is included in PDF extraction. Every rendered page passes exact R=G=B pixel equality. Plot distinctions use black/gray, line patterns, hatching and markers rather than color. Body, titles, table text and captions follow a conventional monochrome academic layout, with numbered equations, booktabs-style rules and restrained running headers.

## Actual all-page visual coverage

I independently rendered and opened **every final page**, through view_image in four batches covering1–4,5–8,9–12,13–16. This is my own complete inspection, not inheritance of the author's partial-r05 render comparison. Reviewed final PNGs remain under `render/`.

|Page|Observed content and visual result|
|---|---|
|1|Complete single-page summary, concentration table and nearby qualifications. No spill or missing symbol.|
|2|Contents and scope paragraph. All listed section/subsection destinations agree with the final document.|
|3|Definitions, supplied-vintage qualification, source table and source distinctions. Baseline and units legible.|
|4|Ten-year equation/table and Figure1, followed by concentration-model introduction. Labels do not collide.|
|5|D/Q/E equations and table of fit diagnostics. Lead-ins stay with displays and mathematical symbols are intact.|
|6|Continued fit explanation, forecast-comparison method, MAE/RMSE equation and score table. Two-line paragraph continuation is readable.|
|7|Monochrome comparison bars, origin/weighting sensitivity including C18, and concentration-path figure. Both captions/legends fit.|
|8|All concentration projections and raw crossings, linked temperature equations and forecast-composition formula. No stranded equation lead-in.|
|9|Temperature-score table, comparator explanation, paths/thresholds and all four candidate outcomes. Caption/table complete.|
|10|Continued crossing qualification, correlation/change figure and diagnostic table. Math, labels and noncausal discussion readable.|
|11|Horizon evidence and envelope definition. Equation and explanatory lead-in remain together.|
|12|Historical envelope/miss figure, miss table and window-sensitivity table. Shading, labels and actual miss remain visible.|
|13|Sensitivity continuation, model limitations and valid-prefix semantics. No clipped or isolated final words.|
|14|Complete conclusion together on one page, with no paragraph stranded on another page.|
|15|Entire Scientific Today article on one page, with readable title, paragraphs and qualifications.|
|16|All references, practice/AI/reproducibility and font disclosure. Complete text and working reference annotations.|

No clipping, overlap, missing glyph, unreadable figure, single-line orphan/widow, isolated heading or stranded mathematical lead-in was observed. Normal multi-line paragraph continuations remain, including pages5–6,8–9 and9–10. Figure/table transitions retain their relevant captions and references. Six figures,11 numbered tables,10 numbered equations, section references and bibliography numbering are coherent. The one-page summary/article requirements are met at pages1/15. The16-page total including contents/references is below25.

## Three every-sentence reviews and substantive continuity

I consumed the complete closed A06 argument, A07 evidence and A08 reader final reports and handoffs. Their final packages are respectively `argument-r01/revised-r03`, `evidence-r01/sentences-r03` and `reader-r01/revised-r03` under `qa/latex-attacks/`. All three canonical verdicts are ACCEPTED_FOR_SCOPE with no outstanding required repair.

I independently checked every ledger against the final register: exactly314 ordered IDs, exact sentence text and recomputed UTF-8 text SHA-256 agree in each of the three ledgers. Every row has an accepted individual verdict and no required repair. This gives942 individual final record bindings. A06 includes263 PASS plus51 FRAGMENT_PASS judgments, A07 has314 PASS_FOR_STATED_SCOPE, and A08 has314 PASS. The complete ledgers retain sentence-specific rationales and prior-review provenance, rather than replacing unchanged records with a summary assertion. All93 registered source blocks occur exactly in final TeX, and all314 normalized records occur in actual final PDF extraction. The54 non-sentence items are separately inventoried and covered by the reviewers' closed continuity checks and my artifact inspection.

The reviewers explicitly carried unchanged text forward from their full review and subsequent19-record repair review. They verified layout-only changes into final r05. This is legitimate exact-version continuity, not a claim that every reviewer freshly reread all unchanged sentences during the final binding turn. I read all16 pages as connected prose and found the final wording natural, varied and purposeful. The vintage limitation now distinguishes observation-year truncation from historical data releases. The saturation statement is restricted to a physically justified capacity. The repaired summary, chronology, threshold cases and article wording preserve meaning and improve readability.

The original17 scientific claims and primary run remain unchanged. All35 primary output identities were independently rechecked. New C18's accepted register/evidence hashes were verified: equal target-year weighting is clearly post-assessment sensitivity using the same predictions, with D selection unchanged and no fresh-validation or significance claim. A07's independent diagnostic acceptance is attributed to A07, not relabeled as a new T16 numerical recomputation.

Equations, units, displayed forecasts/crossings/scores and diagnostic values remain consistent with the previously accepted scientific evidence and the closed A07 exact-sentence/evidence review. The paper preserves annual-versus-March, pure-CO2 versus CO2-equivalent,1951–1980 baseline, D/Q ranking reversal, sequential T1-D versus stronger T1-Q, the2016 miss, noncausality and bounded horizons. Summary, conclusions and article retain these constraints. References1–6 and their embedded primary-source URLs remain appropriate. Disclosure identifies actual Codex collaboration and prior global score exposure, with no fabricated human approval, Claude-native execution or globally unseen holdout.

## Disposition

No further artifact or sentence repair is required for these exact bytes. Root may close the LaTeX delivery gate and publish its final current links after its integration checks. Later source/PDF changes require a new binding and appropriate review. The independent primary numerical tests were not rerun, and future forecasting accuracy, causal attribution and competition submission remain outside this artifact verdict. All reviewer writes stayed in assigned T16 QA/handoff paths, with no target, Git, installation or font-distribution changes. PDF skill was used read-only without an authoring marker.
