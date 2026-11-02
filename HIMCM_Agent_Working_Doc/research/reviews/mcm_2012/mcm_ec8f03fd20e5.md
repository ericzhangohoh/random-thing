# MCM 2012 A — Team 16831 — five modules, conditional biological claims and implementation checks

> Archived prior research: this subject is excluded from further work by the current user instruction. Retained for provenance; not active workflow evidence. See [scope](../../SCOPE.md).

- Source ID: `mcm_ec8f03fd20e5`
- Source: `MCM-ICM-master/2012美赛特等奖/A-16831-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–54, including summary, letter, references, measurements and complete R/MATLAB appendices.
- Visual supplement: physical pp.5–39 inspected for classification images, dendrogram, neural-network diagnostics, projection geometry, overlap plots, light/size surfaces, branching diagrams, statistical tables and biomass comparisons.
- Numeric reproduction: **NOT_REPRODUCED**. No clustering, neural-network training, overlap computation, regression or biomass experiment was rerun. Algebraic observations below are reviewer reasoning, not reproduced numerical results.
- Award provenance: Outstanding filename label, not independently verified. Cover identifies Team 16831 and Problem A.
- Source limitation: no separate original problem statement was present in the corpus inventory; coverage of the prompt is assessed through this submission's restatement.

## Architecture and reasons for the representations

The paper organizes the problem into five modules: leaf classification; leaf shape and overlap; position, illumination and leaf size; leaf dimensions and branching architecture; and total leaf mass. The modules use different evidence types rather than forcing every question into one technique. Image descriptors support classification; controlled geometry isolates shading; a light-response equation connects position to size; published observations support statistical associations; crown volume and trunk diameter provide practical mass estimators.

This division is useful because each requested relationship has its own measurable endpoint. The paper also offers a valuable qualification: whether a leaf should minimize overlap depends on the limiting environmental resource. Light competition can favor a narrow blade or long petiole, whereas water or other constraints can change the objective (p.22). That conditional argument is more defensible than asserting that every observed shape globally maximizes sunlight.

The five modules nevertheless require separate validation. A plausible overlap mechanism does not validate a classification, and a good fit of mass against trunk diameter does not establish the leaf-growth mechanism. This paper is a good source for a workflow that assigns each module a distinct evidence contract.

## Classification: transparent features, but learned labels are not independent truth

The authors choose length-to-width ratio, approximate area, a concavity descriptor and the angle at the leaf base. The latter two are illustrated explicitly (pp.4–5). They extract 32 examples from published leaf images, standardize the feature matrix, use Euclidean distances and Ward clustering, and cut the dendrogram into four groups. The R appendix documents `scale`, `dist`, `hclust(...,"ward")` and `rect.hclust(...,k=4)` (pp.44–46).

Showing the leaves within each group makes the meaning of the mathematical partition inspectable. However, the assertion that a mathematical procedure removes subjective factors is too strong: feature selection, image scale, distance metric and the four-group cut are consequential choices. Approximate area is measured in image pixels; without common physical scaling, it may reflect image preparation. The tabulated approximation is half length times width, so its geometric meaning should be stated consistently.

Eight additional leaves are classified using a neural network trained on the cluster labels. Seven are judged visually consistent with their assigned groups; the mismatch is shown rather than hidden (pp.9–10). This tests a classifier's extension of the chosen partition, not independent botanical validity. The training correlation near one is not held-out accuracy.

The appendix clarifies an architectural inconsistency in the prose. It implements a feedforward network with ten hidden units and one linear output, trained with `trainlm`, then thresholds the scalar output into labels 1–4 (pp.46–47). The main text also describes a generalized-regression-style decision ratio and one hidden neuron per training case. These are not the same implementation. Scalar regression further imposes an ordering on nominal cluster IDs. The model description, output encoding and executable code must agree before interpreting performance.

## Overlap: build the geometry incrementally and test the conventions

The geometric module holds blade area fixed and varies narrowness, petiole length, leaf inclination, internode distance and sunlight direction. Four rhombus leaves on two layers make overlap analytically tractable. The paper progresses from horizontal leaves without petioles to petioles and then inclined leaves (pp.11–23). This sequence is useful: a controlled baseline exposes each added mechanism instead of hiding it inside a complex three-dimensional simulation.

The effective-area ratio divides unshaded blade area by total blade area. A vertical-light, coincident-layer case gives one-half, providing a simple boundary check. Directional curves and tables compare width ratios 1:1, 2:1 and 8:1. The source reports larger mean exposure for the narrowest profile in the selected geometry, and a larger petiole effect for broader blades. These are conditional model outputs, not measurements of a universal evolutionary optimum.

Several specifications need repair before reusing the equations:

1. Petiole length and internode distance are divided by leaf **area** while being treated as scale-normalized lengths (pp.12–13). These ratios retain inverse-length units. A dimensionless length should use a defined characteristic length, such as the square root of area.
2. Solar altitude is defined above the horizontal, but the projection matrix uses height times its tangent (p.15). Later overlap formulas use the tangent of the complementary angle (pp.16–17). The worked altitude of 45 degrees hides the difference. Vertical and near-horizontal sunlight tests would expose it immediately.
3. Some plot captions call the swept variable altitude although the horizontal axis and associated discussion describe azimuth. Distinguish a fixed altitude from a swept direction before averaging.
4. The piecewise overlap formulas need explicit geometric domains, endpoint treatment and clipping when polygons no longer intersect. Algebraic expressions valid within one intersection pattern should not be extrapolated to every spacing or angle.
5. For inclined leaves the authors approximate actual blade exposure through projected-shadow overlap, evaluate three azimuths and infer an approximate mean and maximum (pp.20–21). That is a stated approximation; it is not an exhaustive search over direction.

The local sensitivity exercise changes selected parameters by five percent around one configuration (p.23). It distinguishes petiole effects on the mean from effects on the maximum, which is valuable. Its results should remain local; they do not establish robustness across branching patterns, inclination ranges or different resource constraints.

## Light and leaf size: inspect the mathematical and software interfaces

Vertical light attenuation is represented exponentially, with a linear radial modifier (pp.24–26). The authors motivate the modifier by a weaker horizontal gradient and propose calibrating the coefficients at three canopy locations. They compare the qualitative trend to published apple-tree observations. No residuals, independent prediction errors or parameter uncertainty are supplied.

The next equation makes leaf size increase toward a species-specific limit as illumination increases. This creates a useful intermediate-variable chain: position → light → leaf area. But the monotonic size pattern is largely a consequence of the selected functions, not independent confirmation of the biological claim.

The printed differential equation is `dS/dI = r0 I (1-S/K)`; its printed solution omits the corresponding factor `1/K` in the exponential unless `r0` is redefined (pp.26–28). The low-light rule also jumps from zero to a positive minimum size at the threshold. Such a jump can be an intended survival rule, but it must be identified and tested rather than visually smoothed away. The symbol `I0` is used for both above-canopy illumination and a minimum-light threshold, making the interface ambiguous.

The appendix reveals a more substantive inconsistency. The one-dimensional curve uses the squared-illumination exponential, but the three-dimensional leaf-area surface uses a conventional logistic expression with an exponent linear in illumination (pp.53–54). Thus the displayed surface does not implement the equation used to justify it. The prose below the surface says leaves closer to the trunk are larger, while the stated radial light modifier and final letter imply the opposite. A workflow should generate figures from the same authoritative function and verify the sign of each dependence.

## Branching architecture: statistical association is useful, but provenance matters

The paper distinguishes orthotropic and plagiotropic arrangements, then imports a logistic discriminant involving latitude, petiole length and blade aspect ratio from King and Maindonald (pp.29–34). The model offers a compact way to predict a branching category from measured features. The reported table has 414 correct classifications out of 456 species across four displayed regions, approximately 91 percent. The narrative mentions five areas, so the scope needs reconciliation.

Both coefficients and evaluation data are attributed to the same published study. The submission does not establish an independent held-out test. Moreover, a predictive association does not demonstrate that the measured leaf dimensions causally determine the branching pattern. The accompanying geometric discussion supplies a possible mechanism, which should be labeled as an explanation consistent with the observations.

The t-test tables make the evidence inspectable. They also show why a reader should inspect values rather than rely on the conclusion: one aspect-ratio comparison has `p=0.06261`, despite the generalized claim of significant differences (p.32). The simple-versus-compound bar charts show counts, but similar counts alone do not demonstrate statistical equivalence. The branching illustration's labels also appear inconsistent with the surrounding prose definitions; a figure should clarify a category rather than reverse it.

## Mass estimation: compare models on accuracy and measurement cost

Six geometric crown approximations provide a simple baseline. Multiplying crown volume by leaf mass per volume yields a predicted mass, compared with measurements for fourteen oak trees (pp.34–36). The paper then reduces effective density as crown volume grows and compares this volumetric approach with a quadratic relation between diameter at breast height and mass (pp.36–39).

The authors favor the diameter-based estimator partly because it requires only one convenient measurement. This is a transferable model-selection criterion: a slightly more elaborate estimator may be worse operationally if its inputs are costly or unreliable. The vessel-area argument gives a reason to consider a quadratic form, although it does not identify all coefficients or prove the fitted relation.

The numerical claims require more care:

- The density is printed as approximately `280 g/cm³`, while crown dimensions are in meters and the reported masses are in grams. The unit must be reconciled before using the formula; silently substituting a plausible unit would conceal a source error.
- Mean prediction-to-observation ratios of 1.09 and 1.18 are described as estimates within 12 percent of measured mass. The latter does not support that statement, and neither mean ratio bounds individual errors. Over- and underprediction can cancel.
- The density correction `exp(-lambda V)` is motivated by declining foliage density, but total predicted mass `V LMC exp(-lambda V)` itself eventually decreases with increasing volume once `V > 1/lambda`. That consequence needs a defensible domain, and `lambda` needs inverse-volume units.
- The correction and quadratic fit are assessed on the same small dataset used to select or fit them. The reported `R²=0.98` is in-sample fit, not independent predictive accuracy.
- The quadratic is said to use the earlier data table, but that table supplies crown dimensions and measured mass without the required diameter observations. Coefficients and a complete fitting dataset are necessary for reconstruction.
- Comparing a newly fitted curve with fixed coefficients imported from another study confounds model form with calibration population. Refit both candidates on the same training data and compare on the same held-out observations.

## Transferable workflow rules

1. Give each subquestion a measurable endpoint and its own validation contract.
2. Introduce geometric complexity in stages while controlling total resources and scale.
3. Derive recommendations under the resource that actually limits the system.
4. Distinguish cluster-label consistency from externally meaningful classification.
5. Check units, angle conventions, limits and domains before interpreting numerical sweeps.
6. Trace every plotted result to the exact equation implemented in code.
7. Keep borrowed calibration data separate from independent evaluation data.
8. Compare model error distributions and measurement burden, not only average ratios or fitted correlation.
9. Preserve counterexamples and scope restrictions in the summary and stakeholder letter.

## Reading ledger

All 54 physical pages were read, including every supplied code and data appendix. The final appendix batches were reread after one tool response was truncated. Material visual content was inspected separately; visual checks confirmed the projection convention, statistical-table exceptions, mass units and differences between curves and equations. These are source-review findings, not a reproduced computational study.
