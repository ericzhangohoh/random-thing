# Shared directory and handoff protocol

This protocol is the default for six independent Claude Code sessions working in one local contest project. It is a human-readable operating agreement, not a filesystem access-control system. A role assignment narrows responsibility; it does not remove tools or change operating-system permissions. See [Claude Code setup](CLAUDE_CODE.md) for that distinction.

The reusable working document and the active contest project are different things. Keep the historical PDF library read-only. Resolve `DOC_ROOT` to this working-document folder and `PROJECT_ROOT` to the directory for the current practice problem or competition. Record both absolute paths in `control/state.md`. All paths below are relative to `PROJECT_ROOT`.

## Directory ownership

| Location | Writer | Use and restrictions |
|---|---|---|
| `control/` | Coordinator only | State, task board, assignment manifest, accepted decisions, shared glossary, evidence index, release manifest. Workers propose changes through handoffs. |
| `inputs/` | Domain-data, admission only | Official statement and attachments. Preserve original bytes after admission; a correction is a new version with a source and hash. |
| `research/` | Domain-data | Source register, contextual research, data dictionaries, historical analogies and reading records. Assign disjoint files if multiple researchers run. |
| `data/raw/` | Domain-data, admission only | Retrieved datasets and source snapshots. No cleaning in place. |
| `data/interim/`, `data/processed/` | Computation | Reproducible transformations. Version datasets; do not replace a version still used by a review or run. |
| `models/` | Modeler | Mathematical specifications, candidates, assumptions, validation designs, proposed decisions. |
| `code/` except `code/visualization/` | Computation | Data-processing, model, experiment and test code. No changes to plot code owned by writer-visuals. |
| `code/visualization/` | Writer-visuals | Plot and table rendering from named, immutable result tables. No refitting or changing model outputs here. |
| `runs/<run-id>/` | Assigned computation session | Commands, config, logs, environment, outputs and completion receipt for one invocation. Once closed, immutable. |
| `qa/` | Independent-reviewer | Version-specific findings, review receipts and isolated verification outputs. Never repair the artifact being reviewed. |
| `paper/`, `figures/` | Writer-visuals | Manuscript, bibliography, display tables, figure files, export candidates. Final candidates use distinct version names. |
| `handoffs/<task-id>/` | Each assigned role's own file | Write `<role>-rNN.md`. Never overwrite another role's note. |

The coordinator records one current owner for every writable file or bounded path in `control/role_assignments.yaml`. Use the [assignment template](role_assignments.yaml.template). These paths are defaults; a narrower task assignment wins. A directory owner is not entitled to edit a file already assigned to a second session without a recorded transfer.

## Task lifecycle

Use the main working document's phase gates. For individual tasks, use `READY`, `RUNNING`, `BLOCKED`, `IN_REVIEW`, `CHANGES_REQUESTED`, `ACCEPTED`, or `SUPERSEDED`.

1. The coordinator creates a task with an ID, question, acceptance evidence, dependencies, input versions, owner, allowed output paths, resource/time budget and review route.
2. The worker reads the task and input files. It returns an acknowledgment naming its assignment and any missing dependency. The coordinator records `RUNNING`; a worker does not edit the shared board.
3. The worker creates drafts in its own assigned paths. A draft is not available for downstream scientific claims merely because the file exists.
4. The worker closes a handoff with exact output paths, versions or hashes, results, limitations and a requested next action. The coordinator records `IN_REVIEW` if review is required.
5. The reviewer evaluates the pinned artifact, records findings in `qa/`, and identifies a verdict and its scope. The coordinator updates the task; it cannot rewrite the review verdict.
6. The author repairs findings in a new revision. After the affected checks pass, the coordinator records acceptance and releases dependent tasks.
7. The consumer acknowledges the exact accepted revision, its units/entity/time/schema and the next action in its own handoff before consequential dependent work.

`BLOCKED` means a specific missing dependency or capability prevents this task. State the smallest unblock action and continue other assigned work that does not depend on it. It is not a synonym for uncertain, unfinished, difficult, or awaiting routine self-checks. `ACCEPTED` means accepted for the named purpose and version, not that the entire project is finished.

## Handoff content

Use the main document's handoff template where available. Every handoff must contain the following information even if the file format differs:

```text
Task ID and role/session:
Question being answered:
Inputs actually read, versions/hashes, and any unread material:
Outputs written, versions/hashes, and completion status:
Decision or finding, with the evidence that supports it:
Alternatives considered and reason for rejection or deferral:
Checks actually performed and their outcomes:
Limitations, assumptions, unresolved issues, and affected downstream tasks:
Recommended next action and owner:
```

Say whether a reported number was computed, copied from a source, estimated, or assumed. Separate a successful command exit from a scientifically supported conclusion. Never substitute “done” for an inspectable output.

The default transport is simple: the human copies the handoff path or short notification into the coordinator's session, and then into the next worker's session. The actual evidence stays in files. A shared folder does not automatically notify another session, and a sent message does not prove its recipient read or accepted it. Native messaging is optional; it still points to the same durable records.

If a receipt is missing, the coordinator follows up through the available relay and assigns other independent work. It does not release the dependency based on elapsed time. Use the [execution playbook](../EXECUTION_PLAYBOOK.md) for canonical review-verdict mappings and first assignments.

## Changes and invalidation

An accepted artifact is not edited silently. Its owner proposes a change, identifies the affected dependency chain, writes a new version, and requests review of the affected claims. Preserve the last accepted version until the replacement is accepted.

| Change | Minimum affected work |
|---|---|
| Official requirement or interpretation | Requirement map; affected assumptions, models, experiments and manuscript claims |
| Source dataset, cleaning rule, units or sample definition | Derived data; dependent runs, comparisons, figures and claims |
| Objective, constraints, equations or parameters | Model checks; dependent computation, validation and interpretation |
| Solver implementation or environment affecting computation | Relevant runs and result-dependent reviews |
| Plot style only | Visual/readability review; scientific rerun only if displayed values or transformations change |
| Wording only | Claim-strength, accuracy and final rendering checks; no automatic rerun of unchanged science |

A hash identifies bytes, not mathematical correctness. Use it to prevent reviewing one version and publishing another. A timestamp alone is not sufficient when two files have the same name.

## Collision and recovery rules

- Do not use a common scratch notebook, common `results.csv`, or shared mutable “latest” file as the only evidence. Use unique task, run and revision identifiers.
- One terminal does not own the entire repository. Avoid broad recursive edits, formatters or cleanups that cross another worker's scope.
- If two sessions edited the same file, stop writes to that file, preserve both versions, and let the coordinator assign a reconciliation task. Do not resolve the conflict by taking the newest file automatically.
- Shared checkout means shared branch, index and working tree. Only the coordinator performs Git staging, commit, branch switching and integration. Workers may inspect status/diffs. Git is optional initially; the ownership rule is not.
- A stale assignment is not a lease that expires automatically. Before transferring ownership, confirm the old session has stopped writing; if unavailable, preserve its outputs and use a new path.
- Before a long run, claim its output directory and record the resource budget. Avoid two expensive experiments competing for the same memory, GPU or fixed output filenames.
- A failed or partial run remains a failed or partial run. Preserve its log and create a new run ID for a retry rather than changing its receipt to success.

## Session restart checklist

Read `control/state.md`, your assignment, the current task, accepted dependency versions and the last handoff. Confirm the files still match the versions under review. Then state: current objective, owned scope, accepted inputs, unresolved issues and next action. If remembered conversation conflicts with the current files, investigate the discrepancy; do not silently select whichever story is more convenient.

The coordinator records session labels or IDs so the human resumes the intended role. Resuming the most recent session in a shared directory may resume a different role; explicit session selection is preferable when several are active.

## Independence and disputes

Independence concerns the artifact, not the agent's name. A reviewer who substantially designed or repaired an artifact cannot provide its independent acceptance. Assign a fresh reviewer or clearly label the check as author self-review. Limited staffing does not forbid useful work; it changes the strength of the review claim.

Resolve scientific disagreements through the original question, source quality, a counterexample, a derivation, or a distinguishing experiment. Agent votes and eloquent explanations are not evidence. The coordinator records the resolution and remaining uncertainty. Escalate to the human when the choice changes the intended objective, allowable resources, competition boundaries or an unresolved value judgment that the team must make.

This protocol is a project design choice. The underlying separate-context and file-conflict constraints are documented by [Claude Code's agent-team documentation](https://code.claude.com/docs/en/agent-teams), checked 2026-11-02.
