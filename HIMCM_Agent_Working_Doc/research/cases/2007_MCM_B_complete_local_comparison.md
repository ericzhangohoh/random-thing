# 2007 MCM B: complete local comparison of two boarding papers

## Scope and evidence

Both independently available 2007 B papers in the original collection were read completely: **80 physical pages** in total, with relevant formulas, diagrams, tables and figures visually inspected. Both filenames say Outstanding; awards were not independently verified. The separate official prompt has not been reviewed, so task coverage below is based on the authors' restatements. This is complete coverage of the local two-paper set, not all contest submissions. Numerical reproduction was not performed.

| Paper | Coverage | Architecture | Strongest transferable practice |
|---|---:|---|---|
| [Team 2053](../reviews/mcm_2007/mcm_009e1fc87d77.md) | 30 pages | Idealized and analytical mechanisms → configurable simulation → derived grouping → parameter sweeps → repeatability and aircraft transfer | Use simple models to decide what to simulate; keep a simpler strategy when the new design adds little |
| [Team 2056](../reviews/mcm_2007/mcm_e0dcf8bb60f2.md) | 50 pages | Prototype → finite-capacity processor simulation → preference module and genetic search → practical hybrid | Preserve physical and combinatorial invariants; test mechanism removal and explain an implementation tradeoff |

## A shared decision structure

The operational question is to choose a boarding rule that reduces completion time while remaining implementable for passengers and gate staff. The environment includes aircraft geometry, movement, baggage handling, seat access and passenger behavior. The decision is a call-off order, group assignment or seating policy. Performance depends on both the policy and the environment.

The two papers therefore support a common architecture:

`operational requirements → event/state model → exact policy definitions → common simulation evaluator → fair comparisons → practical recommendation`.

That architecture is more transferable than the rule “use an agent-based model for boarding.” The reason to simulate is that spatial blocking, parallel baggage handling and local interactions determine completion time. A simpler analytical model may still be enough to identify a bottleneck or derive a useful limit.

## Why apparently conflicting conclusions are informative

### Unassigned seats represent different behavior

Team 2053's unassigned passengers have equal seat preferences, walk backward until blocked, sit when blocked and move to the window. Their behavior actively avoids conflicts. That regime is the fastest in the paper's nominal experiments.

Team 2056's passengers prefer front rows and windows or aisles over middle seats. These choices can produce congestion near the front and later seat-access conflicts. Its preference model is slower than the paper's random assigned-seat baseline.

These are different interventions in different behavioral environments. The comparison does not show that one paper has empirically disproved the other. It shows that a policy label is insufficient. The working team must identify which behavior is observed, assumed, encouraged by instructions or imposed by the simulator, and test plausible alternatives before making a practical recommendation.

### The same method name can hide a different rule

Team 2053's pyramid pattern combines row position with window-to-aisle ordering. Team 2056's “reverse pyramid” alternates whole back and front rows toward the center. Its diagram confirms that distinction. Pooling their performance under one name would be misleading.

A policy specification should include a small seat chart and the exact ordering rule. The computation agent should generate the chart from the same rule used in simulation. The reviewer can then compare implemented behavior without relying on a familiar name.

### A physical constraint can reverse the recommendation

Team 2056 demonstrates that unlimited queues make back-to-front boarding look favorable by allowing waiting passengers to occupy no relevant aisle space. Restricting queues to physical capacity changes the ranking. This is a representation change, not a minor solver adjustment.

Team 2053 separately shows that slow external entry can eliminate differences between policies: passengers arrive too slowly for internal conflicts to dominate. Together these cases suggest a two-step question: **where is the bottleneck under the modeled conditions, and does the candidate decision affect that bottleneck?**

## Positive patterns to transfer

1. **Use a prototype as a checkable limit.** Both papers start simpler than their final simulator. Keep the prototype's assumptions and intended comparison explicit; a limit-case check is not an empirical benchmark.
2. **Explain model rejection.** Team 2053 rejects a queue formulation as the main representation because its capacity treatment is inadequate. The reason for rejection is useful even if its qualitative congestion intuition survives.
3. **Separate search from evaluation.** Team 2056's genetic algorithm proposes passenger permutations; the processor model evaluates them. This makes it possible to compare heuristic outputs with simple schemes under a shared environment.
4. **Preserve feasibility in the representation.** A permutation-aware crossover keeps every seat present once. Independently verify this invariant even when the operator is intended to preserve it.
5. **Allow the baseline to win.** Team 2053 finds its new Parabola method close to simpler outside-in. Team 2056's seeded search remains slightly slower than its simple window-to-aisle baseline. Innovation does not require recommending the most elaborate method.
6. **Discuss implementation explicitly.** Team 2056 considers families, staff training and communication. Such constraints may justify accepting a small modeled time penalty, but hypothesized benefits should be labeled and tested.

## Evidence limits that affect justification

The numerical results in both papers are conditional simulation outcomes. Neither supplied report includes executable code and complete run artifacts. Mechanism ablations, visually plausible patterns and agreement with intuition support internal understanding; they do not establish calibrated real-world performance.

The papers also illustrate distinct levels of certainty:

| Evidence | Defensible conclusion | Stronger claim requiring more |
|---|---|---|
| A constructed ideal schedule | This schedule behaves as derived under stated assumptions | No possible schedule is faster |
| A genetic search plateau | This run found no further improvement under its search process | A local or global optimum is certified |
| Observed time range across 500 trials | This was the range in these simulated trials | The schedule will always meet the deadline |
| Removing a modeled source of delay | This component explains part of the modeled difference | The corresponding real-world intervention has the same effect |
| Close baseline outputs from models | The implementations are mutually consistent in this case | Both predict unseen boarding behavior correctly |

The executive recommendation must also preserve exceptions. Team 2053's larger-aircraft examples do not retain its broad outside-in-over-back-to-front ordering. That is a reason to qualify the recommendation and investigate the regime, not omit the table's reversal.

## A prospective agent workflow for an interaction-and-queue problem

This is a project-designed procedure informed by the reviewed cases, not a reconstruction of an actual contest run.

1. **Coordinator and domain-data agent:** define completion time, individual waiting, implementation constraints, system boundary and observed operating conditions. Distinguish data from behavior assumptions.
2. **Modeler:** specify entities, spatial capacity, transitions, update order and time units. Identify a simple limit case and at least one consequential structural alternative.
3. **Computation agent:** implement a transparent baseline policy and generate a small trace. Check seat uniqueness, passenger conservation, capacity, no backward time and final termination.
4. **Independent reviewer:** inspect tiny counterexamples before large runs. A passenger must not move several rows in one step merely because of loop order; a blocked queue must consume space; an event probability must retain its meaning when the time step changes.
5. **Modeler and computation agent:** compare exact policy rules under common scenarios. Separate policy-design runs from final evaluation. Include arrival-limited and congestion-limited regimes plus plausible behavior alternatives.
6. **Independent reviewer:** check uncertainty, ranking reversals, baseline fairness and the evidential meaning of every performance claim. Distinguish simulation variation from uncertain assumptions.
7. **Writer-visuals agent:** show mechanism, common comparison and exception conditions. Present the recommended operational rule with sufficient detail for staff to implement it.
8. **Coordinator and human decision maker:** choose the practical tradeoff, record why a candidate was retained or rejected, and identify the minimum real-world observation needed before deployment.

The central lesson is conditional reasoning: a strategy is justified by its interaction with an explicit environment and decision criterion. The algorithm name alone supplies neither.
