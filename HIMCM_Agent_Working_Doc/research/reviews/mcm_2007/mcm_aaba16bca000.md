# 2007 ICM C — Team 2052: Optimizing the Effectiveness of Organ Allocation

- Source ID: `mcm_aaba16bca000`
- Source: `MCM-ICM-master/2007美赛特等奖/C-2052-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, all **27 physical pages**, including the patient-choice proof, policy letters, and references.
- Visual supplement: physical pages 2, 4–7, 9–11, and 13–16 inspected for the supply/demand chart, equations, simulation flowchart, donation-rate plots, and ethical-objective plot.
- Numeric reproduction: **NOT_REPRODUCED**. No simulation or reported fit was executed; the described C++ implementation is not supplied in this PDF.
- Award provenance: the local filename labels this entry **Outstanding**; this review does not independently authenticate the award.
- Prompt qualification: the team's interpretation of the organ-allocation tasks was read; the separate official prompt was not independently reviewed here. Historical policy and medical statements below describe this 2007 paper, not current clinical or legal guidance.

## What the team chose to model

The paper treats organ allocation as several connected decisions rather than a single ranking formula: how to organize a national network; how to prioritize compatible patients; whether to introduce living-donor exchanges; whether a patient should accept an available organ; and which ethical objectives should govern the system. It instantiates the general framework with kidneys because compatibility and donation data are available (pp. 2–4).

Its central architecture is a daily individual-based simulation on a rooted hierarchy. A node aggregates the waiting lists of its descendants; organs and patients enter at leaves; successive priority rules traverse the hierarchy from local to national. The daily phases are patient arrival, organ arrival, matching/transplantation, then waiting-list mortality (pp. 4–7). The flowchart on p. 7 also shows a failed-operation route back into the system. This should be distinguished from the later patient-choice model's explicit one-transplant assumption (pp. 11–12): they are different modeling scopes, not one fully unified patient process.

For network comparison the authors contrast one large center/queue with twenty smaller ones. Local allocation reduces a fixed transport-related success penalty, while concentrated volume can improve an assumed experience effect (pp. 6, 16–17, 23–24). They compare American and Eurotransplant priority rules, add list-paired living-donor exchange, vary donation availability, and evaluate several social objectives. Separately, they develop an analytical accept-or-wait model using transplant survival curves and random future offers (pp. 11–15).

## Why this approach is instructive

1. **Represent the institution before selecting an optimizer.** A rooted tree and recursive priority rules directly encode local/regional/national jurisdiction. This is more useful than choosing a generic optimizer before specifying who is allowed to allocate which organ. Changing the tree, the allocation rule, or an outcome weight represents three different policy interventions and can be studied separately.
2. **Use one interpretable simulation as a common counterfactual environment.** Patient attributes include age, blood type, HLA, and PRA; organ objects retain their origin. The same process can therefore compare allocation systems with common inputs, rather than constructing a favorable model for each policy (pp. 5–6, 21). A future implementation should also use paired random streams and identical cohort definitions to realize this benefit.
3. **Separate physical mechanisms from values.** Matching compatibility and transport deterioration describe feasible outcomes; counting successful operations, favoring younger recipients, or weighting patient classes describes how outcomes are valued (pp. 6, 16, 22). The paper explicitly admits that no single objective is established as morally correct. This is a strong justification pattern: expose normative choices rather than present them as estimated scientific constants.
4. **Different stakeholders may require different mathematical objects.** The system planner compares networks and allocation rules; the individual patient faces an accept-or-wait decision. The additional survival model is motivated by that distinct question, rather than added merely to increase technique count.
5. **Recommendations can distinguish evidence from an unconfirmed mechanism.** The HRSA letter says that a strong experience effect would favor concentration but that their available data do not establish such an effect (p. 24). This conditional recommendation is more defensible than treating a sensitivity scenario as an observed effect. The proposal to pilot uncertain compensation policies is similarly a decision under incomplete evidence (pp. 17–20, 24).

## Model, solution procedure, and evidence are different layers

| Layer | What the paper supplies | What that establishes |
|---|---|---|
| Generative model | Poisson arrivals, demographic/compatibility sampling, hierarchical matching, success penalties, waiting-list mortality | A proposed representation of the allocation process, conditional on its assumptions |
| Policy comparison | Simulations of network structures and priority systems; a living-donor availability sweep | Reported outcomes under those specified scenarios, not a global optimum over all network/policy combinations |
| Exchange method | Literature discussion of graph matching; implemented list-pair matching to the first compatible waiting patient | The described exchange rule, not evidence that a maximum-cardinality or welfare-optimal matching was solved |
| Patient-choice analysis | A separability assumption, theorem, and threshold-style acceptance heuristic | A candidate analytical argument whose assumptions and derivation still require independent checking |
| Calibration | Reference to 1995–2004 OPTN national active waiting-list data and annual donations (p. 6) | Claimed parameter adjustment; no clearly identified observed-versus-predicted fit panel, residual table, holdout, or numerical calibration recipe is supplied |
| Presentation | Donation-rate time series and two stakeholder letters | Readable communication, whose strength depends on the preceding evidence |

## Results read in their actual scope

The donation-rate plots (pp. 9–11) show the effect of changing an assumed number of associated potential donors. At higher settings, modeled queues shrink; at lower settings, some continue growing. This supports a conditional statement about supply expansion in this model. It does not establish the behavioral participation rate that a real exchange policy would achieve. The authors themselves say that empirical evidence for list-pair participation is inconclusive and that a random fraction of a predefined donor base was assumed (p. 20). Their categorical conclusion that list-paired exchange is an absolute necessity (p. 20) is consequently stronger than the simulation alone warrants.

The letters say that geography-aware regional allocation generally performed better than a geography-blind national queue under their transport penalty and that the modeled American priority scheme was slightly better than Eurotransplant (p. 23). The PDF does not provide a sufficiently detailed comparison table, uncertainty interval, or parameterized transport sweep to independently assess the claimed margins. Moreover, the relevant national comparator should also be allowed to use geography as a tie-breaker: otherwise hierarchy and access to geographical information are changed together.

The ethical-objective figure on p. 16 is a single time series titled “Old Minus One,” not a controlled comparison showing the benefit or fairness of an age rule. Altering a score and observing that score is not independent evidence that the corresponding policy serves an agreed ethical objective.

## Bounded mathematical and implementation concerns

**Probability invariants must precede simulation trust.** The visually checked Poisson expression on p. 4 prints `exp(+gamma) gamma^k / k!`; a Poisson mass requires the negative exponent. The waiting-list model on p. 5 first calls `aT+b` a time-varying death rate but uses survival `exp(-(aT+b)T)`. An instantaneous hazard `aT+b` instead integrates to `exp(-aT^2/2-bT)`. Even taking the printed survival as the intended model, the one-day conditional death probability would be `1-exp(-(2aT+a+b))`, not the printed `exp(2aT+a+b)`, which exceeds one for positive coefficients. These are visible specification errors; absent code, this review cannot decide whether the implementation shared them. They are important because mortality directly controls queue size and policy outcomes.

**Audit axes against the state model.** Figure 6 labels its vertical axis maximum waiting time in days, yet reaches roughly 30,000 days near simulation year one (p. 11). An initialized backlog might produce waits exceeding simulated time, but its age distribution and scale are not documented sufficiently to reconcile this value. The review does not silently relabel it as a sum of waits. The first-year spikes in cured-patient objective plots also make initialization and warm-up policy important. Figure 1's caption mentions transplants/donors while its legend labels waiting list/donors (p. 2); these stocks and flows need distinct definitions.

**A constant probability is not a continuous-time intensity.** The patient-choice section calls `p_i` a probability “at any given time” and then uses exponential waiting times (p. 12). A consistent continuous-time formulation must define it as an arrival rate with time units and specify independence/competition between offers. Survival functions also need a consistent conditional/unconditional interpretation and finite expected lifetime, not only a limit of zero.

**Separability does not automatically establish a time-independent acceptance policy.** The proof on pp. 14–15 asserts that future acceptance comparisons differ only by `a(t2)/a(t1)`. For delayed offers, conditional survival involves `a(t+w)/a(t)` over possible future waits `w`; general separability does not make that quantity independent of current time. A stronger memorylessness condition, or an explicit time-dependent dynamic program, is needed to justify that reduction. The displayed expected-lifetime expression also counts post-offer lifetime without clearly including life lived while waiting, and the integration-by-parts step does not display the derivative of `a`. Thus the theorem should be treated as an unverified proposed derivation, not imported as a proven decision rule. These observations are static mathematical checks, not a reproduced numerical counterexample.

**“Maximal” and “maximum” matching are not interchangeable.** Page 8 calls a maximal matching algorithm best because it finds the greatest possible number of pairs. A maximal matching cannot be enlarged by adding a single edge; it need not have maximum cardinality. If cycles, donor withdrawals, and heterogeneous preferences matter, the exact graph, feasible exchanges, and objective must be stated before an optimality claim.

**Do not confuse plausible inputs with identified effects.** A uniform 5% nonlocal penalty ignores actual travel times and geography; the reported 21% advantage of live kidneys needs a clear outcome definition and adjustment for case mix before being a universal multiplier. The modeled experience effect and donation participation fraction are especially consequential. A parameter table with units, source, population, uncertainty, and role in each equation is needed to reproduce or challenge these choices.

**Conclusions must reconcile their own evidence.** Pages 17 and 19 make conflicting broad statements about donors' responsibility for operation costs. Page 18 retains literal missing-citation placeholders. Strong assertions about long-term donor risk and compensation-market guarantees exceed the descriptive evidence presented. For a competition paper the immediate lesson is citation completion, consistent terminology, and a claim-level audit; these historical statements should not be reused as current medical or policy facts.

## Reusable workflow instructions

- **Coordinator:** create a task-to-model map separating institutional design, allocation, donor behavior, and individual choice; specify which outputs each component must deliver and how shared assumptions agree.
- **Domain/data role:** record the version of every historical policy, define each stock/flow, separate donor willingness from potential-donor supply, and document input distributions rather than citing a database generically.
- **Modeler:** define feasible matches and normative objectives separately; distinguish maximal from maximum matching; derive survival, hazard, and arrival processes with units and probability bounds before implementation.
- **Computation role:** test patient/organ conservation, no duplicate allocation, probability ranges, time-scale conversion, queue initialization, and return-after-failure rules; run common-input comparisons and report uncertainty.
- **Independent reviewer:** challenge confounded policy comparisons, reproduce one small allocation example, verify the threshold theorem or request a counterexample search, and identify claims whose magnitude is unsupported by a displayed result.
- **Writer/visuals role:** show baseline/alternative outcomes alongside fairness and operational metrics, label conditional mechanisms as conditional, reconcile figure captions with axes, and trace every recommendation in the letters to evidence in the body.

The strongest transferable approach is an explicit policy architecture with separable mechanisms and values. Its use requires stricter probability validation, transparent parameter provenance, and calibrated recommendation strength than the PDF itself consistently provides.
