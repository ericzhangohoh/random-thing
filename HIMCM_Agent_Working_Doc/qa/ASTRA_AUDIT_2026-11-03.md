# Independent GPT-6 Astra audit — 2026-11-03

**Current verdict after author repair and independent re-review: ACCEPTED_FOR_SCOPE.** All four findings below are resolved for the final pinned versions. The original findings and initial verdict are retained as review history; see the repair addendum. This acceptance covers written contracts and finite toy evidence, not live orchestration.

**Reviewer/model:** GPT-6 Astra (`gpt-6-astra`), independently assigned as `astra_workflow_audit` with no inherited conversation. I did not author or repair the targets. **Initial verdict: CHANGES_REQUESTED.** Two consequential workflow gaps and two editorial inconsistencies require the bounded repairs below. The synthetic numerical evidence passed. This is not a live orchestration or empirical-validity verdict.

## Scope and identity

I inspected the complete execution playbook, working document, approach/justification chapter, coordination chapter, all six role files and their index, all Markdown templates and the run-manifest template, bootstrap/shared-directory/Claude setup instructions, role-assignment and CLAUDE templates, optional native wrappers and their index, both new walkthroughs, the three shorter workflow exercises and example index, campsite README/input/program/results/manifest, verification record, and existing independent demonstration review and checker. Numerical result inspection combined artifact inspection with the executed checker below.

Exact pre-review file identities are in [initial_hashes.json](astra_audit_2026-11-03/initial_hashes.json). This inventory pins some adjacent files too; inclusion alone does not imply substantive review. [checks.json](astra_audit_2026-11-03/checks.json) confirms no inventoried target had changed during initial checks. All five target hashes in the prior demonstration acceptance matched current files.

No historical paper, biological research, extracted corpus, or scientific source review was read. No Git operation, installation, settings change, or target-file repair was performed. I did not verify repository-upload history, current contest rules, all external links, or complete external product documentation. A narrow consultation of Anthropic's current subagent documentation was a setup sanity check, not live validation. Claude was not found on the executable path. The separate cold-start auditor communicated the two consequential findings; I checked their stated document conflicts independently but did not run that auditor's probes.

## Checks actually performed

Runtime: CPython 3.12.14, Clang 22.1.3. Working directory: `/Users/ericzhang/Desktop/himcm`. All new numerical outputs are confined to `HIMCM_Agent_Working_Doc/qa/astra_audit_2026-11-03/`.

1. Read the prior independent checker before executing it. Copied it unchanged into the new audit directory; its library-relative root remains correct and its output follows its new `__file__` location. Ran `python3 HIMCM_Agent_Working_Doc/qa/astra_audit_2026-11-03/independent_check.py`. All eight scenarios passed. This is a fresh execution of a previously authored independent checker, not a newly written independent implementation by Astra. See [receipt](astra_audit_2026-11-03/independent_results.json).
2. Ran `python3 HIMCM_Agent_Working_Doc/examples/approach_demo/run_demo.py --output HIMCM_Agent_Working_Doc/qa/astra_audit_2026-11-03/reproduction`. The new result bytes exactly match the canonical result, and its manifest records the actual invocation and nondefault output path. See [manifest](astra_audit_2026-11-03/reproduction/manifest.json).
3. Independently checked the resource argument: four camp-night slots bound the base count by four, attained by the four short-trip witness. Requiring L consumes two slots and leaves at most two short trips, making three exact. Closing B/night 2 eliminates L's sole route and leaves three attainable slots. These are mathematical checks of an invented fixture, not empirical validation.
4. Checked code/prompt correspondence for booking-order insertion, route tie-breaking, whole-trip reservation, exit legs, capacity, service-class accounting, closure timing and claim strength. The baseline and optimizer share the supplied constraints. The quota is explicitly a policy change; replanning is not substituted for fixed-plan robustness.
5. Parsed the run-manifest JSON, compiled both Python sources without creating production bytecode, checked inventoried Markdown fence parity, and verified copied-checker identity and previous pinned hashes. These are integrity checks, not general software guarantees.

Exact optima: `4, 3, 1, 1, 0, 3, 0, 0`. Independently enumerated feasible-assignment counts: `58, 9, 2, 2, 1, 21, 1, 1`. Both deliberately invalid schedules are rejected. Arbitrary-input validation, general solver correctness and scale performance were not tested and are explicitly excluded by the fixture.

## Findings

### ASTRA-C01 — consequential: detailed walkthrough skips required framing review

**Location:** `examples/MULTI_AGENT_HANDOFF_WALKTHROUGH.md`, initial task table and section 4 G1 sequence; compare `EXECUTION_PLAYBOOK.md:69–75`.

**Evidence:** the playbook requires R to inspect pinned requirements and framing before the G1 packet. The walkthrough's first R assignment is T06, dependent on T04/T05 after G1. Its G1 sequence proceeds from T01/T02 directly to C's packet without a framing-review task. This was identified by the separate cold-start auditor and verified here against the actual text.

**Consequence:** a new coordinator following the most concrete example can bypass the documented early independent interpretation check. Later architecture review does not retroactively supply the missing pre-G1 evidence.

**Repair owner:** walkthrough author/coordinator. Add a bounded pre-G1 R task and dispatch with pinned framing/requirements, exact QA/handoff paths and explicit release conditions; preserve existing task IDs where practical. Recheck the task dependency table and G1 narrative together.

### ASTRA-C02 — consequential: run identity is specified more clearly than recoverable source retention

**Location:** `roles/computation.md`, Run contract; `templates/run_manifest.json.template`, `code_version`/`code_files`; `setup/SHARED_DIRECTORY_PROTOCOL.md:64,75,82`; equipment walkthrough section 8.

**Evidence:** the contracts permit code hashes instead of a commit and explicitly permit optional Git. They require new revisions and preservation of the last accepted version until replacement acceptance, but do not unambiguously require retaining all source bytes needed by each closed run for that run's lifetime. A hash identifies missing bytes; it cannot recover them. The cold-start auditor identified this gap; this review independently verified the textual basis, not that auditor's experiment.

**Consequence:** a run can retain valid input/output hashes while its formerly uncommitted implementation becomes unavailable after a later accepted replacement. The run then cannot be faithfully reproduced from the documented minimum record.

**Repair owner:** protocol/template author, implemented by computation and checked by coordinator/reviewer. Require retrievable immutable source/dependency/configuration bytes for every retained closed run: for example, a retained snapshot or an actually available commit with all dirty/untracked runtime files captured. Record the recovery location and verify it. A commit string or hash alone is insufficient.

### ASTRA-E01 — editorial: first reproduction command mutates accepted evidence

**Location:** `examples/APPROACH_DEFENSE_WALKTHROUGH.md`, section 7, lines 186–198.

**Evidence/consequence:** the lead command uses the default output directory and overwrites canonical results/manifest. The nearby warning discloses this, and the README already leads with a fresh directory. Invocation metadata can change even when numerical outputs do not, invalidating the earlier manifest pin unnecessarily.

**Repair owner:** walkthrough author. Lead with an unused output directory; distinguish author maintenance regeneration from evidence-preserving review. No numerical repair is needed.

### ASTRA-E02 — editorial: delivery checklist omits consequential findings

**Location:** `templates/DELIVERY.md:13`.

**Evidence/consequence:** it asks only whether blocking findings are resolved, whereas the independent-reviewer role forbids acceptance with unresolved blocking or consequential issues. Stronger canonical requirements remain, so this is an incomplete reminder rather than a demonstrated release bypass.

**Repair owner:** template author. Require resolution of both severities for the release scope and link exact review receipts; retain editorial limitations explicitly.

## What works and what remains unproved

The entry points specify roots, role, task, accepted inputs, write scope, acknowledgment, handoff and release owner. Source admission, mathematical meaning, implementation and presentation have distinct owners. Independent review is tied to authorship and versions rather than agent names. Stale upstream inputs invalidate runs, reviews, claims, figures and final prose; restart instructions require dependency checks rather than conversational confidence.

G1/G2/G3 are substantive human choices. Provisional diagnostics, common work and existing recorded authorization remain available; silence never becomes approval. Apart from C01, the detailed dispatch sequence is usable. These are human-operated contracts, not an implemented scheduler or filesystem enforcement.

Model-choice guidance separates formulation, solver and evaluation, fixes comparable conditions, requires a credible baseline and falsifying test, and distinguishes feasible, best-found, finite optimum and empirical validity. The campsite example actually demonstrates those distinctions. The equipment example offers useful operational branches but explicitly has no executed sessions, target files, approvals or solver output. Its prose must not count as an end-to-end rehearsal.

This initial verdict is confined to inspected documents and finite synthetic evidence at the pinned versions. No fresh Claude agent, automatic notification, concurrency collision, native tool boundary, actual context-loss recovery, rendered contest paper, or target-scale application was tested. Apply the four bounded repairs and request re-review of changed versions. A later claim of live readiness needs an actual bounded rehearsal with durable session/task/receipt artifacts, failure and stale-input branches, independent acceptance, and a rendered deliverable.


## Repair and independent re-review — 2026-11-03

The author repaired seven target files. I independently reread the changed provisions and their surrounding task/release contracts. The **current verdict is ACCEPTED_FOR_SCOPE**: no unresolved blocking, consequential or editorial finding from this audit remains. This is acceptance of the repaired documented workflow and the previously checked finite synthetic example, not evidence that agents have executed the repaired workflow.

The exact current versions of 54 substantive inspected targets are pinned in [final_targets.json](astra_audit_2026-11-03/final_targets.json). The initial hashes and initial check receipts remain unchanged. Future root `README.md` audit links and `qa/VERIFICATION.md` summary updates are explicitly excluded from this frozen substantive target set; neither can silently extend this acceptance to additional behavior. [Repair checks](astra_audit_2026-11-03/repair_checks.json) record the executed structural checks and unchanged numerical identities.

| Finding | Verified author repair | Re-review outcome |
|---|---|---|
| ASTRA-C01 | The equipment walkthrough now adds T02R to the task table, makes T04 depend on its review, supplies a pinned-input R dispatch with owned QA/handoff paths, requires owner repair and affected recheck, and includes T02R evidence in G1. The review accepts a complete decision packet, not the human's unresolved choice. | Resolved. The pre-G1 review has an executable assignment and no circular G1 dependency. |
| ASTRA-C02 | The main run-acceptance rule, computation role, shared-directory protocol, run template and equipment walkthrough now require retrievable exact dependencies. Preservation starts before invocation, survives replacement acceptance, and includes failed/superseded runs. Clean available Git objects may supply committed bytes; dirty/untracked bytes require separate preservation. The inventory is retrieved into a fresh isolated directory and hash-checked before closure. | Resolved as a written operating contract. Missing bytes explicitly prevent reproducibility/accepted-evidence claims. No automatic retention implementation or live enforcement is asserted. |
| ASTRA-E01 | The approach walkthrough now leads with `--output` to an unused revision directory, requires changing the path when occupied, and explicitly explains default/reused-directory overwrite behavior. | Resolved. Canonical evidence is no longer the lead reproduction destination. |
| ASTRA-E02 | Delivery now requires blocking and consequential findings resolved, or removal of affected claims followed by independent acceptance of the narrowed scope. | Resolved. Narrowing scope cannot bypass independent acceptance. |

The retention template was parsed again. Its inventory meaningfully distinguishes the path used during execution, SHA-256 identity, retained-file retrieval location, and Git repository/commit/path retrieval. It includes a separate recovery-check command/procedure, isolated destination, actual outcome and receipt path; defaults remain null/`NOT_RUN`, so the template does not preclaim success. The computation and shared-directory instructions explain the conditions for using those fields and preserve source ownership while allowing read-only copying. This is structure and consistency validation, not execution of a newly implemented retention system.

I coordinated with the cold-start auditor on the consequential repairs. That auditor owns any additional adversarial recovery probes and its separate report. This addendum does not claim those probes as my execution or silently absorb a broader audit verdict.

The four numerical artifacts (`run_demo.py`, `inputs.json`, `results.json`, canonical `manifest.json`) still exactly match the initial audit hashes. Consequently, the eight-scenario checks were not redundantly rerun. The changed approach walkthrough has a new hash: the earlier `APPROACH_DEMO_REVIEW.md` receipt remains valid only for its own historical narrative version and unchanged numerical targets. This new receipt supplies scoped inspection of the repaired current narrative; it does not rewrite the old acceptance.

All initial exclusions remain: no biological or other historical-paper reading, live Claude orchestration, live recovery test, target-scale performance, empirical validation, real contest PDF rendering, or current contest-rule certification. Root may integrate these documents as reviewed written guidance and a checked synthetic teaching fixture. A claim of live readiness still requires the separately described actual rehearsal.
