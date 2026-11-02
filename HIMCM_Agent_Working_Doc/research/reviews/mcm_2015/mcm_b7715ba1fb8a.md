# Full review: 2015 Problem A, Team 32150 — How to Eradicate Ebola

- Source ID: `mcm_b7715ba1fb8a`
- Source: `MCM-ICM-master/2015美赛特等奖/A-32150-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, all 36 physical pages, including the public letter and references. Printed pp.1–34 correspond to physical pp.3–36.
- Visual supplement: physical pp.3, 7–11, 13–25, 27–31 and 33–34 inspected for equations, flow diagrams, fitted and scenario curves, clustering, coordinates, allocations and the public letter.
- Numeric reproduction: **NOT_REPRODUCED**. No epidemic fit, differential-equation solution, clustering or delivery calculation was rerun.
- Award provenance: the source filename labels this paper Outstanding; individual award attribution was not independently verified.
- Original problem: the complete 2015 A statement was read in the archived [official problems page](../../sources/2015_MCM_ICM_official_problems.html). It posits a hypothetical medicine; this review concerns historical modeling practice, not current clinical guidance.

## Architecture and useful reasoning

The paper starts with SEIR, adds hospital and corpse compartments plus contact tracing, fits cumulative case curves, translates the results into medicine demand, places six distribution centers using weighted fuzzy clustering, and discusses manufacturing, efficacy and other interventions. It finishes with control/eradication criteria, sensitivity analysis and a two-page public letter (physical pp.3–36).

The useful modeling argument is mechanistic: hospital exposure, burial-related transmission and tracing change the pathways by which infections occur, so a basic compartment model may omit decision-relevant mechanisms. Demand weights then connect the spread model to the location model. This is a stronger architectural rationale than adding model complexity merely to improve an in-sample curve.

The authors acknowledge local optima in clustering, parameter dependence and limited city-level validation. Those qualifications should survive into the final recommendation. The workflow should retain the linked architecture while testing every link separately.

## State accounting and the observation model

The initial equations and compartment diagram distinguish susceptible, exposed, infectious and recovered populations. The extended model adds hospitalized people and infectious corpses (pp.7–11). The paper's earlier clinical definition of suspected cases is not interchangeable with a model's susceptible population. An explicit observation equation is needed to relate reported confirmed/probable/suspected cumulative cases to latent model states.

In the printed tracing equations, additional negative flows leave E and I without appearing as inflows to another tracked state. With nonzero tracing, a conserved population requires an explicit quarantined/removed population or a stated accounting boundary. The published fitting captions use zero tracing, so the displayed fits do not validate the tracing mechanism.

Two printed transmission formulas use an exponential containing `1 − τ`, where the surrounding explanation describes decay with elapsed time (pp.8 and 13). The visual inspection confirms the numeral in the displayed formulas. This is a specification inconsistency requiring reconciliation with any executable implementation, not proof of how an unavailable implementation behaved. Derivative dots in the ODEs are visible in the original; their absence in extracted text is not an author error.

The reproduction-number section displays F and V as vectors while invoking a next-generation matrix and inverse (p.13). It does not provide the necessary Jacobians. The resulting formula adds hospital and corpse contributions without clearly accounting for the probability of reaching those compartments: setting hospital admission to zero should remove that route; setting all mortality probabilities to zero should remove corpse transmission. These limiting cases are more informative than accepting a named derivation as sufficient evidence.

## Fit quality versus predictive or intervention evidence

The simpler and extended models are compared visually with cumulative observations (pp.9–15). The later model contains more mechanisms and fitted quantities; closer agreement on the calibration series does not establish out-of-sample accuracy, identifiable parameters or causal intervention effects. No held-out forecasting exercise is documented. Cumulative series also share observations over time, so a smooth curve can conceal poor prediction of new cases.

The recovery-rate construction couples it to a transmission-decay parameter through an assumed multiplier (p.13). These are different mechanisms. Each relationship needs a unit definition, independent rationale and a sensitivity treatment, rather than borrowing credibility from the fitted aggregate curve.

## Demand must be defined before locating facilities

The demand expression combines cumulative cases with a short-horizon increment while describing daily unit doses (p.16). Cumulative cases can include recovered and deceased people; it is not automatically the current number requiring treatment. The accompanying demand curve rises and falls, and its caption and narrative use different daily/weekly descriptions (p.17). A decision model needs a precise mapping from incidence and active eligible patients to treatment courses, doses per course, treatment duration and deliveries per period.

Weighted fuzzy clustering is a plausible spatial baseline when demand points and a continuous distance objective are appropriate. The paper gives the objective, membership updates, weighted centers and an elbow-based choice of six clusters (pp.18–21). It also states that the method may find a local optimum.

The elbow is not a total operating-cost optimum. Continuous centers are not automatically feasible warehouses, and straight-line distances are not travel times on usable routes. Candidate sites, road access, storage, cold-chain requirements, route capacity and delivery deadlines are absent from the numerical location model. Hard allocation after fuzzy membership also needs a stated assignment or split-delivery rule.

The coordinate table labels one latitude with an east suffix (p.21, repeated p.34). This requires correction before routing. Allocation percentages total approximately 100% after rounding; that is a useful conservation check but does not establish that every center receives enough medicine on time.

## Manufacturing and interventions require operational interfaces

The paper maps a production shortfall to a larger hospital fatality probability and demonstrates a numerical example (p.22). This makes an assumed consequence of shortage explicit, but the functional relationship and efficacy dependence need independent support. It also treats the mean requirement of 106.2 unit doses per day as sufficient to meet patients' daily needs. Mean production can cover all periods only with an adequate inventory and timing argument; peaks, initial stock, lead times, expiry and dispatch intervals matter.

The efficacy, burial and tracing scenarios illustrate mechanisms that the baseline cannot explore (pp.23–25). However, recovery/burial rates and their reciprocal durations are inconsistently described or scaled relative to the fitted parameters. Rate-versus-duration errors can change results by orders of magnitude. Tracing curves are conditional on admission rates, an important interaction that a single one-at-a-time conclusion would miss.

The control table contains overlapping or reversed fatality ranges and a critical value outside its stated neighboring band (p.27). It cannot serve as an operational threshold table without reconciliation. These are audit findings about the published specification; no numerical reconstruction has established which values generated the figures.

## Outcome definitions and sensitivity limits

The control criterion is nonincreasing incidence, expressed through the second derivative of cumulative cases. That can indicate a turning point while substantial transmission continues. The eradication criterion is exactly zero derivative of cumulative cases (pp.26–29). A deterministic ODE can approach zero asymptotically; an operational endpoint needs a tolerance, a sustained time interval and treatment of remaining infectious reservoirs and importation. The reported earlier endpoint is conditional on that model and its unstated numerical stopping rule.

The incubation figure labels rates as reciprocals of 5, 9 and 15 days, while the prose sometimes treats the rate itself as the duration (p.30). The plotted trajectories differ substantially even though the narrative calls their trends similar. Sensitivity should be measured on the decision output, not only whether curves have a similar shape.

Gaussian perturbations to a fatality probability require a bounded distribution or a documented transformation. The two noise displays do not specify enough replications, temporal dependence or uncertainty summaries to establish robust decisions (pp.30–31). Small changes in a chosen cumulative-curve display cannot establish that manufacturing or efficacy is unimportant in general.

## Communication and transferable rules

The public letter is concrete: it includes a map, coordinates, allocation shares, production guidance and intervention priorities (pp.33–34). That is a useful translation from mathematics to action. Its assurance that mean production meets daily need and its strong characterization of the fitted model exceed the evidence supplied. A nontechnical letter still needs conditional language and the dominant feasibility limitations.

1. Justify an added state by the mechanism and decision it changes.
2. Require a conservation equation and an observation equation for compartment models.
3. Test zero-flow and zero-probability limits before trusting a threshold formula.
4. Separate fitted cumulative cases, forecast incidence, eligible patients, treatment courses and shipment quantities.
5. Propagate demand uncertainty into location, inventory and service-level decisions.
6. Treat geometric clustering as a baseline unless site and route constraints are represented.
7. Distinguish average capacity from period-by-period feasibility.
8. Define rate units, reciprocal durations, operational endpoints and admissible parameter ranges.
9. Compare policies under the same horizon, initial state, demand scenario and accounting rules.
10. Carry the largest limitations into the decision letter instead of leaving them in an appendix.

## Reading ledger

- Physical pp.1–8: summary, full contents, interpretation, assumptions, notation and baseline mechanism read in full.
- Physical pp.9–16: all fitting discussion, extended equations, reproduction-number argument and demand definition read in full.
- Physical pp.17–24: demand curve, clustering, facilities, allocations, manufacturing and pharmaceutical/nonpharmaceutical effects read in full.
- Physical pp.25–30: tracing interactions, control/eradication definitions, all threshold tables and sensitivity discussion read in full.
- Physical pp.31–36: perturbations, strengths/weaknesses, complete public letter and all references read in full.
- Relevant original visual and mathematical content inspected; no numerical reproduction performed.
