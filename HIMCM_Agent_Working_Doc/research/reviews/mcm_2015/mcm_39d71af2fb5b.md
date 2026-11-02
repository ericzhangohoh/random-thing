# Full review: 2015 Problem C, Team 35778 — Human Capital Dynamic Network Model of Team Science

- Source ID: `mcm_39d71af2fb5b`
- Source: `MCM-ICM-master/2015美赛特等奖/C-35778-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–22, including references. Printed pp.1–20 correspond to physical pp.3–22.
- Visual supplement: pp.6–8, 10–11 and 13–20 inspected for the organization, network representation, formulas, flowcharts, all experiment plots, multilayer example and sensitivity results.
- Numeric reproduction: **NOT_REPRODUCED**. All numerical findings below remain author reports unless explicitly labeled as a static interpretive check.
- Award provenance: explicit Outstanding filename label; not independently verified here.
- Original problem: the [official five-page statement](../../sources/2015_ICM_Problem_C.pdf) was read, including visual inspection of its organization and data table.

## Task interpretation and architecture

The paper connects human-capital management to an evolving organizational network. Its most useful modeling decision is to make the **position**, rather than the current employee, the persistent node. A Post Archives Matrix records job level, vacancy status, current occupant attributes, tenure, enthusiasm, costs and position-change history (pp.5–9). This separates a stable organizational structure from the changing people who occupy it.

The architecture is position/relationship representation → state table → monthly departure, promotion and recruitment algorithms → accounting and performance indicators → policy comparisons. The paper then builds a smaller multilayer illustration for one 14-person office (pp.18–19). It does not demonstrate that this smaller multilayer extension drives all earlier company-wide simulations.

The persistent-state design is transferable to machines and operators, facilities and tenants, or jobs and workers. It forces a question that a generic graph diagram can hide: which properties belong to a location and which travel with an entity? The authors explicitly discuss resets after promotion, although the conclusion's statement about carrying archives should be reconciled with the earlier reset rules.

## Representation, mechanisms and justification

The model separates directed managerial affiliation from undirected cooperation, then quantifies cooperation using structural proximity and friendship intensity (pp.6–8). A position's productivity combines basic productivity and tenure-related experience, multiplied by a working-efficiency factor (p.9). Training pushes enthusiasm and departure propensity back toward baseline values through recovery coefficients (p.8).

The main justification is mechanistic: departures remove experience, disturb colleagues, create promotion opportunities and trigger delayed recruitment. The monthly time step is motivated by the recruiting data's time unit (p.6). Explicit flowcharts and stepwise algorithms explain how a departure can initiate a chain of promotion and hiring events (pp.10–12). Recruiting is represented by a countdown vector, making the difference between an open hiring process and an arrived employee visible.

Internal promotion has priority over external recruitment. Candidates are selected using experience and a threshold for the next job level. The state table is updated both at the receiving job and at the newly vacated lower job. These are good examples of describing an event through all affected states rather than updating only its headline outcome.

However, many behavioral constants are assumed. Friendship, enthusiasm, training recovery and the productivity proxy are not calibrated against company measurements. A plausible mechanism is a reason to explore a model, not evidence that its numerical effects are correctly sized.

## Consequential assumptions and task alignment

The baseline assigns the same departure probability across levels (p.9), despite the official problem's concern about elevated middle-management turnover. A later special scenario does distinguish middle-level churn. The baseline simplification should therefore be explicit, justified and tested rather than described as directly supplied by the problem.

More consequentially, the algorithm prevents some middle/high-level employees from leaving until a replacement is available (pp.10, 16). The source motivates this with the operational importance of the jobs. Importance does not establish that a company can postpone voluntary departures. Under a ban on external middle-level recruitment, this rule can mechanically retain dissatisfied employees and improve occupancy. Any apparent policy benefit is conditional on that retention assumption. An alternative with departures proceeding despite vacancies is a necessary structural sensitivity test before giving a real recommendation.

Other assumptions include deterministic recruiting delays equal to supplied medians, willingness to accept every qualifying promotion, no skipped levels, and resetting job tenure on promotion. The annual-to-monthly probability conversion also needs an explicit formula. The published paper does not supply executable code to resolve implementation ambiguities.

## Experiments and validation strength

The authors average ten simulations for two-year budgets and show several trajectories rather than concealing stochastic variation (p.13). They report recruitment and training budgets of 26.22 and 140.15 salary units respectively. The labels of the two adjacent cost plots appear inconsistent with their trajectories and the accompanying discussion: one is a relatively smooth declining series, the other a spiky recruiting-like series. Traceable source data and figure generation would resolve the labels; this review does not substitute corrected totals.

Higher churn produces lower occupancy, enthusiasm and modeled performance (pp.14–15). The discussion connects direct vacancy losses with indirect social effects. Agreement with that qualitative expectation is a plausibility check, not empirical validation. Likewise, a simulated staffing path settling around 80% is not independently verified by an initial 85% staffing figure.

For the recruitment-policy comparison, the authors hold other stated parameters fixed and compare several outputs after ten repetitions (pp.16–17). This is a useful controlled-comparison design. Their phrase “control-variate method” describes that comparison, but the paper does not document a statistical control-variate estimator. Small performance differences should be interpreted with uncertainty, not ranked solely by two plotted means. The final policy prose switches between external and internal recruitment in ways that need editorial reconciliation with the plotted labels.

The stochastic check subtracts the averages of two groups of three runs (p.20). A small difference between those two averages is not an error bound or a confidence interval. Parameter sensitivity changes two assumed coefficients, but similar results above one parameter threshold do not establish that a baseline value outside that region is insensitive. These checks are useful beginnings; stronger uncertainty claims require a clearly specified statistic and enough replicates to estimate it.

## Multilayer extension

The 14-person example represents affiliation, friendship and competition as separate layers and explains how repeated node identities connect the layers (pp.18–19). Its diagram and adjacency description make the representation understandable. Aggregate degree, clustering, path length and density are reported.

More edges or different graph statistics demonstrate a richer representation; they do not by themselves demonstrate better predictions or higher team performance. The assumptions that friendship and competition improve retention/performance require an outcome mechanism and evidence. Complexity can justify a scoped demonstration, but a demonstration must remain labeled as such.

## Transferable operating rules

1. Separate persistent locations/positions from changing occupants and document attribute ownership.
2. List every state changed by an event, including downstream vacancies and resets.
3. Represent delay pipelines explicitly; distinguish recruiting activity from completed arrivals.
4. Challenge assumptions that make a requested policy succeed automatically.
5. Compare policies under a shared scenario, then test whether the ranking survives structural alternatives.
6. Treat replicate averages, uncertainty intervals and numerical error bounds as different objects.
7. Generate labels and reported totals from traceable run outputs.
8. Evaluate extra network layers by their contribution to relevant outcomes, not by richer graph statistics alone.

## Reading ledger

- Physical pp.1–11: summary, contents, context, definitions, all state/relationship models, departure and promotion procedures read in full.
- Physical pp.12–22: recruitment, all budgets and scenarios, multilayer extension, sensitivity, conclusions and references read in full.
- All figures, flowcharts and the network-statistics table were inspected from rendered pages. The record covers the available paper, not an unavailable implementation or an empirical replication.
