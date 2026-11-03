# Mathematical specification r01

T02; modeler; proposed before historical model computation. Constants are design choices, official thresholds or labeled toy inputs. Failures return explicit statuses.

## M00 — observations and fitting

`t` is integer calendar year; `C_t` is supplied annual CO2 concentration in ppm; `T_t` is global annual anomaly in degrees C relative to 1951–1980. Set `x_t=(t-1959)/10`; one x-unit represents a decade. Expected CO2 years: 1959–2021; temperature: 1958–2021; common fitting: 1959–2021. Join by year, never row position.

Require unique integer years, all expected observations, finite numbers and positive CO2. No silent dropping, imputation, further rounding or replacement. Schema/coverage/definition disagreement returns `INPUT_CONTRACT_FAILURE`. No post-2021 observations or current revisions enter. Origin o is the end of its annual record; horizon h targets o+h. Fit all estimated quantities only on years <=o. Mauna Loa CO2 paired with global temperature is an indicator, not a spatial global CO2 sample.

Use QR/SVD least squares with full column rank and finite parameters. Retain full precision; render sensible ppm precision, temperature to hundredths and dates as integer years. No explicit matrix inverse, random sampling or nonlinear optimizer is needed.

## M01 — ten-year arithmetic (R01)

For t=1969,...,2004, `Delta10_t=C_t-C_(t-10)` ppm and `g10_t=Delta10_t/10` ppm/year. Compare 2004 with the maximum over 1969–2003, returning endpoints, changes, all maximizing years, rank, margin and strictly-larger/tied/smaller status. Numerical tolerance 1e-9 ppm handles arithmetic equality, not observational uncertainty. Claims exclude unsupported earlier periods and actual March observations.

Toy C(t)=300+2(t-2000) gives every available ten-year change 20 ppm and annualized change 2 ppm/year; the last must be tied. A nine-interval result of 18 is wrong.

## M02 — three CO2 paths (R02–R04)

All retain required 2050/2100/685 outputs, regardless of selection. None is a calibrated carbon-cycle model.

**D, ten-year drift baseline.** At origin o, `s_o=(C_o-C_(o-10))/10` and `C_hat_D(t|o)=C_o+s_o*(t-o)`. It extrapolates recent average absolute growth, anchored to the latest level. Require eleven consecutive annual observations. This is a forecasting baseline, not an all-history fitted explanation; historical display shows its window/anchor separately. Nonpositive slopes are reported, not changed.

**Q, quadratic path.** Fit `C_t=a+b*x_t+c*x_t^2+e_t` by minimizing sum(e_t^2) over training years 1959 through o. Forecast by the same polynomial. Marginal annual growth is `(b+2*c*x_t)/10`; this tests constant absolute acceleration, with c=0 a linear trend. Do not constrain c to manufacture acceleration. Flag decreasing future segments, turning points and nonpositive values. A nonpositive path cannot feed a logarithm; never clip it.

**E, exponential path.** Let `C_ref=C_1959`, available to every fold. Fit `log(C_t/C_ref)=a+b*x_t+u_t` by OLS. Forecast `C_hat_E(t|o)=C_ref*exp(a+b*x_t)`. This tests constant proportional growth. Fit loss is in log units; comparison is in common ppm units. No lognormal distribution or smearing correction is assumed: this is a central fitted path, not an identified conditional arithmetic mean. Flag overflow.

Record origin, training range/n, parameters, residuals, future predictions and status. Every final refit produces 2050/2100 ppm, signed `C_hat(2050)-685`, relative gap `100*(C_hat(2050)-685)/685` percent, first crossing and path flags. “Reaches by 2050” means first passage, not just an endpoint check for nonmonotone paths. No invented near-agreement tolerance is allowed. The pure-CO2 exercise differs from OECD's CO2-equivalent scenario.

A development-fold failure makes a candidate ineligible; retain failed rows/statuses rather than dropping its worst fold. Still report whether its all-data fit permits the required scenario calculation. If all fail, return `NO_ELIGIBLE_MODEL`.

## M03 — development, final assessment, final refit

Development observations stop in 2011. Fixed rolling origins: 1981, 1986, 1991, 1996, 2001; forecast h=1,...,10 from each, giving 50 origin-target pairs with last target 2011. Training starts in 1959 except D's endpoint rule. Overlapping targets are intentional, not 50 independent replications.

Compute MAE=mean(abs(pred-obs)), RMSE=sqrt(mean((pred-obs)^2)), bias=mean(pred-obs), and MAE by origin/horizon. Select CO2 by minimum development MAE in ppm. Ties within numerical 1e-12 use fixed order D,E,Q. This tolerance is not practical equivalence; near ties require cautious interpretation. Secondary scores explain tradeoffs without changing the rule.

Before final assessment, persist a selection receipt with data/spec/config hashes, eligible IDs, development scores and selected CO2/temperature rules. The official full table was read, so final years were not concealed from readers; “untouched” means excluded from computational fitting, selection and tuning before freeze, not a blinded experiment.

Final holdout: fit at origin 2011 and predict all ten years 2012–2021 without intermediate refitting. Score frozen choices and declared comparators on identical targets. No training/normalizing on those targets. A reversal narrows conclusions; never change the primary rule or pretend a consumed holdout is fresh. Post-holdout redesign requires new evidence and a new decision.

Only afterward refit unchanged forms/rules through 2021 for production forecasts. This is distinct from evaluation. Produce annual paths through 2100, with a separate crossing-search horizon. Agreement with 2050 claims is never a selection criterion.

## M04 — association and shared trends (R06)

Using paired 1959–2021 observations, let z_t=log(C_t/C_ref). Report n and Pearson correlations (C,T) and (z,T); zero variance returns `UNDEFINED_CORRELATION`. Fit `T_t=alpha+beta*z_t+epsilon_t` by OLS, with coefficients and descriptive R-squared. Beta is degrees C per log-concentration unit. `beta*log(2)` is a fitted doubling contrast, not identified equilibrium climate sensitivity.

Regress z and T separately on [1,x], correlate residuals, then repeat with [1,x,x^2] as trend-form sensitivity. Where variance permits, report residual-regression slope. For 1960–2021 also compute dz=z_t-z_(t-1), dT=T_t-T_(t-1), their correlation and OLS `dT=kappa+lambda*dz+v`. These are diagnostics, not additional forecast candidates.

Strong level association, weak change association or detrending sensitivity can coexist. Differencing removes low-frequency information and magnifies relative noise. These diagnostics alone do not prove/disprove a physical greenhouse mechanism or identify its magnitude. Omitted variables, response lags and serial dependence remain. No naive independent-observation p-values, causal percentages or Granger claims.

## M05 — temperature forecast comparison (R05, R07)

**T0 time baseline:** fit `T_t=alpha0+delta*x_t+epsilon_t` to paired years <=o, then predict future x. This tests whether CO2 linkage adds predictive value beyond time.

**T1 linked path:** fit M04's log-CO2 association on observed paired training years <=o. Forecast `T_hat_1(t|o)=alpha+beta*log(C_hat_m(t|o)/C_ref)`, with fixed CO2 candidate m fitted using only years <=o. Never use realized future CO2 in a forecast score.

During development retain T1 paths for D/Q/E. After development CO2 selection, compare T0 with T1 driven by that selected rule; choose minimum development temperature MAE in degrees C, ties within 1e-12 to T0. Freeze both choices before final assessment. Reusing development folds is model development; final holdout supplies the separate assessment.

Invalid CO2 makes its T1 pipeline fail visibly; never rescue it with future observed CO2. T0 stays eligible. For 2a report selected-rule threshold years and alternate as sensitivity. For 2c extend T1 under every CO2 candidate even if T0 wins 2a. This is sequential association projection with no feedback. CO2 forecast uncertainty enters through path sensitivity and end-to-end backtest errors.

## M06 — threshold semantics

For production origin 2021, primary output is the first integer t in [2022,2300] with f(t)>=H: H=685 ppm or 1.25,1.50,2.00 degrees C. Scan increasing years. Require finite positive CO2 at each T1 evaluation. If the fitted origin already reaches H, return `AT_OR_BEFORE_ORIGIN`, not a fictitious future first passage. Check observed historical exceedance separately if relevant.

If none is found, return `NO_CROSSING_THROUGH_2300`, not “never.” Analytic limits for D/E/T0 and roots for Q may supplement this with an eventual mathematical crossing outside the domain. For positive beta in T1 the equivalent CO2 threshold is `C_ref*exp((H-alpha)/beta)`; guard overflow and nonpositive beta. The bounded primary calculation never silently extends to enormous years.

Use numerical tolerance 1e-9 near equality and preserve raw values. Check f(year)>=H and, for a monotone ordinary crossing, f(year-1)<H. Flag nonmonotonicity and possible recrossing. Every date beyond 2031 exceeds the maximum ten-year tested horizon from 2021 and is conditional long extrapolation. These are annual central-path dates, not realized weather exceedances, persistent warming dates or probability quantiles.

Toy f(t)=300+2(t-2000), H=305: continuous crossing 2002.5, first annual 2003. Toy T(t)=0.02*(t-2000), H=0.05 also first crosses in 2003. Constant subthreshold and already-above-origin cases must return distinct correct statuses.

## M07 — uncertainty and supported horizon

1. Retain five development errors for selected CO2/temperature pipelines at each h=1,...,10. Define `B_h=max(abs(error_o,j) for all development origins o and j<=h)`. This nondecreasing historical maximum-error envelope is not a confidence interval. Assess final holdout containment using prediction +/- B_h; report misses without adjusting B. Show a production envelope only through 2031, explicitly without guaranteed probability or future coverage. Temperature errors include forecast CO2 inputs.
2. Show D/Q/E concentration spread and T0 plus T1-D/Q/E at 2050/2100 and crossing dates. This is structural sensitivity, not a probability distribution or guaranteed bound.
3. Refit selected forms on 1992–2021 (last 30 observations) instead of 1959–2021. For T1 both coefficients and its CO2 producer use that window; D retains its ten-year rule. Report 2050/2100 and crossing changes. This predeclared sensitivity cannot select a replacement winner.

Report h=1,5,10 development MAE, origin count, final absolute error and corresponding future year 2021+h. Poor final scores or baseline losses must be explicit. Favorable backtests give only limited conditional evidence within tested horizons, not accuracy 79 years ahead. No universal reliability date or distant threshold probability is identified. Changes in emissions, sinks, omitted forcings, variability and response delays can break continuation assumptions.

## Budget and stopping conditions

Small deterministic regressions and scans of fewer than 300 annual years per path suffice. Record software/environment. Missing rows, incompatible units, rank deficiency, nonfinite outputs, invalid logarithms or failed toy checks block dependent claims with explicit statuses. Changed specifications require new revisions and affected reruns. Modeler toy checks are self-checks, not independent review or computation implementation validation.
