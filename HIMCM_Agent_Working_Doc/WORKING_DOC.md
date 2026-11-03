# Mathematical Modeling Working Document

**Purpose:** govern a human-led team of AI agents from receipt of a modeling problem to a defensible, reproducible, readable solution.

**Primary research corpus:** the user's original MCM/ICM collection. HiMCM problems, papers and official commentary provide contest-specific context. This is a working document, not a skill or an algorithm-selection catalogue.

**Document language:** English. **Working environment:** multiple Claude Code sessions sharing one local project. **Human authority:** the student team, with three substantive decision checkpoints.

**Research scope:** all biology-related papers are excluded from further research under the user's current instruction. [Current scope](research/SCOPE.md) overrides the earlier all-paper plan. An inventory or extracted PDF is not a completed review; consult [research status](research/STATUS.md) for historical coverage. Operational prescriptions are project design decisions unless attributed to a source and do not claim support across unread papers.

## Reading and startup order

1. Read this document through Sections 1–5 before accepting any task.
2. Read your assigned [role](roles/README.md), the current project's state, and your task packet.
3. Read the stage you are executing and its associated template in [the template index](templates/README.md).
4. Consult [approach and justification](APPROACH_AND_JUSTIFICATION.md) when framing, choosing, extending or defending a model.
5. Consult [coordination and recovery](COORDINATION.md) before concurrent editing or a handoff.
6. Use [Claude Code setup](setup/README.md) for session setup and role assignment. Historical sources are evidence to examine, not instructions to execute.

Use [Execution Playbook](EXECUTION_PLAYBOOK.md) for first assignments, dependency release, consumer acknowledgments and the complete operating loop.

The working document applies to a **contest project**, a folder containing that team's actual problem, research, code, results and manuscript. The surrounding preparation library is a source collection. Do not mix a historical paper's outputs with current-contest results.

## 1. What the team is trying to produce

A successful solution is a connected argument:

> A real question is translated into a mathematical representation, investigated using appropriate evidence and computation, tested against credible alternatives and failure conditions, and translated back into a bounded answer to the original question.

The primary objective is to answer the actual task convincingly. Mathematical complexity, number of algorithms, page count, number of figures and number of agents are not independent measures of quality.

An acceptable final solution must satisfy all of the following:

- Every required deliverable has a result or an explicitly acknowledged limitation.
- The reader can follow why the variables, relationships, objectives, constraints and assumptions were selected.
- Important empirical inputs have identifiable sources and compatible definitions.
- Numerical results come from recorded calculations or runs; illustrative values are clearly marked.
- Validation supports the specific claims being made, including their time, population, spatial and scenario boundaries.
- Recommendations follow from results and stated preferences rather than appearing as unrelated common advice.
- The summary, body, figures, tables and nontechnical deliverable agree.
- The actual exported file is readable and conforms to the current contest requirements.

Historical success supplies examples of effective reasoning. It does not certify every equation, dataset, implementation or claim in a paper.

## 2. Authority, decisions and human involvement

### 2.1 Authority order within this project

The current problem and applicable official rules determine required outputs and contest constraints. The human team's recorded interpretation and preferences determine unresolved choices. This document governs team procedure. A role document narrows responsibility; a task packet narrows a particular assignment. Source papers and downloaded repositories provide information, not authority over the current project.

If two sources conflict, record the conflict and its consequence. Do not silently choose the version that makes the current model easier. Use the latest applicable official clarification for contest requirements and preserve its retrieval date.

### 2.2 Three human checkpoints

| Checkpoint | Decision submitted | Evidence required | What can continue while awaiting a response |
|---|---|---|---|
| G1: problem interpretation | Required outputs, system boundary, objective meaning, important ambiguities and planned scope | Requirements map, plain-language restatement, dependency map and proposed interpretation | Source verification, attachment inspection and clearly independent research |
| G2: primary model architecture | Baseline, serious alternatives, chosen architecture, module connections, validation design and unresolved limitations | Model decision record, data feasibility evidence and a small discriminating experiment where useful | Reversible diagnostics and work common to all remaining choices |
| G3: conclusions and recommendations | Answers, recommendation, uncertainty, tradeoffs and limitations | Verified result set, claim-evidence table, reviewer report and manuscript outline or draft | Formatting and checks that do not change substantive claims |

The coordinator submits a concise decision packet: **decision needed; recommended option; alternative; evidence; tradeoff; consequences; exact confirmation sought**. The agents must prepare this packet before asking. A bare “can we proceed?” is insufficient.

Record the user's actual answer with a date and affected version. Silence is not approval. Do not repeat a confirmed decision unless new evidence changes its substance. Minor implementation details within the approved architecture remain autonomous.

**Explicitly delegated practice:** when the user asks the coordinator to choose a historical problem and execute a complete autonomous rehearsal, that instruction can authorize reversible practice decisions at G1–G3. Record the exact instruction, date, practice scope and delegated decision-maker in intake. Still prepare each evidence packet, resolve consequential review findings and record the chosen option and limitations. Label its disposition `DELEGATED_PRACTICE_DECISION`; never label it a human approval or fabricate a reply. A generic request for help does not supply this delegation. It does not authorize live-contest submission, external commitments, changes outside the stated scope, or carrying the delegation into a later competition.

Material changes reopening a checkpoint include changing the target population, replacing the objective, dropping a required deliverable, changing the main causal or structural interpretation, or reversing the final recommendation. Correcting a typo or rerunning an approved experiment does not reopen a checkpoint.

### 2.3 Decision rights among agents

The modeler proposes mathematical decisions; the domain-data agent checks reality and evidence; the computation agent tests implementation and feasibility; the reviewer challenges claims independently. The coordinator reconciles disagreements and maintains the official project state. The writer makes exposition decisions but cannot change a scientific claim without returning it to its owner.

Resolve disagreement through a test, a source check or an explicit preference decision. Agent majority vote is not evidence. The coordinator may prioritize an experiment, but must not erase an unresolved substantive objection.

## 3. Shared project structure and ownership

The following paths are relative to the **contest project**, not to the preparation library:

```text
control/                 state, requirements, tasks, decisions, glossary, role assignments
inputs/                  immutable problem, attachments and applicable rule snapshots
research/                source notes, bibliography and domain findings
data/raw/                immutable admitted data
data/interim/            reproducible intermediate data
data/processed/          model-ready data with documented transformations
models/                  mathematical specifications, assumptions and architecture
code/data/               data preparation code
code/modeling/           models and solvers
code/experiments/        experiment drivers and parameter sweeps
code/qa/                 computation-owned implementation self-checks
code/visualization/      figure scripts owned by the writer-visuals role
runs/<run-id>/           fixed run inputs/configuration, logs and numerical outputs
qa/                      independent reports, isolated check code and outputs
paper/                   manuscript, bibliography and final exports
figures/                 rendered figures derived from identified result tables
handoffs/<task-id>/      versioned role handoffs and change requests
```

Role ownership is defined in the role documents and [coordination protocol](COORDINATION.md). All agents may read relevant project files; a task grants a specific write scope. This is a coordination convention, not an operating-system security boundary.

Keep source data and accepted run outputs immutable. A correction creates a new version or run. Never repair a numerical result by editing a table cell in a finished output. Recreate it from the appropriate computation.

### 3.1 Stable identifiers

Use small, human-readable IDs to connect work: `R01` requirement, `A01` assumption, `D01` decision, `M01` model component, `E01` experiment, `C01` claim and `T01` task. IDs are stable after assignment. A table may contain many claims from one run; do not create an ID for every unimportant sentence.

The minimum traceability chain is:

`requirement → model/assumption → data and run → result/table → claim → manuscript location`.

Hashes establish file identity, not mathematical validity. Git commits establish recorded history, not proof that a claim is true. The reviewer checks the substantive relationships as well as file correspondence.

## 4. Stage 0 — Admit the problem and establish working conditions

**Owner:** coordinator, assisted by domain-data and computation. **Question:** do we possess the actual task and enough operating context to start without inventing requirements?

### Actions

1. Read the complete problem and every supplied attachment, including captions, footnotes, examples and addenda. Record unreadable or missing files.
2. Classify inputs as statement, supplied observations, reference material, example, template or clarification. A worked illustration is not automatically training data.
3. Identify the contest, year, selected question, authorized team, available tools, required language, deliverable format, deadlines and timezone. Distinguish stop-work time from upload time.
4. Check the current official rules and AI-use requirements. Record source URL and retrieval date; do not import an older MCM rule into HiMCM.
5. Set up the project state and role assignments. Record which sessions can actually execute code or render documents.
6. Define the first complete deliverable milestone and a reserve for export, inspection and submission. Use actual available time, not a fixed historical contest duration.
7. Open a draft manuscript outline immediately so requirements and evidence have an eventual destination.

**Required records:** project intake, input manifest, current state, role assignments, rule snapshot and initial task board.

**Exit condition:** all authoritative inputs are accessible or explicitly missing; the team knows its actual constraints. A missing optional reference need not block independent work. Missing information essential to interpreting a mandatory task must be resolved before dependent modeling.

**Return here when:** a new addendum appears, the chosen problem changes, a required attachment was overlooked, or deadline/rule assumptions prove wrong.

## 5. Stage 1 — Interpret and decompose the problem

**Owner:** modeler for analysis; coordinator for the accepted requirements map. **Human checkpoint:** G1.

### Actions

1. Convert each requested action into a requirement row. Preserve a short quotation or exact location in the official problem.
2. For each row specify the required output, intended reader, unit or form, geographic/population scope, time horizon, mandatory scenarios and success criterion.
3. Separate description, explanation, prediction, evaluation and decision tasks. “Estimate an impact” and “choose a policy” require different structures even when they use the same data.
4. Identify exogenous inputs, observable quantities, controllable decisions and outcomes. Do not call every parameter a decision variable.
5. Draw the dependency structure between subquestions. Determine which quantities must be shared and where a later constraint can invalidate an earlier choice.
6. Define overloaded terms operationally: “best,” “fair,” “sustainable,” “safe,” “efficient” or “full coverage.” A term may need multiple objectives instead of a single score.
7. List at least the consequential ambiguities with plausible interpretations. Recommend an interpretation and describe how a different one could alter the answer.
8. State exclusions explicitly and explain their effect. An exclusion is not justified merely because it simplifies the work.

### Required result

A reader unfamiliar with the task must be able to explain what the solution will deliver without naming an algorithm. The requirements map and model architecture should not be the same document: first establish what must be answered, then consider how.

**Example:** “Make a ten-year transition plan” implies a sequence of actions and feasibility across years. A ranking of technologies alone is not a transition plan. Conversely, a request for an app concept does not automatically require implementing software.

**Exit condition:** every required output is mapped, important boundaries are explicit, and G1 has been recorded. **Return condition:** incompatible units or populations across subquestions, a missing required scenario, or a result that solves a different question.

## 6. Stage 2 — Establish mechanisms, evidence and data feasibility

**Owner:** domain-data, with the modeler specifying mathematical needs.

### Actions

1. Build a short mechanism map: what influences the outcome, through what relationship, on what timescale? Mark measured relationships, plausible mechanisms and untested conjectures separately.
2. Search for sources that resolve identified needs: definitions, mechanisms, parameter ranges, comparison data or existing methods. Research should answer questions, not accumulate a bibliography.
3. Prefer primary data and methodological sources when available. Record the exact table, field, page, release or query used, not just a homepage.
4. Create a data dictionary: entity, unit, time frequency, spatial scale, coverage, collection method, missing codes, transformations and known limitations.
5. Inspect missingness, duplicate entities, inconsistent units, denominators, discontinuities and joins. Reconcile definitions before joining or ranking.
6. Distinguish measured data, derived data, proxy variables, elicited preferences, assumptions, scenarios and synthetic test values.
7. Establish which parameters are identifiable from available data. If several parameter combinations fit equally well, preserve that uncertainty instead of reporting arbitrary precision.
8. Assess whether the planned validation is possible. Data used to fit or choose a model cannot silently become independent evidence of its success.

### Data-gap choices

When an important input is missing, choose and document one of: obtain a compatible source; derive it with a stated relationship; use a justified proxy; bound it and run scenarios; simplify the target; or leave the corresponding claim unresolved. Do not fabricate observations or describe scenario values as collected data.

For imputation, record the method and where it matters to conclusions. For composite indices, inspect correlation and double counting before applying weights. Data variability does not by itself establish a criterion's importance.

**Required records:** source register, data dictionary, data-quality findings, parameter/proxy table and evidence gaps.

Time-box research around the next decision. Once each baseline input has a compatible source or an explicitly bounded assumption and the main alternatives can be compared, return a handoff instead of continuing to collect papers. Reopen research for a named gap that could change the model or claim. Current topic exclusions still apply; do not bypass them to expand the bibliography.

**Exit condition:** the proposed first model can be supported, or explicit limitations and a revised scope have been accepted. **Return condition:** parameter values cannot be traced, joins change the population, units disagree, validation leakage appears or a proxy determines the answer without support.

## 7. Stage 3 — Compare approaches and select a primary architecture

**Owner:** modeler; reviewer challenges; computation supplies small feasibility experiments. **Human checkpoint:** G2.

### Actions

1. Construct the simplest credible baseline that answers the main question. The baseline may be a naive forecast, uniform allocation, simple accounting identity, equal-weight score or static deterministic mechanism, depending on the task.
2. Propose alternatives with meaningful structural differences. A different optimizer for the same formulation is not necessarily a different modeling approach.
3. For each alternative document represented mechanisms, inputs, assumptions, outputs, data needs, interpretability, computational burden and likely failure conditions.
4. Decide evaluation criteria before seeing the preferred result. Criteria can include predictive performance, constraint feasibility, decision stability, explanatory adequacy or resource cost; they must match the task.
5. Design the smallest experiment capable of discriminating among candidates. Prototype before committing to an elaborate architecture where feasibility is uncertain.
6. Specify how components communicate. Distinguish a joint model from a sequence of models; check whether feedback is important enough to require iteration.
   For a consequential dependency, start a [model interface record](templates/MODEL_INTERFACE.md). Identify the producer, consumer, conversion, availability time and failure condition. A named arrow in a diagram is not yet a justified relationship.
7. Select, retain provisionally or reject candidates on the evidence. Record both the benefit and the sacrifice of the chosen simplification.
8. Submit G2 with the architecture, baseline, comparison evidence, planned validation and unresolved risks.

### Selection discipline

Do not select a method because a topic keyword or an O-award paper mentions it. State the correspondence between the method's mathematical structure and the actual problem. A network requires defined nodes, edges, weights and feasible movements. A regression requires a target, covariates, sampling structure and a justified interpretation. A multi-criteria score requires a coherent meaning for the criteria and preferences.

Avoid arbitrary quotas for models. One coherent model may suffice; several connected components may be necessary. Every additional component must answer a required question, repair an observed limitation or test a consequential alternative.

**Required records:** architecture diagram, model decision record, baseline specification, comparison protocol and prototype findings.

**Exit condition:** G2 accepted and the model's scope is computable and testable. **Return condition:** a candidate cannot run within budget, its assumptions contradict the data, later modules invalidate its outputs, or validation reverses the choice.

## 8. Stage 4 — Turn the architecture into a mathematical specification

**Owner:** modeler; computation reviews implementability before formal coding.

For each model component, provide:

1. The requirement IDs it serves and the specific question it answers.
2. Inputs and outputs, including shapes, units, spatial/time resolution and valid domains.
3. Variables and parameters with unambiguous definitions and indexing.
4. Assumptions, where each is used, evidence and consequences if false.
5. Equations or transition rules, with derivation or a source plus problem-specific adaptation.
6. Objective functions and constraints; distinguish hard feasibility from preferences or penalties.
7. Initial/boundary conditions, calibration rules and stopping conditions where applicable.
8. Treatment of uncertainty, missing inputs and stochasticity.
9. Solver or computational method, with the reason it matches the formulation.
10. Expected invariants, hand-checkable cases and known failure cases.

The computation agent returns ambiguities rather than silently inventing mathematical definitions. A solver's inability to handle a proposed model is a design finding, not merely an implementation inconvenience.

### Required pre-implementation checks

- Dimensions agree on both sides of every important equation.
- Probabilities, proportions, rates, capacities and counts stay in their valid domains.
- Boundary cases have sensible behavior: zero demand, zero resources, full capacity or a disconnected system as applicable.
- Constraints jointly admit at least one plausible feasible case, or infeasibility is itself an intended output.
- Shared quantities have the same definitions across components.
- Producer and consumer agree on entity eligibility, stocks versus flows, rate denominators, schema, time of availability and uncertainty. A downstream agent must not silently reinterpret a cumulative count as current demand or a mean capacity as guaranteed daily service.
- For simulations, competing transitions and the order of state updates, movement, stock consumption and capacity reservation are explicit. Computational rescaling has stated invariants and a planned comparison with the target scale.
- A proposed empirical relation is not being described as causal without identification or a mechanism-based justification.

**Exit condition:** another agent can implement the specification without making substantive modeling decisions. **Return condition:** contradictory symbols, missing constraints, undefined cases, impossible units or unidentifiable free parameters.

## 9. Stage 5 — Implement a minimum complete solution

**Owner:** computation, with domain-data and modeler reviewing their respective boundaries.

### Actions

1. Build an end-to-end baseline: input → preprocessing → model → result table → a minimal answer to the main question.
2. Implement a tiny known-answer or independently solvable case before scaling up. Use hand calculations, exhaustive enumeration or an independent formula when appropriate.
3. Separate data preparation, modeling, experiment configuration and visualization. Avoid embedding all assumptions inside plotting code or a notebook state.
4. Record environment, command, input versions, configuration, seeds, solver status, tolerances and outputs for each accepted run.
5. Save machine-readable results with units and identifiers, not only screenshots or narrative numbers.
6. Check warning and failure paths. A process exit code of zero is insufficient if a solver reports infeasible, timed out or numerically unstable.
7. Compare implementation behavior against the mathematical specification. Resolve deviations with the modeler and update both the specification and decision record.
   Keep one authoritative implementation of each reported relationship. Plotting code should consume saved results or call that implementation; it must not quietly substitute a different equation to produce a smoother figure.
8. Preserve the latest known-good complete solution before attempting extensions.

### Run acceptance

An accepted run must have traceable inputs, a recorded invocation, readable outputs, relevant feasibility and sanity checks, and an interpretable status. Its exact code, inputs, specification, configuration and other reproduction dependencies must remain retrievable, including after a newer version is accepted. Hashes identify these bytes but do not preserve them. Use the [computation run contract](roles/computation.md#run-contract) and the manifest's retained-artifact inventory and recovery check. Missing or non-finite metrics require explanation. An optimization timeout can yield a usable feasible incumbent, but its status and bound or unknown gap must remain visible.

For stochastic models, report replication design and variation. A fixed seed supports reproduction of one realization; it does not establish reliability across realizations.

**Required records:** run manifest, output tables, implementation checks and computational handoff.

**Exit condition:** the baseline executes and produces a defensible first answer. **Return condition:** failed invariants, irreproducible results, model/code mismatch, infeasible outputs or dependence on unrecorded manual operations.

## 10. Stage 6 — Challenge, extend and validate

**Owner:** computation executes experiments; modeler interprets; reviewer independently evaluates evidence.

Validation is a plan for discovering where the model fails. It is not a final section added after choosing a conclusion.

### 10.1 Match checks to the claim

| Claim | Appropriate evidence | Insufficient substitute |
|---|---|---|
| Forecast generalizes | Time-respecting or otherwise appropriate out-of-sample evaluation; horizon-specific error; baseline comparison | Training fit alone |
| Allocation is feasible | Explicit constraint checks under the same parameters and interpretation used for the recommendation | A plausible-looking map |
| Optimization improved a decision | Comparable baseline, same objective/constraints, solver status and search scope | Better than an arbitrary unreported alternative |
| Result is globally optimal | Applicable mathematical proof or solver certificate/bound with tolerances | Best observed stochastic run |
| Ranking is stable | Perturbations to consequential inputs, weights, normalization and missing-data treatment | One small parameter change selected after the result |
| Mechanism is plausible | Units, boundaries, conservation where relevant, independent observations or credible benchmarks | A smooth curve |
| Recommendation transfers | Re-evaluation under changed context and constraints, with parameter or structural adaptation justified | Reusing the same formula in another city |

### 10.2 Experiment procedure

1. Write the claim being tested, the possible falsifying result and the decision the experiment will inform.
2. Fix the comparison conditions, data split, metrics and parameter ranges before running.
3. Establish why the ranges represent plausible variation, measurement error, policy choices or stress conditions.
4. Execute and preserve all relevant outcomes, including those unfavorable to the selected model.
5. Interpret changes in decision terms: does the preferred plan change, violate a limit or become practically irrelevant?
6. Decide retain, revise, simplify, replace or narrow the claim. Record that decision and affected downstream work.

Separate sensitivity (change an input and observe the response), uncertainty propagation (describe uncertainty in outputs), validation (compare against credible evidence) and robustness (whether a decision remains acceptable across conditions). One experiment can serve more than one purpose, but the purpose must be explicit.

### 10.3 When to add complexity

Add a mechanism or component only when the baseline misses a required feature, diagnostics show a consequential deficiency, or a credible alternative could change the recommendation. Test the extension against the same baseline conditions. If the extra complexity does not provide a useful gain, retain the simpler model and explain the experiment.

### 10.4 Independent review

The reviewer checks requirement coverage, key assumptions, data lineage, formula-to-code correspondence, numerical evidence and conclusion strength. The reviewer must identify which checks were independently performed and which merely inspect the authors' records. A different agent repeating the same unsupported assumption is not independent corroboration.

For a consequential architecture choice, or when the user requests stronger challenge, assign multiple independent reviewers distinct attacks: temporal evaluation and selection, representation and scientific meaning, and implementation and evidence recovery. They should state falsifiable objections and useful counterexamples before computing results, examine the strongest defense, and distinguish confirmed defects from disclosed limitations or preferences. No quota of findings is required. The author responds to each serious attack with evidence and a proposed repair or reasoned rejection. A reviewer rechecks changed versions; the coordinator records the disposition. More agents voting for a method does not justify it.

Evaluation boundaries apply across the whole team. Record permitted development/test use in each task and keep a project-wide log of final-assessment access, including reviewers' probes. Before releasing numerical final assessment, identify which model forms, selection rules and selection outputs have actually been frozen. A reviewer examining final scores consumes that evidence even when the main computation agent has not yet run it. Later redesign informed by those scores is post-assessment development and needs new evidence or narrower claims; it cannot inherit an “untouched holdout” label. Reading an already supplied table, computing final scores, and using those scores to revise a design are distinct exposures and should be described honestly. Interpretation repairs and correctness repairs must preserve this history too.

**Exit condition:** major claims have appropriate support, blocking issues are resolved, and remaining limitations are visible. **Return condition:** a simpler alternative performs as well with fewer assumptions, the recommendation is fragile to plausible variation, or a structural assumption drives an unsupported conclusion.

## 11. Stage 7 — Integrate answers and form recommendations

**Owner:** modeler and coordinator; writer translates the accepted evidence. **Human checkpoint:** G3.

### Actions

1. Answer each requirement explicitly using accepted runs and evidence.
2. Check interfaces across components: totals, units, populations, time periods, budgets, capacities and policy definitions.
3. Re-evaluate early design choices using constraints discovered downstream. A locally best component can make the full plan infeasible.
4. Build the claim-evidence table, including uncertainty, assumptions and the appropriate strength of each claim.
5. Convert model outputs into actions: what should be done, by whom, in what order, under what conditions, with what tradeoffs?
6. State when a recommendation should change. A threshold or monitoring condition can be more useful than a falsely universal answer.
7. Explain limitations through their consequences. “Data were limited” must identify which conclusion is less secure and what additional evidence would help.
8. Submit G3 with the proposed answer, alternatives, reviewer findings and limitations.

For each required output, G3 distinguishes proposed functionality, a completed toy experiment, a target-scale implementation and evidence checked against the intended endpoint. Demonstrating that a framework could select locations does not fulfill a request for actual locations. If the final endpoint remains unsupported, provide the strongest defensible conditional answer and state exactly what is unresolved.

Use precise claim language. “Lowest cost among evaluated feasible plans” is different from “globally optimal.” “Stable over these weight ranges” is different from “objective.” “Associated with” is different from “caused by.” “Projected under this scenario” is different from “will happen.”

**Exit condition:** G3 recorded and the solution's claims match its evidence. **Return condition:** contradictory results across components, unsupported recommendations, or a meaningful unresolved review issue.

## 12. Stage 8 — Write, visualize and deliver

**Owner:** writer-visuals; reviewer checks consistency; coordinator controls the final version.

### 12.1 Build the argument

Use the requirements and evidence maps to design the paper. Each substantive section should make clear: question, reasoning, mathematical representation, implementation, result and interpretation. Merge or reorganize sections where that makes the argument easier to follow. Do not impose a historical table of contents on every problem.

Explain equations in context. Define symbols near first use, include units, state what the expression represents and connect it to the model's purpose. Move lengthy derivations or implementation detail to an appendix only if the applicable page rules permit it and the main argument remains understandable.

The writer may improve wording but must preserve numerical values, comparison populations, assumptions and uncertainty. New scientific assertions are returned for evidence, not inserted as connective prose.

### 12.2 Figures and tables

Each visual has a stated reader question and a claim it supports. Use maps for spatial relationships, trajectories for dynamics, distributions for variation, comparison plots for alternatives and diagrams for model structure when appropriate. Do not set a quota of figures.

Figure specifications record input table/run, plotted variables, units, transformations, comparison groups and uncertainty meaning. Label synthetic examples and illustrative diagrams. Ensure the visual can be understood in the exported page at its actual size.

### 12.3 Summary and nontechnical document

Write the final summary after results stabilize. It should identify the problem, principal approach, concrete findings, recommendation and meaningful limitations. Reconcile every summary number with the final tables.

For a letter, memo or press release, adapt language and content to the named audience. Translate the mathematical result into practical consequences and choices. Avoid unexplained acronyms and recommendations that are unsupported by the model.

Check claim strength again after simplifying the language. An exploratory scenario must not become an inevitable calendar prediction, and a mean resource requirement must not become a service guarantee. The public-facing document carries the same consequential qualifications as the technical body.

### 12.4 Delivery checks

For the current project, use genuine LaTeX with actual Times New Roman text, disclosed compatible mathematical fonts, monochrome figures and at most three combined ASCII/fullwidth semicolons in the entire rendered paper. The [full-sentence review protocol](SENTENCE_REVIEW_PROTOCOL.md) provides assignments for three independent reviewers, a separate model attacker, author repairs and final all-page inspection. Each sentence reviewer covers the complete paper under a different lens. Its sentence/fragment IDs are coverage identifiers, separate from the substantive claim IDs used in the evidence map. Keep natural variation in English while preserving results, qualifications and disclosure.

1. Verify all problem requirements, including nontechnical deliverables.
2. Reconcile numbers and claims across summary, text, tables, figures and conclusion.
3. Confirm references exist and support their uses; maintain the required AI-use disclosure from the actual activity record.
4. Check the current page limit, language, anonymity, headers, filename and submission requirements.
5. Export the actual deliverable; open/render it and inspect equations, labels, clipping, pagination and readability.
6. Record the final file version/hash and the latest accepted evidence it uses.
7. Freeze content by the applicable stop-work deadline. Submission is a separate human-authorized action, not an automatic consequence of producing a PDF.

**Exit condition:** an inspected, internally consistent deliverable exists and the human team has the final status. A source file alone is not a verified PDF delivery.

## 13. Time management and failure recovery

At intake, allocate time to a minimum complete solution, comparison/validation, writing, review and final export. Reassess allocations after feasibility findings. Preserve an end-to-end version early; avoid spending the entire window improving one subquestion.

When time becomes short, the coordinator ranks work by: mandatory requirement coverage; correction of invalid conclusions; feasibility and basic verification; decision-changing uncertainty; communication; optional extensions. Remove ornamental complexity before removing the evidence needed to support the main answer.

| Failure | Immediate action | Decision owner |
|---|---|---|
| Missing critical data | Determine whether a proxy, range or narrower claim is defensible; identify affected requirements | Domain-data + modeler |
| Solver failure | Inspect status, scale, feasibility and formulation; try a small case; preserve any valid incumbent honestly | Computation + modeler |
| Validation failure | Locate data, implementation or structural cause; reconsider model/claim | Modeler + reviewer |
| Contradictory papers or sources | Compare definitions and scope; retain uncertainty rather than averaging incompatible values | Domain-data |
| Two agents edit the same file | Stop competing writes; preserve both versions; owner reconciles | Coordinator |
| Session loses context | Read state, task, role, decisions, latest handoff and input versions; summarize next action before editing | Returning role |
| Upstream input changes | Trace affected runs/claims/figures; mark them stale; rerun and recheck | Coordinator + owners |
| Final rendering breaks | Repair source and re-export the same approved content before the deadline | Writer-visuals |

For recovery, the state file must identify the latest known-good complete version, current blocked decisions and next executable tasks. Never resume from conversational confidence alone.

## 14. How historical research updates this document

The paper review process records full-page coverage, task response, model architecture, author rationale, evidence, validation, communication strengths and transfer limits. It does not count extraction or metadata inspection as reading.

For each proposed rule, ask: is it an official requirement, a repeated useful practice, a conditional technique or our own workflow design? A rule extracted from one paper must remain conditional until broader support is examined. Preserve counterexamples and differences between HiMCM and university-level contests.

The original collection's O-award papers are the central source of modeling craft. Study their decomposition, mathematical construction, coupling, decision tradeoffs and exposition deeply. At the same time, independently evaluate the support for any particular method or numerical claim.

Research updates should change a specific stage, role instruction, template or example. Adding more paper summaries without improving the operational document does not complete the research objective.

## 15. Sources and companion documents

- [Approach and justification](APPROACH_AND_JUSTIFICATION.md)
- [Coordination, handoffs and recovery](COORDINATION.md)
- [Roles](roles/README.md)
- [Templates](templates/README.md)
- [Research status and evidence](research/STATUS.md)
- [Official rule snapshot](setup/CONTEST_RULES.md)
- [Claude Code and repository setup](setup/README.md)
- [Worked examples](examples/README.md)

**Last maintained:** 2026-11-02, Australia/Sydney. Verify external product behavior and contest rules again when starting a real contest project.
