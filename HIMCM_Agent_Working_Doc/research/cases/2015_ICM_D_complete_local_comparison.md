# 2015 ICM D: from measuring sustainability to justifying an intervention

## Scope and evidence status

All six independent 2015 Problem D papers in the original local collection have been read in full: **122 physical pages**, including references, appendices and relevant visual material. Four filenames say Outstanding; two Chinese filenames say first prize and remain separately classified in the inventory. This is complete coverage of this local same-problem set, not all contest submissions. Neither award status nor numerical results have been independently reproduced.

The [official three-page problem](../sources/2015_ICM_Problem_D.pdf) supplies the common task: define sustainability, develop a twenty-year plan for a least developed country, evaluate its effects and investment effectiveness, and consider outside influences. Historical country membership and statistics in these papers are not current eligibility or data claims.

| Team / source record | Pages | Architecture | Strong transferable idea | Main evidential gap |
|---|---:|---|---|---|
| [34985](../reviews/mcm_2015/mcm_c7be0d8bf9c8.md) | 20 | Separate socioeconomic/ecological measures; dependency dynamics; spending-allocation search | Exposes intervention pathways and a preference-dependent tradeoff | Cross-country associations do not establish a country's response to spending; fixed-plan and reoptimized robustness differ |
| [35780](../reviews/mcm_2015/mcm_97fea85bdc35.md) | 24 | Indicator hierarchy; development and coordination; coupled state model; staged control | Separates measurement, forecast and intervention and carries state across planning stages | Abstract control coefficients lack a quantified connection to purchasable programs |
| [38727](../reviews/mcm_2015/mcm_eeb1090fe4b2.md) | 19 | Six-dimensional instability profile; threshold diagnosis; concrete programs; assumed future indicators | Preserves unacceptable weaknesses and explains specific implementation ideas | Assumed future inputs yield a conditional scenario, not an identified policy effect or cost-effectiveness result |
| [38996](../reviews/mcm_2015/mcm_1efe10af3368.md) | 21 | Two-axis trajectory score; baseline ARIMA; intervention dynamics; feasibility screen | Distinguishes current position from direction of change and screens numerical levers for feasibility | A close baseline trajectory does not validate intervention responses; costs and effect sizes are not comparable across programs |
| [37415](../reviews/mcm_2015/mcm_131746ad6fd7.md) | 19 | Pressure/state/response; level, balance and trend; strategy screen; grey/Markov scenarios | Makes a broad concept explicit and compares a no-plan future with a proposed-plan future | Changing the forecasting model along with the policy confounds the comparison; neutral transition does not recover the stated baseline |
| [35630](../reviews/mcm_2015/mcm_4113751a8ab0.md) | 19 | Weighted score; clustering; RBF/BP surrogate; staged indicator targets | Includes monitoring and revision between stages | Synthetic samples add no independent country evidence; surrogate turning points are interpreted beyond their demonstrated meaning |

The table describes observed practices and reviewer interpretation. The prescriptions below are a project design informed by those readings. They are not an inferred official judging rubric.

## 1. Identify the distinct questions before distributing work

The common task contains at least five questions, each with a different evidence obligation:

1. **Measurement:** What does sustainability mean for this decision, and how do indicators represent it?
2. **Forecasting:** What happens over the relevant horizon under stated outside conditions and current practice?
3. **Intervention response:** What changes because a feasible action is taken?
4. **Decision:** Which actions are worth taking under budgets, capacity, timing and stakeholder preferences?
5. **Adaptation:** What should be observed later, and what observation would trigger revision?

One named method rarely answers all five. A weighted score answers a measurement question. A time-series forecast need not identify causal responses. An optimizer finds a good input to the model it is given; it does not supply a missing response mechanism. A neural network trained on a constructed score learns that construction, not a new definition of welfare.

At G1, the human team must accept the intended meaning, scope, country-selection rationale, decision-maker and required outputs. Agents should not silently substitute a classification task for an investment task.

## 2. Choose a measurement architecture for a stated reason

The local papers provide several genuinely different abstractions:

- **Separate components** expose a socioeconomic/environmental tradeoff, as in 34985.
- **Level and balance** distinguish aggregate achievement from uneven development, as in 35780 and 37415.
- **A threshold profile** can flag a severe weakness that should not be compensated by good performance elsewhere, as in 38727.
- **Position and direction** distinguish current conditions from movement toward or away from a target, as in 38996.

These are structural choices. Their justification should explain what a simpler scalar would hide and whether the decision needs the added distinction. Do not choose an index because its diagram looks sophisticated.

Define direction, unit, domain, population, time, missingness, transformation and reference anchor for every indicator. Distinguish modifiable services from natural endowment and country size. Freeze anchors for comparisons across years and scenarios, or explain and test the effect of changing them. Show raw outcomes alongside any composite objective.

A balance measure needs commensurable components. A trajectory measure needs a direction for stationary and reversed paths. A threshold needs a reason independent of the classification it was chosen to produce. Entropy weights describe data dispersion; policy priorities remain a separate judgment.

## 3. Make the intervention contract explicit

Before coding a policy experiment, require this chain:

`action → resources and implementation → affected state → response over time → physical/social outcomes → decision criterion`.

Use one row per action:

| Contract field | Example of the question it must answer |
|---|---|
| Action and responsible actor | Is the action building capacity, changing a rule, subsidizing a service, or providing training? |
| Cost and resource requirements | What is purchased, in which year's currency, and what recurring cost remains? |
| Implementation limit | How fast can trained staff, facilities, equipment or coverage expand? |
| Affected state | Does the action change a stock, rate, access share, behavior or model parameter? |
| Response evidence | Does evidence estimate this intervention's effect in a compatible population, or merely show an association? |
| Delay and persistence | When does the effect start, decay, saturate or require maintenance? |
| Coupled consequences | Which other outcomes may improve or worsen? |
| Uncertainty and failure | Which plausible changes would erase the benefit or make the action infeasible? |

For example, an education budget is not itself an increase in an education index. A model needs a supported link to places, attendance, completion, skills or another relevant state, with capacity and delay. If those links cannot be estimated, use transparent effect-size scenarios and identify the evidence gap. Do not manufacture precision by inserting a guessed multiplier into a complex dynamic system.

34985 offers the clearest intended dependency chain in this set. 35780 exposes the gap between an abstract control parameter and a program. 38727 makes concrete programs visible but assumes their endpoint effects. 35630 shows why moving an input toward a cluster center does not establish that an action can produce that movement.

## 4. Compare plans using a common counterfactual

Represent the distinction explicitly:

`next state = transition(current state, action, outside conditions, parameters)`.

The no-plan and proposed-plan experiments should use the same initial state, transition rules, parameter definitions, outside scenario, horizon and outcome accounting unless a documented structural alternative is being tested. A zero action must recover the specified no-action baseline.

Report the difference between two future outcomes, not merely the change from today to the proposed future. A rising background trend can make an ineffective plan appear successful. Conversely, a plan can improve outcomes relative to a deteriorating baseline even if its absolute trajectory still worsens.

If one forecasting model supplies the baseline and another supplies the policy scenario, first compare both under no intervention. Explain the discrepancy and whether it changes the inferred policy gain. Even close agreement is only a consistency check; independent evidence is still needed for the response to an intervention.

Include costs on the same time basis. “Largest improvement among tested input changes” is different from “largest improvement for the available budget.” Where a common scalar is not defensible, report feasible alternatives and their outcome/cost tradeoffs instead of concealing them in a weight.

## 5. Preserve the actual state between stages

A staged plan is useful when decisions can adapt to observations or computational limits make annual control impractical. Specify what is decided at each stage, what information is then available and which earlier commitments cannot be undone.

Carry the final state of one stage into the next. Do not splice separately optimized trajectories and assume their combination has the displayed properties. Keep decision frequency distinct from the simulation's numerical time step.

Two robustness questions must remain separate:

- **Fixed-plan test:** How does the accepted plan perform when conditions differ from its design assumptions?
- **Adaptive/reoptimized test:** What can a planner recover if allowed to change the plan after learning new information?

The second can be useful, but it cannot certify the first. A monitoring policy also needs an observation rule and an implementable revision trigger. “Revise when necessary” is insufficient if the model never defines necessary.

## 6. Minimum verification before interpreting the result

The six papers expose failures that small checks can catch before substantial computation:

| Small check | What it protects against |
|---|---|
| One indicator improves while all others stay fixed | Wrong direction, label swap, or unjustified surrogate reversal |
| All inputs are zero; one column is constant; a value sits exactly at a category boundary | Undefined normalization, entropy, coordination or classification |
| Same outcome is expressed as a fraction and as a percentage with the declared conversion | Silent scale errors |
| Input country/variable order is permuted consistently | Accidental dependence on matrix ordering |
| Zero intervention is used | A baseline that changes even when the action is absent |
| A transition matrix is checked before and after adjustment | Missing self-transitions, invalid row sums or unintended state changes |
| A control is applied for one small time step | Confusion among a stock, derivative and next-period value |
| A learned surrogate is compared with its direct target function | Treating approximation error as a substantive mechanism |
| Two planning stages are run consecutively from the realized intermediate state | Impossible combinations of individually attractive plans |
| Every component total is reconciled with its table and figure | Inconsistent evidence reaching the narrative |

These are proposed checks for future work. No numerical experiment in this comparison is presented as an executed reproduction of the historical papers.

## 7. Six-role assignment and handoffs

| Canonical role | Work for this problem structure | Handoff and acceptance |
|---|---|---|
| Coordinator | Separate the five questions; select the bounded decision; track requirement coverage and gate decisions | G1 scope and an explicit list of required outputs; no policy task disappears into an index task |
| Domain-data | Define indicators, source-compatible units and intervention-response evidence | Data dictionary and intervention contract; association, observation and assumption are distinct |
| Modeler | Compare measurement structures; formulate dynamics, constraints, baseline and real actions | G2 architecture, mathematical specification and rejection conditions; implementer need not invent causal links |
| Computation | Implement the direct baseline, transition checks, feasible plans and scenario runs | Versioned runs and reconciled outcomes/costs; neutral-policy and staged-state checks pass |
| Independent-reviewer | Challenge scale, domain, causal attribution, comparison fairness and claim strength | Review report with exact evidence, missing checks and consequences; material issues resolved before G3 |
| Writer-visuals | Show separate outcomes, causal chain, tradeoffs and conditional conclusions | Every numerical claim traces to an accepted run; assumptions are not presented as measured effects |

At G2, an unresolved intervention-response gap leads to a narrower scenario question or further research. At G3, the human team accepts only the conclusion supported by the completed comparison. It may be a conditional recommendation with a monitoring rule, a range of acceptable plans, or a finding that available evidence cannot distinguish alternatives.

## 8. What a defensible justification sounds like

**Before execution:** “The task requires an allocation decision. We will first use separate service and environmental outcomes to prevent the aggregate score from hiding a severe loss. The baseline will represent current practice under the same outside scenarios as the proposed plan. Each action will have a resource limit, delay and supported response range. We will retain additional feedback only if it changes feasibility or the preferred action under those ranges.”

**After execution:** report the actual incremental outcomes, costs, uncertainty, failures and decision reversals. If the response range is assumed, the claim remains conditional. If the simpler plan performs similarly, complexity has not earned a stronger recommendation. If no intervention effect can be justified, the honest deliverable is a useful scenario analysis and a prioritized evidence-gathering plan.

The common lesson is to justify the interfaces between model layers. A strong index, solver or diagram cannot supply missing evidence at an interface it does not address.
