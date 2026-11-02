# Evidence-to-Workflow Register

This is a living synthesis of **reviewed cases**, not a completed statistical account of the full corpus. A source paper's use of a method is not a proof that the method is appropriate everywhere. The coverage denominator is reported in [STATUS.md](STATUS.md).

## Evidence classes

- **Official requirement:** current contest instructions or policy, with version/date.
- **Official commentary:** historical judging discussion, informative but not a universal scoring formula.
- **Observed practice:** a documented modeling or communication move in an inspected paper.
- **Reviewer inference:** an interpretation or critique derived from the source, clearly distinguished from the author's claim.
- **Project design:** our chosen ownership, handoff, checkpoint or recordkeeping convention.

## Initial source-grounded rules

| Rule / lesson | Inspected support | What it supports | Scope limit | Operational destination |
|---|---|---|---|---|
| Build a connected architecture and revisit early choices using downstream feasibility | [2019 MCM B, 1924588](cases/mcm2019_b_1924588.md), especially physical pp.7–24 | Fleet, packing, deployment, routes and final range checks form a dependent chain; later location feasibility can reject an earlier fleet candidate | This is a useful architecture, not a certificate that every implementation detail is correct | Stages 1, 3, 7; model specification and change request |
| Separate environment assumptions from a policy/controller and test changes incrementally | [2004 MCM B, 381](reviews/mcm_2004/mcm_3f54f69363bd.md), pp.4–14, 15–32 | The environment, customer behavior and control policy can be examined separately; repeated simulated days expose variation | Simulation supports implications within the assumed environment, not independent empirical truth | Stages 3, 5, 6; experiment template |
| Do not reward complexity when its added value is unestablished | [2004 MCM B, 381](reviews/mcm_2004/mcm_3f54f69363bd.md), pp.29–33 | Candidly reporting similar aggregate outcomes is more informative than declaring the most complicated controller best | The source's significance wording was not independently statistically reproduced | Baseline comparison and retain/simplify decision |
| Track information flowing across spatial, temporal and policy models | [2018 ICM D, 78826](reviews/mcm_2018/mcm_ed3ee7b716f1.md) | Network design, construction sequence, adoption timeline and country transfer have distinct roles and interfaces | Sequential presentation can conceal weak feedback or calibration; inspect actual coupling | Stage 3 architecture and Stage 7 integration |
| Distinguish observed, mapped and simulated quantities | [2017 HiMCM B, 8121](reviews/himcm/HIMCM_2017_B_8121.md), pp.9–11 | Simulated trail attributes do not by themselves prove a geographically feasible trail design | Case-specific terrain issue; general rule concerns provenance and claim strength | Data template, feasibility checks and claim register |
| Justify the meaning of weights and transformations, and test ranking stability | [2017 HiMCM B, 8121](reviews/himcm/HIMCM_2017_B_8121.md), pp.6–9, 13–19, 23–25 | Interpretable factor directions are helpful, but preferences and calibration choices still need support | External ranking agreement is comparative evidence, not objective ground truth | Approach chapter: evaluation and ranking |
| Choose an appropriate primary model and explain why; connect assumptions to actual use | Official [HiMCM commentary](../../HIMCM_备赛资料/03_论文与评审/官方评审/Cons_HiMCM.pdf), physical pp.6–11 | Clear choices, purposeful assumptions, model development and explanation matter | Historical commentary, not a requirement to reproduce a highlighted method | Stages 2–4 and argument writing |
| Human checkpoints, sole-writer files and versioned handoffs | Project design; [coordination protocol](../COORDINATION.md) and [product sources](../setup/SOURCES.md) | A practical way to coordinate separate contexts and prevent conflicting edits | Written conventions are not technical enforcement or proof of correctness | Roles, task/state/handoff records |
| Separate imposed inputs from emergent outputs when validating a simulation | [2015 C, 33572](reviews/mcm_2015/mcm_b32fb4b143f7.md), pp.11–15 | A fixed aggregate churn rate and network-selected departure composition have different evidential roles; analytical flow balance is an internal check | No numerical reconstruction or empirical validation was performed | Simulation guidance and model-specification template |
| Compare assumptions and scenario definitions before comparing conclusions | [All six local 2015 ICM C papers](cases/2015_ICM_C_complete_local_comparison.md), especially sections 3–6 | Persistent entities, event rules, hiring restrictions and imposed targets can explain differing recommendations; tiny cases can expose formula/meaning mismatches | Complete local same-problem reading; no numerical reproduction or universal award explanation | Assumption guidance, simulation guidance, model-specification and review templates |

## Further complete local comparisons

| Rule / lesson | Inspected support | What it supports | Scope limit | Operational destination |
|---|---|---|---|---|
| Separate measurement, forecast, intervention response and decision; justify each connection | [All six local 2015 ICM D papers](cases/2015_ICM_D_complete_local_comparison.md) | Distinct measurement architectures can be useful, but policy claims require feasible actions, costs and response evidence; zero intervention must recover baseline | Full local same-problem reading, not empirical validation or award explanation | Approach section 7.7; model specification and review templates |
| Check a learned surrogate against the direct function before interpreting its response curves | [2015 D, 35630](reviews/mcm_2015/mcm_4113751a8ab0.md), pp.10–17 | Synthetic data and a low training error do not supply independent evidence; an unexplained reversal can be approximation error | Static review of paper and figures; no network rerun | Approach section 7.7; surrogate purpose and fidelity fields |
| Define exact policy scope and preserve the accounting chain through substitution | [All four local HiMCM 2019 B papers](cases/himcm_2019_B_complete_comparison.md) | Policy scope, behavior, material quantities and stakeholder outcomes are separate interfaces; survey-to-variable mapping makes a data plan inspectable | Historical case comparison; no numerical reproduction | Requirements, data dictionaries, scenario and review records |
| Validate each physical conversion and the final endpoint separately | [All four local 2012 MCM A papers](cases/2012_MCM_A_complete_local_comparison.md) | Geometry, exposure, physiological rates and mass are different validation targets; one authoritative implementation prevents equation/figure drift | Complete local reading; no complete numerical reproduction | Stage 4 interfaces; Stage 5 implementation; approach sections 7.4–7.5 |
| Distinguish predicted events, active demand, mean capacity and feasible service | [2015 A, 32150](reviews/mcm_2015/mcm_b7715ba1fb8a.md), physical pp.16–25 and 33–34 | Demand definition and inventory timing connect a fitted mechanism to an operational plan; geometric centers still require site/route feasibility | Individual reviewed architecture, not a completed comparison of all 2015 A papers | Model interface template; stages 3–4 and public-letter checks |
| Preserve implementation maturity and evidence limits in the final answer | [2015 A, 32722](reviews/mcm_2015/mcm_037c369c63c7.md), physical pp.16–35 and 38–39 | Toy experiments, proposed geographic extension and real deployment are different achievements; unsupported scaling and supply rules constrain inference | Source explicitly discloses limitations; no simulator rerun | G3, claim index, approach evidence ladder and delivery writing |
| Preserve the meaning of preferences and hard eligibility when building a personalized ranking | [All five local HiMCM 2020 A papers](cases/himcm_2020_A_complete_comparison.md) | User responsiveness, data robustness and representation correctness require different checks; category-level recommendations do not guarantee an available eligible offer | Complete local paper comparison; specific findings remain tied to individual reviews | Interface schema and eligibility fields; ranking and requirement review |

## Required synthesis after each research batch

1. Compare approaches to the same problem using common task definitions.
2. Record which findings recur and which depend on one problem's structure.
3. Preserve counterexamples and alternative successful architectures.
4. Add or revise a specific workflow rule, template field or example only when the evidence warrants it.
5. Keep the source distinction between explicit author rationale and reviewer reconstruction.
6. Update coverage and the status of unresolved hypotheses.

## Open synthesis questions

- When does a sequential architecture adequately represent feedback, and when does it require a joint formulation?
- Which baseline and validation choices recur across mechanism, forecast, ranking and optimization tasks?
- How do stronger papers explain consequential simplifications and data gaps?
- Which claims repeatedly outrun the evidence, even in otherwise strong papers?
- What modeling depth transfers well to HiMCM without imposing unnecessary computational or exposition burden?

These questions guide the remaining full reading. They are not findings about unread papers.
