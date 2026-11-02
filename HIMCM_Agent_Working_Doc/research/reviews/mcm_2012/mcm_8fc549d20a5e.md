# MCM 2012 B — Team 13074 — scheduling by degrees of managerial control

- Source ID: `mcm_8fc549d20a5e`
- Source: `MCM-ICM-master/2012美赛特等奖/B-13074-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–22, including all schedules, sensitivity tables, references and the two-page manager letter. Headers say “of20” even on the final two pages; the physical file has 22 pages.
- Visual supplement: physical pp.4–18 inspected, including every schedule diagram, route table, dynamic-programming equation, calendar and reported experiment table.
- Numeric reproduction: **NOT_REPRODUCED**. No schedule generator, probability model or optimization was rerun. One explicitly bounded route-distance calculation is reported below.
- Award provenance: Outstanding filename label, not independently verified; page headers identify Team 13074.
- Source limitation: no separate original problem statement was available in the corpus inventory; problem requirements here come from the submission's restatement. No executable code or computational appendix is supplied.

## Architecture: expose the choice of control policy before choosing an algorithm

The paper distinguishes three policies for a 225-mile river with uniformly spaced campsites and trips of different durations and propulsion types: managers fix dates, types and routes; managers fix dates and types but permit route choice; or managers fix dates while allowing type and route choice (pp.1–3). This is its strongest contribution. A scheduling problem changes when managers control different decisions, so the control regime should be explicit before capacity is reported.

For fixed routes, the authors partition campsites into disjoint sets called orbits and construct recurring schedules within them. With fewer campsites, several trip types share an orbit. For flexible routes, they count feasible paths, estimate campsite-day occupancy probabilities and greedily insert trips while limiting a collision-risk measure. The final variant randomly selects among currently admissible trip types. All three models have operational outputs: actual itineraries or departure calendars, rather than an objective value alone.

The manager letter explains the intended tradeoff between capacity and tourist freedom. The flexible models can also incorporate previously booked trips by initializing the occupancy calculation with those trips (pp.15–16). This is a useful extension because a real scheduler usually modifies an existing plan rather than solving an empty season.

## Fixed-route construction: decomposition is useful, but utilization is not the same objective

Disjoint campsite sets eliminate cross-set overnight collisions by construction. Within a set, a leading trip and following departures create a repeated pattern that tries to fill almost every campsite-day after the initial transient (pp.4–10). The authors also relate the allocation of campsites to desired proportions of trip types, recognizing that a schedule must serve a mix of demand.

The important qualification is that maximizing campsite-day occupancy is not generally equivalent to maximizing the number of trips when durations differ. A long trip consumes more campsite-nights. A saturation argument can support a resource bound once the mix and night counts are fixed; it does not prove global optimality over unrestricted trip mixes. Partitioning into orbits is itself a restriction that may sacrifice capacity. The paper does not compare its construction with an unrestricted optimum or provide an optimality gap.

Several feasibility conventions are inconsistent. The paper initially excludes a seven-day oar trip because its average daily rowing requirement exceeds eight hours, then allows it as a small exception in the fixed-route model; the stochastic models exclude it (pp.4, 12, 16). The alternatives therefore do not differ only in tourist freedom. Days and nights also alternate in the explanation: the explicit seven-day route contains six intermediate camps, while a resource formula divides campsite-days by full trip duration. Launch and exit days must be defined consistently.

**Bounded calculation performed in this review:** the explicit seven-day oar itinerary on p.9 ends its campsite sequence at 126. With 150 equally spaced camps between endpoints 0 and 151, its last leg is `225 × (151−126)/151 = 37.2517 miles`, requiring `9.3129 hours` at four miles per hour. That exceeds the stated eight-hour daily limit by substantially more than the average-time rounding exception. This is one route-leg check, not a complete audit of all itineraries. It demonstrates why every route must be checked leg by leg, including launch and exit, rather than only by average trip speed.

The reported fixed-route capacity is 2,340 departures over 180 days. The schedule repeats a two-day launch pattern through the season, but the treatment of trips finishing after day 180 is not specified. A finite-horizon model must say whether all departures or all completions must lie within the open season, and must account for start-up and end-of-season effects before calling the count a seasonal capacity.

## Flexible routes: a promising path-counting representation with unresolved probability details

The paper assumes equal probability for every feasible complete route of a given type. It recursively counts paths reaching campsite `x` after `t` days, then combines counts to obtain the probability of occupying a campsite-day (pp.11–12). This is a natural dynamic-programming representation on a downstream time-expanded network. It avoids explicitly listing a potentially enormous number of routes.

Uniform complete routes are a behavioral assumption, not an empirical fact and not equivalent to choosing each next campsite uniformly. The paper acknowledges this limitation and suggests surveys to estimate more realistic choices. A reusable implementation should support weighted transitions or path preferences while preserving the condition of reaching the exit at the specified duration.

The printed probability formula multiplies a forward count by a reflected-location count whose time argument is the full duration, rather than the remaining duration (p.12). A valid bridge calculation needs a backward count conditioned on the remaining steps, with endpoint and zero-route cases defined. The displayed recursion also states `x ≤ Y` while the denominator requires the exit `Y+1`. These are specification gaps to resolve before using the probabilities.

The collision quantity is the probability that at least two groups occupy a particular campsite on a particular date. The paper invokes a Jordan/inclusion–exclusion calculation but does not supply the implemented formula. Its displayed inclusion–exclusion identity even ends with a union where the final term requires an intersection (p.11). For verification, under explicitly independent group routes, the probability of at least two occupancies can be computed as one minus the probabilities of zero and exactly one occupancy. That small reference calculation would be a useful check against any general implementation; independence itself needs justification if tourists react to other groups.

## Risk is a policy parameter, not an event that becomes impossible

The authors treat a campsite-day collision probability below 0.05 as an event that does not happen in a stochastic sense. This does not provide the hard non-overlap guarantee stated in their own problem restatement. Nor does a five-percent bound at each campsite-day imply a five-percent probability of any collision during the season. Many opportunities for collision accumulate, and their dependencies matter.

A workflow should separate three possible requirements: deterministic exclusion of shared camps; a per-campsite-day chance constraint; or a season-level probability of any shared camp. They lead to different admissible schedules. A numerical threshold such as 0.05 is a manager's risk tolerance requiring justification, not a universal statistical rule permitting an event to be ignored. If the task requires deterministic separation, a chance-constrained alternative must be identified as a changed policy rather than an equivalent solution.

## Search quality and the evidence actually supplied

The greedy algorithm chooses the next trip type that minimizes the maximum local collision probability, keeps adding trips until the threshold is exceeded, and then moves to the next departure date. It is understandable and produces a concrete calendar (pp.12–15). However, minimizing the immediate worst probability does not prove that the largest eventual number of trips is achieved. Early choices can block later opportunities. Multiple starts, local replacement moves and exact optimization on small instances would distinguish a useful heuristic from a certified optimum.

The randomized variant reports eight capacities between 474 and 493, with strongly uneven trip-type frequencies (p.17). The paper acknowledges that this mix may not reflect tourist demand. Selection uniformly among the currently admissible types does not mean the realized seasonal mix is uniform, because admissibility changes over time. A demand constraint or explicitly valued mix is needed if serving diverse preferences is part of the objective.

The sensitivity tables explore the initial trip type, daily travel hours and the risk threshold (p.18). This is good experimental coverage of three different uncertainty sources: search initialization, physical capacity and policy tolerance. Yet the interpretation must follow the actual results:

- Different first types yield 473–500 trips, which demonstrates heuristic dependence on initialization rather than proof that any start is optimal.
- The eight-hour case is reported as 560 in the daily-hours table but 500 for the same stated first type in the other tables. The discrepancy must be reconciled before interpreting sensitivity.
- The hours table is nonmonotonic. More travel time changes the assumed distribution over feasible routes as well as the physical feasible set, so monotonic optimal capacity cannot be asserted without specifying which object is held fixed. Heuristic choices can also affect the result.
- Tightening the local risk threshold from 0.05 to 0.01 reduces the reported capacity from 500 to 215. This is a material policy tradeoff, and the paper appropriately notes that it cannot be ignored.
- The conclusion selects 493 for the random policy, which is the largest observed value among eight runs rather than a certified maximum or a typical-run estimate.

No independent simulation of realized route collisions, no uncertainty interval for seasonal risk and no computational code is supplied. The paper's experiments support comparisons within its specified model only after the formula and table inconsistencies are resolved.

## Transferable workflow rules

1. Specify what the decision-maker controls before choosing the model class.
2. Distinguish trip throughput, campsite occupancy, tourist freedom and demanded trip mix as separate objectives or constraints.
3. Use disjoint-resource decomposition as a constructive baseline, while retaining the restriction it imposes.
4. Verify every scheduled transition, including entry and exit, and define days versus nights and season boundaries.
5. Condition path probabilities on successful completion within the allotted time.
6. Define risk at the same level as the operational promise; a local chance constraint is not a seasonal guarantee.
7. Label greedy and randomized schedules as heuristic results unless optimality is established.
8. Present capacity together with the policy threshold and demand assumptions that produced it.
9. Compare numeric tables and the final letter against one saved experiment record.

## Reading ledger

All 22 physical pages were read, including every row of the route and departure tables, the sensitivity results and the complete manager letter. Visual inspection confirmed schedule boundaries, the missing remaining-time argument, the probability identity and the conflicting eight-hour capacities. Only the explicitly stated final-leg arithmetic was executed; the numerical models remain unreproduced.
