# Full review: 2005 MCM B, Team 770 — The Booth Tolls for Thee

- Source ID: `mcm_de487ee6fa90`
- Source: `MCM-ICM-master/2005美赛特等奖/B-770-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–50, including references, all code appendices and the final data table.
- Visual supplement: all figure-bearing pages (12, 16, 18–19, 23–24, 27–28, 31–32, 36, 38); the periodicity equation on p.8; appendix code on pp.45–46, 48–49.
- Numeric reproduction: **NOT_REPRODUCED**. No supplied MATLAB code was executed and no simulation was rerun. Static checks below are not a reproduction.
- Award provenance: Outstanding filename; the cover also labels the manuscript a 2005 Outstanding/MAA Prize paper. These are source claims, not independently verified award records.
- Prompt qualification: the authors' restatement on pp.2–3 was read. No independent original prompt was reviewed for this record.

## Problem structure and strongest reusable architecture

The decision is an integer number of staffed tollbooths given the entering and exiting highway lanes. Too few booths create upstream queues; too many can create downstream merging delays and incur operating cost. The strongest architecture is **shared demand and objective → simple microscopic benchmark → aggregate economic model → spatial microscopic alternative → comparison and implementable rule** (pp.3–7, 9–39).

The paper gives each representation a role instead of treating three model names as three solutions. The basic queue supplies insight and outflow data; the aggregate model turns waiting into a cost objective; the cellular automaton represents geometrical merging that the simpler models omit. Its best transferable lesson is to choose the level of description according to the unresolved mechanism and show the interfaces between levels.

## Architecture and cross-module links

1. Requirements and objective: reduce customer delay, remain implementable, work over different demand levels, and avoid decreasing recommended booth counts as lane counts rise (p.4). Daily social cost combines occupants' time cost with booth operating cost: `C(B) = alpha * gamma * N * W(B) + Q * B` (pp.5–7).
2. Shared input: 24 hourly traffic observations from a cited toll-road study are converted to a continuous demand curve. A Fourier representation is preferred over a quartic because the intended input is periodic and needed at finer time intervals (pp.7–9, 41–42).
3. Model 1: individual arrivals select the first available booth; service times are exponential with a stated mean of 12 seconds. Downstream merging is omitted. A maximum-wait improvement threshold is used to select a diminishing-return cutoff (pp.9–13; code pp.42–44).
4. Model 2: upstream wait, service time and downstream wait are decomposed. Model 1's averaged outflow supplies a fitted surface in time and booth count; a bottleneck threshold and fitted quartic cost components produce an approximate continuous optimum, then an integer recommendation (pp.14–20; outflow table p.50).
5. Model 3: a cell grid represents cars, empty space and prohibited positions. Forward movement, queue service, lane changes, entry and exit rules generate total time in the plaza. Geometry and update order are explicit components (pp.21–29; code pp.44–49).
6. Comparative experiments: simulate daily and rush-hour demand, vary movement probabilities and booth service delay, count vehicles entering and leaving, and compare booth recommendations across representations (pp.30–36).
7. Communication: summarize the recommendations as a simple integer-valued linear rule and discuss when a one-booth-per-lane design could be adequate; mixed electronic/cash booths remain a proposed extension (pp.36–40).

The first two models are directly dependent: simulation output from Model 1 becomes Model 2 input. The cellular model uses a different representation but shares demand and cost assumptions. Agreement is therefore a useful cross-representation check, with dependencies that must accompany any validation claim.

## Approach and justification

**Author reports:** a conventional multi-server queue initially seemed attractive, but did not represent multi-lane bottlenecks adequately (pp.3–4). A time-only objective was rejected because it could recommend impractically many expensive booths. Monetizing waiting makes user and operator costs comparable, using published time-value and annual operating-cost estimates (pp.5–7). The macroscopic model is computationally convenient; the cellular model is introduced because discrete positions, merging and driver reactions could change conclusions (pp.14, 21–22).

**Reviewer interpretation:** these are task-based justifications: objective mismatch motivates the cost model; unresolved merging motivates spatial simulation; periodicity motivates a particular demand representation. The paper also communicates the price paid by each abstraction, including identical drivers, identical booths, no downstream blockage of booth exits, constant booth availability and demand independent of the toll configuration (pp.4–5).

Important boundary: the cost excludes construction and toll payments (p.6), despite construction feasibility motivating the broader discussion. This is an operating-cost analysis under fixed demand, not a full capital-investment or demand-response analysis. The adopted value of time is a normative/economic input requiring sensitivity, not a universal physical constant.

## Validation design and author-reported findings

- Repeated runs: the basic model averages 20–30 trials, and the cellular model uses approximately 20 trials per configuration (pp.11–13, 30).
- Structural expectations: increasing booth capacity should reduce pre-booth waiting with diminishing gains; lane count should not decrease the recommended booth count (pp.10, 13, 20).
- Parameter sensitivity: for six lanes, changing movement probabilities leaves the cellular recommendation at ten booths; increasing service delay by 25% changes it to eleven (pp.33–34).
- Stress scenario: daily and rush-hour simulations are compared (pp.30, 34). Table 6 includes a two-booth difference at 16 lanes, although p.34 says the difference never exceeds one.
- Conservation: the authors report matching entry and exit vehicle counts after allowing all vehicles to traverse the plaza (p.34). This is a strong simulator invariant, though it alone cannot verify the behavioral rules.
- Model comparison: macro and cellular recommendations are usually equal or one booth apart; a common recommendation table and simple deployment rule close the report (pp.35–39).

No independent observed queue, travel-time or design-outcome dataset is used to validate the recommendations. Regression fit, stability and inter-model agreement are distinct evidence types; none by itself establishes real-world accuracy. The text's suggestion that precision nearly implies accuracy (p.35) should not be adopted as a workflow rule. Agreement could follow from shared demand, cost or implementation assumptions.

## Static checks and limits to reuse

The following are specific inspection findings, not claims from a rerun:

1. **Queue discharge is absent from the printed aggregate formula.** On p.16 the inner integral accumulates only `max(inflow - capacity, 0)`. It can increase or stay constant but cannot reduce an existing queue once service exceeds arrivals. The analogous downstream expression has the same issue. A reusable fluid-queue model needs a nonnegative state with discharge, not a cumulative sum of positive excess alone. This matters even if a final booth recommendation looks plausible.
2. **The periodicity calculation needs repair.** Page 8 prints `omega = 2*pi/24 = 0.2513`; the displayed decimal does not equal the fraction. Appendix coefficients and code also use 0.2513 (pp.42–43, 49). Thus the numerical frequency does not enforce the claimed exact 24-hour period. Excellent fit to the 24 input values cannot settle this boundary-condition issue.
3. **An asserted upper bound is not a demonstrated theorem.** Model 1 uses a 12-second marginal improvement in maximum wait (pp.9–12); the other models minimize average time cost plus operating cost. Omitting merging can motivate an optimistic benchmark, but different objectives and thresholds do not by themselves prove an upper bound on the later optimizer. Preserve the useful benchmark role without treating the bound as certified.
4. **Round-and-compare should replace unexamined rounding.** Model 2 rounds a continuous optimum to an integer (pp.18–20). For a discrete design, compare adjacent feasible integer costs and boundaries directly rather than assuming rounding is always valid.
5. **Appendix and prose require reconciliation before reproduction.** The presented code uses movement probabilities 0.7 and 0.8, whereas the sensitivity baseline uses 0.9 and 0.95 (pp.33, 45, 48). The lane-change code draws its random values outside the vehicle loops and iterates columns in fixed order (p.48), whereas prose specifies randomized priority by row (p.26). The upstream loop spans the entire grid after the downstream loop (pp.45–46), which also warrants checking for unintended double updates. These are reproducibility audit targets; the code may be an intermediate configuration rather than the exact code that generated the tables.
6. **Cost and timing conventions vary by model.** Model 1 excludes service time from waiting (p.10), Model 2 includes it (p.15), and Model 3 counts time occupying the simulated plaza (p.29). These metrics need common definitions before cross-model numerical comparisons.

The conclusion's simple rule should therefore be learned as an example of translating analysis into an operational recommendation, not reused as a validated toll-plaza engineering law.

## Communication strengths and reusable operating rules

The repeating motivation–approach–assumptions–development–results–discussion structure makes each model's role inspectable. Geometry diagrams, the cellular flowchart, explicit tables and code/data appendices support tracing a recommendation back to a mechanism. The six-lane example is carried through all three representations, providing a shared comparison case.

1. Give every model a distinct purpose and name the unresolved mechanism that justifies it.
2. Draw module interfaces, including units and the source of every transferred quantity.
3. Establish a common objective and metric definitions before comparing model outputs.
4. Distinguish a heuristic benchmark, a proven bound, internal verification and empirical validation.
5. Use conservation and boundary conditions as implementation checks.
6. Repeat stochastic experiments and report uncertainty in decision differences, not only the modal optimum.
7. Audit code, prose, equations and tables as one reproducibility chain.
8. Check low, normal and peak workloads; compare neighboring feasible integer decisions.
9. Let a simple operating rule summarize a supported domain, while preserving its assumptions and uncertainty.

## Reading ledger

All physical pages 1–50 were read. Pages 1–8 establish context, objective and demand; 9–13 develop the basic simulation; 14–20 build the macro model; 21–29 specify the cellular model; 30–38 analyze results, sensitivity and special cases; 39–40 conclude and provide complete references; 41–42 give demand coefficients; 42–49 contain all code; 50 supplies the final outflow table. All figure-bearing pages and relevant ambiguous equations/code were inspected visually. The numerical conclusions remain author reports, and mathematical/code concerns are explicitly limited static findings.
