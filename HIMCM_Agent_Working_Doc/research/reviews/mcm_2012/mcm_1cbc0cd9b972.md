# MCM 2012 A — Team 15065 — a reusable tree-and-light simulation architecture

> Archived prior research: this subject is excluded from further work by the current user instruction. Retained for provenance; not active workflow evidence. See [scope](../../SCOPE.md).

- Source ID: `mcm_1cbc0cd9b972`
- Source: `MCM-ICM-master/2012美赛特等奖/A-15065-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–29, including summary, letter, references and complete MATLAB appendix.
- Visual supplement: physical pp.6–23 inspected, covering all classification diagrams, transformation matrices, tree structures, solar geometry, exposure tables, physiology equations, field-measurement procedure and result plots.
- Numeric reproduction: **NOT_REPRODUCED**. The simulation, quadrature, photosynthetic equations and mass estimate were not executed.
- Award provenance: Outstanding filename label, not independently verified. Cover verifies Team 15065 and Problem A.
- Source limitations: some mathematical symbols on pp.17–19 render as empty glyph boxes in the original PDF; surrounding extracted text and visible structure were read, but unavailable glyphs were not silently reconstructed. No separate original problem statement was present in the corpus inventory.

## Connected architecture and selection rationale

The paper builds two reusable components before addressing the outputs: a three-dimensional tree generator and a directional-light model (pp.4–5). The tree generator supplies branch locations, leaves and crown geometry. The light model supplies irradiance and exposure at those locations. The same components then support both a leaf-shape experiment and a leaf-mass estimate.

This is a stronger architecture than attaching unrelated algorithms to each requested answer. Its interfaces have physical interpretations: coordinates, projected areas, irradiance, leaf mass per area (LMA), leaf area index (LAI), total area and mass. The final accounting relation is explicit: area-weighted LMA multiplied by total leaf area.

The shape classification is intentionally coarse because its purpose is to provide tractable geometry for simulation, not a full botanical taxonomy (pp.5–7). Convexity, elongation and location of maximum width define four categories. The branching representation assumes approximate self-similarity and uses recursive vector transformations, with species-specific branching and leaf arrangements (pp.8–10).

The illumination model considers multiple directions over the year instead of relying only on a single overhead sun. A canopy attenuation relation then connects external light to interior positions (pp.11–14). This makes the choice of a three-dimensional representation purposeful: it can express shading interactions absent from a two-dimensional silhouette comparison.

## Controlled experiment and its actual evidence

The authors hold a branching profile fixed, substitute alternative leaf shapes and compare weighted exposure. They report results for pine-like, poplar-like and banana-like profiles (pp.15–16). This is a useful intervention within a model: changing one represented feature while controlling the rest makes the comparison interpretable.

The first two selected shapes match the stated real shapes, while the banana example does not: the table selects palmate and labels the real leaf elliptic. The authors discuss large-leaf numerical difficulties and acknowledge the need for more profiles (pp.16, 24). Preserve this failure case. The stronger statements in the conclusion and letter that shapes maximize exposure generally or always are not supported by three constructed profiles, one of which disagrees.

A convincing next experiment would hold leaf area, leaf count, positions and computational resolution comparable, repeat stochastic tree generation, report the size of the exposure advantage, and test whether the ranking survives geometry and light assumptions. Similar exposure values may be practically indistinguishable at the resolution used. The paper does not establish evolutionary causation merely by matching an observed shape to a simulation's preferred option.

## Mathematical interfaces that require checking

The light geometry provides a valuable example of why explicit units and coordinate conventions matter. The paper defines theta as zenith and phi as azimuth, but later uses the azimuth in the angle-to-ground relation and prints a `cos(theta) sin(phi)` weighting over a full azimuthal cycle (pp.11–14). That factor changes sign across directions; it cannot be accepted as a positive exposure-weight measure without reconciling the variables and integration convention. The radiation rate is also assigned an extra inverse-time unit, and the attenuation exponent combines a geometric path length with a coefficient whose printed units refer to leaf and ground area. The exponent needs a dimensionless optical-depth definition.

Exposure is defined as a sum of individual projected leaf areas divided by crown-shadow area, then asserted to lie in zero to one (pp.13–15). Overlapping shadows make a plain sum different from their union and can exceed the denominator. The diagram and grid algorithm suggest union coverage, so the specification must state which quantity is computed. This is an interface issue with direct biological implications: overlapping leaf areas do not intercept independent copies of the same beam.

The physiological module combines area-based net photosynthesis with peak carbon assimilation per mass through an environmental factor (pp.17–19). The normalization and units of that factor must be explicit; an inequality between differently normalized rates is not meaningful on its own. Several parameter values and the area weights for average LMA are not supplied, so the displayed derivation does not enable independent numerical reconstruction. Some symbols are unavailable in the PDF rendering, as noted above; this review does not invent missing signs or claim to have resolved the full quadratic.

## Calibration, measurement and claimed mass accuracy

For one camphor tree, the authors perform field measurements and try 32 ground-axis orientations, selecting a simulated profile that resembles the measured tree (pp.20–22). This is an explicit calibration procedure and a useful practical response to unavailable branch-angle data. It is not a held-out validation of the same geometry. A quantitative shape discrepancy and uncertainty across acceptable fits would make the selection reproducible.

The resulting crown area is reported as about six square meters; an assumed LAI of 12 supplies the total leaf area. The LMA calculation then gives roughly 12.8 kilograms of leaves (p.22). The text reports LMA first as 177.74 and later uses 177.47, so the final arithmetic should be generated from a single output value. More fundamentally, the paper supplies no independently measured total leaf mass against which this prediction is compared. Agreement of crown area alone does not validate LMA, LAI or total biomass.

The normal distribution assigned to leaf spacing permits negative values unless truncated or otherwise transformed; no such rule is specified. Its scale also needs physical units. An empirically imported LAI is a substantive assumption with a direct multiplicative effect on total mass. It should be tested over a justified range, not treated as a result of the geometry model.

The later height-mass plots use simulated trees, grouped by crown form (pp.22–23). Group-specific patterns are an interesting model implication and highlight heterogeneity that pooled analysis can hide. They are not independent empirical evidence for a cubic biological law. The stated 5-to-10 meter grid with half-meter increments also needs reconciliation with the claimed total of 30 observations.

## What the supplied code establishes

The appendix contains branch generation and grid-based projected-area code (pp.27–29). It does not contain the complete sunlight integration, leaf physiology, LMA calculation or experimental driver. Reading it therefore cannot certify the full pipeline.

The branch implementation uses products of rotation matrices, a selected matrix row and random branch-length multipliers; these must be reconciled with the local-frame and length-scaling description. The projected-area routine counts occupied grid cells containing supplied points. Its interpretation depends on whether the input is a dense sample of leaf polygons or only branch endpoints. It also uses inclusive boundaries and floors the number of cells, creating grid-boundary and partial-cell questions. Tiny known polygons, complete overlap and grid refinement would be more informative verification cases than visual realism alone.

## Transferable workflow rules

1. Build reusable physical components and specify the quantities exchanged between them.
2. Choose the resolution of a representation according to its downstream task.
3. Control geometry and resources when comparing shape or policy alternatives.
4. Treat mismatching cases as information about scope, resolution or mechanism.
5. Verify coordinate conventions, nonnegative integration weights and dimensionless exponents before simulation.
6. Distinguish projected-area sums, unions and hulls; each answers a different question.
7. Separate geometry calibration from independent validation of the final endpoint.
8. Audit the supplied code's actual coverage before claiming a full implementation.

## Reading ledger

All 29 physical pages were read in four untruncated text batches; all material visual pages were inspected. Missing original glyphs and absent pipeline components are explicitly retained as limits. No numerical simulation or empirical reconstruction was performed.
