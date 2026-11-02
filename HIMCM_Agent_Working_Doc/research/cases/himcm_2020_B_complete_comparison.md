# HiMCM 2020 B: complete local-corpus comparison

> Archived prior research: excluded from further work under the current instruction. Retained for provenance, not active workflow evidence. See [scope](../SCOPE.md).

## Coverage and evidence boundary

This comparison covers all four independent 2020 B papers in the local HiMCM corpus. Each has a full page-by-page review, including appendices and relevant visual evidence. All numerical results remain **NOT_REPRODUCED**. The comparison draws conclusions about the papers' reasoning and reporting, not verified real-world conservation outcomes or a ranking of teams.

| Paper | Architecture | Main useful contribution | Central verification issue |
|---|---|---|---|
| [10839](../reviews/himcm/HIMCM_2020_B_10839.md) | Start-year sampling; delayed benefit; cost and annual-spending variation score | Explicit all-project scheduling and benefit floor | Objective/reporting mismatch, candidate-selection defect, absent financial solvency proof |
| [10876](../reviews/himcm/HIMCM_2020_B_10876.md) | Expected benefit/cost ratios; common linear delay penalty; random priority permutations | Clear priority-to-calendar conversion and four-project example | No-savings assumption excludes endowment mechanism; constant-cap plan drops a project; code/result inconsistencies |
| [10997](../reviews/himcm/HIMCM_2020_B_10997.md) | Delay model; entropy/TOPSIS; annual knapsack and greedy baseline; genetic improvement | Constructive baseline, initialization comparison, explicit late-cost exception | Equation sign errors; ambiguous cap enforcement; schedule tables and charts differ |
| [10878, author-public](../reviews/himcm/HIMCM_2020_B_10878.md) | Start-year genetic algorithm; accumulated benefit/smoothness ratio; affine donation fit | Compact schedule representation and separate funding stage | Image-only schedule omits a row; fit objective is not minimum fundraising; prefix constraint missing from formula |

Source prompt: `HIMCM_备赛资料/02_历年真题/2020/2020_HiMCM_Problem_B.pdf`, all three physical pages including Attachment A read. The prompt asks for long-term reliable funding, all 48 projects and future management, a priority order balancing available funds and spending over time, and a one-page nontechnical memo. The supplied 25 cost years are project-relative years. The definition of benefit is an expected relative conservation value, not a monetary return.

## What the comparison changes about the approach

The first modeling decision is financial and temporal, not the choice of optimizer. All four papers build an expenditure schedule, but none fully establishes an endowment capital requirement with a cash-balance recurrence and terminal management liability. They often equate smooth annual expenditure with reliable funding. That substitution is attractive because a variance objective is easy to compute, but it does not answer whether the organization can pay when obligations fall due.

A working agent should separate four objects:

1. **Recovery schedule:** when each project starts and finishes, with each original cost stream shifted intact.
2. **Conservation outcome:** what is gained or put at risk by timing, with units and uncertainty stated.
3. **Funding policy:** initial capital, annual donations, investment returns, withdrawals, restricted reserves, and permitted borrowing.
4. **Cash feasibility:** whether funds cover all commitments at every date and leave enough for management after recovery.

The mandatory constraint is all-project coverage. Partial-coverage scenarios may explain tradeoffs, but cannot replace the requested solution. Papers 10876 and 10997 are useful counterexamples: their lower-cost recommendations exclude projects while discussing how to add them under a larger budget. The working document should force the requirement owner to label such a scenario as an alternative policy, not silently redefine success.

## A defensible modeling sequence

### 1. Establish the data contract

Create a source-preserving table with unique project ID, benefit definition, uniqueness definition, conditional success definition, and all 25 relative cost-year columns. Keep missing values distinct from zero. Duration is the last nonzero required cost year, not the number of positive cells or the first run of zero costs.

Test the assumption that cost profiles decrease. Paper 10997 explicitly identifies the late expenditure of project 486, showing why “most profiles decline” is insufficient. If advance fundraising is used to cover that later cost, record money held in a restricted reserve; do not replace the original expenditure stream without a reconciliation.

Document the unit and entity behind every external financial number. Paper 10876 combines a foundation giving figure with a project-specific cap and an inconsistent allocation fraction. A source number needs an owner, period, currency, accounting basis, and justified allocation bridge before becoming a model parameter.

### 2. Write constraints before objectives

Every project starts exactly once, receives each required cost year, and has a valid finish date. Full spending includes future management and any explicit uncertainty reserve. A source's 25-year cost horizon does not itself require all projects to finish by calendar year 25; paper 10878 makes that unsupported conversion.

Specify whether annual fundraising is capped, whether savings may accumulate, whether borrowing is allowed, and whether a cap is hard or may be exceeded by a defined amount. Paper 10997 alternates between a strict cap and tolerated fluctuations. The validator needs one interpretation, not a prose compromise.

If a schedule is evaluated over a finite horizon, define what happens afterward. Ending the displayed graph while commitments remain does not remove the liability.

### 3. Build the simplest complete baseline

Start all projects immediately if financing permits, or use a clearly stated priority rule and full commitment reservation. Compute the exact expenditure ledger and cumulative cash requirement. These baselines reveal the real tradeoff before adding ranking methods or heuristics.

For a fixed expenditure stream, zero opening reserve, no interest, and constant annual donations received before each year's expenditure, the smallest feasible constant annual amount is the maximum of cumulative expenditure divided by elapsed years over every calendar prefix. This elementary bound is a better first check than fitting a line to annual costs. With initial capital, returns, and reserves, extend the balance recurrence rather than discarding the prefix-feasibility principle.

### 4. Justify the conservation objective

Decide whether the board wants maximum expected absolute conservation value, fairness/coverage, urgency, low extinction risk, or a compromise. A sum of project benefit/cost ratios, used by 10876 and in 10997's evaluation score, is not the same as total benefit per total cost. It favors cheap projects through its weighting. State that policy explicitly if intended.

Avoid treating relative conservation benefit as dollars, as 10878 does, or interpreting uniqueness as population size. Check whether success feasibility is already partly represented in the given benefit before multiplying again. Identify which elements are evidence-based and which are board preferences.

Delay should enter through a transparent scenario model. A literature analogy can motivate the direction of effect, but does not calibrate every species. Test sign, range, initial value, and long-delay behavior before simulation. Paper 10997's typeset differential equation contradicts its plotted direction, demonstrating why this stage must precede optimization.

### 5. Choose an optimizer that matches the state

If a fixed-horizon start-year model is tractable, try a time-indexed integer formulation and retain solver status and bounds. For larger or nonlinear variants, use a baseline plus local insertion/swap search, then a genetic or randomized method if it measurably helps. Method novelty is not a requirement.

Every optimizer must call the same validator. A current-year cost check is sufficient only under a proved invariant; otherwise reserve all future commitments. Crossover and mutation do not preserve annual financial feasibility merely because their parent schedules were feasible. Retain the best feasible schedule, not just its objective value.

Run exact small cases to test the scheduling logic. Paper 10876's block example is an excellent communication device; turning such an example into an exactly solved test would make it a validation device too.

### 6. Evaluate improvement without changing the question

A flatter cost curve may come from delaying benefits, excluding projects, changing the horizon, or tolerating an overrun. Report each component separately. Ratio objectives involving standard deviation or variance need a zero-denominator policy and a fixed evaluation horizon. Candidate-specific min-max scaling can erase the dollar magnitude the model is meant to control.

Compare baseline and improved schedules on coverage, expected benefit, peak annual expenditure, minimum cash balance, terminal reserve, finish date, and total funds. Include runtime, multiple seeds, best-so-far traces, and any optimality bounds. A plateau is evidence about search progress, not proof of global optimality.

## Sensitivity should resolve decisions

Vary delay assumptions, costs, annual fundraising capacity, investment returns, reserves, horizon, criterion weights, and any policy threshold. Separate parameter uncertainty from search randomness with controlled seeds and repeated runs.

Before parameter sweeps, simplify the objective algebraically. In 10876, a common linear delay coefficient simply scales a weighted-delay term when the included projects and feasible set are fixed and no clipping occurs. Changing its magnitude cannot change the exact optimizer under those conditions. An agent that checks this first avoids mistaking random-search variation for meaningful sensitivity.

Report changes in actual decisions: which projects move, by how many years, what loses value, and whether the funding plan remains solvent. Smooth score curves and narrow one-parameter perturbations are insufficient evidence of robust implementation.

## Concrete multi-agent responsibilities

| Role | Owned artifact | Required handoff |
|---|---|---|
| Requirement and policy lead | Coverage, funding rules, horizon, management tail | Explicit hard constraints and approved alternative scenarios |
| Data and evidence analyst | Immutable source table, definitions, external financial provenance | Versioned data contract and exceptions such as late cost spikes |
| Financial modeler | Funding policy and cash/reserve recurrence | Independent solvency validator and minimum-funding baseline |
| Conservation modeler | Value, delay, success, and uncertainty assumptions | Unit/sign/domain checks and scenario parameters |
| Optimization engineer | Feasible initial schedule and improved candidates | Machine-readable accepted schedule, solver status, seeds, and trace |
| Independent verifier and editor | Requirement coverage and cross-artifact reconciliation | Pass/fail audit plus memo generated from the accepted result |

The verifier should not accept a paper because every paragraph sounds plausible. These four reviews expose defects across representations: 10839's selection logic and reporting objective differ; 10876's summary and memo disagree on IDs; 10997's final table and Gantt chart show different starts; 10878's image table has an all-zero project row. Assign explicit ownership for reconciling equations, code, ledger, charts, summary, and memo.

## Required final artifacts

Deliver a source-ID start/end table, project-year expenditure ledger, donation and investment assumptions, annual cash/reserve balances, terminal management requirement, baseline comparison, uncertainty scenarios, and a concise board memo. Generate every number from one accepted schedule version. The memo should state the funding request, initial actions, binding risks, and fallback policy rather than mainly describe algorithm names.

The reusable lesson is that a conservation funding recommendation becomes defensible through a complete, auditable connection from source definitions to schedule constraints, cash feasibility, conservation tradeoffs, and the board's actual decision. More sophisticated search cannot repair a broken connection earlier in that chain.
