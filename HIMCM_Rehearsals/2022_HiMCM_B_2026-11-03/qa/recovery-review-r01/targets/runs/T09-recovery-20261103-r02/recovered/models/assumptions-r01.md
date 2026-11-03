# Assumptions r01

Owner modeler, T02. Entries distinguish source definitions, simplifying representations and scenario conditions. Evidence status is not approval.

| ID | Statement and purpose | Evidence/status and use | Test or bound; consequence if false |
|---|---|---|---|
| A01 | Supplied CO2 values represent the annual Mauna Loa series despite March caption | T01 provisional data-quality r01 confirms annual file/value match; M00/M01 | Consume accepted T01 and preserve caveat; cannot make actual March comparison |
| A02 | Supplied temperature anomaly uses 1951–1980 baseline | Original p4 and T01; all T models/thresholds | Check metadata; changed baseline invalidates thresholds and prose |
| A03 | Preserve supplied 2022-vintage observations through 2021 | Intake; T01 notes current revisions | Hash/version checks; no later/current values in fitting; backtests cannot recreate each historical real-time vintage |
| A04 | Pair annual indicators by calendar year | 63 common years; temperature includes extra 1958 | Exact join/count test; positional join corrupts relationships and invalidates runs |
| A05 | Recent ten-year growth persists under D | Modeling scenario, not a world fact; M02 | Backtest, compare Q/E and endpoint-window sensitivity via other paths; weak performance rejects superiority |
| A06 | Constant absolute acceleration under Q | Modeling scenario; fitted coefficient free in sign | Backtest and derivative/positivity checks; turning/negative extrapolation flags restrict use |
| A07 | Constant proportional total-concentration growth under E | Empirical model assumption, not carbon-cycle law | Backtest, original-unit loss and long-path comparison; limits century-scale claims |
| A08 | Time-only temperature slope can continue under T0 | Empirical baseline assumption | Temporal comparison and last-30-year sensitivity; no physical interpretation |
| A09 | Historical log-CO2/anomaly association transports under T1 | Statistical continuation assumption | End-to-end temporal errors, alternate CO2 inputs and window sensitivity; no causal beta or policy effect |
| A10 | Annual static association is adequate for a simple path | Omits lags, heat storage and other forcings; explicit simplification | Residual/difference diagnostics and final errors; omission limits explanation even with good fit |
| A11 | Short historical error scale is informative only conditionally | Limited empirical evidence; overlapping folds are dependent | Report five origins per horizon, final envelope misses and errors; no probability coverage claim |
| A12 | Integer central-path first passage answers requested date | Operational definition, not observed or sustained crossing | Boundary, non-crossing and already-above tests; explain precise semantics in paper |
| A13 | 685 ppm pure CO2 remains a requested exercise | T01 identifies source value as CO2-equivalent | Keep source correction adjacent; no false refutation/validation of OECD scenario |
| A14 | Simultaneous station-CO2/global-temperature relationship is descriptive | Spatial aggregation mismatch and omitted drivers | Clearly name entity/coverage; cannot extrapolate local weather or claim unique attribution |
| A15 | No stochastic distribution or long-horizon probability law is identified | Data/method limit, M07 | Use empirical errors and sensitivity, not fake precise confidence limits |

Priority is A01–A04 for admission, A05–A10 for predictive/structural evidence, and A11–A15 for claim strength. If an assumption fails, preserve its prior version and revise affected interfaces, runs and claims; do not repair accepted outputs by editing table cells. No assumption makes a preferred policy or winner true by construction.
