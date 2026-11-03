# Supplied-data dictionary r01

Model input authority is `inputs/2022_HiMCM_Data.xlsx`, SHA-256 `73a4c73433d530cdbd3bb7509131bea528eeffd52d1a66b2ddeddf44543a2a4a`. The immutable source supplies observed historical summaries through 2021. Web snapshots are definition evidence only, including when they contain later or revised historical values.

| Proposed field | Exact source | Entity and definition | Unit / grain | Coverage / missingness | Preparation and permitted use |
|---|---|---|---|---|---|
| `year` in CO2 table | `CO2 Data Set 1!A2:A64`, header A1 `Year` | Calendar year of Mauna Loa annual mean | Integer year, one observation per year | 1959–2021, 63 unique consecutive years | Read as integer; no imputation or extra rows. |
| `co2_ppm` | `CO2 Data Set 1!B2:B64`, header B1 `PPM` | Annual atmospheric CO₂ mole fraction in dry air measured at Mauna Loa, Hawaii | μmol/mol, equivalent to ppm; annual mean | 315.98–416.45; all 63 numeric, no blanks | Preserve original values. Interpret as annual mean despite the problem's erroneous March caption; no monthly/annual conversion. It is a site series used as an atmospheric proxy, not a spatial global mean. |
| `year` in temperature table | `Temps Data Set 2!A2:A65`, header A1 `Year` | Calendar year of global annual temperature anomaly | Integer year, one observation per year | 1958–2021, 64 unique consecutive years | Retain 1958 for standalone temperature models if model specification allows; exclude only from the joined CO₂ analysis because there is no supplied CO₂ observation. |
| `temp_anomaly_c` | `Temps Data Set 2!B2:B65`, header B1 `Degrees C` | Global annual land–ocean temperature anomaly, relative to 1951–1980 | °C anomaly, annual | −0.20–1.02; all 64 numeric, no blanks | Keep this baseline. Negative anomalies are valid and must not be treated as missing; no baseline shifting or absolute-temperature conversion. |

The problem identifies GISTEMP v4 and a source access date of 2022-10-18 (statement p4). This is processed observational data, not individual thermometer readings. NASA's L-OTI combines land surface-air and sea-surface temperature anomalies; the problem's phrase “surface-air” should not imply direct air-temperature measurements over every ocean cell.

Join contract: inner join on the integer year produces 63 rows, 1959–2021. It is a temporal association between a Mauna Loa atmospheric proxy and a global temperature index. Do not join by spreadsheet row number: temperature is offset by one year. Spatial scope is not identical. This join cannot identify a causal effect on its own.

Precision: the supplied display and PDF tables use up to two decimal places. A few underlying XLSX numeric strings contain binary serialization tails (for example 316.91000000000003); these are not extra measurement precision. Numeric readers may represent these as 316.91. Audit comparisons use absolute tolerance 1e-10; the source remains unchanged. The data-level ten-year check uses Decimal arithmetic at supplied hundredth-unit precision.

Missing codes: none present. No zero values are present, but zero would be a valid temperature anomaly. No confidence intervals, sample counts, monthly records, emissions, policy variables or exogenous climate drivers are supplied. Do not invent them or label fitted forecast intervals as measurement uncertainty.

Preparation owner is computation. Recommended contract: read exact named ranges or headers, assert record counts/years/unique keys/finite values, retain original provenance, and freeze the observations. Any centering/scaling or model selection must respect training boundaries. No transformation to `data/processed/` has been performed by this role.
