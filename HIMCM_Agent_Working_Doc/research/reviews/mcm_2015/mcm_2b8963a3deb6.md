# Full review: 2015 Problem C, Team 39160 — Organizational churn

- Source ID: `mcm_2b8963a3deb6`
- Source: `MCM-ICM-master/2015美赛特等奖/其他奖项/C-39160-Finalist.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical/printed pp.1–17, including all references.
- Visual supplement: pp.2–14 inspected to recover corrupted mathematical glyphs and inspect every diagram, equation and result figure. In particular, the tensor, satisfaction and performance definitions were read from the rendered pages.
- Numeric reproduction: **NOT_REPRODUCED**. No underlying Python implementation accompanies this PDF in the reviewed material.
- Award provenance: filename explicitly says Finalist, not Outstanding; not independently verified here.
- Original problem: the [official five-page statement](../../sources/2015_ICM_Problem_C.pdf) was read, with its chart and data table inspected visually.

## Architecture and strongest transferable contribution

This report makes model development itself visible. It builds three phases: a simple stochastic staffing framework, a satisfaction-driven departure mechanism, and a performance-aware promotion model (pp.6–11). Each phase lists what changes in initialization and in the update loop. That structure is a useful template for controlled development: first verify identities and flows, then add behavior, then add a decision policy.

The representation distinguishes persistent positions from mobile people (pp.2–5). Positions carry job properties and professional links; Person objects carry individual attributes and move between positions. Three graph layers represent supervision, close collaboration within a work group and looser collaboration across groups in the same office. An explicit alternative representation is discussed at the end, including its implications for maintaining relationships (p.16).

The paper's contribution is therefore more specific than “use a multilayer network”: choose the entity that remains stable, assign attributes to the correct entity, and make state transitions preserve the intended identities.

## Model specification and rationale

The initial simulation has a vacancy queue and a separate queue of positions receiving HR attention (pp.7–8). Recruitment takes time, and active hiring is limited to a fraction of vacancies with an overall capacity ceiling. This distinguishes hiring activity from completed arrivals. Vacancies are represented by flagged placeholder objects so that the underlying position graph remains intact.

In the second phase, satisfaction is a weighted average of previous individual satisfaction, supervisor satisfaction and two peer-group averages, with additional promotion and middle-manager adjustments (pp.8–10). Vacant placeholders have zero satisfaction, creating a mechanism by which vacant neighboring roles affect remaining employees. Departure probability depends on satisfaction.

The third phase introduces performance as a weighted function of competence, supervisor and work-group performance, bounded tenure transforms and satisfaction. Promotion selects the highest-performing eligible employee from the next lower rank (pp.10–11). Team-science ideas motivate tenure, shared experience and peer influences, but the precise weights and response functions are not empirically calibrated in the report.

Using weighted combinations of bounded quantities can preserve an interpretable score range if weights are nonnegative and sum to one. The implementation must also specify how the normally sampled competence variable is bounded. A normal distribution centered at 0.5 does not by itself restrict competence to the interval from zero to one.

## Interpretation and verification questions

The authors explicitly define annual churn using total positions as the denominator (pp.2, 6). That definition differs from a rate per currently employed person. Their initial 1.5% monthly departure probability is applied to occupied positions, so the relationship between that probability and the target annual position-denominated churn must account for occupancy and turnover exposure. Dividing an annual number by twelve does not automatically reconcile these definitions.

The cost assumptions say that table-defined training and recruitment costs accrue each monthly tick (p.7), whereas the official table distinguishes annual training costs from recruiting costs. The prose must state the conversion or allocation rule. The later annual cost plots do not resolve how the implementation treated these amounts. This is a specification ambiguity, not proof that the actual code multiplied costs incorrectly.

The final model is deliberately constructed to make performance strongly related to satisfaction, and Figure 3 confirms that relation in simulation (p.11). This is a check that the implementation exhibits the intended relation; it is not independent evidence that the real-world effect has that strength. Similarly, the conclusion describes two-way satisfaction/performance feedback (p.15), while the printed satisfaction equation contains no explicit performance term. The implemented feedback path would need clarification.

The phased design is valuable, but the paper does not supply a controlled ablation table, full parameter settings, random seeds or sufficient uncertainty reporting to establish the incremental value of each phase numerically.

## Experiments and results

The results show annual recruiting/training and departure patterns over thirty years (pp.11–12). The visualization exposes the relationship between spending, staffing and the HR capacity ceiling. However, the requested two-year recruiting and training budget is not explicitly reported as a pair of totals with an aggregation rule. A longer-horizon graph does not replace that requested output.

High-churn scenarios demonstrate the effect of a binding hiring-capacity limit (pp.12–14). The HR attention curve saturates, while vacancies can continue growing. The paper uses this bottleneck to recommend increased recruiting capacity. The logic is useful: an intervention should target the limiting process, not merely a correlated output. The exact boundary still depends on the assumed hiring delays, priorities and departure model.

The paper also considers the required restricted hiring of middle-level roles while allowing qualified internal promotions (p.14). It states that the effect on HR health is not significant. The report does not provide a statistical test or a sufficiently detailed uncertainty comparison for that wording; it is a qualitative interpretation of the modeled scenario.

In the broader recommendations, placing employees in fuller work groups improves satisfaction under the chosen vacancy-neighbor mechanism. That recommendation should be checked against departmental function and coverage constraints; concentrating staff can improve the constructed social score while leaving necessary functions understaffed.

## Communication and limits

The strongest communication devices are the layer-by-layer network explanation, explicit object attributes, numbered update sequence and phase-specific changes. The alternative people-centered representation is discussed in terms of concrete implementation consequences rather than dismissed without comparison.

The paper acknowledges unrealistic possibilities, such as promoting a supervisor over an otherwise empty work group, and proposes skill matching and persistent friendships as future extensions (pp.15–16). These are honest limitations. The repeated description of the model as realistic is stronger than the empirical evidence available in the paper.

## Transferable operating rules

1. Build an auditable baseline before adding coupled behavior.
2. State exactly what changes between model versions.
3. Distinguish entity identity from the location or role it occupies.
4. Separate queued work, active work and completed work.
5. Make the denominator of a rate explicit and reconcile it with the simulated exposure.
6. Connect recommendations to bottlenecks, then recheck other operational constraints.
7. Do not call an imposed functional relationship independent validation.
8. Return the exact requested horizon and outputs even when longer simulations are useful.

## Reading ledger

- Physical pp.1–9: summary, context, representations, all object attributes, initial model and satisfaction extension read in full; corrupted symbols resolved visually.
- Physical pp.10–17: departure/performance equations, every result, recommendations, limitations, alternative approach and references read in full.
- All diagrams and plots were inspected. This is a full review of the available paper, not a code or numerical reproduction certificate.
