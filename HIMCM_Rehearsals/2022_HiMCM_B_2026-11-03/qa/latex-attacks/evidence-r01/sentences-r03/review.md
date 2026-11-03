# A07 final layout binding and complete evidence ledger

Canonical verdict: **ACCEPTED_FOR_SCOPE**.

Scope: complete sentence factual, numerical and evidence review, carried forward by exact text identity and independently bound to the final LaTeX source and PDF. This does not constitute all-page visual/layout acceptance. T16 performs that separate review.

## Exact final artifacts

- `paper/latex-r01/manuscript-r05.tex`: `1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55`.
- `paper/latex-r01/build-r05/manuscript-r05.pdf`: `2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac`.
- `paper/latex-r01/sentence-register-r06.json`: `2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c`.

The final 314-record ledger is `sentence-ledger.json`, with a complete Markdown companion. Every record includes its exact text, SHA-256, updated source location, evidence references, individual rationale, verdict and prior-review provenance. No record was omitted or replaced by a summary acceptance.

## Independent carry-forward checks

All 314 sentence IDs and text hashes exactly match A07's accepted r03/r04 ledger. There are no added, removed or changed sentence texts. The original complete 311-record review and subsequent 19-record changed/new text review remain explicit in the provenance chain. Both prior A07 findings remain resolved in the unchanged final wording.

The entire actual TeX diff was inspected and independently reproduced from the accepted source using only the stated layout changes: three widow/club/display penalties, nine no-page-break controls after equation lead-ins, and a page break before Conclusions. No other source change is present. An independent balanced-brace scan again verifies all 93 prose blocks and their complete sentence coverage.

All 54 non-sentence content identities match the accepted version. Equations, tables, F05's accepted revised legend, the other figure labels and every scientific output remain unchanged. Prior source-evidence hash bindings were checked against disk. The accepted C18 wording still describes post-assessment weighting sensitivity using the same forecasts, with unchanged D selection and no new validation claim. No rerun of unchanged scientific fitting was needed.

## Final PDF text checks

Independent Poppler extraction finds 16 pages. Every one of the 314 records appears in the PDF after normalization. CO209.02, TEM04.03 and TEM06.02 span page boundaries and reconcile after removal of repeated headers and page numbers. Their surrounding extracted text was inspected. These are complete continued sentences, not missing text.

All nontechnical article records appear on page 15. Both source and extracted PDF contain zero combined ASCII/fullwidth semicolons. Font extraction is retained as supporting artifact evidence, without claiming all-page visual inspection.

The author's closed visual receipt `handoffs/T15/writer-visuals-r02.md` matches SHA-256 `788a1d3690c484a7a56728f4814b1480ad84cf93e791e5d47aebcbd2d7d401c4`. Its identity was verified, but the acceptance here rests on A07's independent text/evidence checks rather than treating the writer's review as independent QA.

## Deliverables and limits

`sentence-ledger.json` and `sentence-ledger.md` contain the complete final 314-record ledger. `non-sentence-ledger.json` contains all 54 additional reviewed items. `evidence-sources.json` binds current source/PDF evidence and unchanged scientific files to exact hashes. `final-binding-checks.json` records the full provenance chain, verified identities, source delta, PDF coverage, page count and punctuation checks. `bind-final-layout.py`, `pdf-text.txt` and `pdf-fonts.txt` preserve the bounded verification method and outputs.

There are no outstanding A07 factual, numerical or evidence repairs for these exact artifacts. Later source/PDF changes require a new binding check. No original artifacts, scientific rules, Git state, installations or accounts were modified.
