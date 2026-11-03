# Coordination, Handoffs and Recovery

The authoritative operational protocol is [Shared directory and handoff protocol](setup/SHARED_DIRECTORY_PROTOCOL.md). It defines directory ownership, task states, handoffs, invalidation, collisions, restart and independent review. Use it together with [the six role instructions](roles/README.md).

For first assignments and the full event sequence, use [Execution Playbook](EXECUTION_PLAYBOOK.md). For concrete cross-session messages and revision handling, use the [handoff walkthrough](examples/MULTI_AGENT_HANDOFF_WALKTHROUGH.md).

## A normal work cycle

1. **Coordinator:** create a task packet with one answerable question, accepted inputs, write scope, dependencies, completion evidence and reviewer.
2. **Worker:** read the packet and role; acknowledge the scope and missing inputs; work only within the assignment.
3. **Worker:** write a versioned handoff containing actual outputs, reasoning, tests, limitations and next action.
4. **Coordinator:** pin the artifact version and assign review where required. A file's existence does not release dependent tasks.
5. **Reviewer:** check the pinned version, write a scoped verdict and actionable findings, and leave the artifact itself unchanged.
6. **Owner:** address findings, create a new revision, and identify which evidence changed.
7. **Coordinator:** record acceptance, update dependency state and release downstream work. Submit G1, G2 or G3 to the human when required.
8. **Consumer:** read the accepted upstream revision and acknowledge its hash/version, interpretation and next action in its own handoff before consequential dependent work. A sent notification is not proof of receipt.

Use [task](templates/TASK.md), [handoff](templates/HANDOFF.md), [review](templates/REVIEW.md) and [change](templates/CHANGE_REQUEST.md) templates. Workers propose state changes through their handoff; only the coordinator edits shared control files.

For an adversarial round, give reviewers different falsifiable questions and disjoint `qa/<attack-id>/` paths. Record actual session identities; reusing a reviewer for another bounded assignment is not a new independent context. Keep an attack-to-author-response-to-recheck ledger. In each assignment state whether final-assessment data may be evaluated and what must be frozen first. Record final-score exposure across all agents, not only inside the main experiment script. Confirmed scientific changes invalidate affected evidence; wording-only qualifications need claim and export review without an automatic numerical rerun.

A concrete notification is: `T05 r01 is ready for review. Read handoffs/T05/computation-r01.md; it pins models/M01-r01.md and runs/E01-r01/manifest.json. Please assign the independent reviewer to feasibility and the stated comparison. No downstream claim is released yet.` Replace every example path and ID with the actual artifact. If no receipt arrives, the coordinator follows up through the available relay and assigns independent work; elapsed time is not acceptance.

## What may run in parallel

| Work | Can run concurrently when… | Must wait when… |
|---|---|---|
| Literature and data investigation | Research questions and output files are separate | A downstream analysis needs an unresolved definition or source |
| Candidate model prototypes | The common problem interpretation and comparison conditions are explicit | Different candidates are silently optimizing different objectives |
| Data preparation and model specification | The shared schema is agreed and changes are reported | An assumption depends on a diagnostic that has not been checked |
| Independent implementation checks | A pinned specification/run exists and checker outputs are isolated | The target is changing without version control |
| Drafting and experiments | Drafts label pending claims and do not invent results | A final claim depends on an unfinished experiment |
| Figures and manuscript integration | Figures use accepted result tables and separate filenames | The underlying run or target claim has been superseded |

Do not add agents to a serial bottleneck merely to increase apparent activity. Give parallel agents independent questions or explicit competing hypotheses, then specify how findings will be compared.

## Decision packet for the human

```text
Checkpoint and affected version:
Decision required:
Recommended option and reasons:
Meaningful alternative and tradeoff:
Evidence inspected:
Unresolved limitations:
Consequences for scope, results and next work:
Exact confirmation requested:
Independent work continuing while this waits:
```

A checkpoint is a substantive choice. Do not route routine formatting, code cleanup or an already approved experiment through it. If new evidence changes an approved choice, explain the change before requesting a new decision.

## Evidence-aware recovery

On restart, read [state](templates/STATE.md), task assignment, role, accepted decisions, latest handoff and the files those records identify. Verify that dependencies still match the reviewed versions. State the next action and its scope before editing.

If a record says a run passed but the output is missing or changed, mark the evidence unresolved and investigate. If a newer chat message conflicts with the board, ask the coordinator to reconcile and record the decision. Do not choose the more convenient story.

## Repository integration

In a shared checkout, all sessions share the branch, index and working tree. The coordinator owns staging, commits, branch changes and pushes. Workers do not switch branches underneath other workers. Use separate worktrees only when the integration plan and data access paths are explicit.

The selected repository is private and includes the source library. See [GitHub setup](setup/GITHUB.md) for the recorded choice, file handling and publication boundary. Repository visibility does not substitute for task ownership or review.
