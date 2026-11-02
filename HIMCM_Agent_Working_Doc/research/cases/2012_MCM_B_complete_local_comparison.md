# MCM 2012 B — full comparison of the six locally available rafting papers

## Evidence boundary

All six local 2012 B papers were read completely: **146 physical pages**, including available code, memos, references and substantive visuals. “Complete” refers to this local set, not every submission to the contest. All six carry Outstanding filename labels; those award labels were not independently verified. No separately supplied official 2012 B statement was located in the corpus inventory, so requirement coverage is based on the submissions' restatements. Every model remains **NOT_REPRODUCED**.

| Team / source ID | Pages | Main architecture | Most useful lesson |
|---|---:|---|---|
| 13074 / `mcm_8fc549d20a5e` | 22 | Fixed route orbits; probabilistic flexible-route assignment; flexible vessel mix | Separate decisions management controls before choosing an optimization model. |
| 13955 / `mcm_a0e5e63c77e2` | 18 | Daily priority scheduler and demand-intensity experiments | Preserve the actual response table when it contradicts the preferred operating ratio. |
| 15171 / `mcm_ce2299363867` | 36 | Resource benchmark, agent simulation, itinerary construction and probabilistic encounter model | Agreement among models is only useful after comparing their assumptions and failure definitions. |
| 15417 / `mcm_df1dd905398a` | 26 | Priority allocation, displacement chains and offline repair; full Java appendix | Audit code against the stated policy and test discrete feasibility thresholds. |
| 15420 / `mcm_8b46b9801a80` | 21 | Priority, continuous density adjustment and zero-crossover sequence growth | Explain throughput together with the accepted duration mix, utilization and encounters. |
| 15878 / `mcm_825774eaa5d3` | 23 | Daily cellular state updates, conflict repair and component ablations | Use controlled experiments, then reconcile the admission and completion ledger. |

Detailed cards are in `research/reviews/mcm_2012/` under these source IDs. Page references below are physical PDF pages.

## What is the actual decision?

These papers do not solve one identical mathematical program. Some fix itineraries, others choose camps daily; some preserve requested vessel types, others assign them afterward; some allow timing deviations, others require a precise duration; some optimize a known season, others admit demand with limited advance knowledge. Their numerical capacities cannot be placed into a league table without normalizing these choices.

Team 13074 explicitly separates fixed route combinations, flexible routes and flexible boat mix. That decomposition is worth adopting before any method selection. The coordinator should state which quantities are inputs, controllable decisions, uncertain future events and outcomes. Otherwise a more flexible policy can appear superior merely because it solves an easier problem.

The core resource is a campsite on a particular night. Individual trips also impose first-leg, intermediate-leg and final-leg reachability constraints. Solitude adds a different kind of condition: two trips can occupy different camps every night and still encounter or overtake each other during the day. A complete representation therefore needs both trip-level trajectories and campsite-night occupancy, plus a precisely defined encounter metric if daytime experience matters.

## How to justify an approach from this evidence

**Begin with a transparent capacity benchmark.** A resource-days bound or a structured orbit schedule is useful because it identifies the bottleneck and provides an interpretable reference. It must use the same accepted duration mix and endpoint convention as the detailed model. Dividing all available campsite-nights by an assumed mean duration gives a conditional bound, not a globally valid optimum across all mixes. Team 15417 exposes this issue; Team 15878's initial `180 × camps` quantity has campsite-night units rather than trip units.

**Use a scheduling heuristic when the decision is a feasible collection of itineraries.** Priorities based on remaining distance divided by remaining days are common because they represent urgency. They are reasonable candidates, not universal laws. Tie-breaking, ordering, displacement and repair determine the actual policy. Team 15417's Java comparator favors motor boats in a tie, contrary to the slow-boat-first account in the prose. A method justification must reach the implementation, not stop at the written formula.

**Use agent or daily-state simulation when behavior or online adaptation is part of the question.** Team 15171 models travel and stopping behavior, whereas Team 15878 isolates daily movement and conflict-resolution components. These support different claims. A behavioral simulation estimates outcomes under assumed behavior; an offline schedule generator constructs a plan. Neither automatically proves that all future requests can be accepted online.

**Use probability to characterize residual risk only after defining the event and sampling process.** Team 13074's path-count probabilities depend on how routes are sampled. Uniform sampling of complete paths differs from choosing the next campsite uniformly. Team 15171's order-statistics approximations depend on spatial dependence and conditioning, and an exact-two-event probability differs from an at-least-two-event tail. The workflow should record the event, population, conditioning and joint assumptions before deriving a formula.

**Use multiple methods to expose tradeoffs or triangulate mechanisms.** Team 15420's comparison makes differences between maximum throughput and zero overtaking visible. Team 15171 supplies complementary perspectives, but common assumptions and different outcome definitions limit claims of independent validation. The purpose of a second model must be stated: a baseline, an ablation, a different policy, a structural check or an external prediction. Those functions are not interchangeable.

## Five recurring failure modes and their corresponding gates

### 1. A trip vanishes when the scheduler cannot place it

Several methods delete failed requests or previously scheduled trips. This is legitimate in an offline admission optimizer if the rejected customer has not departed. It is not an operational response to a party already on the river. Team 15878 explicitly counts rejection before and after loading, while its memo describes advance refusal. Team 15171's itinerary builder and Team 15417's offline repair similarly require clear planning horizons.

**Gate:** state the decision time, information available then, and consequence of failure. Save an admission ledger. Reconcile requests with completed, rejected, waiting and active trips. Report attempted demand separately from accepted output.

### 2. More trips are mistaken for a better schedule

Short trips consume fewer campsite-nights and have fewer opportunities for a placement failure. Team 15420 explicitly explains why a high-throughput sequence initialization serves a shorter accepted mix. Team 15171's removal procedure also changes the mix. A policy can improve count while excluding long trips or particular vessel types.

**Gate:** report requested and accepted duration-by-vessel distributions, group-specific rejection rates, occupied nights and mean duration alongside trip count. Compare policies on matched demand or explain the changed service objective.

### 3. A convenient feasibility check misses a boundary

Team 13074's displayed last oar leg exceeds the nominal eight-hour limit under the stated spacing. Team 15417's checker does not test the final leg or every state invariant. Discrete floors create abrupt reachability changes even when a parameter changes only slightly.

**Gate:** use a checker independent of the scheduler. Validate launch-to-first-camp, all intercamp legs and last-camp-to-exit; downstream motion; maximum travel; exact or allowed duration; one party per campsite-night; valid indices; and consistent identities. Include cases just above and below integer travel thresholds.

### 4. A numerical comparison is called an optimum

Insertion saturation does not establish optimality under replacement. A best random run does not establish a global maximum. A parameter-sweep boundary does not establish the best possible demand level. Team 15420 supplies clear initialization dependence; Team 15878's preferred policy trades off metrics; Team 13955's raw table contradicts a universal best vessel ratio.

**Gate:** label the result as a feasible construction, best tested configuration, local search result, analytical bound or proven optimum. Keep counterexamples in the recommendation. Compare small cases against exhaustive enumeration or an exact solver when optimization quality is a central claim.

### 5. A derived metric changes meaning between body and memo

Examples include per-camp-day risk versus season-wide risk; crossings inferred from overnight positions versus physical encounters; trips versus people; and off-schedule rates without lateness magnitude. Several papers report a highly favorable memo while the body contains important qualifications.

**Gate:** define each metric with numerator, denominator, unit, horizon and aggregation. Have the writer trace every recommendation back to a source result and its assumptions. Assumption-generated zeros should stay labeled as such.

## Strong experimental practices to carry forward

Team 15878 offers a useful component ablation: recalculate movement or not, allow conflict repair or not, and vary its direction. This reveals which mechanism affects capacity and which affects timing. However, an intentionally disabled component is a diagnostic control, not a competent competing optimization method.

Team 15420 presents a multi-outcome table and duration distributions, making a policy tradeoff understandable. Retain that structure and add matched input configurations, replication counts and uncertainty. Its continuous-density alternative also demonstrates why a two-object sign-and-units fixture should precede a large run: the printed update attracts a close pair although the intended effect is separation.

Team 15417 explains sharp numerical changes through integer reachability rather than dismissing them as noise. Sensitivity analysis should therefore include structural transitions and infeasible regions, not only smooth percentage perturbations.

Team 15878 deliberately breaks ideal assumptions with camp degradation and storms. This is valuable scenario design, but its uncalibrated degradation function and unshown storm outputs are not empirical validation. Preserve the distinction between stress tests, parameter uncertainty, implementation checks and comparison with observed data.

## Six-role work allocation for an analogous HiMCM task

| Runtime role | Concrete responsibility | Required handoff |
|---|---|---|
| `coordinator` | Freeze decision horizon, controllable variables, demand commitments, objective order and comparison protocol. | Decision contract, shared scenario table and claim limits. |
| `domain-data` | Establish travel assumptions, campsite geometry, demand distributions and meaning of encounter thresholds. | Unit-checked data table with source and uncertainty for each parameter. |
| `modeler` | Derive a resource bound, select a state representation and propose at least one feasible baseline plus the main policy. | Model specification, invariants, rationale and anticipated failure cases. |
| `computation` | Implement the specification, save input/seed/output records, run matched comparisons and ablations. | Reconstructable schedules, admission ledger, run manifest and outcome tables. |
| `independent-reviewer` | Check schedules independently, inspect code/prose agreement, test boundaries and audit inference strength. | Violations, counterexamples, unresolved assumptions and supported claim levels. |
| `writer-visuals` | Explain the decision tradeoff using trajectories, resource occupancy and demand-mix charts; align memo with evidence. | A source-traceable report whose recommendations retain material qualifications. |

These assignments are project coordination design informed by the cases; they are not official competition requirements. Likewise, the gates above are conditional modeling advice supported by observed strengths and failure modes. The selected papers do not reveal the causal reasons for their award outcomes.
