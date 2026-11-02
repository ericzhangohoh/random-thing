# Full review: 2011 MCM B, Team 9440 — Iterative Extremal Optimization Based on Voronoi Diagrams

- Source ID: `mcm_95f0fa406fe8`
- Source: `MCM-ICM-master/2011美赛特等奖/B-9440-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–41, including the scanned summary sheet, all coordinate/frequency tables, parameter and assumption appendices, and references.
- Visual supplement: physical pages 1,10–12,14–26,33–36,40 inspected for the summary, physical formulas, geometric constructions, algorithm diagrams, claimed optimality proof, sensitivity curves and terrain proposal.
- Numeric reproduction: **NOT_REPRODUCED**. No placement search, capacity estimate, geometric feasibility certificate or reachability simulation was independently executed.
- Award provenance: filename labels Outstanding; team-specific designation not independently verified.
- Page convention: physical page 1 is a scanned summary sheet; printed pages 1–40 correspond to physical pages 2–41. All references below use physical pages.

## Strongest reusable architecture

The paper develops a particularly explicit chain from requirements to optimization: **define weak and strong communication requirements → estimate physical range and capacity → replace mobile discrete users by a continuous density → derive geometric and capacity lower bounds → construct a regular-cell baseline → refine sites through Voronoi cells and minimum enclosing circles → escape local stagnation → assign frequencies and tones → evaluate residual reachability → examine bottleneck changes and density fluctuations**.

The important structural distinction is between every user reaching some repeater and every user reaching every possible destination. The authors formalize capacity, interference avoidance, local coverage and global reachability as separate constraints (pp.5–8). They also identify a simplifying regime: when repeater range exceeds the region's diameter, local coverage implies global reachability under their other assumptions. This regime argument explains why the geometric module can sometimes solve the full abstraction and why a second communication module becomes necessary when range decreases.

## Approach justification

**Explicit author reasoning:** a uniform continuous population avoids tailoring installations to one transient sample of mobile users; nearest-repeater association naturally creates Voronoi service areas. Each cell's area determines its demand, while its smallest enclosing circle determines the required user transmission range (pp.6,12–13,20–21). A hexagonal cellular layout supplies an interpretable analytical benchmark. Relocating sites toward enclosing-circle centers improves geometric coverage, while moving the least-contributing site randomly is intended to escape a local optimum without immediately buying another repeater (pp.14–21).

**Reviewer interpretation:** the model translates two different operational constraints into two measurable properties of the same partition: area for load and covering radius for access. This is a useful approach for facility, sensor and service-zone problems. The architecture also distinguishes a physical model, a feasibility model and a search procedure; success in the search procedure cannot repair an unsupported physical premise.

The algorithm starts at a lower bound on equipment count, iterates until movement is small, checks both capacity and range, makes up to 100 extremal relocations if necessary, and only then increases equipment count and restarts. The convergence threshold is 0.01 miles (pp.20–21,39). That gives a concrete staged escalation policy. Exhausting a search budget does not prove infeasibility at the smaller count, so only separately certified cases can be called globally optimal.

## Assumptions, evidence and model interfaces

The circular region has radius 40 miles, available frequencies 145–148 MHz, a 600 kHz receive/transmit offset and 54 tones. The model uses homogeneous users and repeaters, nearest-site association, uniform demand, a distance-only propagation law and simplified tone/frequency interference rules (pp.5–6,40). It treats different tones as avoiding the modeled interference; that is an explicit abstraction requiring independent radio validation before deployment.

A table of Utah repeater powers motivates a nominal 100 W repeater, and a nominal 3.2 W handheld power is taken from several devices (pp.10–11). With the paper's propagation assumptions, these give repeater range 85.45 miles and handheld range 15.28 miles. The capacity derivation borrows from Shannon/CDMA discussions and produces about 119 users per repeater (pp.11–12). These physical quantities govern almost every later result and therefore deserve a higher evidence priority than tuning the optimizer.

Under continuous density rho = N/(pi times 40 squared), each Voronoi cell must satisfy rho times cell area no greater than capacity. Every point of the region must also lie within handheld range of its site (pp.12–13). This establishes a clean computation handoff: a candidate site table becomes clipped service polygons, polygon areas and enclosing radii, then a feasibility report. Frequency and tone assignment is a separate table, not an attribute inferred from a plotted line.

## Baseline, optimization and reported results

The simple layout uses regular hexagonal service cells. Cell size is limited by both handheld range and capacity, and finite-cell constructions yield 12 repeaters for 1,000 users and 108 for 10,000 users (pp.14–18). The improved search reports 11 and 104 respectively (pp.24–26). Detailed tables expose coordinates, receiver/transmitter frequencies and tones for the main solutions (pp.17,25–32), which is much stronger evidence than an isolated placement picture.

For 1,000 users, the reported maximum Voronoi area is 560.56 square miles, corresponding to about 112 users at the chosen density, below the assumed capacity of 119 (p.24). The authors pair the 11-site construction with a cited disk-covering theorem: ten unit disks cover a disk of maximum radius about 2.532, below the required ratio 40/15.28, about 2.618 (p.25). This is a valuable proof pattern: **a feasible construction plus an impossibility result for one fewer resource establishes optimality within a specified model**. The theorem's source and the construction's continuous coverage were not independently reproduced here, so the review records the paper's conditional proof rather than certifying the real radio system.

When repeater range is reduced to 40 miles, the authors hold sites and equipment count fixed and modify only channel/tone assignments. A graph of potentially communicating sites is reduced through minimum- or maximum-spanning-tree routes, with route components assigned tones (pp.22–23). For 100,000 sampled ordered endpoint pairs, they report 90.708% successful reachability with 11 sites and 97.12% with 104 sites (p.29). These are explicitly incomplete global-reachability results. The paper acknowledges that its second algorithm does not guarantee the strong requirement without additional infrastructure (pp.29,37).

## Validation and mechanism-based sensitivity

The sensitivity section identifies a change in the active constraint. At low demand, geographic range controls equipment count; at higher demand, capacity controls it and required equipment grows roughly linearly with population (p.33). Varying handheld range from about 12 to 19 miles changes the low-population result while leaving the high-population result flat over the displayed interval (p.34). That is a useful explanation of *why* sensitivity differs by scenario, rather than a list of parameter perturbations.

The paper also revisits its continuous approximation. Under independent uniform discrete locations, a cell's occupancy has the displayed binomial mass function, mean rho times cell area and corresponding standard deviation. It proposes reserving approximately two standard deviations of capacity, reducing a nominal 119-user capacity to a planning value near 99 (pp.34–35). This is a meaningful bridge from a deterministic approximation to stochastic headroom. It is a per-cell heuristic, not an established simultaneous network-wide overload guarantee; dependence among cell counts and the number of cells matter.

The terrain extension proposes lower-level relays in valleys and higher-level relays on peaks, with frequency reuse where mountains block interference (pp.35–36). It is a conceptual hierarchy illustrated on a landscape image. No terrain dataset, visibility computation, optimized mountain layout or quantitative validation is supplied. The claim of faster performance than earlier algorithms is also not accompanied by a common runtime benchmark or repeated-run convergence table (p.37).

## Bounded independent checks

The capacity derivation contains serious unit/specification inconsistencies. Information bit rate is described as watts/dB, received power as bits per second, and dimensionless linear gain and energy-to-noise ratios are labeled watts (pp.11–12). Equation 9's displayed algebra also does not preserve the preceding bit-rate factor consistently. The transition from a CDMA capacity relation to a single-frequency repeater is asserted without a channelization or decoding model. Consequently the numerical capacity of 119 remains an unvalidated premise; a geometric optimum conditional on it is not a verified physical minimum.

There are smaller specification conflicts worth routing to independent review. Equation 16 uses 118 in the denominator although the capacity is otherwise 119 (p.14). The text calls the cell occupancy law Bernoulli while displaying a binomial distribution (p.34). The route-splitting rule removes edges only at degree greater than three, although its subsequent description assumes separate routes; degree-three branching therefore needs an explicit assignment check (p.23). None of these observations is a numerical rerun.

The claim that intersecting drawing edges in a maximum spanning tree cause broader signal coverage is a heuristic explanation, not a physical proof (p.23). The actual test should use the directed graph created by frequency equality, tone equality and range, then compute reachable destination areas. The paper's own Monte Carlo endpoint evaluation is a better service metric than the visual density of lines.

## Communication and transferable workflow rules

The numbered constraints, parameter appendix, evolving geometric diagrams and full solution tables make the work inspectable. The scanned summary also names the missing global-reachability guarantee, an effective practice for keeping the main claim calibrated.

- Formalize weak and strong interpretations of a requirement and establish when they coincide.
- Link each operational constraint to a measurable property of the shared representation.
- Derive lower bounds and a simple feasible benchmark before heuristic refinement.
- Separate convergence, feasibility, search exhaustion and a proof of optimality.
- Preserve coordinates and assignments so a reviewer can check a proposed design independently.
- Use regime changes in active constraints to explain sensitivity and extrapolation limits.
- Convert deterministic averages into explicit stochastic safety margins, with the probability scope stated.
- Test reachability on the actual directed assignment graph, not only on geometric adjacency.
- Audit the units and source assumptions of parameters that control the entire solution.
- Mark qualitative terrain proposals and unverified physical capacity as conditional components.

## Reading ledger

All extracted text read: pp.2–7,8–14,15–21,22–28,29–35,36–41. The scan-only summary on p.1 was read visually. Relevant visuals inspected: pp.1,10–12,14–26,33–36,40. Every row of both 104-repeater tables was read as published. No numerical reproduction or external theorem verification claimed.
