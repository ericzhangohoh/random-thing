# Full review: 2011 MCM A, Team 9582 — A half-blood half-pipe, a perfect performance

- Source ID: `mcm_99696cfc5bec`
- Source: `MCM-ICM-master/2011美赛特等奖/A-9582-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–34, including the full optimization discussion and references.
- Visual supplement: physical pages 2,4–15,17–19 and21–33 inspected for coordinate frames, equations, rotation sketches, dependency diagrams, validation tables, parameter sweeps and fitted optimal curves.
- Numeric reproduction: **NOT_REPRODUCED**. No numerical integrator, genetic algorithm or fitted ellipse was independently run.
- Award provenance: filename labels Outstanding; team-specific designation not independently verified.
- Page convention: physical and printed page numbers agree.

## Strongest reusable architecture

The strongest feature is the explicit connection of **course geometry and athlete path → on-snow energy loss and pumping → airborne trajectory → airtime and angular momentum → competing performance objectives → a combined score → repeated-cycle practicality**. The complete dependency diagram on p.19 makes the shared variables and behavioral choices visible. This is a genuinely connected multi-question architecture, rather than a separate algorithm for each question.

The paper first distinguishes a cycle's on-snow and airborne phases (pp.3–6). Course cross-section is represented by y(x), while z(x) represents the athlete's chosen downhill path (p.4). An energy-loss equation includes friction proportional to normal force and quadratic air drag, with curvature affecting the normal force (pp.6–8). Work from standing up near the lip changes launch energy. Projectile motion then supplies height, flight time and downhill flight distance (pp.8–10).

Rotation is decomposed into components the course can influence and components mainly created by the athlete. A rod approximation links curvature and speed near launch to an angular-momentum component; airtime then converts angular velocity to total rotation (pp.10–13,29). Athlete extensions consider redirecting velocity, changing moment of inertia and landing below the coping (pp.16–18).

The geometry evaluator is reused with different objectives: vertical air, flight duration, initial angular momentum, total rotation and finally a score combining airtime with rotation (pp.19–31). The final practicality analysis asks whether a locally attractive jump leaves enough energy and course length for the rest of the run (pp.32–33).

## Why the approaches fit

**Author reasoning:** energy loss is an efficient state variable when exit speed matters more than every detail of the on-snow trajectory (p.5). Conservation of angular momentum motivates focusing on launch conditions for the course's effect on rotation (pp.6,10). Numerical methods are chosen because the loss expression depends on unknown shape and path functions and an analytic functional optimization is difficult (p.8). A genetic algorithm searches convex, smooth transition curves whose control points encode the geometry (pp.23–25).

**Reviewer interpretation:** separating controllable infrastructure from athlete behavior prevents course design from receiving credit for every performance change. Reusing one physical evaluator with multiple objective functions also clarifies whether an apparent disagreement is about physics or about what “best” means. The combined scoring function offers an interpretable tradeoff grounded in cited sports-performance research, instead of arbitrary equal weights.

Those strengths have limits. The authors call several results “global” optima, but bounded enumeration and a genetic algorithm do not provide a global optimality certificate. The paper specifies selection, crossover and mutation conceptually, yet does not report enough run configuration, seeds, repeated-run variability or convergence evidence to establish search reliability (pp.24–26). The safe transferable claim is best found within the stated representation and search.

## Inputs, decisions and outputs

Reference values are friction coefficient approximately0.03, drag coefficient0.15kg/m, rider mass60kg and initial energy7000J (pp.13–15). Standards inform width, height, flat length and slope. The path is simplified using projected arc length, approximately z=kτ(x), with launch location controlling the downhill component (p.14). Geometry is assumed smooth and convex, while construction feasibility is intentionally deferred (p.3).

The main parameter enumeration spans widths13–18m, heights2–6m, flats4–6m, downhill launch locations0–15m and slopes15–20°. For the basic vertical-air objective, it reports width18m, height3m, flat4m, launch location6m and slope20° (p.23). A separate airtime search reports18m,5m,6m,4m,20° and2.749s (p.28). Other shape searches hold width/height/slope at standard values, so these results should not be blended into a single jointly optimized design.

The genetic search generates convex profiles by increasing sampled slopes, normalizing them to meet endpoint height, and fitting smooth curves through control points (pp.24–25). Resulting profiles resemble ellipse segments, with different vertical/flat portions under different objectives (pp.25–30). The hybrid score uses `11.424 × AAT + 0.013 × ADR − 2.223`, attributed to earlier automated-scoring research, and produces a profile fitted by two ellipse segments (pp.30–31). The cited model's applicability and units require checking before transfer to another sport, judge population or competition era.

## Cross-module reasoning worth preserving

The paper recognizes that total kinetic energy and useful vertical velocity need not rank designs identically. A flatter section may lower exit energy while directing more of the motion into the component relevant to vertical air (p.22). Likewise, a steeper chosen path can increase speed yet send the athlete farther down the course, reducing opportunities for later tricks (pp.16–17,23). This is an important distinction between a proxy and the actual task objective.

The final energy of one cycle is intended to become the next cycle's initial energy, and flight distance contributes to the number of tricks possible within a finite run (pp.10,32–33). These are the right interfaces to inspect before recommending a design. The paper mainly presents these repeated-cycle considerations as practical tradeoffs, not as a fully validated optimization of an entire run under athlete-control constraints.

## Validation actually present

A table compares analytic and numerical projectile calculations with the same launch speed and reports relative height differences of approximately0.084% without airborne friction and0.083% with it (p.15). Flight distance and duration are also compared for the simpler case. This is an implementation cross-check under a shared model, not independent validation of all physical assumptions.

The authors perturb four geometric/path inputs by±10% and report vertical-air response; launch location changes height by about8%, width by about6%, depth by about2.5% and flat length by less than1% around the reference point (p.16). These are local sensitivities. Calling the simulation “robust” requires stating robust with respect to which decision and acceptable tolerance; small input response does not establish numerical correctness.

A predicted height around7m is compared with an elite athlete's best performance and typical competition ranges (p.16). This is broad plausibility evidence, not a matched measured run. The reported hybrid score above46 is computed by the objective that was optimized, so it does not independently validate the scoring criterion (p.31).

## Bounded static audit

The cycle-energy bookkeeping needs correction before reuse. On p.10, the paper defines positive downhill potential-energy release and positive athlete work, but its equation for final cycle energy subtracts both. Earlier launch-energy equations add downhill gain and athlete work (p.8). An energy ledger with a fixed reference level and signed inflows/outflows is necessary to resolve this inconsistency. This review does not establish which sign convention the original code used.

The airborne drag derivation on p.9 also simplifies the y projection of a quadratic vector drag to a term depending only on squared y velocity. In general the component is proportional to total speed times the y component; a nonzero downhill component prevents that simplification. Agreement between two implementations of the simplified expression would not validate the physical projection.

The positive design conclusions remain conditional on simplified pumping, fixed/controlled posture, trajectory assumptions and omitted board/snow mechanics. Curvature safety is discussed only after optimization (p.32), so an optimum favoring very small radius may exploit an unbounded assumption. The task workflow should bring such constraints into the evaluator before accepting a final design.

## Communication and transferable workflow rules

The paper's overview and complete dependency maps are valuable: they distinguish geometry, path choice, energy, airtime, angular momentum and practicality rather than hiding all of them inside an algorithm label (pp.5,19). Paired plots often reveal that a performance measure and its proxy move differently. The question/answer/analysis structure makes the response to each task visible.

- Separate environmental design variables from agent behavior and state how they interact.
- Build a shared evaluator before comparing different objective functions.
- Validate a numerical submodule against an analytic case, while labeling the scope of that check.
- Check whether an energy proxy preserves the ranking of the actual directional performance measure.
- Give every search a declared feasible domain, stochastic configuration and best-found status.
- Justify multiobjective weights or scores with evidence, then test sensitivity to their uncertainty.
- Carry end-state energy and consumed distance into the next cycle; avoid optimizing one spectacular event at the expense of completing the task.
- Put curvature, safety and construction limits into the feasible set rather than relying only on a closing discussion.

## Reading ledger

All text read: pp.1–8,9–16,17–24,25–34. Relevant visuals inspected: pp.2,4–15,17–19,21–33. The references and all optimization/practicality sections were read. Numerical reproduction, independent score-model validation and global-optimality verification were not performed.
