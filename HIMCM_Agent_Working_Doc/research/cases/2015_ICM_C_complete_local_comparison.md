# 2015 ICM C: complete comparison of the six local papers

## Scope and evidence status

This comparison covers **all six 2015 Problem C papers in the original local collection**: five filenames labeled Outstanding and one labeled Finalist. All six were read in full, with relevant visual material inspected. Award labels are preserved from filenames; they were not independently authenticated for this comparison. No historical simulation was numerically reproduced.

The [official problem](../sources/2015_ICM_Problem_C.pdf) was also read. The following is a synthesis of the inspected documents, not a ranking of teams, a reproduction study or a claim about every historical competition paper. The overall collection remains in progress in [STATUS.md](../STATUS.md).

| Paper | Local label | Physical pages | Full review |
|---|---|---:|---|
| Team 33572 | Outstanding | 21 | [Layered network and event simulation](../reviews/mcm_2015/mcm_b32fb4b143f7.md) |
| Team 33900 | Outstanding | 20 | [Assignment optimization and dynamic network](../reviews/mcm_2015/mcm_7f8065e88c26.md) |
| Team 35778 | Outstanding | 22 | [Position archives and event algorithms](../reviews/mcm_2015/mcm_39d71af2fb5b.md) |
| Team 37075 | Outstanding | 21 | [Social learning and HR strategy comparison](../reviews/mcm_2015/mcm_1d95d60dc731.md) |
| Team 37284 | Outstanding | 21 | [People–position assignment with search](../reviews/mcm_2015/mcm_dee063ba8b6a.md) |
| Team 39160 | Finalist | 17 | [Phased object-based simulation](../reviews/mcm_2015/mcm_2b8963a3deb6.md) |

Together these records cover 122 physical pages. Per-paper reviews separate author claims, static observations and reviewer interpretation, with page references for each substantive point.

## 1. The common problem beneath the methods

The problem asks for an organizational network and its dynamics, recruiting/training budgets, staffing under higher turnover, a restricted middle-level hiring scenario, and possible team-science/multilayer extensions. It supplies organizational and job-level information but leaves much individual behavior unobserved.

That structure creates several distinct modeling decisions:

1. What is persistent: a person, a position, an office or a job class?
2. How are people assigned to the supplied structure?
3. Which events change the state, and in what order?
4. How does a vacancy become an active search and then a completed hire?
5. Which social effects are represented, and how are they calibrated?
6. Which actions can the manager choose?
7. How are histories converted into staffing, cost and performance outputs?

The useful commonality is this decomposition. The papers do not converge on one universally justified algorithm.

## 2. Architecture comparison

| Paper | Main representation | Dynamics and decisions | Most useful transferable idea | Main condition to check before reuse |
|---|---|---|---|---|
| 33572 | Multiple relationship layers over employees, with ability and job eligibility | Ordered departure, promotion, transfer, recruitment and settlement | Connect all events to downstream staffing and accounting; compare a flow-balance relation with simulation | Aggregate turnover is imposed, so it cannot validate the network's predictive power |
| 33900 | Constructed employee assignment plus personnel and organizational graphs | Turnover scores, stochastic events and similarity-based promotion | Make the missing assignment problem explicit before calculating network measures | Proxy definitions and printed probability/AHP specifications require reconciliation |
| 35778 | Persistent positions with a table of changing occupant attributes | Explicit departure/promotion/hiring procedures with a recruiting countdown | Record every state change, reset and delay in one inspectable event model | Delaying a departure until replacement can determine the apparent policy benefit |
| 37075 | Persistent positions and a time-dependent mapping of people to positions | Beta-Bernoulli-inspired behavior; alternative promotion and recruiting strategies | Compare controllable policies under a shared environment and report several outcomes | Formula/prose correspondence and exact scenario scope need checks |
| 37284 | People graph, position hierarchy and many-to-one assignment | Loyalty/intimacy updates, stochastic events and genetic assignment search | Put the manager's controllable assignment inside the larger dynamic system | An assumed optimal staffing target and probability bounds can dominate results |
| 39160 | Stable position layers occupied by Person objects | Three successive models: random flow, satisfaction, performance-aware promotion | Verify a simple executable framework before adding coupled behavior | Rate denominators, time units and exact requested outputs must stay consistent |

No numerical “winner” is inferred. The productivity measures, recruiting mechanisms, staffing targets and experiment scopes differ. Comparing their budget totals without reconciling those definitions would create a false common benchmark.

## 3. What approach selection should learn

### Choose entities by what must remain identifiable

Teams 35778, 37075 and 39160 explicitly distinguish positions from their current occupants. Team 37284 adds an assignment relation. This is useful when a promotion preserves personal experience but changes a person's workplace and professional links.

The agent should justify its entity choice using the needed transitions. If a person leaves, which relations disappear? If a person transfers, which attributes travel? If a job is vacant, does the job still exist? A representation that cannot answer those questions will force hidden choices in code.

For a small HiMCM problem, the right implementation may be a pair of tables and an assignment key. A complex tensor is warranted only if multiple relationship types actually affect the required outputs.

### Separate descriptive dynamics from controllable actions

Teams 37075 and 37284 make the manager's choices particularly visible. Recruiting effort or assignment can be changed; a voluntary departure cannot simply be treated as a decision variable unless the scenario gives the manager that authority.

The modeler should label each important quantity as observed input, assumed parameter, state, action or derived output. The reviewer should then check whether a proposed policy succeeds by changing an allowed action or by silently controlling an environmental process.

### Add detail only when it can alter the answer

Team 39160's staged construction provides an effective development order. A simple staffing model can establish flow conservation and hiring delays. A social layer can then be added if it changes a relevant prediction or decision. Team 33572's explicit events similarly provide a natural place to isolate one mechanism at a time.

A richer graph has more representational capacity. It also creates more assumptions. A useful comparison holds the environment and accounting fixed, then checks whether the added layer changes the decision, improves an external prediction, explains a discrepancy or reveals an otherwise hidden bottleneck.

## 4. Why apparently reasonable conclusions can disagree

The restricted-hiring examples show why “the paper used this method successfully” is not enough justification.

- In 35778, some departing managers must remain until a replacement is ready. The no-external-hiring policy can therefore retain people by delaying their exit.
- In 37075, the reported stress case removes all external recruitment, which is broader than the specified restriction on particular middle-level roles.
- In 37284, promotion increases modeled loyalty, so new advancement opportunities create an assumed retention/cohesion benefit.
- In 39160, the relevant roles remain a small subset and can be supplied internally under the model's experience and capacity rules.

These mechanisms and scenarios are not interchangeable. A disagreement can arise before any solver is chosen. The correct response is to compare the assumptions and task definitions first, then test alternatives under a common specification. It is not to average the reported outcomes or vote among papers.

The same point applies to hiring. A fraction of vacancies being actively recruited for is a pipeline state or capacity measure. It is not automatically an annual arrival rate. A supplied median recruiting time is not automatically the mean of an exponential waiting-time distribution. Either conversion needs an explicit model and time unit.

## 5. A prospective approach for a new problem with this structure

The following is a proposed workflow informed by the papers, **not a newly executed solution**.

| Stage | Artifact and owner | Reason for the step | Evidence needed to proceed |
|---|---|---|---|
| Interpret | Coordinator + domain/data: requirement-to-output table | Preserve the exact scenario, roles, horizon and requested budget categories | Human G1 confirms the interpretation and unresolved ambiguities |
| Represent | Modeler: entity/state/event diagram | Decide what persists and how promotion, departure and hiring change the system | Tiny examples conserve people, positions and vacancies |
| Baseline | Modeler + computation: aggregate staffing and accounting model | Establish a tractable reference and expose hiring delays/capacity | Manual balance checks and consistent time units |
| Extend | Modeler: one justified interaction or heterogeneity mechanism | Add only detail relevant to a required output or decision | Data/proxy rationale, alternative form and a comparison plan; human G2 |
| Experiment | Computation: shared scenario configurations and repeated runs | Separate policy effects from stochastic variability and changing assumptions | Pinned inputs, seeds, stopping rule and run receipts |
| Challenge | Independent reviewer: structural and numerical review | Check whether the result follows from a hidden assumption, scope change or implementation error | Reconciled discrepancies; claim-level evidence |
| Recommend | Coordinator + writer: conditional decision and limits | Translate the result into an action with a clearly stated domain of validity | Human G3 accepts conclusions and unresolved limitations |

Candidate alternatives could include a fixed-rate aggregate baseline, a role-specific dynamic model, and one interaction-aware model. These are illustrative choices. The actual shortlist must follow the new problem's requirements and available evidence.

## 6. Minimum tests for this architecture

Before any large run, require small, inspectable cases:

- **Empty and full organization:** capacity and occupancy remain within their bounds.
- **One departure, no hiring:** headcount drops by one and the correct vacancy appears.
- **One internal promotion:** total headcount is unchanged; the source and destination roles update together.
- **One delayed hire:** an active search does not count as an employee before arrival.
- **No social influence:** the interaction model reduces to its stated baseline.
- **One old and one recent event:** a claimed memory-decay rule actually gives the intended ordering.
- **Probability boundaries:** updates cannot create undefined or out-of-range probabilities without a specified rule.
- **Recruitment restriction:** only the intended job categories lose external hiring access.
- **Budget reconstruction:** per-event and per-period records reproduce the requested horizon's totals.
- **Policy comparison:** candidates face the same demand, environment and accounting rules.

These are proposed acceptance checks. Their presence in this document does not mean a simulation has been built or passed them.

## 7. Changes carried into the working document

This comparison supports several concrete operating requirements:

1. Model specifications identify persistent entities, occupant attributes and event resets.
2. Reviewers distinguish imposed quantities from genuinely derived outputs.
3. Each scenario maps to the exact requirement it answers.
4. Small counterexamples check signs, ranges, normalization and interpretation before full computation.
5. Model uncertainty and solver tuning are recorded separately.
6. Assumptions that make a policy succeed by construction receive priority in review.
7. Required totals and horizons appear explicitly, even when extra long-run analysis is included.

These changes are reflected in [approach guidance](../../APPROACH_AND_JUSTIFICATION.md), the [model specification](../../templates/MODEL_SPEC.md) and [review template](../../templates/REVIEW.md). They are useful transferable practices, not inferred official scoring rules.
