# HiMCM 2020 A: personalized decisions, feasible choices and faithful interfaces

Coverage: all five independent 2020 A papers in the local archive have been read in full: teams [10549](../reviews/himcm/HIMCM_2020_A_10549.md), [10550](../reviews/himcm/HIMCM_2020_A_10550.md), [10656](../reviews/himcm/HIMCM_2020_A_10656.md), [10701](../reviews/himcm/HIMCM_2020_A_10701.md) and [11135](../reviews/himcm/HIMCM_2020_A_11135.md). The official one-page problem was read in full. This is a complete comparison of the local set, not of all submitted or awarded solutions. All reported numerical results remain **NOT_REPRODUCED**. Full reading includes image-only tables, formulas, supplied code and relevant figures; exact coverage and limitations appear in the individual cards.

## What the decision requires

The problem asks for relevant factors with classifications and units, a model based on each student's circumstances and preferences, at least ten reasonable fictional people, analysis of those demonstrations and a proposed presentation layout. Earnings, savings and time for recreation matter. A running app, an entropy-weighting layer or a globally representative survey are not mandatory deliverables.

The central decision chain is:

`actual offers and student situation → feasibility → personal utility and tradeoffs → uncertainty/stability → useful shortlist and explanation`.

Three distinctions govern the model. **Eligibility** asks whether the student can take the job. **Preference** asks how they value feasible alternatives. **Uncertainty** asks what is unknown about offers or outcomes. A skill prerequisite is not automatically a learning benefit; a personal value is not statistical noise; an ordinal contact-risk rating is not a calibrated probability. All five papers become easier to evaluate when these meanings are kept separate.

## Five architectures and their purposes

| Team | Architecture | Positive contribution to preserve | Main audit question |
|---|---|---|---|
| 10549 | AHP and entropy mixture → additive scores → score clustering → age filter | Returns a set of alternatives; worked example; explicitly considers inconsistent preference input. | Does dispersion weighting change the student's values, and can late filtering leave no eligible option? |
| 10550 | Feasibility proposal → ANP supermatrix → limiting priorities | Separates reusable job blocks from user-dependent blocks; maps recomputation dependencies; perturbs both preferences and assumed network structure. | Do dependencies have evidence, and do the printed matrices describe one executable calculation? |
| 10656 | Boolean-style gates × soft wage/interest/hour factors | Directly explains the behavioral purpose of every term; publishes code and full test data; provides paid-job and internship paths. | Do equations, CSV schemas, code arguments and questionnaire inputs agree at boundaries? |
| 10701 | Net-pay/time/learning indices → AHP → TOPSIS → attribute clustering | Includes commute, incremental-cost intent, schedule conflict and overtime; deliberately diversifies recommendations. | Are offers feasible, and how much decision quality may be sacrificed for diversity? |
| 11135 | Feasibility and minimum thresholds → tailored indices → AHP → benefit/hour ratio | Separates category exploration from specific offers; recognizes preferred intermediate attribute levels; reports rank-change thresholds. | Does the tolerance parameter survive normalization, and does benefit per hour match the student's actual objective? |

These are design choices serving different functions. Method names do not supply a justification by themselves. A direct weighted-utility model can be preferable when the important tradeoffs are simple. ANP needs supported interactions; clustering needs an explicit diversity objective; a ratio needs an efficiency objective. Each extra component should answer a need the baseline cannot adequately address.

## A defensible approach-selection sequence

1. **Specify the decision unit.** Decide whether the output is an exploratory occupation category, a real offer, a schedule or a shortlist. Category averages cannot certify that a local employer has an opening or accepts the student's qualifications. 11135's two-level distinction and 10550's job-type/offer distinction are useful starting points.
2. **Define hard conditions first.** Encode age/qualification, inaccessible commute, unavailable hours, safety limits and any required earnings. Let users mark a preference as flexible when appropriate. Return a reasoned empty-set result instead of recommending an infeasible option or silently relaxing a condition.
3. **Account for money and time.** Keep hourly rate, paid hours, total earnings, work-related incremental expenses, commute and savings separate. A short job with a high rate may not meet a savings target. A twelve-hour or other fixed daily budget is an assumption requiring justification. Clarify one-way versus round-trip commute and available versus required hours.
4. **Elicit useful preferences.** Distinguish larger-is-better, smaller-is-better and preferred-range attributes. AHP may structure tradeoffs, but the user must understand the questions. Record any repaired comparison and ask the user to confirm its meaning. Do not treat internal consistency as observed preference accuracy.
5. **Build a simple baseline.** Start with a feasible-set filter and transparent utility score. Document scale transformations and acceptable compensation. If lexicographic priorities are the user's actual choice, preserve them; do not declare them inferior merely because they produce different rankings.
6. **Add complexity for an identified need.** Use network dependence only for interpretable relationships; diversify a shortlist only within an acceptable utility/regret band; use a benefit/hour ratio only when efficiency is the relevant objective. Compare each addition with the same inputs, feasible set and utility interpretation.
7. **Report conditional choices.** Show why each recommendation meets conditions, which tradeoffs matter and whether small plausible changes reverse the ranking. Use a near-tie band rather than inventing certainty from the third decimal place.

## Tests that these papers show are worth doing

The first group checks **meaning preservation**. In 11135, the preferred interval width becomes a standard deviation, but min-max normalization of absolute z-scores cancels that common scale; differing tolerances around the same midpoint cannot affect the final index as written. Simplify equations before implementation and test whether every advertised parameter changes the intended behavior. Entropy weighting in 10549 is another meaning question: job-to-job dispersion cannot discover what the user ought to value.

The second group checks **contracts across artifacts**. In 10656, the displayed job schema has separate age, risk and wage columns, while the score caller uses `job[2]` for all three. Its hours equation and code also disagree at equality, and the questionnaire omits a required binary preference. In 10550, an all-zero goal-node column in the printed unweighted matrix appears nonzero in the reported limiting matrix despite the stated weighting/power procedure. These findings were made by static inspection, not numerical reproduction. They justify named schemas, executable specifications and a reviewer who reads the appendix as well as the main narrative.

The third group checks **degenerate inputs**: zero/one feasible offer, a constant normalization column, a zero-width preferred range, zero hours, missing ratings, all equal alternatives, inconsistent comparisons and tied scores. Several papers report narrow candidate sets without fully specifying the resulting normalization behavior. These are part of the decision, not optional software polish.

The fourth group checks **decision stability**. 11135's strongest technique is to vary one weight while preserving the ratios of the others and identify the value at which the top choice changes. 10550 separately varies user weights and designer-assigned network weights. Extend these to uncertain offers, simultaneous changes, omitted criteria and candidate-set changes. 10701's deliberate change from knowledge to recreation tests responsiveness; it does not establish stability to measurement noise. The two questions must be reported separately.

The fifth group checks **feasibility and objectives under selection**. Filtering after clustering can discard all of the leading set; diversity can elevate a poor alternative; benefit/hour can favor insufficient total income; long work hours can simultaneously inflate learning and violate a schedule. Require a final constraint certificate for every displayed option, plus a clear statement of whether it maximizes total utility, efficiency or diversity.

## Fictional examples and evidence limits

Ten fictional people are a demonstration requirement, not a representative sample. Construct them to cover mechanisms: a binding income need; a narrow schedule; no feasible offers; a new-skill aspiration; different preferred activity levels; opposite commute constraints; a near tie; missing data; and a contradictory preference response. Explain why each fixture exists and save its exact inputs. Test outcomes against predeclared expected properties, not a biography rewritten to endorse the winning job.

Avoid using social stereotypes as measurement. Personality descriptions do not establish skill, hiring probability or the effect of a job on a student's behavior. A qualitative plausibility check is useful but distinct from external validation. A small AHP consistency ratio, a transformed histogram, a visually similar radar polygon or agreement with a fictional narrative does not demonstrate real-world accuracy.

A stronger evidence ladder is: schema/units → mathematical properties → code/equation agreement → controlled edge cases → held-out or user feedback → decision robustness. Keep missing evidence visible. None of these five papers' numerical results has been independently reproduced in this review program.

## Handoffs for the six canonical roles

| Role | Responsibility | Reviewable artifact |
|---|---|---|
| Coordinator | Prompt coverage, decision granularity, binding constraints, acceptance behavior. | Demand map; required-output list; canonical scenario IDs. |
| Domain-data | Offer/category distinction, eligibility, data units, provenance, uncertain ratings. | Named input schema; source ledger; actual-versus-fictional flags. |
| Modeler | Utility semantics, hard/soft distinction, baseline and justified extensions. | Equations; transformation behavior; objective and constraint definitions. |
| Computation | Input contracts, reproducible pipeline, diagnostics, degeneracies, scenario sweeps. | Executable model; generated tables; explicit failure/fallback states. |
| Independent-reviewer | Meaning preservation, equation–code–UI consistency, rank reversals and objective fidelity. | Static audit; boundary cases; decision-stability report; unresolved assumptions. |
| Writer-visuals | Worked example, understandable reasons, calibrated claims and faithful presentation design. | Traceable narrative; shortlist explanations; interface-to-variable map. |

The working document should require these handoffs before model sophistication is celebrated. The reusable strength across the five papers is making a personal decision concrete through explicit criteria and worked examples; the recurring vulnerability is losing the intended meaning between the user, data, mathematics, code and presentation.
