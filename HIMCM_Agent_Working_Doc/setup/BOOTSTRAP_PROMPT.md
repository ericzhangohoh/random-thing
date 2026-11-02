# Paste into the coordinator session

Replace the bracketed values. This prompt creates the active project's working records when executed by an authorized agent; the file itself has no side effects.

```text
I want you to coordinate our mathematical-modeling work using a complete working
document, not a skill.

DOC_ROOT = [absolute path to HIMCM_Agent_Working_Doc]
PROJECT_ROOT = [absolute path to the active contest/practice project]
Problem = [year, competition, problem identifier, and statement path]
Mode = [practice or live competition]
Deadline = [date, time, timezone; or no fixed deadline]
Human team = [registered team context and division of responsibilities]
Available tools/languages = [known constraints, or inspect locally]

Read WORKING_DOC.md, roles/coordinator.md, and setup/SHARED_DIRECTORY_PROTOCOL.md
under DOC_ROOT. Inspect the current project before creating anything. Preserve
all originals and existing work. Current official problem and competition rules
take precedence over historical examples.

Set up or recover control/state.md, tasks.md, role_assignments.yaml, decisions.md,
glossary.md and evidence_index.md. Record the absolute roots above. Use six logical
roles: coordinator, domain-data, modeler, computation, independent-reviewer and
writer-visuals. You are the only editor of control/. Prepare explicit bounded
assignments for separate Claude Code sessions; I can relay the assignments and
handoff paths manually. Do not assume the sessions share conversation context.

Begin by reading the full statement and attachments, mapping each required
answer, identifying dependent subproblems, and checking the evidence/data gaps.
Have the modeler compare a simple defensible baseline with materially different
alternatives and define checks before large experiments. Allow early prototypes
to test feasibility. Keep an evidence outline and a viable delivery checkpoint.

Give each task an owner, input versions, exact write paths, expected artifact,
acceptance evidence and time/resource budget. Keep sources, assumptions,
computed findings and interpretations distinct. Do not let the writer fill an
evidence gap or let an author's self-check masquerade as independent review.

Do not install skills/plugins, change user settings, create a remote, publish or
push anything as part of this bootstrap. Do not enable native agent teams unless
I choose that setup. Ask only about material unknowns that cannot be resolved
from available files and current official sources; continue independent work.

First report the recovered/current state, important unknowns, dependency graph,
initial assignments and the next concrete evidence checkpoint.
```
