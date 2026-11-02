# Full review: 2007 MCM B, Team 2056 — In the Zone

- Source ID: `mcm_e0dcf8bb60f2`
- Source: `MCM-ICM-master/2007美赛特等奖/B-2056-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, all **50 physical pages**, including references and all three appendices. Physical and printed page numbers coincide.
- Visual supplement: pp.9, 12, 14–17, 21–25, 28–32, 34–36, 38 and 47–50; all flowcharts, topology diagrams, material equations, boarding maps and result tables inspected.
- Numeric reproduction: **NOT_REPRODUCED**. No code, random seeds or complete parameter/run records accompany this PDF.
- Award provenance: explicit Outstanding filename label; not independently verified here.
- Prompt qualification: authors' task interpretation read; separate official problem not reviewed. Historical airline practices are not presented as current information.

## Architecture: separate the environment from the search

The paper develops **a movement prototype → finite-capacity processor simulation → optional seat-choice behavior → permutation search → practical boarding recommendations**. The environment simulation maps an input passenger order to a boarding time; the genetic algorithm searches over such orders. This is a clear distinction between modeling reality and searching for a decision within that model (pp.7–23).

The preliminary line model is explicitly excluded from final experiments and retained as a limit-case reference (pp.8, 47). The extended model adds seat uniqueness, seat-access delays, baggage delays and finite row queues. These are meaningful revisions to a common simulator, rather than disconnected named methods. A shared evaluator permits comparisons under common physical assumptions.

A particularly strong design detail is the back-to-front update order: each passenger can move at most one row in a cycle, preventing a front-to-back loop from carrying the same passenger across the entire aircraft in one nominal time step (pp.10–12). The authors identify an implementation detail that changes the modeled time scale and explain its resolution.

## Representation and physical constraints

Each row acts as a processor, with commands for passing, fumbling, seating, rearranging seated people and stowing baggage. The final model has a one-to-one passenger-seat assignment and limits internal queues to two people (pp.13–17). The queue limit is not a minor numerical setting: it makes a waiting passenger occupy aisle space and allows local congestion to block upstream movement.

The authors show that unlimited queues reverse the conclusion about back-to-front boarding: it changes from slower than random in the finite-space model to faster under the physically unrealistic queue assumption (pp.33, 39). This is a useful structural counterexample. An abstraction that silently removes physical space can change the preferred policy, even if both implementations run without errors.

Multi-aisle topology is represented with branching and connected processor chains rather than simply duplicating a single-aisle result (pp.17–18). This makes shared entry and selected cross-aisle movement visible. Full validation for all proposed layouts is not supplied, so “any plane” should remain a capability claim requiring configuration-specific checks.

## Search design and interpretation

The genome is a permutation of seat assignments. Mutation relocates a contiguous subsequence; crossover is adapted to preserve the set of seats instead of producing missing or duplicated assignments (pp.20–23). This is a mechanism-based reason to modify a generic genetic algorithm: feasibility must survive the representation's operators.

The authors compare random initialization with seeding from recognizable boarding patterns. The seeded search gives a reported normalized time of 0.67, better than the random-start search's 0.81 but slightly worse than the simple window-to-aisle result of 0.64 (pp.32, 36–38). This does not establish that more search is better than a strong baseline. It does support using known feasible solutions as search seeds and inspecting learned patterns for understandable structure.

A plateau after about sixty generations is described as a local optimum. Without evaluating a defined neighborhood or supplying a certificate, it establishes best-found behavior and apparent convergence under that run configuration, not mathematical local optimality. The stochastic objective also needs independent final reevaluation; search can select a candidate partly because it received favorable simulation noise.

The recommended hybrid admits families and window-seat passengers together. The authors justify it by practical grouping and expected family self-organization, even though its reported modeled speed is below pure window-to-aisle (pp.40–42). This is an explicit implementation tradeoff. However, the hypothesized reduction in family seat conflicts is not actually quantified in a dedicated family-behavior experiment. Its practical superiority remains a proposal, not an experimentally established finding.

## Parameter and preference evidence

Seat-conflict penalties are reported as measured in multiple physical trials with a simulated row (p.14). This is a positive attempt to collect task-specific evidence. The number of trials, participants, uncertainty and transfer to real cabin dimensions are not recorded, limiting reproducibility.

Baggage delay is an increasing function of boarding position, formed by scaling a Weibull cumulative distribution and adding Gaussian noise (pp.15–16). This is a shaped response curve, not simply a sample from a Weibull stowage-time distribution. A Weibull hazard does not independently prove the frequency of failure to find overhead space, because the model has not defined that failure event as the distribution's random variable. Missing parameters and treatment of negative noisy delays also need specification. A local bin occupancy model and a global passenger-count proxy make different claims.

The open-seat extension explicitly represents preference for front rows, windows and aisles, with renormalization as seats fill (pp.23–27). It is less behaviorally idealized than an assumption that everyone generously fills the farthest window seat. Yet the stated Markov construction has unresolved interfaces: its displayed matrix is rectangular (30 by 6), while matrix powers and row-to-row transitions require a square state transition matrix. Moreover, the eventual seat chosen by a one-way, capacity-constrained boarding process is not automatically the stationary occupancy of an irreducible recurrent chain. The source must distinguish a hypothetical preference-generating chain from the actual absorbing seating process and explain why one supplies the other's choice probabilities.

The appendix provides definitions and a convergence argument, but diagonalizability does not follow merely from irreducibility and aperiodicity. That technical derivation cannot replace a valid mapping from states to passenger choices. No unavailable implementation is inferred from these printed ambiguities.

## Comparison and validation

The result table uses random assigned-seat boarding as the common baseline, reports the normalization denominator, and describes 1,050 trials per tested pattern (pp.31–32). This gives more comparison structure than isolated favorable runs. It still lacks variance, confidence intervals, run seeds and a clear separation of candidate search from final assessment.

Removing baggage delay, removing seat conflicts and allowing unlimited queues provide useful mechanism checks (pp.38–39). Their outcomes are compared with explicit expected directions. These are internal ablations, not the empirical validation claimed broadly in the abstract. Agreement with intuition or another model does not establish calibrated real boarding times.

The method called “reverse pyramid” is defined here as alternating full back and front rows toward the center (p.31). Its map differs from the window/row-based pyramid arrangement in [Team 2053](mcm_009e1fc87d77.md). Consequently, the two papers' results for that label do not compare the same algorithm. A named policy must be translated into an exact sequence or rule before its results are pooled.

This paper finds its preference-based open seating slower than random assigned seating, whereas Team 2053 finds cooperative unassigned boarding fastest. The disagreement is informative: different behavioral assumptions, arrival conditions and reference schemes can dominate the policy label. Neither paper's outcome is a universal answer about all unassigned-seat policies.

The authors define low sensitivity as inherently desirable. That is too broad: a correct model may be highly sensitive near a real bottleneck or threshold. Validation should ask whether the sensitivity is credible and decision-relevant, not require every output to change only slightly.

## Transferable operating rules

1. Keep the simulator and search procedure separate, with a common evaluator for alternatives.
2. Specify update order and enforce physical capacity before optimizing policies.
3. Design search operators that preserve feasibility, then verify that invariant independently.
4. Retain a strong simple baseline even when using an advanced heuristic.
5. Distinguish mechanism ablation, parameter sensitivity, empirical calibration and independent validation.
6. Record exact policy rules; shared names do not guarantee equivalent interventions.
7. Make behavioral assumptions visible when they drive policy rankings.
8. Label a practical hybrid as a tradeoff and test its extra behavioral benefit before declaring superiority.

## Reading ledger

- pp.1–8: abstract, contents, task interpretation, prior work and model architecture read in full.
- pp.9–18: processor process, assumptions, all extensions, topology and deplaning setup read in full.
- pp.19–27: genetic search, feasibility-preserving operators, seeding and complete preference model read in full.
- pp.28–38: every scheme definition, map, normalized result, search interpretation and start of robustness discussion read in full.
- pp.39–50: all ablations, implementation recommendation, limitations, references, literature appendix, prototype and Markov-chain appendix read in full.

All material visual content was inspected; no numerical reproduction was performed.
