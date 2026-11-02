# Full review: 2007 MCM A — Applying Voronoi Diagrams to the Redistricting Problem

- Source ID: `mcm_e44ee158eaf8`
- Source: `MCM-ICM-master/2007美赛特等奖/A-1034-Outstanding.pdf`
- Team: 1034.
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, all **21 physical pages**, including the voter bulletin and references.
- Visual supplement: pp.7, 9–10, 12–16 and 19; all eight figures, all district maps and the full population table.
- Numeric reproduction: **NOT_REPRODUCED**. No district-generation algorithm was rerun. A direct addition of the printed population table was performed as a static arithmetic check.
- Award provenance: Outstanding appears in filename and archive cover annotation; not independently verified. The paper carries a May 10, 2007 date; whether this is a revised publication is unverified.
- Prompt qualification: author interpretation read; no independent original prompt reviewed for this record. Historical legal assertions are source claims, not current legal guidance.

## Strongest reusable architecture

The architecture is **normative criteria → representation choice → simple geometric baseline → diagnosed failure → population-aware refinement → geographic implementation → public explanation**. Its strongest learning value is the explicit baseline-to-refinement argument: ordinary Voronoi partitions produce simple shapes but fail population balance, so the authors preserve their useful geometry while modifying growth to account for population (pp.14–17).

The paper also treats representation as a substantive decision. It compares grouping existing counties with constructing boundaries from a continuous population field, and explains why existing divisions may carry inherited biases or constrain feasible balancing (pp.4–5). This is a stronger rationale than selecting Voronoi diagrams just because the problem is spatial.

## Selection, assumptions and module interfaces

The stated requirements are equal population and contiguity, with simplicity and geographic coherence preferred (pp.5–7). The authors review competing compactness definitions and decline to collapse them into an unsupported single score. They use an informal combination of convexity, compactness, connectedness and intuitive boundaries instead (p.7).

Ordinary Voronoi diagrams are attractive because Euclidean cells are convex and nearest-site assignment is simple to explain. Three metrics—Euclidean, Manhattan and maximum-coordinate distance—are compared (pp.7–8, 14–15). The modified “Voronoiesque” construction grows regions so their integrated population is controlled instead of simply advancing equal distances (pp.8–9).

Generator sites are placed near population peaks. Dense cities receive a multiplicity, called degeneracy, representing how many districts they need; their initial regions are then subdivided (pp.9–11, 13). This hierarchical treatment addresses the practical conflict between centering districts on cities and splitting cities whose population exceeds a district's quota.

New York is chosen because concentrated cities, constrained geography and 29 districts exercise several challenges at once (p.10). A 792-by-660 image is converted into a density raster and smoothed with a six-pixel moving average because the authors could not use the census data format directly (p.11). The categorical raster feeds peak selection, city multiplicities and final population integration. Thus its errors affect both the structure of the solution and its reported evaluation.

The final geographic interface is boundary adjustment to streets or existing administrative divisions; obstacle-aware growth and further population balancing are proposed refinements (pp.17–19). They were not implemented in the reported solution.

## Reported results and validation

The authors compare maps produced by the three metrics and then the population-aware variant. The latter has substantially less dispersion in modeled district population, with an abstract/caption claim of an average `(3.34 ± 0.74)%` (pp.1, 16). A district-by-district table permits more informative checking than a single aggregate score (p.14). The paper reports runtime below ten seconds (p.20), without hardware or reproducible code.

They explicitly disclose that the raster caps density at 5,000 people per square mile while New York City's cited average is 26,403 (p.11). They connect that limitation to assigning the city fewer districts than expected (p.14). This is a valuable example of explaining how data quality changes a decision rather than merely listing it as a generic limitation.

There is no evaluation against high-resolution census counts, spatial conservation audit, resolution/smoothing sensitivity, seed-placement perturbation, completed geographic snapping test, numerical compactness comparison or independent connectivity audit. No code is included. Claims about avoiding political manipulation are not tested against alternative seed choices, city multiplicities, boundary changes or electoral outcomes.

## Static checks and limits

- **Averages are not balance checks:** if a complete partition assigns all population to 29 districts, the mean share is necessarily `100/29`, irrespective of how unequal the districts are. A mean near 3.45% is not evidence of equal representation. The largest deviation, minimum/maximum share and explicit tolerance matter.
- **Printed-table consistency:** adding the 29 displayed percentages gives **98.85%**, with a mean of approximately **3.409%**, rather than the printed mean of 3.34% (p.14 versus pp.1, 16). Rounding to two decimal places cannot explain a 1.15 percentage-point shortfall across 29 entries. This is a static table check, not evidence about how the unavailable code behaved.
- **Declared requirement remains unmet:** displayed shares range from 2.12% to 6.15% (p.14), far from the 3.45% target and the paper's own rough 5% relative tolerance discussion (p.6). Lower variation than the baseline does not establish feasibility. The conclusion that the goal was satisfied is stronger than the table supports.
- **Statistic identity:** the analysis calls the change from `±2.8%` to `±0.7%` a fourfold reduction in variance (p.17). These displayed dispersions appear to be standard-deviation-like quantities; variance would scale quadratically. The statistic and comparison dataset need explicit definitions, particularly since the metric captions show somewhat different values.
- **Data conservation and domain:** smoothing a capped categorical raster can alter density peaks and move mass across state or coastline boundaries unless the mask and renormalization are handled explicitly. No population-total or masked-boundary check is reported. Better density data would plausibly help, but the exact corrected district allocation is not established without rerunning the process.
- **Inherited geometry guarantees:** convex Voronoi cells in the full plane do not guarantee connected or convex districts after intersection with a nonconvex state or islands. The paper itself identifies this concern (p.18). Modified growth, hierarchical subdivision and obstacle handling require their own connectivity arguments.
- **Growth specification:** equal population at every growth iteration is proposed, but collision handling, blocked growth, finite-grid tie breaking and stopping rules are not fully specified (pp.8–10). The theoretical equality condition cannot substitute for checking the final discrete output. Uniform density also does not by itself guarantee the claimed equivalence to ordinary Voronoi growth once boundary clipping and unequal available areas matter.
- **Geographic adjustment:** a small boundary movement in distance or area can move many people in a dense city. The size comparison on p.17 therefore does not establish negligible population or political consequences. Population balance and connectivity must be checked again after snapping.
- **Objectivity and discretion:** site selection, multiplicities, metric, smoothing and final boundary adjustments contain choices. A computer-generated answer is not automatically impartial. The voter bulletin's assurance of no room for gerrymandering (p.20) outruns the technical qualifications.

## Communication and reusable rules

The visual sequence from simple geometry to hierarchical urban subdivision is clear, and the literature review supports a real design choice. A dedicated audience-facing bulletin is a useful deliverable. Its limitations must remain aligned with the technical body; accessibility should simplify the explanation without upgrading the evidence.

1. Compare representations before algorithms: administrative units, continuous density and raster cells create different feasible sets.
2. Keep a good baseline's useful properties while refining the criterion it demonstrably fails.
3. Check hard constraints on the final artifact, including every geographic postprocessing step.
4. Carry data limitations through the full dependency chain from seed placement to reported fairness.
5. Distinguish deterministic computation from the value judgments and discretionary inputs that define it.
6. Report per-region outcomes and worst cases when averages are mathematically predetermined.

Cross-module link: the same **forward representation → decision generator → final feasibility audit** pattern appears in [2006 A883](../mcm_2006/mcm_12787fd8f903.md), where visually covered irrigation area did not ensure every location met dose requirements. A geometric picture is an explanatory aid, not the feasibility certificate.

## Full-page reading ledger

| Physical page | Material fully read and checked |
|---|---|
| 1 | Cover metadata, abstract, result claim and voter-deliverable promise |
| 2 | Contents and first figure-list entries |
| 3 | Remaining complete figure list |
| 4 | Problem motivation and full comparison of existing method families |
| 5 | Continuous-representation rationale, goal and metric definitions |
| 6 | Remaining definitions and evaluation criteria/compactness alternatives |
| 7 | Voronoi illustration, informal simplicity choice and mathematical definition |
| 8 | Metrics, geometric properties and population-controlled growth equations |
| 9 | Growth diagram, population invariant and site-selection alternatives |
| 10 | Hierarchical subdivision diagram, procedure and New York case rationale |
| 11 | Raster extraction, smoothing, density cap and site selection |
| 12 | Both density-map views and caption |
| 13 | Complete before/after subdivision maps |
| 14 | City multiplicities, baseline/refinement comparison and all 29 population shares |
| 15 | All three metric maps and displayed statistics |
| 16 | Full refined map and both urban enlargements |
| 17 | Boundary implementation argument and empirical tradeoff discussion |
| 18 | General failure scenarios and proposed refinement |
| 19 | Obstacle diagram, unfinished refinements and opening bulletin |
| 20 | Complete voter bulletin, conclusion, runtime claim and first reference |
| 21 | Remaining complete references |

All 21 available pages were read. The population-table arithmetic was checked; the redistricting algorithm was not numerically reproduced.
