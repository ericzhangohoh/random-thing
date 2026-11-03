# Source and data quality findings r01

## Evidence inspected

The complete official four-page statement was read, including all requirements, bibliography, both complete printed tables and their source notes. Artifact Tool imported both workbook sheets and read A1:Z100. A separate ZIP/OOXML inspection covered every stored cell, all sheet metadata, defined names and annotation/object parts. Thus sparse cells outside the visible A:B tables were also checked. No workbook edit/export occurred. No historical solution paper was read.

## Executed checks

- Original PDF and XLSX were copied byte-for-byte into `inputs/`; direct byte equality and SHA-256 were verified.
- Both sheets contain exactly the headers and observations reported in the dictionary. CO₂: 131 stored cells, 128 populated cells, 63 data rows; XML dimension A1:H64. Temperature: 134 stored cells, 130 populated cells, 64 data rows; XML dimension A1:H65. The seven remaining stored cells are blank formatting cells. Nonempty data occupy A:B only.
- Neither sheet has hidden rows/columns; both sheets are visible. No formulas, notes, threaded comments, merged cells, hyperlinks, defined names, drawings, embedded tables or external workbook links exist in the OOXML package. Artifact Tool's two detected “tables” are inferred rectangular data regions, not native Excel Table objects.
- Every populated value from Artifact Tool agrees with OOXML within 1e-10 absolute tolerance (text exact). Initial exact decimal comparison failed on ordinary XLSX binary floating-point serialization, e.g. B3=316.91000000000003 versus 316.91. The check was corrected to a numeric tolerance; original bytes were preserved. This is a reader-representation issue, not missingness or an altered observation.
- Every one of the 127 year/value pairs in the statement's printed tables matches the workbook at the stated precision.
- No missing years, duplicated years, missing values or nonnumeric observations. CO₂ rises each year; annual changes range 0.42–3.40 ppm. Temperature annual changes range −0.25–0.28°C. These data-level summaries do not justify discarding any point.
- Join verification: 63 matched years 1959–2021; 1958 is temperature-only. Direct row-position join would be wrong.

`workbook-xml-audit-r01.json`, `workbook-artifact-allcells-r01.json` and `data-checks-r01.json` preserve the checks and all inspected cells. `audit-source-r01.py` and `check-data-r01.py` make the inspection reproducible.

## Definition conflicts and bounded conclusions

1. **Annual versus March — confirmed caption/attribution conflict.** The problem's p3 describes March averages but cites NOAA's annual-mean file. The supplied values match the annual series, including 2004=377.70. NOAA's current monthly file has March 2004=379.06 ppm, illustrating that March and annual means differ. Current monthly values are only contextual verification, not a substitute historical dataset. Treat the supplied series as annual and state that it cannot directly test a March-specific claim. [S03–S05]
2. **Ten-year increase — computed on supplied annual values.** Define an interval by ten elapsed years, C(y)−C(y−10), and its average growth by division by ten. In 1994–2004 the increase is 18.74 ppm (1.874 ppm/year). Among prior available intervals ending 1969–2003, the largest is 1993–2003 at 18.77 ppm (1.877 ppm/year). Therefore 2004 is not strictly the largest in the supplied annual series; the 0.03 ppm difference is small and should not be overstated as a physically significant distinction. This is not a test of all periods before 1959 or of March observations. [S01–S02; computed `data-checks-r01.json`]
3. **May 2022 — source claim supported with matching frequency.** NOAA's June 3, 2022 release reports a May monthly average of 420.99 ppm from NOAA and 420.78 ppm from the independent Scripps record, consistent with the rounded 421 ppm statement. It is a monthly Mauna Loa concentration, not a 2022 annual global mean. It remains outside fitting/validation data. [S06]
4. **OECD 685 — confirmed unit/scope error in the problem.** The OECD 2012 report's chapter 3, printed p83 (physical PDF p85), gives approximately 685 ppm CO₂-equivalent in 2050 for greenhouse gases. It separately gives CO₂-only levels around 530 ppm in 2050 and 780 ppm in 2100. Its baseline assumes continuation without new policies and is a conditional scenario. Still solve the required 685 ppm CO₂ crossing exercise, but do not describe disagreement as falsifying OECD's different quantity. [S07]
5. **Temperature baseline — explicit and unchanged.** Use anomalies against 1951–1980. The requested 1.25, 1.50 and 2°C thresholds are relative to that baseline, and must not be relabeled as pre-industrial warming or Paris target dates. NASA's FAQ confirms that its anomalies use this base period. No contemporary baseline correction is imported. [S01, S08]
6. **Archive versus live revisions.** Current NOAA annual data agree with the supplied values for 1959–2018 but differ for 2019 (411.65 versus supplied411.66), 2020 (414.21 versus414.24) and 2021 (416.41 versus416.45). NOAA warns of revisions. These small differences reinforce freezing the supplied vintage; they are not evidence of workbook transcription errors. Current-source observations after 2021 are prohibited from all modeling inputs. [S04]

## Limits that affect modeling

This is a 2022-vintage retrospective data exercise, so backtests use a single supplied vintage and cannot prove what an analyst would have known at each earlier date. Shared upward time trends can inflate level correlations. The data alone cannot identify climate sensitivity or separate CO₂ effects from omitted drivers and lags. Annual residual variation, extrapolation form, reference-vintage changes and policy/scenario changes are distinct uncertainties. Long-range projections should remain conditional; no data-quality check licenses accuracy through 2100.

Not performed: full external-report reading, monthly reconstruction of every historical March ten-year interval, external model benchmarking, greenhouse-gas equivalence conversion, causal identification, model fitting or forecast validation. These are outside T01 or unsupported by supplied fields. Independent review is still required.
