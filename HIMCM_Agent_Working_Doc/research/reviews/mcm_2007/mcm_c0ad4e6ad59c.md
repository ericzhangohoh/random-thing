# Full review: 2007 MCM A, Team 1035 — Getting the Votes to Count

- Source ID: `mcm_c0ad4e6ad59c`
- Source: `MCM-ICM-master/2007美赛特等奖/其他奖项/A-1035-Honorable.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, all **15 physical pages**, including both appendices and references. Physical and printed page numbers coincide.
- Visual supplement: pp.4–6, 8–11 and 13–14; source maps, gridded density, every output map, probability formulas and satellite comparison inspected. The p.9 output was also inspected at full-page scale.
- Numeric reproduction: **NOT_REPRODUCED**. No code or machine-readable population grid is supplied in this PDF.
- Award provenance: cover explicitly says 2007 Honorable Mention; filename agrees. This paper must not be relabeled Outstanding because of its parent folder.
- Prompt qualification: author interpretation read; separate official prompt not reviewed. Historical legal and political statements are not current guidance.

## Architecture and strongest lessons

The architecture is **define requirements → discretize density → grow competing regions → use local reassignment probabilities → repair disconnected pieces → inspect population and shape outcomes**. The authors explicitly separate the political choice of a good district from the computational mechanism that implements a chosen preference (pp.2–3). This is a useful boundary: a flexible algorithm does not decide which fairness conception is legitimate.

The most valuable result is their candid report that the implementation misses its own population target. A stated statewide range-variance goal of 0.7% becomes observed differences of approximately 3.3% to 4% (pp.8–9). The paper therefore offers a prototype with diagnosed limitations, not a feasible final districting solution. Preserving that distinction is a stronger learning outcome than praising the named algorithm.

## Representation and selection rationale

Population is represented on a 67-by-46 grid, estimated by hand from color-coded density maps (pp.4–5). New York City receives a separate finer-scale treatment, with 13 districts allocated there and 16 elsewhere based on the authors' census interpretation (p.7). This is a response to heterogeneous density, but the boundary and cross-region population accounting require verification if the two solutions are to form one valid statewide partition.

Districts start at randomly selected cells and acquire adjacent unassigned cells. Later cell transfers depend on population imbalance and the change in the number of interior cells. Interior cells have no north, south, east or west neighbor in another district, making the shape preference operationally explicit (pp.3–5).

The authors call the procedure a genetic algorithm. The actual description is a stochastic local growth-and-reassignment process; it does not specify a population of complete candidate partitions, crossover or conventional evolutionary selection. The transferable object is its transition mechanism rather than the label.

They compare the idea conceptually with recursive split-line districting and prefer adjustable criteria (pp.6–7). That is a reason to seek a modular objective, but it is not proof that deterministic algorithms are inherently inflexible. A deterministic search can also optimize different objectives. The report does not implement the competing method on the same data and metrics.

## Validation actually supplied

The paper compares population-only transfers with transfers also favoring interior cells. The maps visibly become more regular (pp.9–11). This is an interpretable component ablation: it shows the consequence of adding the shape preference. However, the report supplies no numerical interior-cell metric, repeated-run distribution, independent compactness measure or seed record. Two representative realizations establish illustrative behavior rather than reliable typical performance.

The manually constructed density raster is visually compared with satellite imagery (p.14). This can identify major geographic mistakes, but a satellite image does not independently validate population counts. The raw mapping from color classes to cell population, scale conversion and aggregate census reconciliation remain necessary.

Reported runtime is about 40 seconds with graphical delays, with an estimated 15 seconds without them (p.12). The estimate is not a measured benchmark. The suggested 200-by-200 grid and expected achievement of the 0.7% target are proposed improvements, not tested results.

## Feasibility and transition details

Several specification issues limit direct reuse:

1. **Local stopping is not a global constraint.** Transfers stop when a neighboring pair's relative imbalance becomes small. A chain of locally similar districts can still have a much larger statewide maximum-minus-minimum difference. The authors recognize this explicitly (pp.5–6). A final global check is indispensable even after every local rule passes.
2. **Shape preference does not enforce connectivity.** Disconnected components are manually reassigned and the simulation restarted (p.6). A repair may change population balance and new transfers may recreate disconnection. The final artifact needs both invariants checked together, with a defined repair/termination policy.
3. **Probability domains are incomplete.** The first formula contains the square root of a signed population difference. It needs an explicit branch when the proposed direction has a negative numerator. The second formula multiplies by a shape factor and gives no stated upper bound of one. Clamping negative final values alone does not resolve an undefined square root or an excessive probability (pp.13–14).
4. **The stated cutoff changes with the shape factor.** The population-only formula has the described 0.01 imbalance cutoff. Once the interior-cell factor is introduced, that same cutoff no longer follows unless enforced separately. A prose threshold and the actual transition formula must agree.
5. **Update ordering is part of the model.** The authors note that an early changed cell can propagate its region through later cells in the same sweep, causing directional cascades (p.12). Their proposed one-ring-per-iteration alternative is not tested. A synchronous-versus-asynchronous choice should be specified before interpreting the resulting shapes.

The algorithm description also alternates labels for the donor and recipient region. An executable specification should use one direction convention and tiny two-region tests. None of these static observations establishes which behavior an unavailable program actually used.

## Decision and communication implications

The authors openly identify subjective tuning of the 0.3 shape coefficient and the danger of claiming neutrality merely because a computer performs the transfers (pp.7, 12–14). They also distinguish implemented criteria from proposed extensions such as county boundaries or demographics. These are useful habits for an agent workflow: surface value choices and keep untested capability separate from demonstrated behavior.

For HiMCM, transfer the explicit baseline-versus-extension comparison, spatial refinement motivated by density, and honest failure against a declared criterion. Add a requirement that grid resolution be justified by the precision demanded by the task, that local moves preserve or recheck hard constraints, and that any proposed finer discretization be tested before the final recommendation claims feasibility.

## Physical-page reading ledger

- pp.1–3: cover, Honorable Mention provenance, abstract, introduction, political-versus-mathematical boundary, population target and shape requirements.
- pp.4–7: all input construction, initialization, transition, stopping, manual repair, alternative-method discussion and separate-city design.
- pp.8–11: density maps, population-only map, both state/city weighted-map examples and all accompanying result claims.
- pp.12–15: limitations, runtime claims, proposed refinements, extension ideas, both probability equations, satellite comparison and references.

All available text and relevant visual material were examined; no numerical reconstruction was executed.
