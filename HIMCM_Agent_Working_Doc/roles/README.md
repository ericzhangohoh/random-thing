# Six roles

These are detailed role instructions inside the working document. They are plain Markdown and can be used in independent Claude Code sessions. They are not skills and do not configure tools by themselves.

Read [WORKING_DOC.md](../WORKING_DOC.md) first, then the [shared-directory protocol](../setup/SHARED_DIRECTORY_PROTOCOL.md), then the assigned role. Each role file contains a pasteable assignment prompt, input/output boundaries, procedure, evidence requirements, failure handling and completion conditions.

| Role | Owns | Main handoff |
|---|---|---|
| [Coordinator](coordinator.md) | Shared control records and accepted project state | Bounded assignments, integration decisions and deliverable manifest |
| [Domain-data](domain-data.md) | Research records and admission of immutable sources | Source-backed mechanisms, data definitions, quality/coverage limits |
| [Modeler](modeler.md) | Mathematical specification and model-choice reasoning | Implementable model, alternatives, assumptions and validation design |
| [Computation](computation.md) | Data/model code and versioned runs | Reproducible outputs, implementation checks and experiment evidence |
| [Independent reviewer](independent-reviewer.md) | Review receipts and isolated checks | Evidence-based verdict for a pinned artifact and scope |
| [Writer-visuals](writer-visuals.md) | Manuscript, plot code and display artifacts | Clear evidence-linked argument, figures and rendered candidate |

The coordinator alone edits `control/`. Computation owns `code/` except `code/visualization/`, which belongs to writer-visuals. The reviewer does not repair its targets. The [assignment manifest](../setup/role_assignments.yaml.template) maps actual sessions to narrower paths before parallel work begins.

Every worker's first response names its task, inputs actually read, exact owned paths, missing dependency, first action and expected handoff path. Use [Execution Playbook](../EXECUTION_PLAYBOOK.md) for the first-dispatch table. Independent reviewer scripts and outputs belong under `qa/<review-id>/`; `code/qa/` contains computation-owned self-checks.

A role is a responsibility, not a requirement to buy another account, run six agents continuously or use a particular model. One person may relay tasks between sessions. Independence is assessed per reviewed artifact: if the same agent authored and reviewed it, label the result self-review or assign a fresh independent reviewer.

For three independent every-sentence reviews, model challenge, repair and exact final PDF acceptance, use the [Sentence Review Protocol](../SENTENCE_REVIEW_PROTOCOL.md).

Use [setup/README.md](../setup/README.md) for launch instructions, native-role template options and GitHub practices.
