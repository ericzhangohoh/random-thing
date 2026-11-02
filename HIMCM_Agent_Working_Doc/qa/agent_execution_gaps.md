# Operational gap review: the first six-agent work cycle

Reviewed 2026-11-02: `WORKING_DOC.md`, `COORDINATION.md`, all six role files, the shared-directory protocol, bootstrap prompt, assignment manifest, and intake/task/run/claim templates. This is a document review and proposed edit list, not a live Claude-session test. No main documents were edited. Biological sources were excluded from recommendations.

**Finding:** the current documents already define responsibilities, versioned handoffs, scientific checks, and human checkpoints well. The main missing piece is a concrete first dispatch: which six tasks begin immediately, which exact files they produce, and which observation releases the next task. Add one operational page rather than another general explanation of collaboration.

## First dispatch to insert after intake

The coordinator assigns these task IDs once per project, adapting paths and budgets. The first pass produces a G1 decision packet and an end-to-end execution plan; it does not prematurely approve an architecture.

| Role / first task | Immediate action | Exact first output and write owner | Dependency and acceptance |
|---|---|---|---|
| Coordinator / T01 | Record `DOC_ROOT`, `PROJECT_ROOT`, statement, actual deadlines and known authority; assign sessions and disjoint paths; create T02–T06 with budgets. Do not wait for every uncertainty to disappear. | Coordinator: `control/intake.md`, `control/state.md`, `control/requirements.md`, `control/tasks/T01.md`–`T06.md`, `control/tasks.md`, `control/role_assignments.yaml`. | Accessible statement is enough to start provisional framing. T02 supplies source admission; T03 proposes interpretation; T05 audits it. G1 requires an explicit human response for the pinned interpretation, or a previously recorded applicable response. Each unresolved input names only the tasks it blocks. |
| Domain-data / T02 | Admit and read the complete statement/attachments; classify examples versus observations; inventory available data; investigate only evidence gaps affecting the first baseline. | Domain-data: new immutable `inputs/` and `data/raw/` admissions; `research/intake_sources-r01.md`, `research/data_dictionary-r01.md`, `research/data_gaps-r01.md`; own handoff. | Start from supplied files immediately. Return each proposed model input as available, derivable, scenario-only, or unavailable, with units, grain and provenance. Supply source/hash corrections to coordinator instead of editing `control/`. End external search at the assigned budget and recommend a fallback. |
| Modeler / T03 | Read statement independently; propose requirement interpretation, boundary, decision/output distinction, subquestion dependency map and simplest credible baseline. Identify a materially different alternative only if it could change the decision. | Modeler: `models/framing-r01.md`, `models/candidates-r01.md`, `models/toy_spec-r01.md`; own handoff. | May start alongside T02 using explicitly provisional inputs. Toy specification needs exact inputs, objective, feasibility rules and independently checkable expectation. Final data-dependent architecture waits for T02. G1 precedes commitment to the disputed interpretation; G2 precedes production implementation. |
| Computation / T04 | Inspect the existing runtime; record capabilities; inspect supplied data formats without cleaning originals. After a pinned toy specification is available, implement one baseline and its tiny known-answer check. | Computation: `code/experiments/toy_baseline.py` or the chosen-language equivalent; a unique `runs/T04-<timestamp>-r01/` containing manifest, logs and result table; own handoff. | Runtime/schema inspection can begin immediately. Scientific implementation waits for an implementable toy spec and explicit prototype scope; production runs wait for G2 and the complete accepted specification. Failure, timeout and infeasibility are recorded outcomes. No writer-facing “final result” is released merely because a prototype runs. |
| Independent reviewer / T05 | Read the statement before the proposed framing; compare every requested output with the draft requirements map; identify one decision-changing failure test. Review the toy specification and output when pinned. | Reviewer: `qa/T05-framing-r01/review.md`, isolated calculations/check outputs there, own handoff. | Framing review needs only statement plus T03's proposed map. Computational review waits for the pinned toy spec/run. Declare nonauthorship. Return target-specific evidence and verdict, not implementation repairs. The coordinator releases the reviewed version; the reviewer does not update shared state. |
| Writer-visuals / T06 | Map each requested answer to a section, figure/table question or nontechnical deliverable; create an evidence outline and test the chosen export path with a clearly labeled synthetic placeholder. | Writer: `paper/outline-r01.md`, `paper/claim_requests-r01.md`, minimal source and `paper/export-smoke-r01.pdf`; plot code only under `code/visualization/`; own handoff. | Starts with provisional requirements and audience. Outline and export do not wait for numerical results. Numerical claims and final plots wait for accepted tables and a reviewed interpretation. Inspect the actual rendered file; a file's existence alone does not pass the export task. |

The first complete baseline is reached through **T02 input meaning + T03 specification → T04 run → T05 scoped review → coordinator acceptance → T06 evidence-linked draft**. G1 and G2 restrict consequential choices, not every reversible diagnostic. The coordinator should explicitly identify common work allowed while a decision is pending; otherwise the present gate wording can be read as unnecessarily serial.

## Acceptance must be executable or directly inspectable

Add the following fields to `templates/TASK.md`, and require the coordinator to fill them for the first dispatch:

```text
Acceptance check ID:
Claim or contract checked:
Check type: executable / document inspection / human decision
Exact command and working directory, or exact inspection procedure:
Read-only inputs and pinned versions:
Allowed output directory:
Expected exit/status and substantive expectation:
Evidence receipt path:
Timeout/resource bound:
Who checks the evidence and releases the dependency:
Failure action and unaffected work that continues:
```

Use two separate layers. An integrity command establishes that a file exists or matches its expected bytes; scientific acceptance establishes that it answers the right question. Do not turn a successful filesystem check into a scientific verdict.

Concrete first-cycle criteria:

- **Coordinator:** inspect each official requested action against a requirement row with statement location, output, owner, dependency and criterion; no mandatory action is unassigned. Every dispatched task has one actual session and a bounded output path. The readiness record includes actual human decisions, not a Boolean filled by an agent on the human's behalf.
- **Domain-data:** hash every admitted original; inspect one-row meaning, units, keys, coverage and measurement status for each baseline input. Open cited source locations. If a parameter remains unknown, acceptance is a documented range/fallback with its affected claim, not a fabricated value.
- **Modeler:** an agent other than the author can trace the toy case from input to expected output without choosing an unspecified weight, update rule, capacity interpretation or boundary. Record the hand calculation and the exact assertion computation must satisfy.
- **Computation:** execute the recorded command in a fresh run directory; assert the independently specified toy answer, hard constraints and expected failure behavior. Re-execute with the same pinned inputs in another directory and compare the declared outputs/tolerances. Baseline and candidate share evaluation inputs and objective. Preserve actual statuses.
- **Reviewer:** independently check at least the assigned consequential proposition, such as enumerating a tiny allocation's feasible assignments or verifying a conservation identity. Pin the source/run hashes before inspection and confirm they remain unchanged at the end. A review with no executed numerical check must say so.
- **Writer:** render the minimal export with the project's actual documented command and inspect its pages. Later, reconcile each consequential number with the accepted table's row/column, scenario and units. Export acceptance and scientific-claim acceptance are separate records.

For source admission, a real command available on the current Mac is `shasum -a 256 inputs/<admitted-file>`. The task must substitute the actual path. For computation, require the implemented program to support an explicit output directory, for example `python3 code/experiments/toy_baseline.py --input models/toy-input.json --output runs/<new-run-id>`. This is a **proposed interface**, not a claim that this script already exists. Record the final real command once implementation is complete. A shell `test -s <path>` can check that an output is nonempty, but cannot replace the scientific assertions or rendered-page inspection above.

## Specific edits, in priority order

| Priority | Location | Required change and reason |
|---|---|---|
| 1 | `WORKING_DOC.md`, immediately after Stage 0; `COORDINATION.md` | Insert or link the first-dispatch table and dependency sequence. Current stage descriptions identify owners but leave the coordinator to invent the actual first assignments from scratch. |
| 1 | `templates/TASK.md`; each role's assignment prompt | Add executable/inspectable acceptance fields. Add a first-response contract: task ID, inputs actually read, exact owned paths, missing dependency, first action, expected handoff path. The worker's response should make dispatch failure obvious before extensive work. |
| 1 | `WORKING_DOC.md` §§3, 7–9; shared-directory protocol | Resolve `code/qa/` ownership. The tree calls it independent checks, while computation owns all nonvisualization code and the reviewer is restricted to `qa/`. Prefer computation-owned reusable tests in `code/qa/`, reviewer-owned independent check scripts and outputs in `qa/<review-id>/`. State this consistently. |
| 1 | `roles/coordinator.md`, `templates/README.md`, bootstrap prompt | State that `control/tasks.md` is the board/index and `control/tasks/T-ID.md` is the full packet. Both conventions already appear, but their relationship is implicit. Coordinator owns both. |
| 1 | All review instructions and templates | Use one canonical review vocabulary. Current reviewer file uses `PASS / CHANGES_REQUIRED / INCOMPLETE`; the requested implementation now specifies `ACCEPTED_FOR_SCOPE / CHANGES_REQUESTED / INSUFFICIENT_EVIDENCE` with severity `blocking / consequential / editorial`. Reconcile globally; do not confuse review verdicts with task lifecycle states. |
| 2 | `templates/run_manifest.json.template` | Add explicit model-specification path/hash, experiment-plan path/hash, check result/status fields and output-schema/units location. `code_version` alone cannot identify the mathematics a run implements. Define actual run status values and retain solver status separately. |
| 2 | `COORDINATION.md` | Add one concrete relay message: “T04 r01 ready; handoff path; pinned input versions; output path; requested next recipient/action.” State what happens if no receipt arrives: coordinator follows up or assigns other work; shared folders are not notification systems. |
| 2 | Stage 0, bootstrap and `control/state.md` template | Record the research scope and stop condition. For the present preparation task, biological-related papers are excluded and further corpus expansion is stopped. Do not interpret that preparation choice as an instruction to omit mandatory requirements of a future contest problem. |
| 2 | `roles/writer-visuals.md` and claim template | Give ownership to the proposed claim ledger in `paper/claim_requests-rNN.md`; coordinator alone integrates accepted entries into `control/evidence_index.md`. The present “proposed by writer/modeler” guidance should name separate files so neither edits a shared claim table concurrently. |

## Minimal rehearsal to prove the document is usable

Use one tiny non-biological scheduling or allocation fixture. Dispatch the six packets, record actual acknowledgments, derive a baseline and a small exact comparison, produce a closed run and scoped independent review, then render one page explaining the result and its limitation. Deliberately change one input after acceptance and check that the old run/claim/figure becomes stale without erasing it. Rehearsal success means that a fresh role session can find its next action from files and reproduce the named evidence; it does not claim real-world validity or that six Claude sessions were launched unless they actually were.

This is sufficient to test execution, dependencies, ownership and recovery. Further historical-paper accumulation is not needed to resolve these operational gaps.

## Resolution check after implementation — 2026-11-02

Re-read the completed `EXECUTION_PLAYBOOK.md`, updated coordination and shared-directory protocols, bootstrap prompt, relevant role instructions, task/review/state/claim templates, run-manifest template, and research-scope record. This was a static operational-consistency review; no live Claude sessions or additional numerical experiments were run for this check.

**Status: the consequential gaps identified above are resolved for document delivery.**

| Gap | Resolution inspected |
|---|---|
| Concrete first dispatch and dependencies | Playbook §§1–4 name the six roles, first artifacts, recipients, permitted provisional work, gated transitions, and bounded task packet. Acceptance of a pinned version releases consumers. |
| Runnable or inspectable acceptance | Task template now records command/procedure, substantive expectation/tolerance, evidence receipt and checker/release owner; it also requires pinned inputs, allowed output, budget and failure action. Role index and bootstrap specify the first acknowledgment. |
| Conflicting `code/qa/` ownership | Main working-document tree and role index assign it to computation; independent scripts and outputs belong in `qa/<review-id>/`. The worked demo was repaired to match. |
| Task index versus full packets | Playbook, bootstrap and state template explicitly distinguish `control/tasks.md` from `control/tasks/<T-ID>.md`. |
| Review vocabulary | Playbook, reviewer role and review template use `ACCEPTED_FOR_SCOPE / CHANGES_REQUESTED / INSUFFICIENT_EVIDENCE`, with the required severity terms. Review verdicts, task states and human approval remain distinct. |
| Run specification identity | Manifest template now pins code, model specification, experiment plan and output schema, alongside execution status and check records. Execution success is explicitly separate from scientific acceptance. |
| Missing receipt/relay behavior | Coordination includes an actionable relay example; protocol and playbook require consumer acknowledgment and follow-up when receipt is absent, without treating elapsed time as acceptance. |
| Research scope and stopping | Scope record, main document, bootstrap, state template and playbook preserve the biology exclusion, stop open-ended archive expansion as a delivery prerequisite, and tie future research to named decision gaps. Future contest requirements retain their own authority. |
| Proposed claim ownership | Claim template and writer role assign proposed rows to `paper/claim_requests-rNN.md`, modeler corrections to its own artifact/handoff, and accepted integration to the coordinator. |

The actual non-biological demonstration now has a separate [independent review receipt](APPROACH_DEMO_REVIEW.md), with executed checks and a scoped verdict. That supports the mathematical teaching example, not a claim that all six operational roles have been exercised in live sessions.

One editorial clarification remains optional: `templates/STATE.md` includes an inline “Task board” table as well as the link to the canonical `control/tasks.md` board. Labeling the inline table “Current task summary; canonical status lives in control/tasks.md” would prevent treating it as a competing authoritative board. The coordinator owns both records, so this does not block the current document's use or delivery.
