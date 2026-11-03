# A06 full sentence and argument review of frozen LaTeX r02

Disposition: **one focused repair requested** before final acceptance. The LaTeX rewrite materially improves argument and cadence. Every one of the 311 registered records has an individually authored contextual judgment. The separate non-prose review also explicitly covers sentence-like headings and the article title.

## Identity, independence and scope

| Frozen target | SHA-256 |
|---|---|
| paper/latex-r01/manuscript-r02.tex | f9f60adb63996ae83d2bffeec43e4e3b9e04cc10d9e85cbd1c3f452db8bed35b |
| paper/latex-r01/build-r02/manuscript-r02.pdf | c0e4a245b2b5013effbd7fcca5262db2114ab5b48e3162b5a7482707e2137e8e |
| paper/latex-r01/sentence-register-r03.json | 80e9e581927f4483cf99a3038dea6fb387ba9a903edec7b9b36cd69b8e940e7e |
| control/accepted-claims-latex-r01.json | 907aa514b72f760fcb9a38e6faf06ff3ad108912ffb7562ac378fd5765f2d334 |

All target hashes were checked before and after ledger generation. This reviewer authored no target text, made no target edits, and used no subagent or Git operation. Read authority: accepted G3 claims, additional C18, interpretation r02, the complete registered text and surrounding TeX. Independent Poppler extraction was used instead of the author's extraction script. This is a prose/argument/precision review, not independent numerical reproduction, font verification or visual acceptance.

## Coverage and checks

- `ledger.json` and `ledger.md` contain all 311 exact IDs/texts, exact-text SHA-256 identities, source lines, checked dimensions and a specific rationale or repair for each record.
- Counts: 248 PASS, 51 FRAGMENT_PASS, eight optional NOTE records and four REPAIR records sharing one substantive issue. Notes are individually authored, not blanket generated approvals.
- An independent balanced-brace scan found all 92 prose macros and no extra/missing block IDs.
- All 311 records matched independently extracted PDF text after Unicode/whitespace/punctuation normalization. No unmatched record was ignored.
- Source, raw PDF text and layout PDF text each contain **zero ASCII semicolons and zero fullwidth semicolons**. The user maximum of three is satisfied.
- Omitted-sentence search: after removing registered prose, source residue contains only headings/titles, environments, figure inclusions, reference item commands and layout control. After removing registered records from normalized PDF text, the residue contains the expected tables, displays, plot labels, headings, titles, TOC and page/reference furniture. Both residues were inspected, not merely counted.
- `nonprose-review.md` separately assesses all 54 inventory entries. The question heading, imperative heading and complete article title are explicitly treated as sentence-like content. Bibliographic and caption noun phrases that the register labels “sentence” are classified as fragments without avoiding their review.

Normalization establishes text presence, not typography or layout quality. The read-only PDF text extraction and source inspection do not substitute for the assigned visual review.

## Required repair A06-R02-01 — P2: restore the supplied-vintage limitation

The original manuscript explicitly stated that retrospective supplied data do not recreate the exact vintage available to historical forecasters. That qualification is absent from this rewrite. Meanwhile VAL01.01 says observations were “available through” the historical origins, TEM03.01 says they were “available by that date,” and APP01.02 says forecasts “respect the observations available at their origin.” These can be read as recreating information actually available then, rather than truncating the later supplied workbook by observation year.

Repair once, clearly, in the data/method discussion. For example: “These retrospective tests truncate the supplied data vintage by year. They do not reconstruct the releases actually available at each historical forecast origin.” Qualify the three availability phrases as “dated no later than the origin in the supplied workbook,” or use one sufficiently explicit shared definition. No refit or model change is requested.

The four REPAIR ledger rows are DAT02.05 as the insertion location plus VAL01.01, TEM03.01 and APP01.02 as affected statements. They are one issue, not four independent defects. Acceptance requires exact new text to preserve year-based future-input exclusion while acknowledging retrospective vintage. Exposure and vintage are separate limitations, so the existing prior-score disclosure does not fix this issue.

## Optional precision/cadence notes

These do not independently block the paper's scientific interpretation. The writer may adopt or decline them with reasons.

| Records | Concrete improvement |
|---|---|
| SUM04.03, ART05.04 | Dates are first annual crossings along conditional paths. Saying that dates “describe paths” is a slight category mismatch. Keep the realized/sustained/Paris limits. |
| SUM05.02 | Separate the 2016 miss from the 2031 horizon-derived cutoff. Their current conjunction compresses two different arguments. |
| TEM05.03 | “Calling T1-D the global minimum would therefore misrepresent the results” repeats the explicit adjacent ranking in defensive editorial language. A positive statement of sequential-selection status is smoother. |
| FC05.02 | Replace repeated internal “accepted” terminology with the fitted curve and diagnostic changes the reader sees. The plot legend has the same optional wording issue. |
| REL02.02 | Figure 5 shows levels and differences. Table 8 supports the full preceding contrast, including detrending. Cite Table 8 as well or narrow the figure-reference sentence. |
| SEN02.04 | Comparisons are not a model. State that these results neither select a replacement model nor provide probability bounds. |
| APP04.05 | “Rescue” is a loose metaphor for a prohibited gap-bridging operation. State directly that actual primary paths remain valid throughout the search domain. |

## Disposition of the six earlier findings

1. **Design rationale:** resolved in substance. CO201 contrasts assumptions, VAL01 labels choices as declared rather than optimized, VAL02 explains MAE/task weighting, and TEM04 explains sequential selection.
2. **Abstract overload:** materially improved. Separate association paragraph and shorter result sentences clarify the hierarchy. SUM04/SUM05 retain optional compression notes, not a demand for blanket rewriting.
3. **Repeated warnings:** improved. HOR01 and CON04 now state positively what testing establishes. Necessary local baseline/frequency/quantity limits remain. Some defensive phrasing is optional polish.
4. **Mechanical cadence:** improved through connected methods, short direct answers and longer explanations where dependencies warrant them. Conventional sections replace page-sized audit units. No arbitrary length metric or detector-evasion criterion was used.
5. **Exposure disclosure:** resolved. VAL03.03–04 place the limitation next to the scores and DIS03 preserves full context. No globally blind holdout is claimed.
6. **Conclusion synthesis:** resolved. CON03 connects ranking reversal, stronger comparator, 2016 miss and fitting-window sensitivity. CON04 preserves useful comparative evidence without inventing a universal reliability deadline.

## Scientific-boundary check

Annual/March, CO2/CO2-equivalent, 1951–1980, D-development/Q-final, sequential T1-D versus stronger T1-Q, the 2016 miss and noncausality remain explicit. C18's method and rounded scores agree with its accepted scope. It is called post-assessment, uses the same forecasts under a different loss, and leaves selection unchanged. The full sentence ledger found no additional substantive overstatement within this review's remit.

## Next acceptance step

The paper requires only the focused vintage repair for this reviewer. Any resulting TeX, PDF or register change creates a new target identity. This review cannot approve future bytes. Bind a delta check to the exact repaired artifacts, inspect every changed/new record and surrounding context, repeat rendered-text coverage/semicolon checks, and explicitly carry forward unchanged sentence judgments by exact text identity. Multiple independent sentence reviews remain the coordinator's responsibility.
