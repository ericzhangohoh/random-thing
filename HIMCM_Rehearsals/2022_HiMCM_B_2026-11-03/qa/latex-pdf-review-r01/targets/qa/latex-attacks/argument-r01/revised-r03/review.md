# A06 canonical final r05/r06 binding

Verdict: **ACCEPTED_FOR_SCOPE**.

Scope: argument, natural English cadence, precision, complete registered-text coverage, omitted-prose search and semicolon compliance. No all-page visual review, font certification, numerical rerun or acceptance of future bytes is claimed. T16 remains the separate visual reviewer.

## Exact accepted targets

| Target | SHA-256 |
|---|---|
| paper/latex-r01/manuscript-r05.tex | 1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55 |
| paper/latex-r01/build-r05/manuscript-r05.pdf | 2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac |
| paper/latex-r01/sentence-register-r06.json | 2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c |

Prior independently accepted ledger: `../revised-r02/ledger.json`, SHA-256 `1cef09881b045272729d396769fe3d47bf58977e90ae894d96ada89e26a3e6fc`.

## Identity and substantive review carry-forward

All **314 IDs, exact texts and text hashes match** the reviewer's own accepted r03 ledger. No ID or text was added, removed or changed. The complete final `ledger.json` and `ledger.md` retain all 314 individual rationales and verdicts. Each JSON row records the immediate prior ledger/hash and preserves its earlier provenance. There are 263 PASS and 51 FRAGMENT_PASS judgments, with no unresolved repair or optional sentence note.

The full source diff was read. The only changes from accepted r03 are three page-breaking penalties, nine `nopagebreak` commands after equation lead-ins and a `clearpage` before Conclusions. Programmatic removal of exactly those layout commands yields byte-identical source text. The 93 prose blocks remain unchanged. All 54 non-prose inventory contents, including the previously reviewed sentence-like headings/title, tables, equations and plot labels, match exactly apart from source-line metadata. Figure PDF hashes were also checked.

Accordingly, the prior vintage repair closure and all earlier argument, cadence and precision judgments remain applicable. Scientific boundaries, nonblind evaluation disclosure, C18 post-assessment weighting scope and AI disclosure are unchanged. This is an explicit identity-based carry-forward, not a claim that this turn performed a new manual reading of every unchanged sentence.

## Independent final PDF checks

Fresh Poppler raw and layout extraction confirms all **314 registered records appear in the final PDF**, with no unmatched record. Source and both PDF extraction modes each contain **zero ASCII semicolons and zero fullwidth semicolons**. The user limit of at most three is satisfied.

The omitted-prose search removes the registered records from final PDF text and compares the residue to the previously inspected residue. Every difference was inspected and consists solely of updated table-of-contents page numbers. The alphabetic remainder is identical. The source equality check independently rules out added unregistered prose. This preserves the prior explicit review of caption fragments, references, sentence-like headings and the article title rather than silently excluding them.

Text extraction establishes content presence, not layout quality. No visual conclusion is inferred from the author's pagination or widow fixes.

## Delivery and independence

`verification.json` records the target identities, coverage, source-diff result, residual differences and semicolon counts. `build-review.py` reproduces the identity and text checks. No target was edited, no Git operation occurred and no additional agent was spawned. Target hashes were unchanged after the checks.

This closes A06 on the exact r05 TeX/PDF and r06 register above. Any later textual or artifact-byte revision requires a fresh binding and appropriate review.
