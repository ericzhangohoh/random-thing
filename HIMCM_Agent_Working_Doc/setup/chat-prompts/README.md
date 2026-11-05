# Fixed-role chats for the Himcm project

This pack gives the human one setup prompt for each of 11 dedicated chats. Each prompt makes its agent read the actual working document, explain its responsibility and stop at a readiness checkpoint. It does not create chats, start the 2026 contest, choose a problem or install an agent framework.

Use [COPY_PASTE_PROMPTS.md](COPY_PASTE_PROMPTS.md) for the short messages to paste. Each message opens a full role prompt below, which loads [the common contract](00-common.md) and the required workflow files. The prompts are English. The user may receive readiness explanations in Chinese, while project artifacts and paper prose remain English.

## Set up the visible chats

1. In the `Himcm` project shown in the user's sidebar, use one designated coordinator and a separate chat for each worker/reviewer. The existing `working agent` chat can be the coordinator. Keep one active coordinator for a given problem project.
2. For this shared-directory recipe, use the local checkout `/Users/ericzhang/Desktop/himcm` for each chat. Have each agent verify its actual checkout. The official OpenAI guidance distinguishes using the current checkout from creating an isolated worktree. A worktree would need an explicit different integration plan. See [OpenAI's environment guidance](https://developers.openai.com/blog/mastering-codex-remote-for-engineering), checked 2026-11-05.
3. Give each chat the suggested title below and paste only its own setup message. Start review chats as separate contexts without authoring the artifacts they will later review.
4. Expect `READY_FOR_ASSIGNMENT` with actual files read, responsibilities, expected inputs and future write boundary. `PROJECT_ROOT: UNASSIGNED` is normal during setup. If a workflow file cannot be read, the agent must report `SETUP_INCOMPLETE` rather than claim readiness.
5. Relay readiness messages to the coordinator. Once the human selects the problem and starts the project, the coordinator records the active directory, authority and exact task assignments. Every worker receives a bounded task before editing files.

Each chat can be initialized now, but not every role has useful substantive work at the same moment. Initial project work typically involves coordination, data, modeling, computation, scientific verification and an evidence outline. Model attacks need an explicit design/evidence target. R1/R2/R3 require a frozen paper packet. Final PDF review follows closed author and complete sentence-review receipts.

## One prompt per role

| Suggested chat title | Setup file | Responsibility |
|---|---|---|
| 01 Coordinator | [Full prompt](01-coordinator.md) | Task assignment, accepted state, dependencies and integration |
| 02 Domain & Data | [Full prompt](02-domain-data.md) | Sources, definitions, provenance and data quality |
| 03 Modeler | [Full prompt](03-modeler.md) | Mathematical specification and approach justification |
| 04 Computation | [Full prompt](04-computation.md) | Implementation, experiments and reproducible runs |
| 05 Scientific Verifier | [Full prompt](05-scientific-verifier.md) | Independent mathematics/code/result verification |
| 06 Writer & Visuals | [Full prompt](06-writer-visuals.md) | English paper, LaTeX, figures and author repairs |
| 07 Model Attacker | [Full prompt](07-model-attacker.md) | Consequential assumptions, alternatives and counterexamples |
| 08 R1 Argument Review | [Full prompt](08-r1-argument.md) | Every sentence's reasoning, precision and justification |
| 09 R2 Evidence Review | [Full prompt](09-r2-evidence.md) | Every sentence's facts, numerical support and citations |
| 10 R3 Reader Review | [Full prompt](10-r3-reader.md) | Every sentence's clarity, natural prose and coverage |
| 11 Final PDF Review | [Full prompt](11-final-artifact-reviewer.md) | Every final page, fonts, compilation, coverage and punctuation |

The six base roles remain intact. The scientific verifier is the base independent-reviewer role focused on science and implementation. The model attacker, three sentence reviewers and final artifact reviewer are five additional specialized assignments. This is a suggested 11-chat roster, not evidence that 11 new chats have already been created or are running.

## How a task moves between chats

```text
Human starts a selected problem project
    -> Coordinator pins active root, authority, roles and task packets
    -> Assigned worker reads packet and acknowledges accepted inputs
    -> Worker completes its owned outputs and a versioned handoff
    -> Human relays handoff path/version to Coordinator
    -> Coordinator assigns exact-version independent review
    -> Author repairs, reviewer rechecks, Coordinator releases accepted result
    -> Next consumer acknowledges the accepted input before using it
```

The default mechanism is durable files plus human relay. Sharing a project is not a reason to assume that another chat knows your conversation or noticed a new artifact. Direct tool messaging can be used only when the human has authorized that route and actual destination IDs/tools are available. A reviewer does not edit author targets. Only the coordinator edits active `control/` or performs authorized Git changes.

An example follow-up message after a real task exists is:

```text
Continue as your configured role. Read the active project state and your
released task packet at [absolute actual task path]. Verify the input versions
and assigned write paths, acknowledge the task, then complete the assignment
and its versioned handoff. Do not execute this template with placeholders.
```

After setup, the human can give the coordinator this activation template with real values:

```text
Activate a new project using the workflow you have read.
Selected problem: [actual year/problem and statement path]
PROJECT_ROOT: [actual dedicated project directory]
Mode: [practice or live competition]
Deadline and timezone: [actual deadline or no fixed deadline]
Human team and decision authority: [actual participants and authority]
First scope: [e.g. intake, requirement map and initial task packets]
Use the existing role chats through [human relay, or explicitly authorized
messaging with actual destination IDs]. Record current requirements and assign
bounded work. Do not treat unfilled fields as permission to invent values.
```

The role setup does not select either of the downloaded 2026 statements. The active project directory is deliberately separate from the reusable manual and the historical 2022 rehearsal. Earlier practice decisions, PDF acceptance and public-repository authorization retain their original scopes. New contest work must use its actual instructions and requirements.

## Validation and limits

These files are setup instructions, not tool permission enforcement, automatic chat creation or a live orchestration test. The prompts can be inspected through the [independent review](../../qa/CHAT_SETUP_PROMPTS_REVIEW_2026-11-05.md). A static review checks the documented contracts. A new chat proves initialization only when it actually reads the files and returns its readiness response.

The same folder's [earlier bootstrap](../BOOTSTRAP_PROMPT.md) is for an explicitly activated project and can create its control records. This pack's initialization-only turn is narrower. Reading an example does not execute it.
