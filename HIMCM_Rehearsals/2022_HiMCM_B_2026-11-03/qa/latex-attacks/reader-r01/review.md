# A08 independent reader review, frozen manuscript-r02

Disposition: four minor but concrete editorial repairs recommended before prose acceptance. No consequential scientific claim error identified within the accepted C01–C18 scope. This is an independent reading, not reliance on a prior sentence review. No other sentence review was read. No target artifact was edited.

Exact artifacts:

- TeX SHA-256: `f9f60adb63996ae83d2bffeec43e4e3b9e04cc10d9e85cbd1c3f452db8bed35b`
- PDF SHA-256: `c0e4a245b2b5013effbd7fcca5262db2114ab5b48e3162b5a7482707e2137e8e`
- Register SHA-256: `80e9e581927f4483cf99a3038dea6fb387ba9a903edec7b9b36cd69b8e940e7e`

## Concrete repairs

1. `SUM06.01`, TeX line 55, PDF page 1: “associated at level” is nonstandard English and unnecessarily opaque in the summary. Use “strongly associated in their observed levels”. Retain the trend-removal and differencing caveat.
2. `VAL03.03`, TeX line 137, PDF page 6: “primary selection receipt” is undefined project-workflow jargon exactly where readers need to understand exposure chronology. Use “before the primary run recorded its selection”. Retain the prior score exposure and the next sentence's no-blind-holdout limitation.
3. `APP04.03`, TeX line 281, PDF page 13: “Already-above-origin” fails to say above what, while “valid non-crossing-through-2300” reads as a machine status. Use “Paths already above the threshold at the forecast origin are distinguished from valid paths that do not cross it by 2300.” This preserves both algorithmic cases.
4. `ART05.04`, TeX line 294, PDF page 14: the antecedent of “They” is dates, but dates do not describe paths. Use “These are crossing dates on conditional annual paths, not established deadlines, sustained warming dates or Paris targets.” All limitations remain.

Two optional clarifications are recorded separately, not escalated to mandatory style changes: `SUM02.04` should preferably call D the choice under the prespecified rule, since the rule rather than the winner was prespecified. `APP04.05` can say all actual primary paths remain valid throughout the search domain, avoiding “such a rescue”, whose nearest referent is a prohibited invalid-gap bridge.

## Every-record reading and cadence

The ledger contains all 311 exact register IDs, their SHA-256 text hashes, exact text, verdict, specific rationale and any proposed repair. Each rationale was written after reading the record and its paragraph/equation/table context. The script only aligns the manually authored per-block reasons to IDs and checks counts. It does not manufacture default PASS reasons. There are 305 passes, four repairs and two optional suggestions.

The prose generally varies purposefully: short claims introduce results, longer sentences explain conditions, and concrete boundary values justify the numerical precision. Technical sections appropriately retain notation and numerical detail. The article uses shorter explanations and rounded ranges. Repeated limitations across summary, body, conclusion and article are justified by those sections' independent reading uses. No arbitrary length target or variation quota is recommended.

The C01–C18 limits survive: annual/March distinction, physically insignificant arithmetic margin, OECD quantity mismatch, development-versus-later ranking reversal, sequential rather than global temperature selection, conditional baseline-specific annual crossings, noncausal association, short overlapping tests, 2016 envelope miss, no probability bounds, sensitivity and no intervention-effect estimate. C18 is clearly post-assessment, uses the same forecasts with another loss, and does not reselect D.

## Independent completeness and punctuation check

A separate balanced-brace parse of the actual TeX finds 92 p/txt blocks, exactly matching the register's block IDs and exact block TeX. Personal reading of the full source and PDF-extracted content found no unregistered prose elsewhere. Equation lead-ins are deliberately completed by equations, not incorrectly rejected as incomplete prose. Reference fragments are conventional bibliographic elements.

The 54 non-sentence entries were inspected: nine mathematical environments, twelve tables including the summary table, 26 headings, six imported figure-label sets and one furniture inventory. These cover table cells, annotations, legends, titles, running heads, footers, contents repetitions and numbering. The titles and running text outside p/txt are accounted for by furniture. Disclosure and bibliography prose are in the sentence ledger. Figure label text introduces no omitted sentences.

A fresh `pdftotext -layout` extraction of all 15 PDF pages contains **0 ASCII semicolons and 0 fullwidth semicolons**, including imported figure text. Source TeX likewise contains zero of each. The requested maximum of three is satisfied. This textual review did not need additional raster rendering, and is not a separate layout or font certification.

Artifacts: `sentence-ledger.json`, `sentence-ledger.md`, `manual-reasons.txt`, `build-review.py`, `completeness-and-punctuation.json`, and the fresh `pdf-text.txt` under this directory. Any author repair creates a new artifact requiring an exact-version recheck. This review closes only the specified r02/r03 combination.
