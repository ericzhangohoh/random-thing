# HiMCM 2019 A — Five complete-paper comparisons for workflow design

All five independent 2019 A papers in this local archive have now been read in full, including their appendices, code and visually inspected mathematical material. This is a complete comparison of the **local five-paper set**, not a claim that these are all submissions or all award-winning solutions. Numerical reproduction remains false for every paper. Page references below are physical PDF pages; individual reviews record exact coverage, source hashes and limitations.

## One prompt, five different decision models

The official task joins five demands: consumption history/forecast, costs and payment, venue variation, initiatives with modeled effects, and a school-newspaper article. A strong workflow must preserve those distinct outputs while choosing a coherent central decision. These papers demonstrate that topic similarity does not imply model equivalence.

| Paper | Main architecture | Most useful transferable choice | Main qualification |
|---|---|---|---|
| [9564](../reviews/himcm/HIMCM_2019_A_9564.md) | Stochastic EV service simulation; phone battery-state demand; cost/service frontiers and spatial provision | Separate insufficient capacity from poor geographic access; represent an intervention inside the model | Several paper/code constants and formulas differ; service scores and weights need defensible domains |
| [9824](../reviews/himcm/HIMCM_2019_A_9824.md) | Ownership regressions; devices-per-outlet rules; daily cost less assumed commercial benefit | Use a break-even threshold when a benefit parameter is unmeasured | A threshold is conditional, not proof that charging attracts enough profitable customers |
| [9844](../reviews/himcm/HIMCM_2019_A_9844.md) | Adoption forecast; public energy fractions; venue cost ledger; intervention multipliers | Separate total energy from the fraction supplied publicly and expose cost components | Fitted recurrence does not preserve the claimed Bass structure; major cost arithmetic and unit discrepancies |
| [10057](../reviews/himcm/HIMCM_2019_A_10057.md) | Sales-to-stock lifetime integrals; direct/space/security/convenience costs; component optimization | Distinguish annual sales from the installed stock and make stakeholder impacts explicit | Component optima are not a joint optimum; stated constraints and derivatives do not establish the claimed solution |
| [10174](../reviews/himcm/HIMCM_2019_A_10174.md) | Visitor/device agent simulation plus EV throughput simulation; tariff forecasts | Model finite availability and time-of-day interactions when averages hide bottlenecks | Displayed national annual costs match daily aggregation; mean-energy plateaus do not establish access guarantees |

## What the prompt should make the team decide first

The word “cost” supports several objects: an electricity bill, first-year cash spending, annualized ownership cost, a firm's net profit change, or total social cost. The papers move among these objects with uneven clarity. The working document should require a one-sentence objective before model search, followed by a stakeholder ledger. State whose cost is counted, over what time period, under what service requirement, and whether transfers between stakeholders cancel in the chosen objective.

For example, a coffee surcharge can shift payment to visitors without reducing electricity consumption. A removed outlet can reduce a firm's bill while increasing unserved charging demand. More visitor spending is revenue, not automatically profit or social benefit. A land purchase is capital expenditure, while annual energy is a recurring flow. These distinctions determine the correct equation before any optimization method is selected.

## Choose complexity by the unresolved mechanism

A defensible hierarchy emerges from the comparison:

1. Start with a dimensionally explicit accounting identity: operating devices × activity × energy intensity × public/free share. Give every factor a source, population and period.
2. Add stock dynamics only when sales, retirement or adoption changes matter. A lifetime integral is a structural assumption about survival; a fitted curve is a forecast assumption, not a mechanism by itself.
3. Add capacity/queueing when timing and finite chargers create unmet demand. National ownership ratios cannot reveal local waiting time.
4. Add agent states when multiple device batteries, dwell time and shared outlets create behavior that aggregate service models cannot adequately express.
5. Add economics only with a clear decision variable, benefit/cost units and feasible constraints. A named optimizer does not create a well-posed decision problem.

This hierarchy is a reviewer inference, not an algorithm prescribed by the five authors. It turns “why this approach?” into an evidence-backed explanation: identify the observable behavior the simpler baseline cannot represent, then show that the extension improves a relevant diagnostic or decision.

## The model must possess its stated justification

9824 rejects exponential ownership growth because it cannot continue indefinitely, then uses an unbounded quadratic. 9844 invokes Bass adoption theory but fits a relationship with response/sign inconsistencies. 10057 calls a saturating attraction value at `n+1` a marginal benefit without subtracting its value at `n`. These are different versions of the same failure: the method label and verbal rationale outrun the actual mathematics.

Require a **property checklist** in each candidate-model memo: domain, nonnegativity, saturation or conservation if claimed, boundary behavior, units, and the exact quantity being predicted. Evaluate those properties on the implemented equation, not the textbook name. A simple model that meets the requirements can be easier to justify than a sophisticated model whose implementation violates them.

## Validation must answer a different question from calibration

These papers supply several kinds of evidence that the workflow should keep separate:

- A regression's in-sample R² measures fit, not future accuracy.
- Agreement with another forecast checks plausibility, not realized error.
- Repeated simulation estimates Monte Carlo variability conditional on assumptions; it does not validate behavioral rules.
- A ±5% parameter sweep describes local formula sensitivity; it does not estimate whether an intervention can change that parameter by 5%.
- A one-year aggregate energy comparison tests one output and scope; it cannot validate every venue, mechanism and forecast horizon.
- A break-even calculation tells a decision maker what must be true, even when current evidence cannot establish whether it is true.

The most useful next checks are often small: an independently recorded charging day, a withheld year, a hand-calculated one-user case, nonnegative forecast counts, or a capacity/access counterexample. Require the validator to state which claim each check can and cannot support.

## Integration deserves its own role

Across the set, material errors occur at interfaces: cents versus dollars, sales versus stock, public versus free, per-device versus per-venue, days versus years, plot labels versus array order, and manuscript constants versus code. In 10174, the appendix permits a direct check showing that a value described as annual is daily national cost. In 9564, body/code discrepancies affect charging power and service scoring. These are not solved by adding more citations or a more elaborate model.

Assign one integration owner to a machine-readable quantity ledger with fields for symbol, meaning, unit, geographic scope, population, time basis, source, uncertainty and producing script. Every figure and table should derive from a frozen run with a traceable output file. Independent reviewers should recompute a few representative rows and reconcile summary/article claims to the same artifacts.

## Practical role assignments after receiving a similar prompt

The **problem lead** produces the demand map, stakeholders and decision statement. The **research/data agent** establishes source definitions, comparable populations and uncertainty ranges. The **baseline modeler** writes the smallest accounting model and identifies unresolved mechanisms. A **specialist modeler** adds only the required queueing, adoption or agent-state component, with explicit interfaces. The **implementation agent** owns reproducible runs, exports and consistency with the equations. The **skeptical validator** challenges boundary cases, feasibility, aggregate scaling and independent evidence. The **writer** turns the verified decision result into a technical argument and the required public article.

A useful handoff sentence is: “This module accepts these quantities in these units, produces this output at this aggregation level, represents these mechanisms, and has passed these checks.” The justification paragraph can then follow a reliable pattern: requirement → baseline limitation → chosen mechanism → assumptions/data → diagnostic evidence → decision implication → remaining limitation. These five papers provide examples for each part, and enough counterexamples to make the checks concrete.
