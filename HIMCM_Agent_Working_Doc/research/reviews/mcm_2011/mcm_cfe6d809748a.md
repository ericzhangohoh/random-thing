# Full review: 2011 MCM A, Team 11199 — Designing the Optimal Snowboard Half-Pipe

- Source ID: `mcm_cfe6d809748a`
- Source: `MCM-ICM-master/2011美赛特等奖/A-11199-Outstanding.pdf`
- Problem context: the contemporary COMAP press release in `MCM-ICM-master/2011美赛特等奖/Results/2011-Problem-A.pdf` independently confirms the vertical-air, twist and practical-tradeoff tasks. Despite its filename, that file is a results press release, not the complete original problem statement.
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–21, including the references and all endnotes.
- Visual supplement: physical pages 2–3, 5–15 and 17–18 inspected. These recover geometry diagrams, image-heavy derivations, simulation curves, comparison tables and the rotation argument.
- Numeric reproduction: **NOT_REPRODUCED**. No original simulation was rerun. The limiting-case checks below are static mathematical inspection, not numerical reproduction.
- Award provenance: source filename says Outstanding. The press release confirms eight Outstanding papers overall but the team-specific designation was not independently cross-checked.
- Page convention: physical PDF pages; this paper's printed numbers agree with them.

## Strongest reusable architecture

The valuable architecture is **a frictionless benchmark that exposes a degenerate objective → a secondary time objective → restoration of friction through a common energy equation → controlled comparisons of geometric families → continuous parameter and friction sweeps → a rotation extension that reveals competing objectives**. The sequence explains why each model is introduced; it is more instructive than treating the final recommended profile as a universal answer.

The original decision concerns a course shape that gives a skilled snowboarder more vertical air, possibly more twist, while remaining practical. The paper begins by connecting judged performance to total air time and average degree of rotation through cited sports research, then records historical course dimensions and industry construction practice (pp.2–3). It fixes deck design because its principal role is safety, concentrating analytical effort on the transition and bottom.

1. With friction absent and equal coping heights, conservation of energy makes exit speed independent of the intervening profile. This is a useful negative result: the simplified model cannot discriminate among shapes for the primary objective (pp.4–5).
2. The authors then introduce minimum crossing time as an entertainment objective and obtain a cycloid from a brachistochrone calculation (pp.5–6). This is explicitly a change of objective, not proof that the cycloid maximizes vertical air.
3. A common energy balance adds Coulomb friction. Local normal force includes curvature-dependent centripetal acceleration. In squared-speed form, the loss separates into a horizontal-width term and an integral involving curvature and speed (pp.7–8). Shape can now affect the primary objective.
4. Semicircular, cycloidal and flat-bottomed oval profiles are passed through the same governing relationship (pp.9–11). Comparisons first fix width, then fix arc length, which tests whether the apparent advantage merely follows from shorter travel distance (pp.11–12).
5. Width, flat-bottom fraction and friction sweeps refine the candidate comparison (pp.13–15). The paper then adds a flight/rotation argument and pumping discussion, exposing a conflict between conserving speed and providing space/time for rotation and landing (pp.17–19).

## Why these approaches fit, and where the justification stops

**Explicit author reasoning:** conservation provides the natural starting point; friction is needed because the frictionless model gives identical exit energy; common arc-length and curvature notation makes different shapes comparable; numerical simulation is adopted when competing curvature and arc-length effects prevent an obvious analytic winner (pp.4–10). The candidate set includes a simple constant-curvature benchmark, the earlier frictionless-time optimum, and a flexible family with separately adjustable straight and curved sections.

**Reviewer interpretation:** the best modeling lesson is to first ask whether an objective is identifiable within the simplified representation. If the answer is no, add the mechanism that makes the design matter. The fixed-width/fixed-arc-length comparison is especially valuable because it checks a plausible explanation for the first result rather than merely generating more examples.

However, superiority among these candidate families is not global optimality over all physically feasible profiles. The mathematical limit of a nearly horizontal bottom joined to infinitesimal-radius curves is not automatically a buildable or safe course (p.15). A future model should express allowable curvature, normal acceleration, height and construction constraints before treating the optimum as a design recommendation.

## Inputs, assumptions and cross-module handoffs

The initial hypotheses include symmetry, a point-mass rider, equal coping heights, fixed entry speed, Coulomb friction and smooth-enough geometry (p.4). Historical dimensions and friction ranges inform scenarios rather than a fitted trajectory model (pp.3,10). The principal numerical comparison uses 18 m width, coefficient 0.05 and entry speed 20 m/s (pp.10–11).

The common handoff is **profile → arc-length position and curvature → speed trajectory → exit speed → vertical height or flight time**. For example, the fixed-width table reports exit speeds of 15.7 m/s for the semicircle, 14.0 for the cycloid, 16.5 for the 15 m flat bottom and 16.0 for the 5 m flat bottom (p.11). These are author-reported values, not independently recomputed results. Fixing arc length instead preserves the broad family ordering while changing the widths and speeds (p.12).

The rotation extension assumes comparable rider ability and roughly fixed rotation period, so more flight time means more rotations (pp.17–18). Pumping and landing below the coping introduce a different geometric benefit from a deeper transition. This creates a genuine interface issue: the no-pumping speed model and the pumping/landing interpretation do not constitute one fully calibrated biomechanical model. The paper ends with a qualitative tradeoff, not a numerically weighted multiobjective optimum (p.19).

## Validation actually present

The energy formulation includes a straight-track special case: zero curvature eliminates the curvature loss term, leaving the expected width-dependent friction loss (p.8). Mass cancels, as expected under the selected friction and gravity representation. The authors compare curves under two separate common constraints and sweep width, flat-bottom fraction and friction (pp.11–15). They acknowledge a small simulation bump associated with 0.01 m discretization and say smaller steps give similar results, but do not provide a convergence table or error bound (p.13).

The paper's two Olympic-rider images illustrate differences in rotation and score (p.18); they do not isolate a causal effect of course geometry. No independent measured trajectory, external held-out comparison or experimental calibration validates the complete profile-to-performance chain. The stated stability of family rankings across friction scenarios is conditional robustness, not external validation.

## Bounded independent checks and limitations

The paper usefully acknowledges omitted air drag, longitudinal motion, wear and rider launch behavior (pp.15–17). Its attempt to subsume drag by changing a friction coefficient because one friction contribution also contains squared speed is an approximation, not equivalence of force direction or dependence on normal load.

A decisive static check is available for the printed launch-angle correction on p.17: it multiplies the unadjusted height by `(1 − cos φ)^2`, where φ denotes deviation from a vertical launch. At zero deviation it gives zero height rather than recovering the unadjusted formula. Therefore that equation, and the associated small-loss claim, should not be reused without rederivation. A second visible transcription issue is the cycloid ordinate on p.6, printed with `θ − cos θ` rather than the conventional `1 − cos θ`; the subsequent geometry must be checked independently before implementation. These defects do not erase the useful hierarchy of models; they explain why architecture extraction and equation verification are separate jobs.

More broadly, safety and practicality are largely discussed rather than imposed as bounds. The point-mass assumption is also least adequate precisely where rider rotation and pumping become central. The workflow should return to the assumptions and model interface when the question changes, instead of automatically carrying the original simplification forward.

## Communication and transferable workflow rules

The shape diagrams, common speed-trajectory plots and paired constraint tables make model comparisons inspectable (pp.5,9–15). The reader sees why an initially appealing analytic shape loses its advantage after the objective and mechanism change. That explanatory structure is worth emulating.

- Start with a conservation or limiting-case baseline; record what it can and cannot distinguish.
- Declare an objective change explicitly. A minimum-time solution is not automatically a maximum-height solution.
- Use one governing evaluator for competing designs, and explain the physical reason each candidate belongs in the comparison.
- Test an explanation for a ranking by controlling a different relevant quantity, as the width/arc-length comparisons do here.
- Separate ranking stability within a model from measured validation of the model.
- When a new subquestion introduces pumping, rotation or other mechanisms, reopen assumptions and interfaces.
- Turn mathematical boundary optima into constrained practical designs before recommending dimensions.

## Reading ledger

Text read in full: pp.1–10 and 11–21, including all references and endnotes. Relevant visuals inspected: pp.2–3,5–15,17–18. Contemporary problem summary checked in the collection's COMAP press release; the full original statement was not independently read. No simulation, trajectory fit or construction design was reproduced.
