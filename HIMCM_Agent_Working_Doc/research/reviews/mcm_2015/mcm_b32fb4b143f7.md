# Full review: 2015 Problem C, Team 33572 — Simulation company

- Source ID: `mcm_b32fb4b143f7`
- Source: `MCM-ICM-master/2015美赛特等奖/C-33572-Outstanding.pdf`
- Coverage: **FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED**, physical pages 1–21, including all references. Printed pages 1–20 correspond to physical pages 2–21.
- Visual supplement: physical pp.4–11 and 13–20 inspected for network diagrams, formulas, event ordering, trajectories and image-encoded tables. Text was read in full in two untruncated page batches.
- Numeric reproduction: **NOT_REPRODUCED**. Reported simulation values are author results; no simulation code is supplied or executed here.
- Award provenance: explicit Outstanding filename label; not independently verified for this review.
- Original problem availability: the five-page [official 2015 ICM C statement](../../sources/2015_ICM_Problem_C.pdf) was subsequently retrieved and read in full; the organizational chart and data table on physical p.3 were inspected visually. Retrieval metadata are saved beside the PDF.

## Task structure and strongest reusable contribution

The paper describes a company with 370 positions and asks how staffing, departures, promotions, recruitment and training interact. Its reported tasks include a human-capital network, ten-year organizational dynamics, two-year recruiting/training budgets, higher-turnover scenarios and a restricted-recruitment case (pp.2, 13–20).

The strongest modeling contribution is a clear separation between **organizational representation and event dynamics**. The same employee appears in several relationship layers; explicit monthly events change staffing and those relationships; accounting then converts the simulated history into budgets and productivity measures. This is a reusable way to turn a static organizational chart into an executable model.

## Model architecture and interfaces

1. A position-allocation procedure maps seven job categories to management and executive layers of the organizational chart (pp.3–4). Its replacement rules allow several eligible job types to fill some locations.
2. Four network layers represent department structure, friendship, information flow and leadership, with the same employee represented across layers (pp.5–8).
3. Network properties and an ability/promotion system generate five indices: department vacancy, friendship, message influence, leader departure and occupation dissatisfaction (pp.6–10).
4. AHP-derived weights combine the indices into a departure-priority score. A role-specific, externally specified churn rate determines how many departures to sample; the score selects which employees depart (pp.11–12).
5. Ordered monthly events process departure, promotion, transfer, recruitment and settlement (pp.11–13). Promotion can occur with or without a transfer, and transfer searches progress through increasingly broad organizational locations.
6. Staffing and ability feed aggregate productivity and budget accounting, followed by different churn and recruitment scenarios (pp.14–20).

This structure makes event ordering and interfaces inspectable. A departure changes vacancies, potential promotions, recruitment needs and relationships. The report explains several of these downstream consequences instead of presenting network analysis and accounting as unrelated sections.

## Approach and justification

**Author-reported rationale:** a single department graph cannot represent all relevant employee relationships, so a multiplex representation combines distinct relation types (pp.4–8). Trust and influence are simplified into the leadership layer. Monthly updates reflect pay and recruiting time units (p.10). Ability thresholds and job eligibility express the experience required for promotion (pp.9–10). The events are decomposed to improve intelligibility and reflect recognizable organizational actions (pp.11–13).

The authors explain individual indices through a mechanism: vacancies reduce cohesion, leader departures disturb morale, communication transmits dissatisfaction and blocked advancement raises dissatisfaction. They introduce degree-based and PageRank-based quantities to operationalize parts of this account (pp.6–9).

**Reviewer interpretation:** the event decomposition is better justified than several exact numerical choices. Multiple layers make a useful representation possible, but do not establish that all four materially improve predictions. No controlled single-layer versus multiplex ablation is reported. The claim that two systems both contain nodes and edges is insufficient on its own to justify PageRank as a measure of negative-message influence. The mapping needs an interpretation of transition weights, direction and the outcome it predicts.

## Data and assumptions

The paper openly states that friendship, leadership and information relations lack real data and must be constructed using assumed relationships and experience (p.7). The final limitations acknowledge randomly generated edges that may not represent reality (p.21). These are hypothetical company scenarios, not observed employee networks.

Important assumptions include the event order, no ordinary demotion/discharge, a fixed baseline churn rate, restricted advancement for administrative staff, ability-based promotion, assigned growth rates/caps and a fixed recruitment rule (pp.3, 10–13). AHP weights are reported, but the underlying pairwise judgments and consistency assessment are not shown. Productivity is a constructed ability score reduced by a weighted dissatisfaction term, not an observed monetary output (pp.15–16).

The distinction between imposed and emergent behavior is essential. The aggregate churn rate is an input; the network-derived index helps choose employees within a departure quota (pp.11–12). Thus a matching aggregate departure rate cannot independently validate the network's ability to predict departures. Layer effects could instead be tested against their implications for departure composition, productivity, vacancy distribution or other genuinely derived outcomes.

## Validation, results and limitations

The authors derive a staffing-balance equation from expected departures and recruitment, giving a steady-state count near 291 at the baseline 18% churn. They compare it with the simulation's staffing range and later use the same formula for higher churn scenarios (pp.14–15, 18–19). This is a valuable analytical consistency check on a simulation. It is not independent empirical evidence that the assumed recruiting or social mechanisms are accurate.

The budget section displays three stochastic realizations, with role-level breakdowns for recruiting, salary and training (pp.17–18). The summary's recruiting and training amounts correspond to the first displayed realization, rather than an identified ensemble mean. Three examples make randomness visible but do not establish precise uncertainty intervals. Statements that training costs are invariant should be qualified because Table 3 contains slightly different totals across realizations.

Higher-turnover scenarios produce lower staffing, greater recruiting costs and lower salary/training expenditure; the paper interprets lower total expenditure alongside the undesirable loss of capacity (pp.18–19). This is a useful example of explaining why a lower cost is not automatically a better organizational outcome. A no-external-recruitment scenario reveals leadership vacancies and a substantial staffing decline (pp.20–21).

Static review questions remain: the recruiting-event mean, recruiting interval and annual flow-balance approximation should be reconciled explicitly; symbols for occupation dissatisfaction and ability caps vary; and plausible alternatives for network construction, weights and growth parameters are not evaluated. The official statement's fraction of vacancies actively being recruited for describes recruiting activity; converting it into a fraction filled per year requires an additional timing assumption. That distinction should be traced through the recruiting rule and balance equation. No implementation is provided to resolve these questions by inspection or execution. The claimed proof of accuracy/stability in the summary is stronger than the scenario and internal-balance evidence alone supports.

## Communication strengths

The layered network picture (p.8) shows how the same individual carries different relational properties. The event-order diagram (p.11) makes a simulation assumption visible. The ability-to-productivity diagram (p.15) connects representation to an output. Role-level budget tables support interpretation rather than reporting only a single total. The scenario discussion connects spending, vacancies and productivity instead of treating each metric in isolation.

## Transferable operating rules

1. Separate static representation, state transition and outcome accounting.
2. Specify event order and eligibility rules; they are part of the mathematical model.
3. Label synthetic relationships and assumed preferences explicitly.
4. Distinguish imposed aggregate inputs from emergent outputs before designing validation.
5. Use analytical balance relations to check a simulation, while labeling them internal verification.
6. Evaluate the contribution of additional relationship layers with controlled comparisons.
7. Preserve the identity of a stochastic realization or aggregate when reporting a number.
8. Interpret cost together with service/capacity outcomes; a cheaper failure is not a better plan.

## Reading ledger

- Physical pp.1–10: summary, problem restatement, assumptions, organization allocation, all network layers and ability system read in full.
- Physical pp.11–21: all event algorithms, dynamics, productivity, budget, sensitivity, restricted-recruitment case, strengths/weaknesses and references read in full.
- Relevant diagrams, equations, trajectories and all image tables were inspected from rendered pages. No missing appendix was implied to have been read.
