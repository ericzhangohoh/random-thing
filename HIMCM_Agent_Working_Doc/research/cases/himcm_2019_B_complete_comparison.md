# HiMCM 2019 B: policy scope, substitution and impact accounting

Coverage: all four independent 2019 B papers in the local archive have been read in full: teams [9548](../reviews/himcm/HIMCM_2019_B_9548.md), [9869](../reviews/himcm/HIMCM_2019_B_9869.md), [10337](../reviews/himcm/HIMCM_2019_B_10337.md) and [10407](../reviews/himcm/HIMCM_2019_B_10407.md). The official five-page problem and separate Concord FAQ were read before the papers. This is a complete comparison of this local set, not a claim to cover every submitted or awarded solution. No paper's computations have been independently reproduced. Source hashes, exact reading coverage and page-specific audits are recorded in the individual reviews.

## What the prompt actually demands

The task is broader than “are plastic bottles bad?” It asks for positive/negative effects, the information required and a way to collect it, applications to Concord and San Francisco, an airport adaptation, a revised Concord policy represented in the model, generalization and a one-page public article. Actual data collection is explicitly unnecessary, so a well-specified research design can satisfy that part without pretending to have observations.

The treatment must be precise. Concord restricts sale of plain, nonflavored, nonsparkling water in PET bottles at most one litre; permitted products, free distribution and emergency exceptions matter. San Francisco's described restriction concerns city property, while an airport creates a different access environment. A model that deletes all bottled-water consumption citywide evaluates a different intervention.

The common causal chain is:

`policy scope and enforcement → available products/access/prices → consumer substitution → quantities/materials/resources → stakeholder outcomes → policy judgment`.

Skipping a link produces a result that looks quantitative while leaving its main assumption hidden.

## Four approaches and the work each actually performs

| Team | Core approach | Useful contribution | Main boundary of the evidence |
|---|---|---|---|
| 9548 | Beverage competition equations feed energy, waste, health and employment branches. | Tries to model substitution dynamically rather than removing PET impacts in isolation. | Competition parameters and lower bounds are not calibrated; residual categories need conservation checks. Several outcome equations/results conflict. |
| 9869 | Beverage profiles plus city/airport replacement models, followed by entropy-weighted policy ranking. | Separates multidimensional impact description from policy ranking; introduces an airport outside option. | Replacement shares and weights fail basic sum checks; polynomial fit and entropy dispersion do not validate behavior or social priorities. |
| 10337 | Survey-derived drink shares feed cost, energy and waste accounting. | Explicit question-to-variable mapping and separate physical outcomes make the data plan inspectable. | Illustrative assumptions drive results; cost horizons, energy boundaries and some arithmetic are inconsistent. |
| 10407 | Localized normalized beverage shares, price-response reweighting and impact vectors. | Clear stage interfaces, intermediate tables and normalization conserve volume in the intended equations. | Convenience and impact coefficients are subjective; the geometric score is equal-weight addition, not independent evidence of net benefit. |

These approaches are not interchangeable alternatives to be ranked by sophistication. Dynamics are justified only if transition timing matters and can be parameterized. Static accounting can answer a counterfactual with less complexity, but still needs defensible substitution inputs. A composite score is a decision layer added after consequences are estimated; it cannot repair a weak behavioral layer.

## A stronger approach-selection argument

An agent should justify the model at each interface:

1. **Define the policy.** List restricted and permitted products, geography, actor, time, compliance and exceptions. Encode the difference between a sale ban and a consumption ban. State whether cross-border purchases and manufacturer responses are in scope.
2. **Define the decision and stakeholder.** Consumer spending, concession profit, municipal budget, physical waste and social welfare are different outcomes. A change from city residents to airport retailers requires a deliberate objective change.
3. **Choose the behavioral baseline.** Start with displaced PET volume allocated across feasible alternatives, including delayed/no purchase where appropriate. Require nonnegative shares summing to one. Preserve unaffected consumers in the baseline; a model in which everyone reconsiders all drinks requires additional evidence.
4. **Add complexity for a specific need.** Time-dependent competition requires rates and initial states; heterogeneous preferences require segments; airport access requires terminal locations or service capacity. A named theory alone is insufficient justification.
5. **Translate quantities into outcomes with consistent boundaries.** Use per-litre, per-container or per-person factors deliberately. Track reuse cycles and recovery/incineration separately. Define primary versus final energy, manufacturing versus use, and local versus global effects.
6. **Keep outcomes visible before aggregation.** Present volume, waste, energy, costs and any defensible health proxies separately. Add stakeholder weights only when a decision needs them; label them as values rather than discoveries from a normalization algorithm.
7. **Compare a revised policy.** Change implementable variables, charge intervention costs, rerun the same scenario set and report incremental effects. Merely recommending fountains after finding tap water attractive does not complete the revision task.

## How to justify a data-poor model honestly

10337's strongest transferable element is its explicit survey-to-variable table. Extend it into a contract with columns for question/source, population, unit, denominator, transformation, expected bias, uncertainty and downstream use. A respondent's percentage of drinks is not automatically the population's volume share. Intended choices are different from realized purchases. A frequency of recycling is different from the mass recovered. Airport cluster sampling requires a sampling design, not just a larger number of respondents.

10407 offers a useful branch: use local observations where available, otherwise use a national baseline with local adjustment. The fallback must remain labeled as a proxy. “Large population” does not make a locality representative of national averages. A convenience rating is not a measured elasticity; a narrative source may motivate its sign without determining its magnitude.

The minimum useful uncertainty analysis should vary substitution to tap/soda, packaging alternatives, cross-border purchases, compliance, reuse cycles and the main unit-impact factors. Report whether the policy recommendation changes, not just whether a score moves smoothly. If the sign depends on one uncertain behavior, identify the observation that would most reduce decision uncertainty.

## Validation hierarchy revealed by these papers

The first layer is **internal validity**: shares and weights sum correctly; components reconcile; percentages do not masquerade as fractions; physical and financial periods agree; container counts remain feasible. The observed errors are material: 9869's displayed city shares and primary weights sum to 1.110, 10337's San Francisco energy total differs by roughly a factor of 1,000 from its components, and 10407's airport comparison changes the effective population denominator without labeling it.

The second layer is **behavioral validity**: test predicted substitution against held-out observations, a comparable policy case or a carefully designed survey. A high in-sample polynomial R², qualitative plausibility or agreement with legislative intentions does not provide this test.

The third layer is **impact validity**: check unit factors and boundaries. Total industry revenue is not economic benefit per extra litre; additive ordinal health scores are not health outcomes. Thermal conversion, fuel refining and fuel combustion cannot be mixed without a common accounting convention.

The fourth layer is **decision robustness**: vary uncertain inputs and stakeholder weights, compare feasible policies and identify reversals. A ranking with one set of subjective weights is a conditional preference statement, not a universal answer.

The final layer is **communication fidelity**: the public article must retain the evidence status. “Our scenario suggests” is appropriate when the pre/post values were constructed; “the data conclusively show” is not. Accessible writing should simplify the explanation without upgrading the certainty.

## Assignment within the six canonical roles

These are functions within the existing six sessions, not additional mandatory agents:

| Canonical role | Concrete responsibility for this problem family | Reviewable handoff |
|---|---|---|
| Coordinator | Demand map, exact policy scope, decision-maker, alternative-policy definition. | Scope table and acceptance criteria for every requested output. |
| Domain-data | Measurement plan, local/national source distinctions, sampling and proxy limits. | Source/variable dictionary plus survey-to-input mapping. |
| Modeler | Substitution baseline, structural alternatives, accounting boundaries and value judgments. | Equations and interface contract with conditional/unconditional shares identified. |
| Computation | Scenario execution, conservation, units, component reconciliation and policy comparison. | Reproducible tables, checks and input-to-output trace. |
| Independent-reviewer | Scope fidelity, denominator/horizon audits, validation and robustness challenges. | Issue log distinguishing arithmetic defects, unsupported mechanisms and value choices. |
| Writer-visuals | Evidence-calibrated public article, separate outcome displays and readable mechanisms. | Claims ledger and figures whose labels state units, population, horizon and scenario status. |

The governing lesson is to make the causal and accounting interfaces reviewable before arguing over the final score. These papers provide useful architecture and communication examples alongside concrete failure modes that the working document should prevent.
