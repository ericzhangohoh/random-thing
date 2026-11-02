# 2008 MCM B — Team 3780: Ease and Toil, Analyzing Sudoku

- Source ID: `mcm_3da11eeffc41`
- Source: `MCM-ICM-master/2008美赛特等奖/B-3780-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, all **62 physical pages**, including the complete printed Java/PHP/Python listings on pp. 23–62 and generator screenshots.
- Visual supplement: physical pages 6–13, 17, 20, 28, 42, 47, 53, 60, and 62 inspected for strategy examples, histograms, equations, statistical tables, runtime plots, exact implementation conditions, tuning settings, and displayed outputs.
- Numeric reproduction: **NOT_REPRODUCED**. All code findings are static inspections of the printed appendix; no executable generator, statistic, or timing was run.
- Award provenance: **Outstanding** is the local filename's label, not independently authenticated here.
- Prompt qualification: the paper's stated four-level generation, unique-solution, and complexity requirements were read; no separate official-prompt review is claimed.

## Chosen architecture

The team seeks an inexpensive difficulty proxy that can be evaluated repeatedly inside a puzzle generator. Its weighted normalized ease function (WNEF) summarizes the initial distribution of candidate counts across empty cells. If `c_n` is the number of empty cells with `n` candidates, the intended score is `sum(w(n)c_n)/(w(1) number_of_empty_cells)`. Larger scores indicate greater ease. The team compares exponential, squared, and linear decreasing weights, then selects exponential weights after finding broadly similar trends (pp. 10–13).

The generator first constructs a completed legal grid with a randomized row-based search. It then removes clues through a mixture of heuristic proposals, rejecting removals that fail a uniqueness test. To seek lower WNEF it sometimes restores a few clues and searches again, retaining the best mask found. The paper calls this annealing; the implementation is more specifically a perturb-and-improve search with a saved incumbent, rather than a documented temperature schedule and Metropolis acceptance rule (pp. 14–17, 51–54). That operational description matters more than the method name.

Published puzzle labels calibrate the score; a PHP profiler measures the cost of generating different score ranges; mean-comparison tests assess changes after perturbation and separation among the generator's four levels. The appendix includes both a Java metric implementation and a PHP generator/metric implementation, plus interface code and a Python control-puzzle extraction script. These distinct implementations create an important consistency obligation.

## Useful modeling and workflow choices

1. **Match evaluator cost to how often it will be called.** A static local candidate histogram is cheaper than repeatedly simulating a full human solution. The paper explains that computational tradeoff and explicitly bounds the intended local lookup work on a fixed 9-by-9 grid (pp. 10–11, 21). Such a score can be a useful proposal heuristic even when a stronger final evaluator is required.
2. **Define what the project is not trying to optimize.** The stated scope excludes forcing particular human techniques, generating the hardest possible puzzles, and enforcing visual symmetry (p. 3). This prevents unrelated features from consuming the competition's time while keeping feasibility and requested difficulty levels central.
3. **Build feasibility into each transformation.** Start from a known solution, remove one clue, test, and restore it on rejection. This offers a clear invariant and an inspectable move history (pp. 14–17). The invariant is only as sound as the uniqueness oracle, so it should be checked independently.
4. **Make heuristic proposals modular.** The code separates strategies for random removal, candidate-count preferences, dense groups, repeated values, and dependence counts. Tuning chooses among these strategies without changing the whole generator (pp. 47–54, 59–61). This is a practical structure for agents to test alternatives under a shared interface.
5. **Measure the actual bottleneck.** Instrumentation records call counts and elapsed times for key routines (pp. 18, 32). Normalized runtime relative to a baseline helps compare configurations on the same environment, while absolute time and hardware should remain available for practical interpretation.
6. **Use ablations and acknowledge the attainable range.** The paper reports before/after perturbation score distributions and varies the allowed failed-removal count (pp. 19–20). It also admits that the generator's hardest category is easier than published hard examples and that the local score can miss puzzles requiring specialized techniques (p. 21). These are valuable boundaries to carry into a recommendation rather than hide.

## Evidence should be interpreted at the correct level

The control collection comprises 40 puzzles from WebSudoku, 40 from a printed collection, 2000 GNOME puzzles labeled hard, and 2365 puzzles from a difficult-puzzle list (p. 11). This is strongly imbalanced by source and difficulty. A difference between difficulty-group means can therefore reflect source-specific construction conventions as well as difficulty. The paper assumes independent identically distributed puzzles within a source; it does not demonstrate representativeness of the larger user population, independent human solve times, or a held-out source evaluation.

Table 1 reports decreasing mean WNEF across the four control classes, approximately 0.268, 0.111, 0.092, and 0.041 (p. 13). The mean curves for all three weight families descend, but similar mean trends do not establish agreement on individual puzzle rankings. The t-tests address differences of means, not non-overlapping classes or reliable per-puzzle classification. Per-source confusion matrices, overlapping distributions, and out-of-sample classification would answer those stronger questions.

Table 2 reports lower means after the search perturbation, and the four final generated classes have approximate means 0.319, 0.262, 0.194, and 0.166 with `n=60` (p. 20). That is evidence of separation in the generator's chosen score, conditional on the implementation. It does not show that people experience four corresponding difficulty levels. The final class means also differ materially from the control-class means; the authors explicitly acknowledge a lower difficulty ceiling (p. 21), and the differing metric implementations below make a direct comparison especially unsafe until reconciled.

The runtime scatterplot uses `log2(t/t0)` and shows the most intensive observed outputs taking on the order of tens of baseline runtimes, with some easy outputs faster than the baseline (pp. 19–20). It is an empirical sample, not a worst-case bound. Moreover, different tuning levels use 1, 5, 10, or 100 perturbation attempts (pp. 59–60), so runtime clusters partly reflect assigned computational budgets. They cannot be interpreted solely as inherent puzzle difficulty.

The before/after test is naturally paired if the same initial puzzles are followed through perturbation. The printed test uses an unpaired standard-error formula (p. 19). The experimental unit, pairing, random seeds, and equality of computation budgets should be specified. A small p-value does not mean the model is “proved with” the corresponding confidence percentage, as the conclusion suggests (p. 21), and mean improvement alone does not establish global optimality.

## Critical implementation correspondence

### The two printed WNEF implementations are different

The intended equation and PHP code sum weights over **empty** cells; PHP explicitly checks `our_mask[a][b] == 0` on p. 42. The Java function on p. 28 instead checks `cells[i][j] != 0`, so it sums over **filled** cells while dividing by the count of empty cells. Its histogram routine also includes every cell without an empty-cell filter (p. 27). These are visually confirmed source conditions, not extraction artifacts. They undermine the assumption that metric calibration and generated results use one identical quantity.

The review does not infer which exact historical runs used which version, nor attribute every reported numerical difference to this bug. The appropriate repair in a new workflow is a shared fixture suite: evaluate a nearly completed board, a sparse board, and the same fixed corpus through the equation, an independent reference implementation, and every production implementation. A score/version hash should accompany calibration and results.

### Uniqueness requires more than a Boolean branch result

The deduction-only mode has a sound conceptual route: if singles logically force the entire board, those deductions certify uniqueness relative to the clues. Failure to finish is **unknown**, not evidence that multiple solutions probably exist (p. 15). The text acknowledges false negatives but then combines this incomplete test recursively using a Boolean value that conflates contradiction, multiple solutions, and search-limit exhaustion (pp. 17, 45–47).

In the pseudocode, a parent returns true when exactly one child returns true. That is insufficient if another child returned false because it had multiple solutions or hit the depth limit. An exact counting solver should distinguish zero, one, and at least two solutions, with a separate unknown result for resource exhaustion; a conservative uniqueness certificate requires one proven solution and every other branch proven impossible. Counting only children labeled unique is not equivalent to counting solutions.

There is also a direct implementation mismatch: the PHP recursive guess sets its mask entry to **0**, meaning hidden, then increments the supplied filled-cell count (p. 47, lines 892–894). The pseudocode sets that entry true (p. 17). Since `FindChoices` honors the mask, the printed implementation does not enforce the guessed value as intended. The count and actual revealed cells can diverge. This must be repaired and retested before the implementation can support a uniqueness guarantee. No generated-puzzle counterexample was executed in this review.

### Stopping conditions and output labels need a final check

Inside the loop bounded by `anneal_attempts < num_anneal_attempts`, the code tries to extend the budget when `anneal_attempts >= num_anneal_attempts` (pp. 52–53). That branch is unreachable under the displayed loop condition. The routine returns its final score after cleanup without a separate demonstrated target-range rejection gate (p. 54). Thus a tuning request and an achieved score range must be recorded separately; returning the best result within a time budget is acceptable if it is labeled honestly.

The interface's fixed thresholds on p. 33 differ from the Java Gaussian-density classifier using control means and variances (pp. 23–24, 28). The latter assumes a normal class-conditional score model and effectively equal class priors without explaining those choices in the body. The screenshot on p. 62 is evidence of a working-looking interface, not independent validation of its category semantics.

## Algorithmic claims needing qualification

- **Minimal is not minimum, and an incomplete oracle changes minimality.** A full pass of clue removal with an exact uniqueness oracle can produce an irreducible puzzle: no single remaining clue can be deleted while retaining uniqueness. It does not minimize the total clue count globally. With a deduction-limited oracle, rejected deletions may simply be unresolved, so even irreducibility under true uniqueness is not certified (pp. 14–16).
- **Recursive branching is not linear in depth.** The claimed hybrid uniqueness cost grows only linearly with allowed guesses in the paper's analysis (p. 18), but each guess can branch into several candidate values. The search-tree size can grow exponentially in depth. Even the singles stage may require repeated scans until closure, so one `81 × 81` comparison count does not by itself bound the whole procedure as claimed.
- **Fixed-size complexity is not a practical performance guarantee.** All work is formally bounded for a fixed 9-by-9 board, but the bound can be enormous. Measured latency, failure rate, resource limits, and output quality are the useful competition metrics. NP-completeness refers to a generalized family of Sudoku instances, not a finite fixed-size set.
- **Optimizing the proxy can exploit what the proxy omits.** An initial candidate histogram loses spatial structure, deduction order, and specialized patterns. Distinct puzzles can share the score while differing in human difficulty. Once a generator deliberately optimizes WNEF, validation on ordinary published puzzles alone becomes less convincing; generated outputs need a second evaluator or human test.

## Transfer into an agent workflow

The **coordinator** should separate the score's intended construct, the generator's feasibility conditions, the computational budget, and the target category's acceptance rule. The **domain/data role** should preserve source-level groups and human labels, withhold a source or puzzle set, and identify how specialized puzzles differ from the calibration population. The **modeler** should justify a cheap surrogate as such and specify the invariants and exact/unknown semantics of the uniqueness test. The **computation role** should share metric fixtures across languages, use an independent solution counter, log requested versus achieved ranges, and profile with consistent budgets. The **independent reviewer** should audit branch-return semantics, unreachable conditions, score disagreement, and the gap between statistically different means and useful classification. The **writer/visuals role** should show overlap and failure rates, name perturb-and-improve search accurately, and preserve the stated difficulty ceiling.

This paper's strongest contribution is a clear speed-versus-representation tradeoff with modular generation and empirical profiling. Its most consequential review lesson is that a long implementation appendix must be checked against the mathematical contract; code quantity and a polished interface do not establish that calibration, optimization, and feasibility use the same definitions.
