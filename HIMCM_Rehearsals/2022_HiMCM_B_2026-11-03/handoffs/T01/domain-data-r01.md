# Handoff — T01 — domain-data — r01

- Producing role/session: domain-data, `/root/rehearsal_data`, 2026-11-03 UTC.
- Next recipient: coordinator `/root`, then independent reviewer and modeler/computation consumer.
- Status: complete for T01 scope; requests independent review, not self-acceptance.
- Question: Are the statement/workbook intact, compatible and sufficiently defined for the historical modeling exercise, and how should the March, May2022, OECD and temperature-baseline claims be interpreted?
- Ownership: all writes limited to `inputs/`, `research/`, `data/raw/`, and this role's T01 handoffs. No model/computation/reviewer authorship, processed-data transformation, control edits, solution reading, biological research, Git or installations.

## Inputs actually read

`domain-data-r00.md` records the exact initial control-input hashes and acknowledgment before source work. Read DOC_ROOT WORKING_DOC sections1–6, role/domain-data, shared-directory protocol, coordination and source/handoff templates. Applied the Spreadsheets skill and its read-only/API/style guidance. Full four-page source statement and every workbook cell/package annotation were inspected.

Original archive directory: `/Users/ericzhang/Desktop/himcm/HIMCM_备赛资料/02_历年真题/2022/`.

| Admitted original | SHA-256 | Verification |
|---|---|---|
| `inputs/2022_HiMCM_Problem_B.pdf` | `fb9000006eb0402d24c4e810a0e6d4cd69f26f94181a48adbfe9c795d6669ece` | 212551 bytes; exact byte equality to archive; all4 pages read. |
| `inputs/2022_HiMCM_Data.xlsx` | `73a4c73433d530cdbd3bb7509131bea528eeffd52d1a66b2ddeddf44543a2a4a` | 14857 bytes; exact byte equality; both complete sheets and metadata audited. |

Primary references actually inspected: NOAA data definitions, annual and monthly file headers/selected historical values, June3 2022 concentration release, NASA GISTEMP baseline/L-OTI FAQ, and OECD2012 relevant climate/scenario passages. Exact URLs, dates, scope and retained evidence are in the source register. Current references are definition/context evidence only. No later or revised observation replaces supplied modeling values.

## Output packet and identity

Complete23-artifact inventory: `research/artifact-hashes-r01.json`, SHA-256 `4c4161752d7eac5dd01a01d35be18e7b10a65701f77cdcf6b66e943fd5d68451`.

| Main artifact | SHA-256 | Contents |
|---|---|---|
| `research/data-dictionary-r01.md` | `7b3d932b653b835431b068f857f540ca28bc1ab66dfab6c3e72a81a072c27028` | Exact ranges, fields, entities, units, frequency, join, precision and preparation contract. |
| `research/data-quality-r01.md` | `3a73e4241c5a872f6782735efac5ab7081d62ee5ab8ee3e5245c7e27db3cfb1a` | Executed checks, source conflicts and claim limitations. |
| `research/source-register-r01.md` | `9efcc164ce5e11aa7aec725fa8895c88d632b40e2846db0fd76eefa9bbb2be75` | Eight source IDs, actual URLs/dates, read coverage, archival paths and limitations. |

The inventory additionally pins: input/web-snapshot manifests, complete problem extraction, Artifact Tool overview/allcells JSON, raw OOXML audit JSON, all six retained web references, `data-checks-r01.json`, reproducible read-only inspection scripts and execution outputs. Web originals versus tool extracts versus selected exact quotes/paraphrase are distinguished in the snapshot manifest. No unretained source hash is passed off as an archived original.

## Findings and consequences

1. **Supplied data contract:** 63 CO₂ annual means for1959–2021,64 annual temperature anomalies for1958–2021. No missing/duplicated years or values. Join by year yields63 matched records1959–2021 and excludes only temperature1958. Do not join by row number.
2. **Annual/March:** NOAA's annual-source link and matching values establish that the supplied CO₂ series represents annual means. Its March caption is contradictory. Current NOAA month3/year2004 is379.06 ppm, whereas its annual2004 is377.70 ppm. Do not claim this supplied annual dataset tests March-specific observations.
3. **Computed annual ten-year check:** with C(y)−C(y−10),1994–2004 gives18.74 ppm,1.874 ppm/year; the greatest prior available window is1993–2003 at18.77 ppm,1.877 ppm/year. Thus the2004 annual increase is not strictly largest. The0.03 ppm gap is small and no measurement-significance inference is justified. All36 windows ending1969–2004 are recorded.
4. **May2022:** the June3 NOAA release reports monthly NOAA420.99/Scripps420.78 ppm, supporting rounded421 ppm. It stays outside the frozen fitting/backtesting data.
5. **OECD:** primary printed p83/physical PDF p85 says685 ppm **CO₂-equivalent** for greenhouse gases in2050, with CO₂ alone about530 ppm2050 and780 ppm2100. It is a conditional baseline without new policies. The problem misattributes685 as CO₂. Keep the required mathematical685 ppm CO₂ crossing exercise, but do not label it verification/refutation of OECD's different quantity.
6. **NASA:** temperature thresholds remain relative to1951–1980; do not relabel them as pre-industrial or Paris-target crossings. L-OTI combines land-air and ocean-SST anomalies, so this is an observational index, not absolute temperature.
7. **Source vintage:** current annual NOAA values differ slightly for2019–2021. Freeze supplied411.66/414.24/416.45; do not substitute current411.65/414.21/416.41. Current source files include later years but are excluded from every fit and validation input.

## Checks performed, limits and alternatives

Executed: source byte equality/hashes; Artifact Tool import and complete cell read; OOXML all-cell/annotation/metadata inventory; independent-reader numeric comparison; all127 printed-table year/value pair comparison; missing/duplicate/year-range/value-range checks; join count; exact hundredth-unit Decimal ten-year arithmetic; historical vintage-difference check. All final checks passed. The exact-decimal cross-reader check initially exposed binary float serialization tails and was corrected to1e-10 absolute numeric tolerance, without changing originals. This failure/repair is described in the quality report.

Inspected, not computed: NASA baseline/source methodology and NOAA/OECD reference definitions. No forecast model fit, causal identification, full historical March reconstruction or external forecast benchmark was performed. No workbook was changed/exported. The OECD report was not read in full; biological chapters and historical solutions were not researched.

Access limits: original NOAA page/data and NASA HTML retained. Direct NOAA news/OECD PDF downloads returned403, so successful web-source text and selected OECD evidence are retained with explicit format labels; the old OECD highlights URL returned410. No automatic approval rejection occurred. These are archival-format limitations, not invented source contents.

Rejected alternatives: silently treating annual values as March; changing temperature baseline; replacing observations with live revisions; fitting to OECD scenario numbers; inferring greenhouse-gas equivalents from CO₂ alone; expanding literature beyond the bounded definitions. Each would change the task or supported meaning.

## Requested next action

Coordinator: pin this packet and assign independent source/data review. Adopt or explicitly revise the annual interpretation and corrected OECD attribution for G1. Modeler/computation: acknowledge the accepted dictionary/packet revision in your own handoff before consequential use; independently parse the supplied XLSX, retain2021 cutoff and baseline, assert the63-row year join, and keep source-context values separate from fit/validation. Reviewer may independently recompute the ten-year result and check exact ranges/hash identities.

No unresolved missing input blocks provisional empirical modeling. The specific March-only claim and causal interpretation remain unsupported by these supplied data. A consumer acknowledgment is still required; this producer does not fabricate one or edit another role's handoff.
