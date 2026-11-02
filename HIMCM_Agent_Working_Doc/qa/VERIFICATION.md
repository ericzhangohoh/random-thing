# Verification Record

Checked 2026-11-02, Australia/Sydney. This record describes actual checks and their limits.

## Document and setup checks

- Local Markdown links checked across the authored document set and current review records: no missing local targets at the check.
- Markdown fence balance checked: no unbalanced fenced blocks.
- Run-manifest JSON template parsed successfully.
- Role-assignment YAML template and all six optional native-agent frontmatters parsed successfully.
- Ownership consistency inspected: coordinator owns shared control; writer owns visualization code; reviewer writes isolated review outputs and does not repair targets.
- Optional read-only native reviewer returns its report for the coordinator to save; it cannot claim numerical execution with read/search tools alone.
- Document-level failure exercises cover leakage, unit changes, edit conflicts, solver failure, overstated optimality, missing inputs, reviewer independence, context loss, losing candidates, stale outputs, export failures and deadlines.

The exercises are protocol walkthroughs, not successful numerical solutions to the historical problems. Claude Code was not installed in this environment; native agents/teams have **not** been live-tested. No settings were changed to bypass permissions.

## Executed non-biological teaching fixture and operational revision

- The [campsite approach example](../examples/APPROACH_DEFENSE_WALKTHROUGH.md) now has executed synthetic inputs, source, results and provenance under `examples/approach_demo/`.
- Eight scenarios were run and independently enumerated; reported schedules, exact optima, feasible-assignment counts and service-mix accounting matched. A separate reproduction returned byte-identical result bytes.
- Two negative checks reject an overlong final travel leg and a fixed plan using a newly closed campsite slot.
- The independent reviewer found invocation-provenance and ownership defects, returned them to the author, and accepted the repaired pinned versions. See the [scoped review receipt](APPROACH_DEMO_REVIEW.md).
- The [operational gap review](agent_execution_gaps.md) checked the first-dispatch sequence, dependencies, review vocabulary, file ownership, task packets, acceptance evidence and run provenance. Consequential gaps were resolved in the execution playbook and templates.
- The [equipment-project handoff walkthrough](../examples/MULTI_AGENT_HANDOFF_WALKTHROUGH.md) was read for role/path/state consistency. It is an explicitly unexecuted illustration, not a second numerical trial.
- Progress reporting preserves all 473 archived paper records, labels 14 currently known topic exclusions without treating the remainder as screened, and retains the interrupted excluded paper as partial. JSON/YAML templates and Python syntax were checked.

These checks support the finite teaching mathematics and the inspected operating contracts. They do **not** establish arbitrary-input solver correctness, empirical validity, target-scale performance, PDF export of a real competition paper, or live Claude orchestration. `claude` was still unavailable during this revision; no installation was performed.

## Repository checks

- Repository created at [ericzhangohoh/himcm](https://github.com/ericzhangohoh/himcm).
- GitHub API/CLI confirmed `isPrivate: true` and `visibility: PRIVATE` before upload.
- Initial source commit `f0735f3` was successfully pushed to `main`.
- All **1,617 tracked source-library files** were checked against their Git blob identities using the original working-file bytes. **Zero byte mismatches** were found.
- No substantive source files were found silently omitted by ignore rules in that check.
- Credential-pattern and sensitive-filename checks found no candidate credentials in the upload scope. These are bounded checks, not a universal secret-detection guarantee.
- Source-folder Git attributes preserve original bytes, including historical text line endings.

Later working-document and review commits are identified in Git history. A local commit is not treated as a successful upload; the coordinator verifies the remote branch after pushing.

## Research checks and remaining work

The original 502 PDFs have a classified inventory and page-bounded extraction. **This is not full review completion.** Review progress is computed from explicit reader-authored coverage records, with partial and unread papers retained. See [current status](../research/STATUS.md).

Reviewed papers distinguish author reports, reviewer interpretation, static checks and numerical reproduction. Full historical numerical reconstruction has not been performed. The user's [current scope](../research/SCOPE.md) excludes all biology-related papers and supersedes exhaustive archive reading as a delivery requirement. Prior material remains archived; new operational guidance uses non-biological cases.
