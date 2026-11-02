# Full review: 2011 MCM A, Team 12149 — Designing a Halfpipe for Advanced Snurfers

- Source ID: `mcm_cb2b7105a6f3`
- Source: `MCM-ICM-master/2011美赛特等奖/A-12149-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–24, including complete printed code, figure appendices and references.
- Visual supplement: physical pages 4–12, 14 and 17–23 inspected to recover force diagrams, trajectories, code details and image-only velocity tables.
- Numeric reproduction: **NOT_REPRODUCED**. Printed code was read but not compiled or executed; reported error and trajectories were not independently reproduced.
- Award provenance: filename labels Outstanding; team-specific award not independently verified.
- Page convention: physical PDF pages, one greater than the printed body-page number. The cover is physical p.1.

## Strongest reusable architecture

This paper develops **conservation-of-energy intuition → a two-dimensional force model → a three-dimensional extension → a common shape/slope experiment → a practical recommendation**, then checks whether the more elaborate model reduces to the simpler one under suitable limits. Its strongest transferable contribution is the combination of a model hierarchy with explicit reduction tests (pp.3–8,14–15).

The three levels have different jobs. The energy model establishes that, without added work, a rider cannot exceed the original height and that the launch direction matters (pp.3–5). The two-dimensional model introduces curvature, normal force, snow friction, air drag and a simplified pumping force, allowing cross-sectional shapes to be evaluated through velocity at the lip (pp.5–7). The three-dimensional model rotates the coordinate frame to account for downhill slope and adds the longitudinal velocity component (pp.7–8).

The candidates share initial edge position and total width, while their depth differs: `z(y)=0.07y²−7`, `z(y)=0.1y²−10` and a semicircular profile (p.9). Reported simulations compare these profiles and mountain slopes of 25°,35° and45°, with different cycles shown in the appendix (p.22). The authors recommend the shallower parabola at45° for the largest modeled vertical velocity and at25° for a practical course, where repeat crossings and rider control matter (pp.12–13).

## Approach selection and its justification

**Author reasoning:** the energy model is analytically transparent but cannot represent friction or select a complete geometry; Newton's law admits those mechanisms; numerical Runge–Kutta integration then computes the trajectory for an editable shape function; adding the downhill dimension addresses a specific omitted energy source (pp.3–8). This is a good example of increasing model detail because an unanswered decision requires it, rather than because a complicated algorithm sounds impressive.

**Reviewer interpretation:** separating the shape function from the force evaluator is an effective modular interface. The same evaluator can compare candidate geometries without rewriting the whole conceptual model. However, all candidates being easy to substitute does not prove the evaluator is physically correct, and three sampled slopes do not establish a continuous global optimum.

The recommendation of25° includes qualitative judgment about a snowboarder's ability to redirect downhill velocity through carving and other techniques (p.13). Those techniques are explicitly omitted from the simulation (pp.8–9). The practical recommendation is therefore a model-informed judgment with unmodeled behavior, not a fully optimized rider-control solution. Likewise, the original twist/stunt objective is discussed through trajectory and practical use; the paper does not construct a separate angular-momentum or rotation model.

## Assumptions, inputs and module handoffs

The model uses a prescribed constant pumping force in the travel direction, with pumping restricted to the cross-sectional plane in3D. Active steering is absent, and no explicit airborne projectile motion is simulated after leaving the halfpipe (pp.8–9). The printed code gives, among other parameters, mass75, friction coefficient0.04, air density1.225, frontal area0.87 and drag coefficient0.7 (p.17). These are visible computational choices; the paper does not document a separate empirical calibration for every one.

The intended handoff is **shape and mountain slope → local geometry and force components → integrated position/velocity → lip velocity → inferred vertical-air ranking → practical course judgment**. Frame definitions matter: after rotating the axes, a velocity in the model's z direction must be related consistently to the requested physical vertical height. The paper's prose sometimes uses velocity, vertical air and combined y/z velocity interchangeably. A reusable implementation needs a precise output definition and an explicit coordinate transformation.

The image-only appendix is essential evidence. It separates first and subsequent cycles; for the shallow parabola at45°, the first listed z velocity is3.034146m/s and the second is4.231989m/s (p.22). The main table uses approximately4.232m/s (p.12), while the abbreviated appendix table uses3.034m/s (p.23). These are different cycles, so the apparent discrepancy can be explained by reading the full appendix. Each result table should carry the cycle/event identifier rather than expecting the reader to infer it.

## Validation actually present

The authors physically built a paper halfpipe and rolled a marble through it, reporting qualitative agreement with their simulated path (pp.13–14). This is a useful independent representation for gross trajectory checking. It does not directly validate snowboard friction, pumping, rider control or a quantitative vertical-air prediction: no measured coordinates, scale analysis or residuals are reported.

Their internal tests are unusually explicit (pp.14–15): remove friction and drag to recover undamped oscillation; remove pumping with dissipation present to obtain decay; set mountain slope to zero so the3D model agrees with the2D model; and compare the complete model with a simpler case. These are valuable metamorphic and model-reduction tests. The paper reports a0.1% Runge–Kutta position error at a time step of0.00001s over30s, but gives no reference solution or convergence table that would independently substantiate that percentage (pp.15–16).

## Bounded static audit

The main3D table ranks the shallow parabola above the deeper parabola in z velocity, yet the bullet immediately below says Parabola2 is44% better than Parabola1 (p.12). The table and final recommendation support the opposite ordering. This is a concrete example of why tables, percentages and concluding prose need a shared result source.

The printed appendix also requires repair before reuse. Its C++ uses integer expressions such as `(1/4)` in the position definition, and the shown `main` initializes y[0] through y[3] but does not visibly initialize y[4] and y[5] before using them in the loop/printing (pp.19–20). The geometry branches contain a second `if` that overrides the first branch's second derivative and an `else` that assigns `dzdy` twice (pp.17–18). These are static observations about the submitted listing, not a claim that this exact listing produced every published plot. It may differ from the actual computational version. Accordingly, the0.1% claim cannot substitute for matching a frozen code version to its run outputs.

The energy equation on p.4 adds `2W` to a squared-speed expression although W was just defined as force times distance; without defining W per unit mass, this is dimensionally inconsistent. Such normalization needs to be resolved before translating equations into code.

## Transferable workflow rules and communication

The repeated “how it works / consequences / strengths / weaknesses” presentation makes the escalation between models legible. Force diagrams support the coordinate definitions, while the marble demonstration gives a concrete independent plausibility check. The useful lessons are:

- Give each model level a distinct purpose and a clear reason for adding the next mechanism.
- Make the higher-dimensional model recover the simpler one when the added parameter is zero.
- Compare shapes through one evaluator, while recording all quantities that differ between candidates.
- Treat event number, coordinate frame and launch condition as part of every result's identity.
- Separate qualitative physical plausibility, numerical integration error and real-world predictive accuracy.
- Archive the actual executable code and input configuration that produced a figure; a printed appendix alone may contain transcription defects.
- Mark practical recommendations that depend on unmodeled rider choices as judgments, and specify the additional model or measurement needed to strengthen them.

## Reading ledger

All text read: pp.1–8,9–16,17–24. Relevant visuals: pp.4–12,14,17–23. Complete code listing and references read; no program execution or numerical reproduction performed. Problem coverage assessed against the paper and the contemporary COMAP task summary, not a newly retrieved complete original statement.
