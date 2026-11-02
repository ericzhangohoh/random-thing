# Walkthrough: Comparing Forecasts Without Selecting a Winner in Advance

**Historical anchor:** [2022 HiMCM B](../../HIMCM_备赛资料/02_历年真题/2022/2022_HiMCM_Problem_B.pdf), which asks for modeling and prediction of atmospheric CO₂ and temperature. This exercise illustrates a prospective workflow. No model has been fitted or validated by this exercise.

## 1. Coordinator: admit and interpret

Create `R01` for model comparison, `R02` for requested future estimates and `R03` for the interpretation of forecast reliability. Copy exact wording, data ranges and horizons from the official problem before treating the map as complete.

Separate the target quantities, their units, information available at each forecast origin and the difference between short-horizon evaluation and distant extrapolation. Submit G1 with this interpretation and the consequential ambiguities.

## 2. Domain-data: establish compatible observations

Deliver source versions, measurement definitions, time frequency, coverage, missingness and revisions. Explain whether a temperature series is an absolute measurement or anomaly relative to a baseline. Do not join annual and monthly data without a documented aggregation rule.

The handoff must say which data are suitable for fitting and whether independent validation observations are available. A claimed physical relationship between CO₂ and temperature requires more than correlating two trending series.

## 3. Modeler: propose candidates and a comparison

Candidate families might include a simple trend baseline, a differently shaped growth curve and a time-series formulation if the diagnostics and sample size support it. These are hypotheses to compare, not a mandated list.

Proposed decision record:

- Task fit: predict identified quantities at defined horizons and compare reliability.
- Mechanism/structure: trends and temporal dependence; physical plausibility for extrapolation.
- Data fit: diagnose trend, residual dependence and sample size before increasing complexity.
- Comparison: preserve time order; use common forecast origins and horizons; compute errors on the same observations.
- Rejection condition: a candidate that loses to the baseline, violates plausible long-run behavior or is unstable across reasonable origins is not selected merely for a high training fit.

Submit G2 after a small feasibility experiment where needed. Record a provisional architecture rather than prewriting the final winner.

## 4. Computation: run the agreed experiment

Implement the baseline first. Check time indexing and ensure preprocessing does not learn from future observations. Save each prediction with origin, target date, horizon, actual observation and model version.

Run the agreed comparisons. Preserve unfavorable results and failures. Report horizon-specific errors with units and variation across origins; do not silently average incomparable horizons into one flattering metric.

## 5. Reviewer: challenge the claim

Check leakage, matching evaluation periods, metric definitions, model tuning and the difference between interpolation and extrapolation. Ask whether a distant projection is conditioned on continued historical relationships. If no model is reliably distinguishable, request an honest comparison and narrower claim rather than a forced winner.

## 6. Writer: express only the observed finding

Before results exist, write “We will compare…” in the working notes. After accepted runs, replace this with the actual findings and references. A suitable final claim has the structure:

> Over [identified evaluation origins and horizons], [model] achieved [actual metric] relative to [baseline]. Its projection to [future date] assumes [conditions]; the available backtest does not establish accuracy at that distant horizon.

Brackets are required inputs, not permission to invent numbers. The final choice remains unresolved until real evidence is available.

## 7. What this exercise checks

The workflow produces a requirement map, data questions, comparable candidates, a falsifiable selection protocol, role-specific handoffs and an appropriately bounded claim. It deliberately does not treat training fit or a historical winner's method name as sufficient justification.
