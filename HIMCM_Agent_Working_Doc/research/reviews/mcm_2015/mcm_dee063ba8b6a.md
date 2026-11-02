# Full review: 2015 Problem C, Team 37284 — Human Capital Management in Organizations

- Source ID: `mcm_dee063ba8b6a`
- Source: `MCM-ICM-master/2015美赛特等奖/C-37284-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–21, including references. Printed pp.1–20 correspond to physical pp.2–21.
- Visual supplement: physical pp.3–20 inspected for relationship diagrams, all equations, assignment encoding, worked matrix example, event/GA flowcharts, result tables and experiment plots.
- Numeric reproduction: **NOT_REPRODUCED**. Numerical outcomes remain author reports; checks below concern the printed model and interpretation.
- Award provenance: explicit Outstanding filename label; not independently verified here.
- Original problem: the [official statement](../../sources/2015_ICM_Problem_C.pdf) was read, including visual inspection of the organization chart and job-level data.

## Task interpretation and architecture

The report distinguishes three objects: a relationship graph among people, a hierarchy among jobs, and a bipartite assignment between people and job classes (pp.3–6). The bipartite representation is many-to-one because multiple employees can occupy a class with several positions. Time then changes employees, relationships and assignments.

The dynamic loop separates social-state updates, simulated departures/recruitment and the manager's assignment decisions (pp.7–14). The decision component uses a genetic algorithm to search assignments under job-capacity and promotion constraints. This is a useful example of locating the controllable decision inside a larger uncertain environment: the manager changes assignments, while departure behavior is simulated rather than directly commanded.

## Approach and justification

Two interpretable behavioral variables are introduced: loyalty describes an individual's propensity to remain, and intimacy describes influence from other people (pp.3–4). Promotion and time spent in a job change loyalty; changes in relative job levels change intimacy (pp.7–9). A worked two-person matrix example shows how an assignment change updates the appropriate loyalty multiplier. This small example helps connect a compact matrix expression to the intended operation.

Departures are separated into individual and social-influence components, with social effects delayed to the next monthly step (pp.9–10). The chosen delay prevents an instantaneous cascade within one update. It is a substantive timing assumption that should be varied if cascade speed matters.

The authors motivate the assignment encoding in concrete terms: each gene records a person's current class; capacity violations are rejected; mutation/crossover are modified to represent promotions (pp.12–13). This is stronger than naming a genetic algorithm without specifying how a candidate solution represents a real decision. However, restricting changes to upward moves also restricts the feasible search space. It needs justification against realistic experience/eligibility requirements and alternative assignment methods.

## Data and assumptions

The model uses supplied job counts and costs, but constructs the interpersonal graph randomly and assigns random initial behavioral values, then adjusts loyalty to obtain approximately the desired churn rate (p.14). A later discussion explains how real observations could estimate these parameters (p.18); it does not establish that those observations were available or used in these runs.

The model groups administrative clerks and inexperienced employees into a common salary level. Equal salaries do not imply equal recruiting time, training cost or eligibility, so the retained distinctions must be stated in the implementation. The paper also acknowledges that it uses the job-class table without fully representing the supplied departmental chart (p.20). Department structure is deferred to future work.

A particularly consequential assumption is that the observed 85% staffing level maximizes output (pp.2–3, 10–11). An observed operating state is not evidence of an optimum. The model penalizes deviations from that target, so it can prefer restoring the assumed target by construction. The target should be a scenario or empirically supported objective, not a conclusion inferred from its own penalty function.

Other assumptions include tenure as an ability proxy, salary-driven promotion preferences, no firing/demotion, and no separate initial training cost for new recruits. The paper states these choices, making their role inspectable, but the choices remain conditional.

## Objective, algorithm and validation

The objective combines ordinary payroll/recruiting/training expenses with a penalty for an unbalanced distribution of employees among job levels (p.11). This makes the cost of structural shortages visible. The penalty's conversion into salary units is an additional value judgment, requiring justification and sensitivity analysis. Minimizing such a cost is not automatically equivalent to maximizing profit when output is unknown.

The algorithm experiments examine population size, iteration count, mutation and crossover settings (pp.18–19). A convergence plot motivates the chosen iteration budget, and parameter sweeps examine how long the search takes. This is **solver configuration analysis**. It does not test uncertainty in the loyalty, intimacy, staffing-target or structural-penalty assumptions. A plateau in a stochastic search also does not certify global optimality. The report appropriately calls the algorithm approximate in parts of its method, while some summary language is stronger.

For the two-year budget, the paper reports an average of five simulations and supplies monthly departures, arrivals and cumulative costs (p.15). That detailed table is useful for stock-flow and accounting checks. It reports recruiting and training totals of 38.20 and 127.08 salary units. The averaging/rounding procedure and variation across runs are not supplied, so the displayed precision should not be read as an uncertainty estimate.

High-churn experiments adjust hiring to meet a staffing threshold and display both direct and structural costs (pp.16–17). A two-parameter feasibility map distinguishes adequate staffing with a good structure, adequate staffing with a poorer structure, and failure to meet the target. This is a useful decision-oriented visualization, provided the definitions of “good structure” and scenario feasibility remain explicit.

The cost table on p.16 labels one column as training, while surrounding discussion of the total invokes salary. Its scale also differs substantially from the earlier training budget. The categories and time aggregation need reconciliation before numerical reuse; the paper does not provide run receipts to settle whether a label or an accounting definition caused the mismatch.

## Probability and policy checks

Loyalty and intimacy are interpreted probabilistically, but their multiplicative update rules can exceed one without explicit bounds. The social-departure expression adds influences from departed neighbors, and can also exceed one if enough weighted contributions are present (pp.7–10). A faithful executable specification must state bounds, dependence assumptions and how individual and socially induced events combine. Silently clipping a probability would introduce a new model choice; a reviewer should request the choice explicitly.

The restricted-recruitment table tracks arrivals, departures and promotions by class, which is a useful conservation representation (p.18). The authors infer that higher middle-level churn can improve cohesion through new promotion opportunities. That conclusion depends on their assumed promotion-to-loyalty relationship and does not include an independently measured cohesion outcome. It should therefore be described as a conditional mechanism, not evidence that higher turnover is generally beneficial.

The information-flow layer in the final section is a conceptual extension with a diagram (pp.19–20). It is not a separately validated improvement to the earlier simulations.

## Transferable operating rules

1. Separate people, positions and assignments when they have different lifecycles.
2. Identify exactly which variable the decision maker controls.
3. Use a small worked example to verify matrix or encoded state transitions.
4. Check probability bounds and competing-event logic before simulation.
5. Do not infer an optimal target from a single observed operating point.
6. Keep solver tuning separate from uncertainty in model assumptions.
7. Report flows by category so conservation and budget totals are auditable.
8. Use feasibility maps to expose tradeoffs, while defining every region's acceptance rule.

## Reading ledger

- Physical pp.1–11: summary, introduction, all assumptions, three graph representations, state updates, worked matrix example, churn process and objective equations read in full.
- Physical pp.12–21: assignment search, all experiments/tables, parameter analysis, extension, further work, limitations and references read in full.
- Every figure and table was inspected visually. No unavailable code, statistical calibration or numerical rerun is implied by this full-paper review.
