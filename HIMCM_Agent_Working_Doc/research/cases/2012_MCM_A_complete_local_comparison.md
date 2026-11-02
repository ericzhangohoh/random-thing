# 2012 MCM A — complete local four-paper comparison

## Scope and evidence status

This comparison covers all four original 2012 Problem A submissions in the local corpus: Teams 14297, 14990, 15065 and 16831, totaling **170 physical pages**. Every paper has a separate full-text-and-relevant-visuals review, including all supplied appendices. None of the complete numerical models was reproduced. Outstanding designations below come from filenames, not independently verified award records. No separate official problem statement was available in the corpus inventory; this comparison is about the submissions' handling of the leaf/branch/tree questions.

| Paper | Physical pages | Architectural contribution | Main evidence boundary |
|---|---:|---|---|
| [14297](../reviews/mcm_2012/mcm_5cb8073eb1ab.md) | 45 | Individual leaf → interaction → branch mechanics → whole tree; explicit fallback when physiological parameters cannot be identified | Local geometry or moment agreement does not validate whole-tree leaf mass; several printed error claims conflict with displayed values |
| [14990](../reviews/mcm_2012/mcm_e2428f0d3227.md) | 42 | Reusable shape descriptors across classification and silhouette comparison; controlled fixed-area geometry | AHP consistency does not validate classification; carbon and CO2, annual rates and standing mass require explicit conversion |
| [15065](../reviews/mcm_2012/mcm_1cbc0cd9b972.md) | 29 | Shared three-dimensional tree generator and directional-light component support multiple questions | A fitted crown shape does not validate total leaf mass; assumed leaf area index and physiology still require evidence |
| [16831](../reviews/mcm_2012/mcm_ec8f03fd20e5.md) | 54 | Five modules with tractable geometry, statistical association and inexpensive mass estimators; conditional limiting-resource argument | Cluster-label consistency is not botanical truth; fitted regressions are not independent validation; plotted functions differ from described equations |

## What the four approaches jointly teach

The useful common pattern is **a chain of interpretable intermediate quantities**. A leaf representation supplies area, shape or exposure; exposure connects to a physiological or geometric relationship; that relationship informs a tree-scale estimate. The chain is the reason to select models. A method earns its place because it answers a particular subquestion or supplies an input required elsewhere.

The main design choice is how much of the chain to model mechanistically. Team 14297 attempts the most extensive mechanism chain but explicitly encounters unavailable parameters. Team 15065 reuses simulation components across tasks. Team 16831 separates geometric explanations from statistical estimators and favors a convenient diameter measurement for the final mass estimate. These are alternatives within a common architecture, not a ranking by sophistication. An agent should select among them using available measurements, identifiability, approximation error, computation time and the final decision.

A compact feature system can be useful without being a complete biological taxonomy. All four papers simplify shape. The defensible question is whether that simplification preserves the feature relevant to the downstream task: overlap, a silhouette comparison, image classification or a mass estimate. A descriptor that is convenient for classification need not preserve mechanical loading or light interception.

## A decision process extracted from the comparison

1. **Map questions to endpoints.** List the required descriptive, explanatory and predictive claims separately. For each, identify a measurable output and the evidence needed to support it.
2. **Choose a shared representation.** Define geometry, units, coordinate conventions and environmental inputs once. Record which real objects the representation excludes.
3. **Build the smallest controlled baseline.** For a shape comparison, hold leaf area, count, arrangement and environmental conditions fixed. For a mass estimate, start with a clearly calibrated volume-density or allometric baseline.
4. **Justify each added mechanism.** Explain which missing effect it represents and what observation or decision it can change. Do not add a physiological equation if its parameters cannot be estimated within the task.
5. **Verify interfaces before fitting.** Check area versus length normalization, azimuth versus altitude, union versus sum of projected areas, carbon versus CO2, and rates versus stocks. These recurring issues can invalidate a chain despite plausible individual modules.
6. **Validate at multiple levels.** Test exact geometry cases first, approximation error second, and the final endpoint against independent measurements third. Do not substitute an upstream check for downstream validation.
7. **Compare operational alternatives.** Report error distributions, uncertainty and measurement burden. A single reliable diameter may be preferable to many poorly estimated crown or physiology parameters.
8. **Preserve conditions in the conclusion.** Light-limited growth, selected species, a particular branch arrangement and a small calibration sample must survive into the abstract and stakeholder letter.

## How to justify the chosen approach

A defensible justification has four connected parts: the task requires a particular quantity; the chosen mechanism or statistical relation produces that quantity; its assumptions fit the available evidence; and a simpler competing approach was considered. For example, fixed-area rhombi can isolate narrowness effects on overlap, but cannot by themselves explain why a real species evolved its observed leaf. A trunk-diameter estimator can provide a practical mass prediction, but its accuracy depends on calibration species and diameter range rather than the biological plausibility of a quadratic alone.

The papers repeatedly demonstrate the need to separate **a mechanism hypothesis, a model implication and an empirical observation**. A simulated preferred leaf shape is a model implication. Agreement with a few selected real shapes is limited observational support. A universal evolutionary claim would require much stronger evidence and alternative explanations.

## Concrete controls for agent roles

| Role | Required artifact | Check prompted by these papers |
|---|---|---|
| coordinator | Question-to-endpoint matrix and validation assignments | Separate shape description, overlap, branching association and leaf-mass prediction; assign an evidence contract to each |
| domain-data | Parameter provenance and calibration table | Identify borrowed coefficients, reused datasets, unavailable inputs and unsupported conversions |
| modeler | Component and interface specification | Define which outputs are shared, their units, and which modules are explanatory versus computable |
| computation | Authoritative functions, boundary fixtures and saved numerical outputs | Ensure plotted surfaces and formulas implement the same relation; check nonnegative exposure, geometry, units and parameter domains |
| independent-reviewer | Claim-to-evidence audit and independent endpoint comparisons | Prevent a training correlation, consistency ratio, plausible picture or crown-area fit from certifying a different endpoint; inspect out-of-sample mass error |
| writer-visuals | Conditional conclusions and reproducible result tables | Keep counterexamples, scope and uncertainty in the final narrative; generate reported numbers and figures from saved outputs |

These controls are review-derived recommendations. They do not claim that any one source paper implemented the complete workflow or that these four papers establish universal contest-winning practices.
