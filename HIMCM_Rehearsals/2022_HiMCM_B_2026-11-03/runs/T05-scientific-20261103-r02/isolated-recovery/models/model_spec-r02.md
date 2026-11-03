# Mathematical specification r02

T06; modeler; proposed interpretation/boundary repair of released r01. Original equations, candidates, splits and selector are unchanged. Independent adversarial A01 final scores have been consumed; this revision cannot reset that exposure. Constants are design choices, official thresholds or labeled toy inputs. Failures return explicit statuses.

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

Final holdout: fit at origin 2011 and predict all ten years 2012–2021 without intermediate refitting. Score frozen choices and declared comparators on identical targets. No training/normalizing on those targets. A reversal narrows conclusions; never change the primary rule or pretend a consumed holdout is fresh. Post-holdout redesign requires new evidence and a new decision. The final segment has already been evaluated by A01 before the primary execution receipt; the primary receipt certifies local execution order for unchanged predeclared rules, not project-wide unseen scores.

Only afterward refit unchanged forms/rules through 2021 for production forecasts. This is distinct from evaluation. Produce annual paths through 2100, with a separate crossing-search horizon. Agreement with 2050 claims is never a selection criterion.

## M04 — association and shared trends (R06)

Using paired 1959–2021 observations, let z_t=log(C_t/C_ref). Report n and Pearson correlations (C,T) and (z,T); zero variance returns `UNDEFINED_CORRELATION`. Fit `T_t=alpha+beta*z_t+epsilon_t` by OLS, with coefficients and descriptive R-squared. Beta is degrees C per log-concentration unit. `beta*log(2)` is a fitted doubling contrast, not identified equilibrium climate sensitivity.

Regress z and T separately on [1,x], correlate residuals, then repeat with [1,x,x^2] as trend-form sensitivity. Where variance permits, report residual-regression slope. For 1960–2021 also compute dz=z_t-z_(t-1), dT=T_t-T_(t-1), their correlation and OLS `dT=kappa+lambda*dz+v`. These are diagnostics, not additional forecast candidates.

Strong level association, weak change association or detrending sensitivity can coexist. Differencing removes low-frequency information and magnifies relative noise. These diagnostics alone do not prove/disprove a physical greenhouse mechanism or identify its magnitude. Omitted variables, response lags and serial dependence remain. No naive independent-observation p-values, causal percentages or Granger claims.

## M05 — temperature forecast comparison (R05, R07)

**T0 time baseline:** fit `T_t=alpha0+delta*x_t+epsilon_t` to paired years <=o, then predict future x. This compares predictive accuracy against this specified full-history linear-time baseline; it cannot identify unique predictive information from CO2 beyond every representation of time.

**T1 linked path:** fit M04's log-CO2 association on observed paired training years <=o. Forecast `T_hat_1(t|o)=alpha+beta*log(C_hat_m(t|o)/C_ref)`, with fixed CO2 candidate m fitted using only years <=o. Never use realized future CO2 in a forecast score.

During development retain T1 paths for D/Q/E. After development CO2 selection, compare T0 with T1 driven by that selected rule; choose minimum development temperature MAE in degrees C, ties within 1e-12 to T0. Freeze both choices before final assessment. Reusing development folds is model development; final holdout supplies the separate assessment.

Invalid CO2 makes its T1 pipeline fail visibly; never rescue it with future observed CO2. T0 stays eligible. For 2a report selected-rule threshold years and alternate as sensitivity. For 2c extend T1 under every CO2 candidate even if T0 wins 2a. This is sequential association projection with no feedback. CO2 forecast uncertainty enters through path sensitivity and end-to-end backtest errors.

## M06 — threshold semantics (r02 boundary clarification)

Origin is 2021, search end 2300. Thresholds are 685 ppm and 1.25, 1.50, 2.00 degrees C. Check integer annual values on the inclusive domain [origin,search_end]. A CO2 path requires finite positive concentration; a T1 path requires finite positive upstream CO2 and finite anomaly; T0 requires finite anomaly. Negative anomalies are valid. Missing/nonfinite values or evaluation errors are invalid, not zero. A path is valid for first-passage inference only on its contiguous valid prefix beginning at the origin; do not skip an invalid year and resume later.

Let k be the first invalid year in that inclusive domain, or null if all years are valid. Let v be k-1, or search_end if k is null; if the origin itself is invalid, the valid prefix is empty and valid_through_year is null. On that prefix define the first annual future crossing t* as the least integer t>origin with f(t)>=H, provided the origin is below H. Use tolerance 1e-9 only for floating equality; retain raw values. Invalidity takes precedence over an apparent threshold hit in the same year.

Apply these decisions in order: reject an invalid origin; classify a valid already-above origin; retain a crossing on the valid prefix; otherwise classify invalidity or fully valid bounded non-crossing. Primary status is exactly one of:

- `INVALID_PATH`: origin invalid, or a valid below-threshold origin is followed by invalidity before any valid future crossing. Set first_year=null even if a later re-entry would exceed H. The failure means a crossing over the declared path cannot be established; it is not a no-crossing claim.
- `AT_OR_BEFORE_ORIGIN`: valid origin already reaches H. Set first_year=null. Later invalidity is separately warned and does not invent a future first crossing.
- `CROSSED`: valid origin below H and t* exists within the contiguous valid prefix. Preserve first_year=t* even if a later year becomes invalid. The established annual event is not erased by later path failure; the path is nevertheless not valid over the full domain.
- `NO_CROSSING_THROUGH_2300`: every required value in the whole inclusive domain is valid and none reaches H after a below-threshold origin. This is not “never.”

Every row also reports `search_domain_valid` (boolean), `valid_through_year`, `invalid_from_year` (k or null), `invalid_reason` (null or explicit reason), and `monotone_flag` assessed only on the contiguous valid prefix, with `monotonicity_end_year`. If fewer than two valid prefix values exist, monotone_flag=null; otherwise it means nondecreasing within tolerance. Later invalidity never disappears merely because CROSSED is retained. Check the whole declared domain for the earliest invalid year; any resumed valid values remain excluded from crossing inference.

For ordinary crossing store f(t*) and f(t*-1) and verify the threshold boundary; first-passage search is in increasing annual order and handles nonmonotone paths/recrossing. A CROSSED row with later invalidity must be presented as “first annual crossing on valid prefix; path invalid from [year/reason],” not as a fully valid long-run forecast. The status establishes arithmetic only, not physical credibility. Display forecasts beyond invalidity remain invalid.

Analytic limits/roots may separately supplement bounded non-crossing with a later mathematical root; they do not override invalid-prefix status or silently extrapolate to enormous years. For T1 with positive beta the equivalent CO2 level is `C_ref*exp((H-alpha)/beta)`; guard overflow and nonpositive beta. Dates beyond 2031 exceed the maximum tested ten-year horizon from 2021 and are conditional extrapolations, not realized weather, persistent warming, Paris/pre-industrial dates or probability quantiles.

Required r02 synthetic tests: valid crossing then later nonpositive/nonfinite/missing value preserves CROSSED and warning; invalidity before crossing yields INVALID_PATH; apparent hit at invalid year fails; recovery after invalidity does not restore crossing; already-above valid origin followed by invalidity preserves AT_OR_BEFORE_ORIGIN plus warning; invalid origin fails; all-valid subthreshold gives bounded non-crossing; negative temperature anomaly is valid; exact/fractional threshold and nonmonotone first passage remain correct. These cases supplement original r01 toy tests and require independent implementation verification.

## M07 — uncertainty and supported horizon

1. Retain five development errors for selected CO2/temperature pipelines at each h=1,...,10. Define `B_h=max(abs(error_o,j) for all development origins o and j<=h)`. This nondecreasing historical maximum-error envelope is not a confidence interval. Assess final holdout containment using prediction +/- B_h; report misses without adjusting B. Show a production envelope only through 2031, explicitly without guaranteed probability or future coverage. Temperature errors include forecast CO2 inputs.
2. Show D/Q/E concentration spread and T0 plus T1-D/Q/E at 2050/2100 and crossing dates. This is structural sensitivity, not a probability distribution or guaranteed bound.
3. Refit selected forms on 1992–2021 (last 30 observations) instead of 1959–2021. For T1 both coefficients and its CO2 producer use that window; D retains its ten-year rule. Report 2050/2100 and crossing changes. This predeclared sensitivity cannot select a replacement winner.

Report h=1,5,10 development MAE, origin count, final absolute error and corresponding future year 2021+h. Poor final scores or baseline losses must be explicit. Favorable backtests give only limited conditional evidence within tested horizons, not accuracy 79 years ahead. No universal reliability date or distant threshold probability is identified. Changes in emissions, sinks, omitted forcings, variability and response delays can break continuation assumptions.

## Budget and stopping conditions

Small deterministic regressions and scans of fewer than 300 annual years per path suffice. Record software/environment. Missing rows, incompatible units, rank deficiency, nonfinite outputs, invalid logarithms or failed toy checks block dependent claims with explicit statuses. Changed specifications require new revisions and affected reruns. Modeler toy checks are self-checks, not independent review or computation implementation validation.

## M08 — claim and diagnostic safeguards introduced after A01/A02

The selected CO2 rule is the **prespecified pooled-development selection**, not automatically the most accurate model on every assessed sample. Report pooled development rank, per-origin winners, per-horizon errors and final-segment rank separately. If ranks reverse, the R04 answer must state the reversal and absence of a uniformly supported winner; future accuracy remains unknown. Report the selected sequential temperature pipeline relative to its eligible comparison (T0 versus T1 driven by selected CO2), not as the best of all declared T1 paths. Show all comparator scores.

From existing development error rows, additionally report leave-one-origin-out pooled CO2 winner and counts of per-origin wins. These summaries are post-A01 robustness diagnostics, not predeclared selection criteria, a new candidate search or permission to switch winners. Mark their introduction after assessment exposure. No p-values or independence claims follow from five overlapping origins.

Report every final historical-envelope miss as year/horizon, error, radius and exceedance. Literal containment counts describe the observed ten related checks only; do not infer coverage probabilities, call 2031 a validated reliability date or widen radii to absorb misses. Reconcile primary results with the independent adversarial evidence before release; disagreement triggers investigation, not copying either result automatically.

T1-E has the exact algebraic form alpha+beta*a+beta*b*x when E is C_ref*exp(a+b*x), so it is linear in future time even though calibrated in a different way. Neither beating T0 nor a high level correlation establishes unique CO2 information or causation. Preserve annual/March, CO2/CO2-equivalent, Mauna Loa/global and temperature-baseline restrictions beside substantive claims. No new physical model or causal method is introduced by these repairs.
