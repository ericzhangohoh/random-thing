# Worked walkthrough: six agents scheduling equipment upgrades

This is a **wholly synthetic practice example**, not a historical HiMCM problem or an executed project. Its purpose is to show precisely how six roles share one project from problem receipt to delivery. All project numbers below are invented teaching inputs. No solver has been run, no agent sessions have been launched, no acceptance has occurred, and no files under the illustrated active-project paths have been created by this example.

Use this alongside [the working document](../WORKING_DOC.md), [coordination](../COORDINATION.md), [the shared-directory protocol](../setup/SHARED_DIRECTORY_PROTOCOL.md), and [the six roles](../roles/README.md). The role names, ownership boundaries, task states, review verdicts, and G1/G2/G3 checkpoints come from those documents. The equipment scenario and dispatch sequence below are an operational illustration, not empirical evidence that this particular approach wins a competition.

## 1. The practice prompt arrives

Assume the human team receives this fictional prompt:

> A school council must schedule twelve equipment-upgrade projects over six months. Every project must finish by the end of month six. Projects require spending in particular months after they begin, and each requires a technician crew while active. At most two crews are available. Some projects require another upgrade to finish first. Recommend a schedule and monthly funding plan, explain the order of priority, examine uncertainty in costs and crew availability, and write a one-page memo for the council. The attachment contains project IDs, durations, expenditure profiles, dependencies, and stated service priorities.

This says what to deliver; it does **not** yet define whether unused monthly funding can carry forward, when funds arrive, whether crews are interchangeable, or how “priority” should influence the objective. Those questions are framing work. They are not implementation details that the computation agent may silently choose.

Use two distinct roots:

```text
DOC_ROOT     = /absolute/path/to/HIMCM_Agent_Working_Doc
PROJECT_ROOT = /absolute/path/to/equipment-upgrades-practice
```

All active-project paths in this walkthrough are relative to `PROJECT_ROOT`. The reusable document, historical source library, and this example remain outside the active project's result directories. Replace the roots with real absolute paths before sending a prompt.

## 2. Assign actual Claude sessions

The default is six logical roles with separate conversations. A role is a responsibility; it does not require six paid accounts or six continuously running processes.

| Terminal/session label | Canonical role | First useful responsibility |
|---|---|---|
| C | coordinator | Admit the task, maintain shared records, dispatch and integrate |
| D | domain-data | Read supplied sources, preserve originals, define the data |
| M | modeler | Frame the decision, specify alternatives and tests |
| X | computation | Implement the baseline, validators, and approved experiments |
| R | independent-reviewer | Inspect pinned specifications/results without repairing them |
| W | writer-visuals | Build the evidence outline, then manuscript and displays |

First open the coordinator in the intended active directory, using the [existing setup instructions](../setup/CLAUDE_CODE.md). The following are launch examples, not commands already executed:

```bash
cd '/absolute/path/to/equipment-upgrades-practice'
claude
```

Paste the [bootstrap prompt](../setup/BOOTSTRAP_PROMPT.md), replacing its roots, problem path, practice/live mode, actual deadline and timezone, human team, and tool constraints. If the active directory already contains records, the coordinator recovers them rather than creating a competing state file.

The coordinator copies and adapts [role_assignments.yaml.template](../setup/role_assignments.yaml.template) into `control/role_assignments.yaml`. Record the actual conversation IDs if available; terminal labels alone are acceptable when that is what the user can identify. Before simultaneous editing, replace broad default ownership with the narrower paths of each task.

Open a separate Claude session for each worker when its first task becomes useful. In each session, paste its role's assignment prompt, filled with the task ID and exact input/output paths. The common prefix can be:

```text
PROJECT_ROOT = /absolute/path/to/equipment-upgrades-practice
DOC_ROOT = /absolute/path/to/HIMCM_Agent_Working_Doc
Your session label is [D/M/X/R/W]. Your role is [canonical role].
Read DOC_ROOT/WORKING_DOC.md sections 1–5, your role document, and
DOC_ROOT/setup/SHARED_DIRECTORY_PROTOCOL.md. Then read control/state.md,
your entry in control/role_assignments.yaml, and the task packet named below.
Do not assume another session's conversation is available to you.
Write only the task's assigned paths. Send acknowledgments and completion
evidence through your own versioned handoffs. Do not edit control/.
```

Each dispatch later in this walkthrough supplies the task-specific continuation. The full canonical prompts are in [domain-data](../roles/domain-data.md), [modeler](../roles/modeler.md), [computation](../roles/computation.md), [independent-reviewer](../roles/independent-reviewer.md), and [writer-visuals](../roles/writer-visuals.md).

The optional [`CLAUDE.md` template](../setup/CLAUDE.md.template) is an instruction entry point. Inspect any existing project file before merging it. The [native role wrappers](../setup/optional_native_agents/README.md) are inert `.template` files until deliberately copied and configured; they neither launch agents nor enforce directory permissions. Independent sessions require none of those wrappers. The strict read-only native reviewer cannot execute numerical checks, so its review scope must say so. No native-team setup is required for this walkthrough.

The user relays messages manually:

```text
Worker → user: Handoff ready: handoffs/T01/domain-data-r01.md.
User → C: Read handoffs/T01/domain-data-r01.md and reconcile task T01.
C → user: Send the T04 dispatch below to M.
User → M: [paste that dispatch, including pinned inputs and write scope]
```

The handoff file carries the evidence; the short message carries the notification. Saving a file does not wake another terminal. A message sent to C does not itself establish that C has read or accepted the artifact. Resume a known role explicitly rather than continuing whichever conversation happens to be most recent.

## 3. Create the working records and first assignments

Only C writes the control records. The initial records identify the real inputs and constraints; they do not prefill approvals or successful results.

```text
control/
  intake.md
  state.md
  tasks.md
  tasks/T01.md ... T11.md
  role_assignments.yaml
  requirements-r01.md
  glossary.md
  decisions.md
  evidence_index.md
  ai_use.md
inputs/
  statement-v01.pdf
  attachments-v01.xlsx
research/
  admission-r01.md
  data_dictionary-r01.md
  evidence_gaps-r01.md
models/
  framing-r01.md
paper/
  outline-r01.md
handoffs/<task-id>/<canonical-role>-rNN.md
```

These are expected paths, not a claim that they already exist. D admits the actual statement and attachment into `inputs/`, records provenance and hashes, then preserves those bytes. C records current contest requirements separately if this is a live task; this synthetic example does not supply current rules, deadlines, or permission to use a particular service.

Initial task packets use [TASK.md](../templates/TASK.md). Keep one summary board in `control/tasks.md`; individual packet paths contain the detailed assignment.

| Task | Owner | Question/output | Dependency before substantive completion |
|---|---|---|---|
| T01 | D | What do the statement and attachment actually define? | Actual files accessible |
| T02 | M | What is the decision, and which interpretations matter? | Statement; T01 definitions may still be pending |
| T03 | W | What evidence must the paper and memo eventually contain? | Statement and provisional requirement IDs |
| T04 | M | Which baseline/architecture fits the confirmed problem? | Accepted T01/T02 and recorded G1 |
| T05 | X | Can the candidate logic pass a tiny discriminating test? | Pinned T04 candidate and interface |
| T06 | R | Is the architecture/specification coherent and implementable? | Pinned T04/T05 evidence |
| T07 | X | Does the accepted target model yield a checked schedule? | G2, accepted specification and data |
| T08 | R | What do the target results actually support? | Closed T07 run and pinned inputs/code |
| T09 | W | Can the accepted evidence become a coherent paper/memo? | Accepted results and claim set; G3 before final conclusions |
| T10 | R | Does the rendered candidate preserve accepted evidence? | Named T09 PDF/source version |
| T11 | C | Is one inspected final deliverable ready for the human? | G3, accepted T10, delivery checks |

The IDs identify work, not a rigid clock. T03 can proceed alongside source inspection. T07 cannot run a scientifically meaningful target comparison against an unresolved objective merely because X is available.

### Dispatch T01 to D

```text
Task T01: admit and interpret the supplied equipment-project data.
Read the complete statement and every attachment sheet, note, and footnote.
Write inputs/statement-v01.pdf and inputs/attachments-v01.xlsx only as new
admissions; preserve them thereafter. Write research/admission-r01.md,
research/data_dictionary-r01.md, research/evidence_gaps-r01.md, and your
handoff under handoffs/T01/.

Explain one row's meaning; project IDs; currency and scale; calendar versus
project-relative month; duration; crew demand; precedence; and missing/zero
values. Identify any later expenditure after an intervening zero. Separate
official instructions from assumptions and external estimates. Do not clean
the original attachment or choose the model's objective.

Return the full input coverage, definitions, concrete contradictions/gaps,
and whether a baseline can be supported. Budget: use the actual limit in
control/tasks/T01.md; stop expanding research when these decisions are resolved.
```

D first acknowledges scope. The acknowledgment may be `handoffs/T01/domain-data-r00.md`; completion uses `r01`. C reads the acknowledgment and changes T01 from `READY` to `RUNNING`. The worker does not edit the board.

### Dispatch T02 to M and T03 to W in parallel

```text
M / T02: Write models/framing-r01.md and handoffs/T02/modeler-r01.md.
Restate the required decision without selecting an optimizer. Propose the
meaning of full completion, timing of expenditures and crew use, carryover,
priority, and the requested uncertainty scenarios. Mark definitions still
awaiting T01. Give C a requirement/dependency proposal for G1; do not edit
control/requirements-r01.md yourself.
```

```text
W / T03: Write paper/outline-r01.md and handoffs/T03/writer-visuals-r01.md.
Map the required schedule, funding plan, justification, uncertainty analysis,
and council memo to sections and evidence needs. Use PENDING_EVIDENCE markers
where results are not available. You may create an illustrative architecture
diagram labeled as proposed; do not invent a schedule, savings, or winner.
```

## 4. Handle a real blocker before it becomes hidden mathematics

Suppose D cannot determine whether a monetary column is dollars or thousands of dollars. This is a **hypothetical blocker branch**, not a finding about an actual attachment.

D's message should identify the exact dependency:

```text
T01 is blocked for cost-scale admission. The header in [exact sheet/cell]
and the statement's [exact page] do not establish compatible units.
I have completed the ID, duration, and precedence dictionary. I have not
assigned a monetary scale. See research/evidence_gaps-r01.md, issue U01.
Needed: authoritative unit clarification or an explicitly approved bounded
scenario treatment. A target funding recommendation depends on this.
```

C records `BLOCKED` for the affected task, its unblock action, and downstream effects. X can still construct a labeled synthetic logic fixture; W can still develop the outline; M can still compare formulations symbolically. None may describe those activities as a target result using the real attachment.

If the unit is explicitly stated in an overlooked sheet note, D resolves it from that source and updates a new revision of its findings. If it remains unknown, C prepares a concrete choice between defensible scenario treatment and obtaining missing information. Only a material unresolved decision goes to the human. Ordinary clarification by reading available evidence requires no additional approval.

After T01/T02 are ready, C copies the accepted interpretation into the requirements map and submits G1. A suitable decision packet is:

```text
G1 / requirements-r01.md
Decision: confirm the proposed system boundary and interpretation.
Recommendation: all twelve upgrades must finish by the required deadline;
resource limits are hard; priority affects completion timing rather than
permission to omit low-priority projects. Funding carryover is [supported
interpretation with source, or explicitly unresolved choice].
Alternative and consequence: [material alternative, if one remains].
Evidence: T01 source definitions; T02 framing; exact unresolved issue list.
Confirmation requested: accept this version, or specify the changed choice.
Independent work continuing: source checks and evidence-outline preparation.
```

C records the human's actual response and the version. This example supplies no default “approved” response. Once G1 is already confirmed, routine implementation proceeds without repeatedly asking the same question.

## 5. Compare approaches before a large run

T04 asks M for a small set of meaningful candidates. For this practice scenario, plausible **proposals**, not selected results, are:

| Candidate | Why it is relevant | What would expose a limitation |
|---|---|---|
| Feasible priority-first baseline | Easy to explain; reserves every future cost and crew commitment | Poor timing compared with an exactly solved small case |
| Time-indexed integer schedule | Discrete starts, deadline, precedence and resource limits have direct mathematical representations | Runtime or missing-data assumptions defeat the target use |
| Local improvement of a feasible schedule | Useful fallback if exact search cannot finish within budget | No meaningful improvement or frequent feasibility repair |

Do not add a method solely to fill the table. M may retain only the baseline and one justified alternative.

T04 outputs should be concrete:

```text
models/D01-architecture-r01.md          from MODEL_DECISION.md
models/M01-scheduling-r01.md          from MODEL_SPEC.md
models/I01-data-to-schedule-r01.md    from MODEL_INTERFACE.md
models/E01-small-case-r01.md          from EXPERIMENT.md
models/assumptions-r01.md             from ASSUMPTIONS.md
handoffs/T04/modeler-r01.md
```

The interface must settle questions that cross role boundaries:

| Field | Required agreement |
|---|---|
| `project_id` | Source ID retained; row positions are not IDs |
| `relative_month` | Month 1 means the project's first active month |
| `cash_cost` | Named currency, scale, price basis, and treatment of missing values |
| `start_month`, `finish_month` | Integer bounds; finish equals start plus duration minus one |
| `crew_demand` | Crew-month demand at each active month; availability calendar supplied separately |
| Precedence | Whether predecessor completion permits a successor in the same month or the next |
| Funding | Receipt time, expenditure time, carryover, opening balance, and borrowing rule |
| Objective | A defined quantity whose units and preference meaning are explicit |
| Outputs | Schedule, expenditure ledger, crew ledger, funding balance, solver status and limitations |

If priorities are ordinal labels, X must not silently treat their numbers as cardinal weights. M must justify a lexicographic rule, an elicited weighting interpretation, or another representation and return any necessary value choice to C.

### Dispatch T05 to X

```text
Implement only the accepted-for-prototyping candidate versions named in
control/tasks/T05.md. This is a small feasibility experiment before G2,
not authorization for a target-scale result or a final recommendation.

Own code/data/prepare_projects.py, code/modeling/schedule.py,
code/modeling/check_schedule.py, code/experiments/run_small_case.py,
data/processed/toy-r01/, runs/T05-small-r01/, and your T05 handoffs.
Do not write code/visualization/ or control/.

Map each constraint to implementation. Check a known small schedule,
an impossible deadline, a late cost spike, and zero available crews.
Compare with an independently enumerated small case where feasible.
Do not fill unspecified mathematical choices yourself. Return them to M.
Record all actual commands, input/code hashes, environment and outcomes.
```

### A fixture with an independently checkable failure condition

The following invented input is a mathematical teaching fixture, not a run result. Money is in arbitrary budget units. There are three months, capacity of four budget units per month, and two available crews. No carryover is allowed in this fixture. Each active project uses one crew; there are no precedence requirements.

| Project | Duration | Costs by project-relative month |
|---|---:|---|
| A | 2 months | 1, 4 |
| B | 2 months | 3, 3 |

Starting both in month 1 fits that month's cost, `1 + 3 = 4`, but creates month-2 cost `4 + 3 = 7`, exceeding the cap. Starting B in month 1 and A in month 2 gives monthly costs `3, 4, 4`; both finish by month 3 and crew use is `1, 2, 1`. These sums are explicit hand reasoning about the fixture. They are not evidence that an implementation has passed.

This fixture distinguishes a full commitment validator from a first-month-only check. X records the program's **actual** behavior after running it. If the program accepts the invalid simultaneous-start schedule, X must retain the failed output and repair the implementation before using real data. If the specification itself permitted that shortcut, M owns the specification repair.

## 6. Use a complete handoff rather than “done”

The following is a **fillable handoff example**. Bracketed fields stay unresolved until the corresponding action actually occurs. Do not copy it into a real project as an acceptance receipt.

```text
Handoff — T05 — computation — r01
Producer: X; date [actual timestamp]
Next recipient: C, then R for T06
Question: Does the proposed scheduling logic enforce future commitments?

Inputs actually read:
- models/M01-scheduling-r01.md [actual SHA-256]
- models/I01-data-to-schedule-r01.md [actual SHA-256]
- models/E01-small-case-r01.md [actual SHA-256]
Unread/missing: [state any missing sections, files, or scientific choices]

Outputs:
- code/modeling/schedule.py [actual hash]
- code/modeling/check_schedule.py [actual hash]
- runs/T05-small-r01/manifest.json [actual status]
- runs/T05-small-r01/outputs/checks.csv [exists/not produced]
- runs/T05-small-r01/receipt.md [actual status]

Findings: [computed results with exact rows; or failure with evidence]
Checks actually performed: [method, expected property, actual outcome]
Not checked: target attachment, real cost uncertainty, target optimality.
Limitations: this fixture verifies implementation behavior, not empirical
validity or the quality of a target recommendation.
Requested next action: review these pinned files under T06, or return the
named mathematical ambiguity to M. Do not release target runs yet.
```

C verifies files and versions rather than merely copying the claimed status. A task moves `RUNNING → IN_REVIEW` when its submitted evidence is ready for the required review. It does not move directly to `ACCEPTED` because the worker says a command exited successfully.

After C releases an accepted dependency, its consumer acknowledges receipt in its own next handoff: upstream task and version/hash actually read, downstream use, units/entity/time/schema, unresolved interface issues and next action. The consumer does not edit the producer's receipt. If this acknowledgment is missing, C follows up through the relay; elapsed time is not confirmation.

## 7. Independent review and a repair loop

Dispatch T06 to R with a precise target:

```text
Review the pinned T04 specification and T05 implementation evidence.
Write qa/Q01-specification-r01/review.md and
handoffs/T06/independent-reviewer-r01.md only. If controlled execution is
available, place any independent check outputs under that qa/ directory.
Do not modify models/, code/, data/, or runs/.

Check requirement coverage, unit/timing agreement, full-horizon feasibility,
the fixture oracle, objective meaning and formula/code correspondence.
State whether you inspected records, independently checked selected arithmetic,
or reran a specified experiment. Do not claim target-scale validation.
```

Use the standard verdicts:

| Review verdict | Coordinator action |
|---|---|
| `ACCEPTED_FOR_SCOPE` | Accept the named purpose/version if its task conditions are met; do not expand the verdict's scope |
| `CHANGES_REQUESTED` | Record findings and route the task to its author for a new revision |
| `INSUFFICIENT_EVIDENCE` | Identify what is missing; use `BLOCKED` only when a specific unavailable dependency prevents progress |

Finding severities are `blocking`, `consequential`, and `editorial`. These are review labels; task states remain `READY`, `RUNNING`, `BLOCKED`, `IN_REVIEW`, `CHANGES_REQUESTED`, `ACCEPTED`, and `SUPERSEDED`.

For example, **if** the invalid fixture schedule is accepted by the submitted code, R could record:

```text
Q01-F01 / blocking
Target: [exact code hash and function/line]
Evidence: [actual independent check or inspected result location]
The candidate starting A and B in month 1 spends seven units in month 2
against a cap of four, yet the target labels it feasible.
Consequence: a target schedule may promise unaffordable future commitments.
Repair owner: X if the spec already reserves every month; otherwise M first.
Required check: reject this candidate and accept the hand-verified feasible
candidate, then recheck all affected resource constraints.
```

The repair sequence is explicit:

1. R writes the finding; C records the task as `CHANGES_REQUESTED`.
2. C assigns the repair to the owner. R does not fix the target and then certify its own repair.
3. The owner writes a new specification/code revision and a new handoff. A new invocation uses `runs/T05-small-r02/`; the failed `r01` run remains unchanged.
4. R reviews the changed bytes and affected checks in a new review receipt. Unrelated checks are not repeated merely to increase the test count.
5. C records the accepted version and the scope of acceptance. The earlier failed evidence remains linked for provenance.

C can then submit a substantive G2 packet using the model decision record, data feasibility, small-case evidence, review findings, and a resource estimate. The human chooses the architecture on that concrete record. A successful toy check is not itself human approval of the main model.

## 8. Run the target model and preserve the evidence

After G2 and an implementable final specification are recorded, T07 can begin. X reads the actual accepted versions—not whichever files have the highest-looking filename—and writes a unique run directory.

Expected target artifacts include:

```text
data/processed/projects-v01.csv
data/processed/project_costs-v01.csv
data/processed/precedence-v01.csv
code/data/prepare_projects.py
code/modeling/schedule.py
code/modeling/check_schedule.py
code/experiments/run_target.py
runs/T07-target-r01/
  manifest.json
  config.json
  command.txt
  environment.txt
  stdout.log
  stderr.log
  outputs/schedule.csv
  outputs/monthly_cash.csv
  outputs/monthly_crews.csv
  outputs/checks.csv
  outputs/baseline_comparison.csv
  receipt.md
```

The [run manifest template](../templates/run_manifest.json.template) starts with `NOT_STARTED` and null results. Populate timestamps, command, input hashes, code hashes or commit, solver status, objective/bound/gap where applicable, and output hashes from actual execution. Hash the actual code if uncommitted changes are used; a repository commit alone does not describe those bytes.

The schedule should retain source project IDs, start/end months, duration, scenario ID, and decision version. The cash ledger separates expenditure, funding receipt, opening balance, closing balance, and any restrictions. The crew ledger reports demand and available capacity in the same time units. A final check reconstructs those ledgers independently from the source cost profiles and schedule.

The receipt must distinguish:

- A feasible solution from an infeasible or partial attempt.
- A solver-proven optimum under its stated tolerance from a feasible incumbent with an unknown or nonzero gap.
- A deterministic scenario from a probabilistic reliability claim.
- A completed target run from the earlier toy demonstration.

If a run times out, preserve its actual status and any checked feasible incumbent. Do not turn a timeout into an “optimal” result or repair a closed CSV by hand. Any retry gets a new run ID.

Sensitivity tasks should specify what could change the recommendation: a cost range, a crew-availability interruption, or an uncertain project duration, with justification for each scenario. Compare the same coverage requirements and objective. Report changes in schedule, funding feasibility, and practical tradeoffs rather than only a smoother score curve. These are planned checks until executed; no scenario result is supplied here.

T08 sends R the target model/data/code versions and the closed run. R may find correct arithmetic but unsupported cost assumptions, or a valid schedule but overstated optimality. Those are different findings with different repair owners. C releases downstream numerical claims only after the required review scope is accepted.

## 9. Turn results into an evidence-linked manuscript

While T07/T08 run, W can improve the nonnumerical explanation. It cannot fill pending result slots with plausible numbers.

Once accepted evidence is available, C provides W with the exact claim set and input tables:

```text
T09: use only the accepted target run [run ID/hash] and claim IDs [list].
Write paper/manuscript-r01.md, paper/council-memo-r01.md,
paper/claim_proposals-r01.md, code/visualization/schedule_plot.py,
figures/F01-schedule-r01.svg, figures/F02-funding-r01.svg,
and your own T09 handoff. Do not modify numerical run outputs.

Explain why the formulation matches the decision; compare the accepted
baseline; show coverage and resource feasibility; state uncertainty and
when the recommendation changes. Use exact source project IDs.
Bind every figure to its input table and every numerical claim to a row
and column. Return any missing calculation to its owner.
```

A claim-evidence row should be filled from real evidence, for example:

```text
Claim ID: C01
Intended claim: [actual accepted wording about deadline/resource feasibility]
Requirement: R01
Model/data versions: [accepted versions]
Run/table: [closed run]/outputs/checks.csv, [specific check rows]
Scope: [exact scenario and horizon]
Review: [Q02 receipt and verdict scope]
Qualification: [cost/crew assumptions and remaining uncertainty]
Manuscript: [section and figure]
```

W owns `paper/claim_proposals-r01.md`; C incorporates accepted entries into `control/evidence_index.md`. This avoids two agents editing the shared claim register.

M and C interpret the results, then submit G3 with the proposed recommendation, alternatives, reviewed evidence, limitations, and draft. The human's answer governs the conclusion. Neither a private repository nor an AI consensus substitutes for that choice.

## 10. A changed input makes downstream work stale

Consider another **hypothetical branch**: a corrected attachment changes one project's month-2 cost after a target run has been accepted. D admits `inputs/attachments-v02.xlsx` as a new original and writes `handoffs/T12/domain-data-change-r01.md` using [CHANGE_REQUEST.md](../templates/CHANGE_REQUEST.md). D does not overwrite `v01`, edit X's prepared data, or patch W's chart.

C records the dependency chain:

```text
attachments-v02
  → data dictionary / processed cost data
  → affected target and uncertainty runs
  → feasibility and baseline comparison
  → target-result review
  → claims C01…[actual affected IDs]
  → schedule/funding figures, summary, council memo, PDF
```

The prior artifacts remain historical records. Their status for current use is marked stale in `control/state.md` and the evidence index. Their old `ACCEPTED` task status describes an earlier version's acceptance; C must prevent it from being mistaken for approval under `v02`. Use `SUPERSEDED` when the task/version has actually been replaced, not as a substitute for explaining the changed dependency.

C dispatches only the affected work:

- D owns the new admission and definition changes.
- X regenerates processed data, reruns affected experiments, and creates new immutable runs.
- M checks whether the correction changes feasibility or model interpretation.
- R checks the changed results and consequential claims.
- W regenerates affected displays and prose after replacement acceptance.

Unchanged background text, notation cleanup, and export tooling can continue. W must not present stale numerical figures as final while waiting. A data correction does not automatically reopen every human gate: reopen G1/G2/G3 only if its substantive decision changes. If the new costs reverse the recommendation, G3 needs a new concrete decision packet.

A style-only figure change requires visual/claim consistency review, not a fresh numerical run. A change in displayed aggregation or units may affect meaning and must be traced farther upstream.

## 11. Recover from a session loss or write collision

If X loses context, the replacement session reads its canonical role, `control/state.md`, `control/role_assignments.yaml`, `control/tasks/T07.md`, accepted model/data versions, and the latest T07 handoff. It then reports:

```text
I am recovering session X for T07. My write scope is [exact paths].
The current accepted dependencies are [versions/hashes]. The previous run
is [actual status], and [specific evidence] is missing/present. My next
action is [bounded check or new invocation]. I will not overwrite a closed
run or assume an earlier chat claim is verified evidence.
```

If the old session may still be writing, C confirms it has stopped before transferring that scope. Until then, the replacement uses a newly assigned path. A stale assignment is not an automatically expired lock.

If two sessions edit the same file, they stop writes to that file and preserve both versions. C assigns a reconciliation owner. Taking the newest modification time is not a valid resolution strategy. In one shared checkout, all sessions share the Git index and branch; only C stages, commits, changes branches, and integrates. Workers do not switch branches underneath each other.

For optional worktrees, follow [GitHub setup](../setup/GITHUB.md) and give each session its actual root and input paths. The current project's authorized private-upload choice does not grant publication rights for an unrelated future project. No push or repository creation occurs as part of this example.

## 12. Review the actual export and close the loop

W exports a distinct candidate such as `paper/exports/solution-r01.pdf`, records the source and tool versions, and inspects the rendered pages. T10 assigns R that specific PDF and its source/claim versions. A filename and a successful export command do not establish readable equations, correct pagination, or complete references.

If R requests layout changes, W creates `solution-r02.pdf` and R inspects the affected pages plus any page-count/flow consequences. If a scientific claim changes during layout repair, route it back through the appropriate evidence review; do not treat it as cosmetic.

C completes [DELIVERY.md](../templates/DELIVERY.md) in `control/delivery-r01.md`, including actual G3 response, accepted data/model/run/claim versions, resolved blocking findings, current requirements, export inspection, final hash, and the person responsible for submission. The latest usable complete export remains identifiable throughout the process.

The final user-facing handoff should be concise and factual:

```text
Final artifact: [actual path/hash]
Answers delivered: [requirements covered]
Evidence: [accepted data/model/run and independent review]
Checks performed: [actual computational and rendered-artifact checks]
Limits: [remaining assumptions or unsupported endpoints]
Submission status: [not submitted / actual authorized outcome]
Human next action: [only the real remaining action]
```

Do not say “submitted” when the team has only produced a PDF. Do not say “globally optimal” when the evidence is a best-found heuristic schedule. Do not say “all agents verified” when only one scoped review exists.

## 13. What the user actually relays at each handoff

The manual workflow can be operated with short messages once the durable records exist:

| Moment | Message to send | What it enables |
|---|---|---|
| Start D/M/W | Paste the role prompt plus the specific task packet path | Clear responsibilities without shared chat memory |
| Worker finishes | `C: read handoffs/Txx/<role>-rNN.md.` | C inspects evidence and routes review |
| Review begins | `R: review these pinned versions under task Txx; own qa/Qxx-rNN/.` | Independent, bounded scrutiny |
| Repair required | `Owner: address findings Qxx-F01… in a new revision; preserve old evidence.` | A traceable author repair |
| Dependency accepted | `Next worker: use version/hash X accepted for purpose Y; ignore superseded Z.` | Safe downstream release |
| Upstream changes | `C: read change request path; identify stale descendants before release.` | Coordinated invalidation |
| Session resumes | `Resume the named role; read state, assignment, dependencies and last handoff first.` | Recovery from files |
| Final candidate | `R/C: inspect the named exported file against accepted claims and current requirements.` | Review of the artifact actually delivered |

The operating pattern is consistent throughout: **bounded assignment → acknowledged scope → inspectable artifact → versioned handoff → independent review where required → owner repair → recorded acceptance → downstream release**. Each arrow has an owner, a file, and a condition. That is what makes multiple Claude conversations behave as one accountable project.
