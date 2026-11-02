# Full review: 2015 Problem D, Team 35780 — Sustainability? Responsibility!

- Source ID: `mcm_97fea85bdc35`
- Source: `MCM-ICM-master/2015美赛特等奖/D-35780-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pp.1–24, including both reference pages. Printed pp.1–22 correspond to physical pp.3–24.
- Visual supplement: physical p.4 and pp.6–21 inspected for the indicator table, all material equations, matrix diagrams, rankings, scenario plots, activity/control tables and sensitivity figure. Visual inspection recovered absolute-value signs lost in text extraction.
- Numeric reproduction: **NOT_REPRODUCED**. No entropy calculation, ODE integration or dynamic-programming solution was rerun.
- Award provenance: explicit Outstanding filename label; not independently verified here.
- Original problem: the [official three-page statement](../../sources/2015_ICM_Problem_D.pdf) was read in full.

## Task structure and model architecture

The paper explicitly separates measurement, forecasting and intervention. Seventeen indicators become environmental, social and economic performance measures; those measures become development and coordination scores; a three-state dynamic system predicts their evolution; control parameters represent interventions; a four-stage planning procedure searches a twenty-year strategy. External perturbations are added afterward.

This is a useful architecture because a current score, an uncontrolled forecast and an intervention scenario answer different questions. The paper compares trajectories with and without a plan rather than treating an improving trend alone as evidence of policy benefit (pp.17–18).

## Indicator selection and justification

The indicator selection criteria include coverage, possible policy influence and recurrence in earlier indicator systems (p.5). The hierarchy is shown explicitly, making omissions and category assignments inspectable (p.6). Normalization distinguishes positive, negative and target-valued indicators; the latter include inflation and population measures (pp.6–7).

Entropy weights summarize variation in the selected country sample (p.8). Development is a weighted combination of the three domain measures. Coordination is one minus their coefficient of variation, so a country with highly uneven domain scores receives a penalty (pp.8–9). A two-dimensional diagram shows development and coordination separately before reducing them to distance from an ideal point.

The positive practice is to define both aggregate level and imbalance, rather than allowing a high result in one domain to conceal every weakness elsewhere. The mathematical choices still need justification. Variation across countries does not determine social importance. The reference-country set affects normalized values and entropy weights. A fixed classification threshold therefore needs a stable reference scale if it is to retain meaning over time or across samples.

The coordination formula is undefined at an all-zero state and can be negative for sufficiently unequal nonnegative components. Its displayed classification table covers zero to one only. Those boundary cases require an explicit rule before using the score as a universal objective. The values of the development-combination weights and the intended scale also need to be recoverable.

## Forecasting and the bridge to intervention

The authors adapt a coupled differential-equation idea from Lanchester models into a linear state-space system for the three domain performances (pp.10–11). The justification is that each domain has self-effects, cross-domain interactions and outside inputs. Reducing seventeen indicators to three states makes the proposed dynamics manageable.

The transferable reasoning is the interaction structure, not the military-model label. A linear coupled model needs its own justification for signs, time scale, parameter identification and valid range. The paper fits using 2009–2013 information and projects twenty years ahead (pp.11–12), but supplies no held-out evaluation or forecast intervals. Short historical data and long extrapolation make structural alternatives particularly important.

The intervention model changes the dynamics with diagonal direct and indirect control matrices (pp.13–14). Dynamic programming is motivated by four successive five-year stages and carries the previous stage's final state into the next stage (p.15). This recognizes path dependence instead of optimizing four independent snapshots.

However, the report gives the state, action description and cumulative score without a complete Bellman recursion, discretized action/state sets, numerical solution record or optimality certificate. “Optimal” therefore remains an author claim that cannot be independently verified from the supplied description.

## Decision relevance and policy evidence

The Democratic Republic of the Congo is the selected case (p.16). Single-control perturbations show which abstract parameters have larger effects on the modeled indices, followed by baseline-versus-plan trajectories (pp.17–18). The authors then map domain priorities to a list of concrete activities, including technical support and settlement renewal.

This last mapping is the weakest interface. A numerical control coefficient is not itself a purchasable program. The report does not provide a quantified expenditure-to-control relationship, implementation capacity, intervention delay or explicit investment budget. It therefore does not establish the most effective program per dollar, even if the abstract state-control calculation were correct. The authors acknowledge that the connection from specific strategies to changes in performance needs more quantitative evidence (p.22).

The activity-score citation also needs verification: the narrative points to reference 22, which is unrelated to the described strategic environmental assessment; a thematically relevant source appears elsewhere in the bibliography. This illustrates why a citation number must be checked against the actual source rather than accepted as evidence by appearance.

## Static specification questions

The printed state-space equations have dimensional inconsistencies before the later perturbation reformulation. The displayed input matrix is a three-element column and the input is a three-element row, whose product is a matrix, while the state derivative is a vector (pp.10, 13). The component equations suggest a different intended arrangement. The model needs one dimensionally consistent specification.

The continuous derivative and discrete next-state versions also need an unambiguous transition definition, including the time-step factor on outside inputs. Coefficients in the control-effect table are interpreted relative to one even though sign and discrete growth multiplier are different concepts. The later control table must clarify whether its entries are absolute multipliers or deviations from baseline (pp.14, 19).

These are observations about the printed formulation. No unavailable implementation was inspected, and this review does not infer which version produced the plots.

## External effects and sensitivity

External effects are represented as Gaussian perturbations to the state dynamics (pp.19–20). The authors show a favorable trajectory at one noise setting and report negative performance values at a larger setting. This is useful disclosure of a failure boundary. Negative values also expose a structural domain problem: a nonnegative performance index needs dynamics that preserve its domain or a clearly justified boundary treatment.

A favorable plotted realization is not a probability guarantee. The disturbance distribution, dependence, time scaling, replication count and likelihood of failure need specification before making a robustness claim. The assumption that exceptional shocks are rare does not by itself justify symmetric Gaussian noise for all listed external factors.

The one-at-a-time parameter analysis examines changes in outputs for one interaction coefficient (pp.20–21). It supports a local, conditional sensitivity statement, not comprehensive stability of the entire model. It should be distinguished from numerical stability, structural uncertainty and uncertainty in the policy-effect mapping.

## Transferable operating rules

1. Keep measurement, forecast and intervention models distinct and connect their interfaces explicitly.
2. Report level and imbalance separately when both affect the decision.
3. Freeze and disclose the reference population behind normalized indices.
4. Check zero states, score ranges and matrix dimensions before forecasting.
5. Use a no-intervention counterfactual to interpret policy effects.
6. Tie every controllable coefficient to a feasible action, cost and response mechanism.
7. Document enough of a planning algorithm to reproduce its state transitions and search.
8. Distinguish local sensitivity, random scenario behavior and formal stability.

## Reading ledger

- Physical pp.1–8: summary, contents, context, assumptions, indicator hierarchy, normalization and entropy aggregation read in full.
- Physical pp.9–16: coordination/scoring, state equations, rankings, forecasts, controls, planning formulation and policy activity table read in full.
- Physical pp.17–24: all scenario results, control tables, perturbation and sensitivity analyses, limitations and references read in full.
- All tables and relevant mathematical/graphical material were inspected visually. Full-paper reading does not imply numerical or empirical reproduction.
