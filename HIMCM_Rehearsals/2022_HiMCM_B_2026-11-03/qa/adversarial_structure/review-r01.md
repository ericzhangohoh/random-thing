# A02 adversarial structure review r01

**Verdict: ACCEPTED_FOR_SCOPE.** Scope is the pinned r01 model architecture and interpretation, challenged with independent development-only alternatives. This is not acceptance of implementation, numerical production forecasts, final holdout performance, article or PDF. No consequential model defect was established by these attacks. Preserve the narrowing conditions below in the final claims.

## Version and evidence

`target-hashes-r01.json` pins the workbook, original PDF and six model documents. Complete official four-page statement was freshly extracted with `pdftotext -layout` to `official-statement-r01.txt` and read, including both tables. Read intake/state/task, T02 handoff, source-register/data-quality/dictionary r01 and source evidence listed below. Prior review decisions were not used as correctness evidence. The first extraction attempt failed because fitz is absent; no install occurred, and pdftotext succeeded.

`probe-plan-r01.md` was saved before empirical calculations. Independent `probe-r01.py` reads original XLSX with openpyxl and fits NumPy least squares, without importing project modeling code. `probe-results-r01.json` retains all 450 development predictions/errors and metrics. Exact command: `/Users/ericzhang/.venvs/default/bin/python3 qa/adversarial_structure/probe-r01.py`. No final-2012–2021 alternative scoring or model selection occurred. The entire official table was visible, so human exposure is not concealed; computational final holdout remains unconsumed by this reviewer. No main full-model result run was available in inspected run inventory. This report does not certify source web retrieval independently; it checks the actual retained original NOAA data/text and labeled OECD excerpt evidence.

## Attack 1 — Missing simple temperature comparator

Target: M05/D05 wording that comparison with T0 tests predictive value “beyond time”; possible unfair advantage of a nonlinear proxy over a rigid time baseline. Strongest defense: T0 is explicitly a baseline, T1 is not causal, and model selection is bounded to declared candidates. Discriminator: predeclared same-origin quadratic-time OLS plus fixed last-20-year linear time OLS, with no window search, using development targets only.

Evidence (MAE °C): T0 0.1000108243; T1-D 0.0872137195; T1-Q 0.0836869121; T1-E 0.0956337310; quadratic time 0.1609087523; recent-20 linear time 0.0959001504. D wins CO2 development (1.48122 ppm versus Q 1.75903, E 3.78876), so T1-D is the specified eligible linked comparison. Neither omitted time alternative overturns T1-D. Quadratic time is much worse on early origins and better on the last two; recent20 is better on three origins but worse overall.

Outcome: attack does not establish a repair-worthy alternative winner. Severity: advisory wording limit. Affects R05–R07. Minimal safeguard: say “outperforms the specified full-history linear-time baseline on development MAE,” not “CO2 uniquely adds predictive information beyond time.” Do not promote my exploratory comparators into a retrospectively predeclared primary experiment. Recheck: final prose must retain comparator, metric and sample restrictions; no claims of universal optimality or causal attribution.

## Attack 2 — Shared trend masquerading as explanatory relationship

Target: high level correlation could be read as evidence that fitted beta measures the CO2 effect. Strongest defense: M04 explicitly reports multiple detrending orders and differences and forbids causal/physical-sensitivity identification. Independent development-through-2011 evidence: corr(logCO2,T)=0.936123; linear-detrended=0.488295; quadratic-detrended=0.503431; first-difference=0.364474. Trend removal materially weakens but does not eliminate association; it does not prove an absence of physical effects.

An exact structural counterexample strengthens the interpretation guard: if C_hat_E=Cref exp(a+b x), T1-E=alpha+beta a+beta b x, exactly a straight line in time. Calling this path a mechanically distinct causal temperature forecast would be incorrect even if its fitted line differs from T0. Outcome: existing noncausal language defeats the attack. Severity: accepted limitation, not defect. Affects R06/R07. Minimal repair: none to equations; keep beta/log(2) contrast explicitly descriptive and discuss shared trend. Recheck actual final relationship conclusions and labels.

## Attack 3 — Why D/Q/E; long extrapolation unconstrained by ten-year accuracy

Target: a winner at h<=10 could be promoted to accurate 2050/2100 or reliable crossing dates. Strongest defense: model specification distinguishes constant absolute growth, constant acceleration and constant proportional growth and explicitly disclaims carbon-cycle mechanics, probability bounds and long-horizon validation.

Test: compare assumptions/algebra and official requirement. D is linear in future time; Q is quadratic; E is exponential. Long-run divergence follows even when near-term fits match, and no <=10-year scores discriminate actual 79-year policy/sink changes. The declared structural spread and last30 comparison expose, but cannot bound, this issue. A shifted exponential excess-CO2 model could be another scenario, but absent a concrete demonstrated failure it is not justified as mandatory merely because the statement mentions 280 ppm. Logistic capacity/physical models require unsupported inputs. Outcome: architecture has a defensible compact scenario set; not exhaustive. Severity: accepted consequential limitation. Affects R02–R04/R07. Minimal repair: none to candidate set; constrain “most accurate” to declared comparison and require all-model dates/spread. Recheck production table and conclusions before release.

## Attack 4 — Temperature threshold baseline and observable meaning

Target: threshold dates could be mistaken for absolute temperatures, pre-industrial/Paris thresholds, realized annual first excursions or persistent climate crossings. Strongest defense: official p4 supplies anomalies relative to 1951–1980 and M06 explicitly defines annual central-path crossing. Test: compare original p1 2a/p4 and M00/M06. Both units/baseline match. No reconstruction of the baseline mean is needed to forecast a supplied anomaly; the observation base period need not be fully present in this workbook. Historical supplied anomalies are all below 1.25°C; hence no earlier observed threshold defeats the requested future first crossing. Discrete integer evaluation, bounded non-crossing and beyond-2031 labels are explicit.

Outcome: attack rejected for r01 design; stochastic first-passage uncertainty is honestly outside identification. Severity: no defect. Affects R05/R07. Minimal repair: none; dates need immediate “central path, 1951–1980 baseline” labels. Recheck actual numerical crossing boundaries separately (not performed here).

## Attack 5 — Annual versus March claim and global-site mismatch

Target: an annual difference could falsely refute the March-specific assertion. Strongest defense: source quality and M01 explicitly limit the conclusion. Original p3 contains “Annual month of March” but cites `co2_annmean_mlo.txt`; retained NOAA annual/monthly files independently distinguish annual and monthly quantities. Therefore the internally contradictory official caption does not justify converting annual inputs into March observations. The 0.03-ppm annual maximum margin also should not become a large scientific effect.

Outcome: required annual exercise is honestly scoped; the March historical claim remains unverified, not disproved. Severity: accepted source limitation. Affects R01/R02. Minimal repair: none to data; final wording must state inability to verify actual March/all-earlier-history claim. Mauna Loa must remain named as a proxy rather than global spatial mean. Recheck summary/article for this distinction.

## Attack 6 — OECD and May-2022 claims

Target: 685-ppm pure CO2 forecasts could be falsely compared with OECD greenhouse-gas CO2-equivalent, or May421 assimilated as an annual point. Strongest defense: source quality and design explicitly preserve differing quantities and historical cutoff. Retained NOAA news text lines39–40 supports rounded May421 from 420.99/420.78 monthly Mauna Loa means. Retained OECD evidence is transparently a labeled excerpt/paraphrase, not original PDF; it identifies CO2-equivalent685 and CO2-only530/780 under a conditional baseline. I did not re-fetch OECD independently. The architecture retains the requested pure-CO2 threshold while forbidding an OECD falsification claim.

Outcome: no demonstrated structural defect. Severity: accepted provenance/interpretation limit. Affects R03/R08. Minimal safeguard: paper must explicitly address May421 as a source-backed monthly contextual observation; it has no separate framing-matrix row but source evidence is present. Recheck all three opening claims in final paper and source citations. Do not silently insert later annual observations or call scenario mismatch model validation.

## Attack 7 — Full question coverage and “how far reliable?”

Target: qualifications might replace answering the problem. Strongest defense: r01 has per-model2100/2050/685 values, selected threshold dates, linked extension even if T0 wins, and horizon evidence with an honest absence of a guaranteed reliability date. Original questions were compared individually against framing R01–R09 and M01–M07. They are covered at architecture level. A single deterministic reliability date cannot be scientifically deduced without an accuracy tolerance/loss criterion; giving h=1,5,10 error evidence and declining a guarantee is a substantive answer, not necessarily evasion.

Outcome: accepted planned coverage, actual completion pending. Severity: not a confirmed defect. Affects R01–R09. Recheck actual result tables, source corrections including May421, bounded practical recommendations without inferred policy effects, <=1-page article, summary/contents/references and <=25-page rendered PDF. No acceptance of those artifacts is implied here.

## Release conditions and independence

There is no mandatory structural rerun supported by this reviewer’s evidence. Existing candidate can continue. The strongest actionable narrowing is the “beyond time” wording: the result is relative to one stated baseline, and my limited alternative challenge does not establish unique CO2 information. If authors change candidate set using these exploratory results, record that as new development and preserve prior freeze/holdout history; no reset of scientific chronology. Numerical implementation, final holdout and release/PDF remain for their respective reviews.
