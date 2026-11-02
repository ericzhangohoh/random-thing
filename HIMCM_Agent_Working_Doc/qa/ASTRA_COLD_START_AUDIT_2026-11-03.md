# Astra cold-start contract audit — 2026-11-03

**Current verdict: ACCEPTED_FOR_SCOPE** after the changed-version re-review below. **Initial verdict: CHANGES_REQUESTED:** no blocking finding, two consequential findings and one editorial finding. The initial findings and trace are preserved as historical evidence.

**Actual model:** GPT-6 Astra (`gpt-6-astra`). The parent confirmed the spawn used this model with `fork_turns='none'`. **Reviewer:** `/root/astra_cold_start_audit`. **Independence:** this reviewer did not author or repair the targets and did not read prior conversation/history. The supplied task and current files were the context.

## Scope and evidence limits

This was an adversarial **documentary dry run**, not executed multi-agent behavior. I read local documentation and reasoned through new agents following it. I did not launch Claude sessions, perform the illustrated experiments, rerun campsite calculations, inspect biological papers, install software, use Git, or alter target documents. Audit-created files are this report and `qa/astra_cold_start_2026-11-03/initial_hashes.json`.

A successful documentary transition means the files specify a next action, owner, evidence and permission boundary. It does not establish reliable behavior by a particular product/model/team. No external product claims were verified.

Inspected files, relative to `HIMCM_Agent_Working_Doc`:

- `README.md`, `WORKING_DOC.md`, `EXECUTION_PLAYBOOK.md`, `COORDINATION.md`.
- `setup/BOOTSTRAP_PROMPT.md`, `setup/SHARED_DIRECTORY_PROTOCOL.md`, `setup/CLAUDE_CODE.md`, `setup/CLAUDE.md.template`, `setup/role_assignments.yaml.template`.
- All seven Markdown files in `roles/` (index and six roles).
- `templates/README.md`, `INTAKE.md`, `REQUIREMENTS.md`, `STATE.md`, `TASK.md`, `HANDOFF.md`, `REVIEW.md`, `CHANGE_REQUEST.md`, `DELIVERY.md`, `run_manifest.json.template`.
- `examples/MULTI_AGENT_HANDOFF_WALKTHROUGH.md` in full.

Initial content identities are in the adjacent hash manifest. Finding line numbers refer to that initial inspected revision, before repairs. Other research/QA reports were not used to establish findings. The separate workflow auditor owns numerical-example evaluation and independently corroborated CS-01's textual mismatch after I reported it.

## Concrete documentary trace

This trace uses the walkthrough's synthetic twelve-equipment-project/six-month prompt. For the normal initial branch I assume the supplied statement and attachment exist outside an otherwise empty active project. This is a declared scenario input, not a claim that this audit inspected an actual workbook. The unresolved monetary-unit branch is hypothetical, as it is in the walkthrough.

| State | Action a new agent derives from files | Documentary outcome |
|---|---|---|
| Fresh empty project, supplied files | C reads bootstrap/process, records absolute roots, practice mode and available constraints, creates control records and assigns D admission. D admits originals with hashes/provenance. C can read supplied originals before admission. | Runnable given a capable environment and paths. No existing state is required: coordinator prompt says “if they exist.” No invented contest approval or C writing D's files is necessary. |
| First two workers | C assigns D/T01 input audit and M/T02 framing with disjoint paths and bounded scope. Both acknowledge; only C edits board. M marks pending definitions. | Concurrency is defined. YAML defaults must be narrowed. Two workers do not imply two writers to one file. M's literal acknowledgment filename has a minor ambiguity (CS-03). |
| G1 pending | C prepares requirements, alternatives and concrete G1 packet. D verifies sources; M keeps alternatives provisional; X may run explicitly provisional independent diagnostics; W may outline. Substantive T04 architecture waits. | Silence is not approval. This is an intentional human gate, not deadlock. Walkthrough omits the playbook's pre-G1 R task (CS-01). |
| Ambiguous monetary input | D identifies exact unresolved sheet/header and statement locations, withholds cost scale and requests smallest unblock. C blocks cost-dependent work only. M compares symbolically; X can use a synthetic fixture; W outlines. | Prevents hidden assumptions and whole-project paralysis. A missed footnote is resolved by reading. A genuinely unresolved interpretation goes to human with a concrete packet. |
| First review | Following the playbook, C creates R's framing-review task on pinned T02/requirements. R writes scoped verdict without editing target. Author repairs consequential defects; C cannot rewrite verdict. | General contract works. Following the populated walkthrough alone instead reaches G1 without this review (CS-01). Candidate targets can be pinned for review without first being scientifically accepted. |
| Review then consumer receipt | After scoped acceptance, C separately checks human gates/dependencies and records accepted artifact/use. Consumer reads the released version, records units/entity/time/schema and next action in its own handoff, then executes dependent work. | No circular receipt/acceptance deadlock: acceptance precedes receipt, which precedes execution. Verdict is not human approval. Manual relay is required; saving a file does not wake a worker. |
| Small run and repair | C authorizes T05 for prototyping only. X records actual status; R reviews pinned spec/code/run evidence. Failed check triggers owner repair and new run, preserving failed output. | Sound run immutability/reviewer separation. Hashes alone do not preserve retrievable historical source (CS-02). No run was executed by this audit. |
| Changed upstream input after acceptance | D admits v02 without changing v01 and writes change request. C marks affected evidence/claims stale; old ACCEPTED status is historical. Owners regenerate/review affected descendants only. | Explicitly closes the stale ACCEPTED loophole. Gates reopen only if substance changes. Consumers must read current state and pinned inputs, not choose highest filenames. |
| Session restart | Replacement X reads role/state/assignment/task/accepted inputs/latest handoff, verifies identity and reports bounded next action. If old X may still write, C confirms stop or assigns a different path. | Good documentary recovery. No expired lease by elapsed time. Missing/changed evidence stays unresolved. A saved hash cannot recover lost bytes (CS-02). |

## Findings

### CS-01 — consequential: walkthrough omits prescribed pre-G1 review

**Location:** `EXECUTION_PLAYBOOK.md:71–75`, especially 74; `examples/MULTI_AGENT_HANDOFF_WALKTHROUGH.md:111–123,188–203`.

**Evidence:** the playbook says “R examines pinned requirements and framing and returns actionable findings” before C submits G1. The walkthrough lists T01 D, T02 M, T03 W, then T04 M dependent on G1; its first R task is T06 reviewing T04/T05. The G1 packet cites T01/T02, with no framing review.

**Dry-run consequence:** a new coordinator following the concrete sequence either omits independent framing review or invents a missing dispatch/dependency. The omitted check concerns interpretation adopted downstream, so this is consequential. The general protocol permits recovery; no unavoidable deadlock is claimed.

**Minimal repair:** add an explicit pre-G1 R task, e.g. T02R, with pinned requirements/framing, QA/handoff paths, review scope and G1 dependency. Cite its receipt in G1; retain T06 for later architecture/prototype review.

**Owner:** document author/coordinator. **Recheck:** revised task/dispatch can run before G1 without depending on post-G1 T04.

### CS-02 — consequential: hashes can outlive the only retrievable code bytes

**Location:** `roles/computation.md:49–59`; `templates/run_manifest.json.template:12–17`; `setup/SHARED_DIRECTORY_PROTOCOL.md:64,75,82`; walkthrough `:251–253,293–297,353–359,370–392`.

**Evidence:** computation requires “code commit or code hashes.” Manifest has `code_version` and path/hash but no source-retrieval/snapshot requirement. Walkthrough uses stable `code/modeling/schedule.py` and `check_schedule.py` for small/target work and explicitly allows hashes of uncommitted code. Git is optional. Prior accepted version preservation is explicitly required only “until the replacement is accepted.” Closed runs retain logs/results, not necessarily executable source bytes.

**Adversarial documentary branch:** X closes accepted r01 using bytes A and hash(A). Later revision B is accepted; A is no longer retained (no Git, or uncommitted run code). Closed runs/hashes remain, but only B exists at the stable code path. Fresh R detects the mismatch correctly yet cannot retrieve A. Detection works; promised reproducibility/recovery fails. This is a contract gap, not an observed overwrite during this audit.

**Minimal repair:** every retained closed run must name retrievable immutable code/spec/config/input bytes for its lifetime. Allow retained versioned files, an immutable run-local source snapshot, or recoverable clean commit. Dirty/uncommitted code needs retained snapshot or complete recoverable patch. Add retrieval location to manifest and existence check to acceptance. Large immutable data can remain at a retained versioned path; duplication is unnecessary.

**Owner:** document author, then X for real run records. **Recheck:** no-Git same-name source change preserves A and B so R can retrieve exact code of either closed run; a hash alone fails retention acceptance.

### CS-03 — editorial: exact r01 handoff scope leaves acknowledgment naming unclear

**Location:** walkthrough `:58–59,148,153,162`; `templates/TASK.md:35–37`; shared protocol `:24`.

**Evidence:** workers send acknowledgments and completion through versioned handoffs. D gets explicit r00 acknowledgment/r01 completion. M/T02 and W/T03 each name only an r01 handoff as write target. Narrower assignment wins over default scope.

**Dry-run consequence:** a literal worker puts acknowledgment in r01 then asks C for a completion path, or guesses r00 permission. This is a small avoidable coordination detour, not itself corrupted scientific acceptance.

**Minimal repair:** grant r00 and r01 explicitly or a bounded task-local handoff revision pattern consistently. Distinguish acknowledgment from final evidence.

**Owner:** document author. **Recheck:** M/W can create both records within scope without overwriting a completed handoff.

## Usability judgment

The default is **runnable as a manually relayed operating agreement**, given supplied files and available sessions/tools. It is not an autonomous scheduler. Human relay at completions, review dispatches and releases is unavoidable under this default and explicitly disclosed. G1/G2/G3 additionally require actual human decisions when not already authorized. Independent work can continue while decisions wait.

Control records plus per-task packets, acknowledgments, handoffs and reviews impose clerical cost. Templates say to copy only what the stage needs; C is instructed to keep records usable rather than exhaustive. No evidence establishes that this is inherently impractical, but no elapsed-time/session study was executed. STATE duplicates board information by design while explicitly disclaiming a second authority; that is a maintenance risk, not a demonstrated contradiction.

Changed-input invalidation, single-writer scope, closed-run immutability, reviewer separation and restart recovery survived the documentary branches. CS-01/02 prevent acceptance of the initial revision for cold-start completeness. Repair can support documentary acceptance for scope, but cannot establish live Claude orchestration.


## Changed-version re-review — 2026-11-03

**Current verdict: ACCEPTED_FOR_SCOPE.** CS-01, CS-02 and CS-03 are resolved for the inspected documentary startup/role/task/handoff contract. No unresolved blocking, consequential or editorial finding remains from this audit. This supersedes the initial verdict, not the historical record above.

The same independent GPT-6 Astra reviewer inspected the actual repairs in `roles/computation.md`, `templates/run_manifest.json.template`, `setup/SHARED_DIRECTORY_PROTOCOL.md`, `WORKING_DOC.md`, and `examples/MULTI_AGENT_HANDOFF_WALKTHROUGH.md`. Final hashes for all substantive targets inspected by this audit are in `qa/astra_cold_start_2026-11-03/final_substantive_hashes.json`. That manifest also identifies changed files and hashes the recovery probe evidence. `README.md` and `qa/VERIFICATION.md` are excluded from the final substantive freeze to permit the parent's later audit-index updates. Acceptance is tied to those substantive hashes, not to unspecified future edits.

| Finding | Rechecked actual repair | Resolution |
|---|---|---|
| CS-01 | Walkthrough lines 116–117 adds T02R and T04's dependency; 191–204 supplies a pinned pre-G1 review dispatch, owner scopes and repair/recheck loop; 214–215 includes its scoped receipt in G1. R may accept a complete decision packet with unresolved human choice without choosing on the human's behalf. | Closed. The reviewer task can run on drafts before G1 and depends on no post-G1 task. No approval cycle introduced. |
| CS-02 | Computation lines 52, 61–63 requires pre-invocation byte preservation, retained inventory, continued preservation for failed/superseded runs and actual isolated retrieval/hash check before closure. Manifest lines 19–22 provides retrieval location/method and check receipt fields. Shared protocol line 64 extends retention after replacement and permits read-only source copying into an assigned reproduction directory. WORKING_DOC line 257 makes this part of run acceptance; walkthrough line 415 carries it into the populated sequence. | Closed for the documented contract, supported by the executed file-recovery probe below. A hash alone is explicitly insufficient. Failure to retrieve must prevent a reproducibility claim or acceptance as evidence. |
| CS-03 | Walkthrough line 109 grants task/role-specific rNN handoff revisions and defines r00 acknowledgment/r01 completion; lines 154–155 and 164–165 explicitly use the pattern for M/W. New substantive repair paths still require C's scope update. | Closed. Both lifecycle records fit the permitted scope without overwriting a completed handoff. |

### Executed recovery-contract probe

Unlike the initial paper trace, this narrow check **was executed**. It tests only file preservation/retrieval and SHA-256 identity, not numerical validity, live Claude sessions, or actual multi-agent orchestration.

- Script: `qa/astra_cold_start_2026-11-03/retention_probe.py`.
- Command: `python3 HIMCM_Agent_Working_Doc/qa/astra_cold_start_2026-11-03/retention_probe.py`, working directory `/Users/ericzhang/Desktop/himcm`.
- Receipt: `qa/astra_cold_start_2026-11-03/retention_probe_r01/receipt.json`; inventory beside it in `inventory.json`.
- Actual result: exit 0; receipt `PASSED`. A retained copy of source A was recovered into a fresh directory after the working source changed to B. Recovered A matched `2299179e1cf372efa02b59979e4e7134a75190d2459d7629e5680a32847aff63`. Working B remained unchanged with hash `b10e26e616cd49234d8e79a436f2f3aafbb000bae1528b530c0d89d561263369`.
- Negative branches: a hash-only inventory with no retrieval location, a missing snapshot, and a retrieval location containing B instead of A were all rejected. The original retained A remained unchanged.
- All probe writes stayed within the assigned QA directory. No Git was used. The script refuses to overwrite its existing evidence directory. It is an audit-only illustrative checker, not a shipped production validator and not proof of complete dependency discovery for arbitrary real software.

The changed `templates/DELIVERY.md` was also inspected: it now requires resolution of consequential as well as blocking findings, or removal of affected claims with independent acceptance of the narrowed scope. This is consistent with the reviewer contract. The revised run-manifest template also parsed successfully as JSON. Copy/restoration authority was inspected: the protocol permits reading a source to preserve its bytes in an assigned reproduction directory; this does not transfer source ownership. Restoration must use an isolated assigned destination and cannot switch the shared checkout. The default run-local directory can contain the fresh retrieval check before closure, so the new requirement does not inherently force X to write into R's QA area.

Remaining limits are unchanged: default manual notification still requires a human relay, real unresolved gates require actual human decisions, and no live product/session rehearsal was performed. The source-retention fix adds a recoverability check; it does not claim mathematical correctness, successful execution of the retained model, or preservation of all future external runtime availability. Those distinctions are now explicit in the contract and this report.
