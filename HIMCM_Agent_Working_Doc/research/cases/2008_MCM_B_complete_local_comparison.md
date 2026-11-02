# 2008 MCM B — Complete local comparison: modeling difficulty and generating Sudoku

## Evidence boundary

This case compares **both competition papers in the local 2008 B collection**, **88 physical pages** in total, after complete text and relevant visual review. It does not claim to cover every submission to the contest. Both local filenames label the entries Outstanding; that metadata is not independent award authentication. The separate official prompt was not reviewed for this case, and neither program nor reported numerical result was executed.

| Paper | Physical pages | Primary source review |
|---|---:|---|
| Team 2858, *hsolve* | 26 | [Full review](../reviews/mcm_2008/mcm_7bdc6242e203.md) |
| Team 3780, *Ease and Toil* | 62 | [Full review](../reviews/mcm_2008/mcm_3da11eeffc41.md) |

The useful comparison is how each team defines and operationalizes the same ambiguous target, then connects evaluation to construction. The review does not infer that any particular feature caused an award.

## Two coherent approaches to the same task

| Design decision | Team 2858 | Team 3780 |
|---|---|---|
| Meaning of difficulty | Expected work of a specified hypothetical expert | Initial candidate ambiguity summarized by an ease score |
| Representation | Candidate graph plus trajectory through a human-style strategy library | Histogram of candidate counts over empty cells |
| Evaluation mechanism | Expected within-tier search cost, randomized move selection, repeated solves | Decreasing candidate-count weights normalized by empty-cell count |
| Main advantage | Describes a proposed mechanism of human effort | Inexpensive enough for many evaluations during construction |
| Main limitation | Depends on strategy tiers, equal check costs, and idealized search behavior | Omits spatial structure, deduction sequence, and specialized techniques |
| Generator | Random clue insertion plus deduction, then score-based rejection; a separate hard-seed variant | Completed solution followed by clue removal, feasibility checks, and repeated perturbation/improvement |
| Runtime question | Expected time to hit a requested score interval | Cost of tuned generation relative to a random-removal baseline |
| Recognized tradeoff | Hard seed reuse improves yield but limits structural novelty | Low-cost scoring and tuning cannot reliably reach the hardest published cases |

Neither approach follows merely from “Sudoku is a search problem.” A fast exact solver, a human-difficulty model, a unique-solution checker, and a generator serve different purposes. The positive workflow lesson is to assign each component a separate contract before combining them.

## What to learn about choosing and justifying an approach

**Begin with the construct.** Team 2858 makes the target solver explicit and derives its score from a hypothesized process (physical pp. 6–9). Team 3780 emphasizes the cost of evaluating the score inside a large search (pp. 10–11, 21). Both are defensible starting points when their scope is stated. The choice should depend on the user-facing requirement: predicting human time calls for matched behavioral evidence; steering a generator may permit a cheap surrogate if a stronger final check is retained.

**Reduce a complex process only where the reduction is justified.** Team 2858 integrates out random search order using `(p+1)/(v+1)` while preserving random move trajectories. Team 3780 compresses a board into a local histogram. The former reduction preserves a specified conditional expectation; the latter discards structural information and therefore needs empirical validation for its intended use. An agent should say what information a reduction retains, what it loses, and which downstream claim depends on the lost information.

**Let the first method's failure determine the extension.** Team 2858's hard puzzles are rare under random construction, motivating a seed-based generator and an explicit diversity tradeoff. Team 3780's removal search reaches a score floor, motivating clue restoration and another improvement pass. The extra method addresses an observed bottleneck. Its value should be measured against the original baseline under equal budgets, with target-hit rate and feasibility intact.

**A shared metric must really be shared.** Team 3780's Java and PHP code implement different cell filters for the nominally identical WNEF; its calibration and generation results cannot safely be joined until that discrepancy is resolved. This is a general multi-agent integration hazard: two roles can agree on a function name while computing different quantities. A common input/output fixture and versioned metric definition should be part of the handoff.

## Feasibility must be certified independently of quality

Both teams recognize that a solved board and a uniquely solvable puzzle are different objects. Team 2858 modifies its backtracking behavior so that a lucky successful guess is not treated as a forced deduction during construction (p. 13). That is a reusable positive example: when repurposing a solver, reconsider its return semantics and proof obligations.

Team 3780 illustrates the corresponding failure mode. A bounded solver's false result can mean contradiction, several solutions, or inability to finish. A parent that counts only children returning “unique” can overlook an unresolved or multiply solvable branch. Its printed implementation additionally leaves a guessed cell hidden while incrementing the count of fixed cells. These static findings do not establish the failure frequency of published outputs, but they prevent treating the procedure as a verified uniqueness certificate.

A reliable construction pipeline should therefore carry separate outputs:

1. **Validity:** all clues respect the puzzle rules and at least one solution exists.
2. **Uniqueness:** exactly one solution is established by a sound complete method or a valid deduction certificate; unknown is a distinct state.
3. **Difficulty:** score and uncertainty under a named model, including unresolved status where applicable.
4. **Target achievement:** the final score lies inside the requested interval under a frozen calibration.
5. **Diversity:** novelty relative to seeds and symmetry-equivalent previous outputs.
6. **Cost:** time, failed proposals, retries, and the computational budget.

High difficulty cannot compensate for ambiguous feasibility, and a valid puzzle can still miss its requested difficulty.

## Validation claims that must not be merged

Team 2858 reports ordinal agreement with 800 externally labeled puzzles. Team 3780 reports mean score differences among labeled groups and among generated groups. These test different questions. Association with labels is not calibration in minutes, and different means are not non-overlapping classes. Both need evaluation on held-out puzzles and preferably a matched human-time dataset if the claimed target is human difficulty.

Team 2858 compares its overall score histogram with an Easy-puzzle time distribution across unrelated users. Similar right-skewed shapes are only a qualitative check. Team 3780 draws controls disproportionately from different sources for different difficulty levels; source effects can masquerade as difficulty effects. A large total sample does not repair mismatched experimental units or confounded labels.

Both papers offer direct opportunities for arithmetic and provenance checks. Team 2858's printed chi-square exceeds the bound for the table dimensions and sample size; some generated outcomes are unaccounted for in its interval counts. Team 3780's claimed linear complexity in recursive guess depth omits branching, and its score tables use ranges not aligned with the original control categories. These points should become small, mandatory review tasks rather than broad instructions to “check the statistics.”

Neither paper proves that a generator optimizing its own score produces outputs satisfying an independent conception of human difficulty. A particularly useful extension would be to use a cheap score for proposals and a separately validated process model or human sample for final acceptance. That is a prospective design suggestion, not a result reported by either paper.

## Concrete role handoffs for a new contest problem

| Role | Required handoff | Acceptance question |
|---|---|---|
| Coordinator | Decision contract: target users, requested categories, valid outputs, budget | Can every deliverable be judged without guessing what “difficulty” means? |
| Domain/data | Versioned benchmark with source, skill level, sampling scheme, and held-out split | Are calibration and validation populations aligned with the claim? |
| Modeler | Score definition, assumptions, boundary cases, and lost information | Does the score represent the construct or explicitly function as a surrogate? |
| Computation | One metric implementation or cross-implementation fixtures; independent feasibility oracle | Do all roles compute the same score, and can unknown feasibility be mistaken for failure or success? |
| Computation/modeler | Baseline and proposed generator under comparable budgets | What improves: hit rate, score, runtime, or diversity, and what deteriorates? |
| Independent reviewer | Counterexample cases, table arithmetic, branch semantics, and classification error | Which headline claims survive direct checks? |
| Writer/visuals | Separate charts for score overlap, target-hit rate, runtime, and diversity | Can a reader distinguish mathematical guarantees from observed performance? |

This case supports a general approach to ambiguous evaluation tasks: define the quantity, choose an appropriate representation, validate it externally, and only then optimize against it while protecting independent feasibility conditions.
