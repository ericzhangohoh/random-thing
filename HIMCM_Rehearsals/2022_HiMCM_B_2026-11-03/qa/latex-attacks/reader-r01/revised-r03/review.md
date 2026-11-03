# A08 final sentence acceptance

**ACCEPTED_FOR_SCOPE** — exact final manuscript-r05 / sentence-register-r06.

Scope: reader clarity, natural purposeful variation, preserved caveats, full per-sentence provenance, source/register completeness and independent PDF textual coverage. This is **not an all-page visual review**. T16 performs the separate visual review.

Actual bytes verified:

- `paper/latex-r01/manuscript-r05.tex`: `1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55`
- `paper/latex-r01/build-r05/manuscript-r05.pdf`: `2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac`
- `paper/latex-r01/sentence-register-r06.json`: `2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c`

The earlier r03 recheck remains preserved in `../revised-r02/`. Its 19 changed/added records were personally reread with complete paragraph contexts. All four original required repairs and both optional clarifications were resolved. The data-vintage and physically justified saturation qualifications are clear and bounded.

For final r05, all 314 ordered IDs and exact sentence texts match that reviewed version. Every final ledger row verifies its text SHA-256, retains the specific rationale, and records the prior ledger path/hash and full earlier provenance chain. There are 314 PASS records with no unresolved sentence finding.

I independently read the r03-to-r05 source diff and verified that removing the specified widow/club/display penalties, no-page-break directives and clear-page directives makes the two sources identical. The balanced-brace inventory finds all 93 prose blocks and exact block text. All 54 non-sentence inventory items retain their equation/table/heading/figure/furniture text. Thus no sentence or numerical-text change is silently accepted as layout.

A fresh `pdftotext -layout` extraction of the exact final PDF has 16 pages, with the nontechnical article on page 15. All 314 normalized sentence texts occur after removal only of running heads and terminal page-number furniture. No omitted or unregistered prose was found. ASCII semicolon count is **0** and fullwidth semicolon count is **0**, including imported figure text, satisfying the maximum of three.

Complete final ledgers: `sentence-ledger.json` and `sentence-ledger.md`. Reproducible bounded checks: `bind-final.py`, `checks.json` and `pdf-text-r05.txt`. Acceptance applies only to the verified bytes above, not future revisions or scientific validation beyond the already stated evidence scope.
