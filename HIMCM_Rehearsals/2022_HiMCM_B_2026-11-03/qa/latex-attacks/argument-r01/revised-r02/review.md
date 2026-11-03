# A06 exact-r03 final argument and sentence review

Canonical verdict: **ACCEPTED_FOR_ARGUMENT_PROSE_PRECISION_AND_TEXT_COVERAGE_ON_EXACT_R03**.

No required repair or optional sentence note remains open from A06. This is acceptance only within the named review scope and for the exact hashes below. Visual layout, fonts, numerical reproduction and other reviewers' acceptance remain separate.

## Bound artifacts

| Target | SHA-256 |
|---|---|
| paper/latex-r01/manuscript-r03.tex | 2c86588b978e271eaafae26f89a4adada724316981586051f5566d509c610685 |
| paper/latex-r01/build-r03/manuscript-r03.pdf | 4b9457da90c3b7a91343a0570fe1072a5bd5f7ff52aa36ecae10d80b687c3ff4 |
| paper/latex-r01/sentence-register-r04.json | ef5ac7a999d90934b0e686cc0b36c80f6a69d6686f105f9c7431537b64c73f33 |
| paper/latex-r01/sentence-delta-r03.json | b7c46ade1e8d4cc6fc549906ce23d50749fa4c840dbf3cc2b9f1cc30703ccf72 |

Predecessor review ledger: `../revised-r01/ledger.json`, SHA-256 `a154b07f075accf98b0df61c55e908f2d549c6f2cc2e07e49d2a2caea259baba`. It contains the original individual judgments for all 311 records, authored after reading every record and its surrounding TeX. This reviewer remains independent of the manuscript author and has not edited a target artifact.

## Exact-delta review and complete ledger

The independent comparison confirms 295 exact unchanged IDs/texts, 16 changed records, three added records and no removed ID. Every changed or added record was read together with its full paragraph. Their 19 individual fresh rationales appear in `delta-notes.txt`. DAT02.05 was also reassessed in its new adjacent context because its previous REPAIR verdict identified the insertion location for the missing qualification.

The complete `ledger.json` and `ledger.md` contain **314 rows**, with exact registered text, SHA-256 text identity, current source line, checked dimensions, rationale, verdict and explicit provenance. There are 294 straight exact-identity carry-forwards, one unchanged sentence with fresh contextual reassessment, and 19 fresh changed/new judgments. No judgment was carried merely because an ID stayed the same. Final counts are 263 PASS and 51 FRAGMENT_PASS, with no NOTE or REPAIR verdict outstanding.

## Closure of the required vintage repair

DAT07.01–02 now explicitly state that the retrospective tests truncate one supplied vintage by observation year and do not reconstruct releases actually available at each historical origin. VAL01.01, TEM03.01 and APP01.02 now refer to supplied-workbook observations dated no later than the origin. This resolves the earlier ambiguity without weakening the ban on realized future inputs. DAT02.05's insertion-location flag is therefore closed.

## Closure of optional notes and other changes

- SUM04.03 and ART05.04 correctly describe crossing dates on conditional paths.
- SUM05.02 and new SUM05.02a separate the 2016 miss from the horizon-derived 2031 display cutoff.
- TEM05.03 states sequential selection and the lower-error T1-Q comparator positively.
- FC05.02 names the fitted relationship and annual-change variables directly.
- REL02.02 distinguishes Table 8's detrending evidence from Figure 5's levels/change contrast.
- SEN02.04 properly states that sensitivity results neither select a replacement nor provide probability bounds.
- APP04.05 directly states actual-path validity instead of invoking a rescue metaphor.
- Additional changes improve observed-level wording, prespecified-rule wording, exposure timing language, the physical saturation-capacity limitation and path-status language. The fresh ledger notes give a specific rationale for each.

These repairs do not change the selected models, numerical results or accepted claims. Annual/March, CO2/CO2-equivalent, 1951–1980, D-development/Q-final, sequential T1-D/T1-Q comparator, the 2016 miss, noncausality and nonblind evaluation remain explicit. C18 text is exact unchanged and retains post-assessment, different-loss, same-forecasts and unchanged-selection qualifications.

## Independent rendered-text and omission checks

Independent Poppler raw and layout extraction both report **zero ASCII semicolons and zero fullwidth semicolons**. Source counts are also zero. All 314 records match the newly extracted PDF text. The independent source inventory finds 93 prose blocks, corresponding to the prior 92 plus DAT07, with no missing or extra block ID.

An explicit omitted-sentence search removed all registered prose and compared the remainder with the independently inspected r02 remainder. The normalized PDF residue is exactly unchanged except for `Accepted log-CO2 fit` becoming `Fitted log-CO2 curve`. The source residue is unchanged after normalizing masking whitespace and accounting for the six figure filenames changing from r01 to r02. Thus no newly unreviewed prose appeared outside the register.

All 54 separately inventoried non-prose entries retain their prior contextual judgments except the F05 label, reviewed afresh below. This carry-forward includes explicit review of the interrogative section heading, imperative heading and complete article-title sentence in `../revised-r01/nonprose-review.md`. These are not silently excluded from review because of their heading role.

The first, second, third, fourth and sixth figure PDFs have new paths but identical bytes to their r01 counterparts. F05-r02 has SHA-256 `d093330e77ac9c7b7b70c8f76ff011d8061b179303005125a9d597c22ad0368e`. Its independently extracted text confirms **Fitted log-CO2 curve** and the absence of the old Accepted label. The other labels, variable definitions, periods and correlations remain unchanged. The new wording is reader-facing and scientifically accurate within this contextual review.

## Limits and final disposition

The earlier six argument/prose concerns were resolved in substance in r02, and the remaining vintage issue and optional notes are now closed. Cadence is judged by argument and readability, not sentence-length quotas or detector evasion. No deliberate errors, lost scientific qualifiers, invented findings or hidden AI assistance were requested or introduced by this review.

This exact r03 candidate passes A06. A subsequent change to source, PDF or registered text requires new identity binding and appropriate delta checks. No acceptance of future bytes, numerical rerun, visual check or font audit is implied.
