# Choosing and Justifying a Modeling Approach

This chapter supplies the reasoning procedure used in Stages 1–7 of the [working document](WORKING_DOC.md). It is a set of operational prescriptions. Historical examples and the strength of the supporting research are tracked separately in [research status](research/STATUS.md).

## 1. Start with the quantity or decision, not the method

Write a sentence of the form:

> For **[decision-maker/population]**, determine **[quantity or action]** over **[space and time]**, using **[available evidence]**, subject to **[non-negotiable conditions]**, and assess success by **[criterion]**.

If that sentence cannot be completed, an algorithm shortlist is premature. Several sentences may be needed for different requirements. Link them when one result becomes another model's input.

Distinguish these objects:

| Object | Meaning | Example in a fleet-transition problem |
|---|---|---|
| Observation | A recorded measurement | Distance driven by a bus in a year |
| Parameter | A quantity treated as fixed within a run | Energy use per kilometer |
| State | A quantity evolving through the model | Fleet composition at the end of year t |
| Decision variable | A quantity the planner can choose | Buses replaced in year t |
| Outcome | A result used to evaluate the decision | Total discounted cost or lifecycle emissions |
| Constraint | A condition that limits feasibility | Annual expenditure cannot exceed available funds |
| Preference | A tradeoff between acceptable outcomes | How much extra cost is acceptable for lower emissions |

The same quantity can have different roles in different models. Record its role rather than relying on its symbol.

## 2. Build a problem structure before choosing a model family

Ask what generates the outcome and what can be changed. Useful structural distinctions include:

- **Stocks and flows:** accumulation, depletion, conservation and capacity.
- **Interactions:** contact, competition, queues, congestion, contagion and feedback.
- **Networks and geometry:** connectivity, distance, travel feasibility and spatial coverage.
- **Temporal dependence:** trends, seasonality, lag, adaptation and irreversibility.
- **Resource choices:** competing actions under budgets, physical limits or deadlines.
- **Measurement and preferences:** observable indicators versus values assigned to their consequences.
- **Heterogeneity:** whether one average case conceals different populations or regimes.

These questions guide model representation. They are not a lookup table that maps “environment” to one algorithm or “transport” to another.

Draw an architecture with typed connections. For each connection state the transferred quantity, unit, time interval, spatial resolution, version and uncertainty. For example:

`activity scenario → annual vehicle distance → energy demand → emissions/cost accounting → feasible replacement schedules → recommendation`.

If a chosen schedule changes demand, and demand changes cost, check whether the architecture needs feedback. Sequential presentation in a paper is not evidence that modules are actually coupled.

## 3. Separate formulation, solution and validation

Three levels must remain distinct in every model decision record:

1. **Representation/formulation:** what mathematical objects stand for reality and what relations, objectives and constraints connect them.
2. **Solution/computation:** how those equations, transitions or decisions are evaluated or solved.
3. **Validation/evaluation:** what observations, comparisons or properties assess the resulting claims.

“Use a genetic algorithm” describes a search procedure, not the decision problem. “Use Monte Carlo” describes repeated sampling, not the mechanism being simulated. “Use TOPSIS” does not define what sustainability means. An agent must supply the missing representation before these choices can be evaluated.

When comparing algorithms, keep the formulation and budget comparable. When comparing formulations, acknowledge differences in represented objectives or feasible sets. Otherwise an apparent performance gain may arise from solving an easier problem.

## 4. The justification chain

Every central choice needs a connected explanation across six layers:

| Layer | Question | Evidence or explanation |
|---|---|---|
| Task fit | Which requirement needs this component? | Requirement ID and required output |
| Reality fit | Which mechanism or tradeoff does it represent? | Domain evidence and explicit abstraction |
| Mathematical fit | Why do these variables and relations encode that mechanism? | Derivation, definitions, dimensions, constraints |
| Evidence fit | Are the inputs and assumptions supportable? | Data diagnostics, sources, parameter ranges |
| Comparative fit | What is gained or lost relative to a simpler or genuinely different option? | Common comparison protocol and observed results |
| Claim fit | What conclusion can this evidence support? | Validation, uncertainty and scope limitations |

A citation can support a mathematical method or a domain fact, but it does not automatically justify applying the method to a new problem. The application bridge must be written.

### Weak and stronger explanations

**Weak:** “We selected this model because it is accurate, objective and widely used.”

**Stronger, before the experiment:** “The required output is a feasible annual replacement schedule. Replacement counts are discrete, and annual budget and charging capacity are explicit limits. We will therefore test an integer decision formulation against a simple oldest-first replacement rule. We will compare feasible total cost and emissions under identical demand and funding assumptions. If the optimization provides negligible gain or cannot be solved reliably, the rule-based schedule remains a valid baseline.”

**Stronger, after the experiment:** report the actual comparison, solver status, observed difference and limits. Do not insert invented gains into a generic paragraph. The reasoning must remain valid if the simpler model wins.

## 5. Choosing a baseline and genuine alternatives

A baseline is a credible point of comparison, not a deliberately poor opponent. Match it to the task:

| Task | Potential baseline | Candidate extensions worth considering when justified |
|---|---|---|
| Time-series forecast | Last observation, seasonal repetition or simple trend | Dynamic regression, structured time-series model, mechanistic scenarios |
| Resource allocation | Equal allocation, current practice or a transparent priority rule | Constrained optimization, uncertainty-aware decisions |
| Ranking | Explicit criteria with equal weights | Elicited weights, alternative normalization, non-compensatory rules |
| Dynamics | Deterministic aggregate model | Heterogeneity, spatial effects, stochastic events, feedback |
| Spatial coverage | Regular spacing or nearest-service rule | Capacity-aware placement, network travel, phased construction |

These are examples, not mandatory algorithms. A baseline that violates the problem's hard constraints must be repaired or used only as a clearly labeled infeasible reference.

Use alternatives to test consequential choices: static versus dynamic; aggregate versus individual; joint versus sequential; deterministic versus stochastic; compensatory score versus threshold constraint. Multiple names for nearly identical methods may provide less insight than one carefully chosen structural alternative.

Before comparing, write what would cause each candidate to be retained or rejected. If the alternatives cannot be distinguished with available evidence, report that and favor the option whose extra assumptions are least consequential for the decision.

## 6. Assumptions as controlled simplifications

For each important assumption record:

`statement → purpose → evidence → location in the model → expected effect → test or bound → consequence if false`.

Separate assumptions used to define a scenario from claims about the world. “Fuel prices remain constant in the baseline scenario” does not assert that prices will remain constant in reality. Separate an assumption introduced for a prototype from one retained in the final model.

Prioritize assumptions that could change feasibility, ranking, trend direction or recommendation. Do not pad an assumption list with harmless facts while omitting a consequential simplification hidden in code.

An assumption can be useful without being literally true. Its justification must show why its approximation is adequate for the question and what happens when it is relaxed. “There was no data” explains a difficulty, not the adequacy of ignoring a mechanism.

Prioritize assumptions that make the favored policy succeed by construction. For example, preventing employees from leaving until replacements exist can make a recruitment restriction appear to preserve staffing. Treat that retention rule as a consequential assumption and test an alternative. Similarly, an observed operating point does not establish an optimal target merely because the objective penalizes deviations from it. The [complete local comparison of 2015 ICM C papers](research/cases/2015_ICM_C_complete_local_comparison.md) shows why these distinctions matter.

## 7. Guidance by task structure

### 7.1 Prediction and extrapolation

Define the target, forecast origin, horizon, frequency, population and information available at prediction time. Separate interpolation, short-horizon prediction and long-range scenario extrapolation.

Preserve temporal order in validation when future information would otherwise leak into training. Fit preprocessing within each training partition when it uses estimated quantities. Compare models over identical periods and horizons. Report a meaningful error measure with units or a clearly defined normalization.

Test whether selection changes across origins, horizons or regimes. A single favorable holdout is not decisive evidence of universal superiority. Model tuning and final assessment should not silently use the same information.

For long-range forecasts, inspect structural plausibility: negative populations, explosive growth, bounded adoption, resource ceilings or regime changes. Small recent errors do not certify distant predictions. Provide conditional scenarios or uncertainty where justified, and identify which future assumptions dominate.

### 7.2 Evaluation, indices and ranking

Start by defining the concept being evaluated and the decision it informs. Document directionality, units, scaling, missing-data handling, aggregation and the meaning of compensation between criteria.

Weighting is a substantive choice. Entropy-based variation measures do not determine moral or policy importance. Equal weighting is also a choice. AHP requires defensible judgments and consistency checks; dimensionality reduction summarizes variation rather than automatically identifying welfare or causal importance.

Check correlated indicators and double counting. A change in normalization, reference population or alternatives may change a score's interpretation. Evaluate whether rankings are stable under plausible weights and data treatment, and whether a threshold rule is more appropriate than allowing all disadvantages to be offset.

Agreement with an external ranking is useful comparative evidence, not proof of objective correctness. Explain differences in definitions and preferences before claiming one list is wrong.

### 7.3 Optimization and planning

Define decision variables, objective, hard constraints, planning horizon and information available when decisions are taken. Distinguish resource limits from preferences. Justify discounting, weights and penalties in terms of their role, not convenience alone.

Check feasibility before optimizing. Verify budgets and capacities across all relevant periods, not just in aggregate. Ensure decisions remain operationally meaningful: an integer fleet, connected route, admissible schedule or accessible location.

Report solver status, runtime, tolerances and the relevant search domain. State a bound or gap if available. If using heuristics, compare to known small cases or appropriate baselines and multiple runs. A best-found solution is not automatically a global optimum.

For multi-objective decisions, expose the tradeoff. Use a Pareto comparison, explicit preferences or constrained formulation as suitable. Arbitrary weighted sums can conceal a value judgment and can behave badly when units differ.

Test whether uncertain costs, demand or capacities change the decision. A nominal solution with almost no feasibility margin may be less useful than a slightly less efficient robust alternative.

### 7.4 Mechanistic and dynamical modeling

Specify states, flows, interactions, time scale, initial/boundary conditions and the mechanisms omitted. Derive equations from those relationships where possible. Check dimensions, signs, conservation and valid state ranges.

Identify parameters that can be estimated and those that require external evidence or scenarios. Do not treat a good trajectory fit as proof that every parameter or mechanism is correctly identified.

Validate qualitative and quantitative behavior: equilibria, limiting cases, response to perturbations and comparison with credible observations. Check numerical stability and time-step dependence when discretizing.

Extend to spatial or individual-level models when aggregation hides a mechanism important to the answer. Additional entities and parameters bring additional evidence and computational obligations.

For a multi-step physical or resource chain, check every conversion and then the final endpoint. Geometric agreement does not validate an inferred mass; a calibrated epidemic curve does not establish treatment demand; an average demand does not establish an inventory-feasible delivery schedule. Use the [interface template](templates/MODEL_INTERFACE.md) to preserve definitions, timing and uncertainty between agents. The [four-paper 2012 leaf/tree comparison](research/cases/2012_MCM_A_complete_local_comparison.md) illustrates alternative chains and their different evidence burdens.

### 7.5 Simulation

Specify the simulated entities, state, events/transitions, randomness, interaction rules and observation process. Record what is sampled and why its distribution is defensible. Separate modeled uncertainty from arbitrary randomization used for searching.

Verify simulation logic on small cases. Check replication count, convergence or precision of the reported statistic, initialization and warm-up effects where relevant. Preserve seeds, but investigate more than one realization.

Define how competing transitions are sampled and when shared resources are reserved. A probability derived from a mean duration must match the actual waiting-time process, including other exits. A smaller computational population must preserve the intended capacity ratios, rates and decision behavior; compare it with the original scale instead of assuming proportional scaling is harmless.

Specify which entities persist, which attributes move with them, and which reset after an event. Distinguish waiting work, active work and completed arrivals. Reconcile every rate with its denominator and time exposure. Use tiny counterexamples to check claimed directionality: an older event should receive less weight under a decay rule, a promotion should preserve total headcount, and a probability must remain within its declared range.

Keep solver configuration experiments separate from model uncertainty. Changing a search algorithm's population size does not test an uncertain behavioral response or an assumed optimal staffing target. Map each scenario to the exact requirement it answers; a stronger stress scenario is useful only when its difference from the requested scenario is explicit.

Simulation output tests implications of the assumed model. It is not independent real-world validation of those assumptions. Use external observations or credible benchmarks where available, and describe the remaining evidential limits.

Identify which outputs are imposed by construction. If a simulation fixes aggregate turnover and uses a network score only to select who leaves, matching the imposed turnover cannot validate the network's predictive value. Test genuinely derived consequences, such as the distribution of departures or changes in service capacity. An analytical balance calculation can verify internal simulation consistency without becoming independent empirical validation.

### 7.6 Spatial and network models

Explain node and edge meanings, direction, weights, capacity, connectivity and the relationship between geometric and network distance. Decide whether travel, coverage, flow, assignment or scheduling is the actual problem.

A route must obey operational constraints as well as visit locations. Check obstacles, access, duration, service time, energy, congestion and route continuity when relevant. A visual path crossing a forbidden region is not feasible because its endpoint distances are short.

Distinguish an exact graph result for a simplified graph from an exact solution to the original physical problem. The abstraction itself requires justification and testing.

### 7.7 Measurement, forecasts and interventions in one problem

Treat these as separate questions: what the current condition is, what would happen under current practice, what a feasible action changes, and which action is preferable. A composite index defines a measurement convention. A forecast estimates an outcome under stated conditions. Neither automatically identifies the effect of spending or changing a policy.

Before a policy experiment, specify `action → resources/capacity → affected state → response and delay → outcomes → decision criterion`. A control coefficient, indicator target or cluster center is not itself a purchasable intervention. Where response evidence is insufficient, use labeled effect-size scenarios and narrow the conclusion accordingly.

Use the same initial state, outside conditions, transition rules, horizon and outcome accounting for the no-plan and proposed-plan futures. Check that a zero intervention recovers the specified baseline. Compare two future outcomes to assess incremental benefit; improvement from today's value alone mixes policy effects with background trends. If different models generate the two scenarios, compare their no-intervention behavior first and disclose any consequential difference.

Carry the realized state between planning stages. A fixed-plan stress test and a test that reoptimizes after a shock answer different questions. Report them separately. Compare costs under a common budget and time basis before claiming cost-effectiveness, and preserve separate outcomes when a scalar objective hides the relevant tradeoff.

If a learned model approximates an existing scoring function, retain that direct function as a baseline. Synthetic training data do not add independent observations. Test fidelity, bounds and expected monotonicity before interpreting surrogate response curves as domain knowledge. A turning point introduced by approximation is not evidence of a real-world optimum.

The [complete local 2015 ICM D comparison](research/cases/2015_ICM_D_complete_local_comparison.md) gives six contrasting architectures, the evidence obligations at their interfaces, role assignments and small verification cases.

## 8. Claim strength and the evidence ladder

| Supported statement | Evidence obligation |
|---|---|
| We implemented the specified method | Reproducible code and a correspondence check |
| The output satisfies the modeled constraints | Explicit checks under the stated inputs |
| The method beats this baseline here | Fair comparison over identified cases and metrics |
| The decision is stable over these conditions | Defined perturbation/scenario set and decision changes |
| The model predicts held-out observations well | Appropriate independent evaluation and uncertainty |
| This causal mechanism explains the change | A defensible identification strategy or sufficient mechanism-based evidence |
| This is globally optimal | A suitable proof or optimization certificate within the stated mathematical problem |

Do not climb this ladder through stronger wording alone. Also distinguish absence of a detected failure from evidence that no failure exists.

Maintain a separate implementation-maturity label: proposed mechanism, executed toy example, target-scale implementation, or endpoint evidence checked. These are not interchangeable. A modular design can support future experiments without having executed them. Qualitative claims still need defined scenarios and limits; they do not become universally true merely because no precise number is reported. The [2015 A32722 review](research/reviews/mcm_2015/mcm_037c369c63c7.md) supplies both a useful admission of this boundary and an example of a final bulletin exceeding it.

## 9. Writing justification as an argument

An effective paragraph often follows this structure:

1. State the modeling requirement or observed problem.
2. Explain the relevant mechanism or mathematical property.
3. Describe the chosen representation and the simplification it makes.
4. Compare with the meaningful alternative or baseline.
5. Point to the actual evidence and its limitation.
6. Explain the consequence for the decision or next model component.

Not every paragraph needs all six sentences. The complete argument must contain the necessary links somewhere clearly identifiable.

Avoid empty assurances such as “scientific,” “reasonable,” “comprehensive” or “highly accurate” without a defined basis. Replace “the results are reasonable” with the specific invariant, comparison or external observation they satisfy.

When a parameter is borrowed, state whether its population, technology, year and units are compatible. When a method is adapted, identify the adaptation and recheck properties that may no longer hold.

## 10. Rejection, rollback and reconsideration

A failed experiment is a useful result when it changes a decision. Diagnose the level of failure before changing algorithms:

- **Task failure:** the output answers the wrong question → revisit requirements.
- **Evidence failure:** incompatible data, leakage or unsupported parameters → revisit sources and scope.
- **Representation failure:** omitted mechanism or wrong objective → revisit architecture.
- **Mathematical failure:** inconsistent equations or constraints → revise specification.
- **Implementation failure:** code does not implement specification → repair and rerun.
- **Inference failure:** acceptable output described too strongly → narrow the claim or add evidence.
- **Communication failure:** valid reasoning is hard to follow → revise exposition.

Record the failed candidate, observed issue, affected conclusions and next action. Keep rejected alternatives in the research record; include them in the final paper only when they explain a useful tradeoff or strengthen the argument.

## 11. A model-choice review checklist

- Can the requirement be stated without naming the method?
- Are the decision, outcome and assumptions distinct?
- Does the mathematical representation correspond to the stated mechanism?
- Are required data available at the correct scale and time?
- Is the baseline credible and feasible?
- Are alternatives genuinely different in a consequential way?
- Were comparison conditions defined before selecting the winner?
- Could any planned check actually cause rejection?
- Do solver guarantees survive the problem-specific adaptation?
- Are effects of subjective preferences and unsupported proxies visible?
- Is the final claim no stronger than the evidence?
- Can a new reader trace the choice to sources, runs and a decision record?

## 12. How to learn from O-award papers

Study the construction of the argument, not only the named algorithms. Extract how the authors identify a tractable question, organize interacting subproblems, build a baseline, make a principled simplification, reveal a tradeoff, test a claim and communicate a result.

Record what the authors explicitly justify and what remains implicit. Preserve strong ideas even when a numerical detail is questionable. Conversely, do not promote a weak justification into a universal rule because the paper received an award.

For transfer to HiMCM, ask whether the same mechanism, data availability, mathematical burden, computational resources and explanatory demands apply. Use a simpler representation when it preserves the decision-relevant reasoning. More advanced mathematics is useful when it resolves a real modeling need and can be defended clearly.
