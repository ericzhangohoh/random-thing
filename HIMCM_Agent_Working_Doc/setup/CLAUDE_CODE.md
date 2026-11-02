# Claude Code: six roles over one local project

## Default: independent sessions with explicit handoffs

Open separate Claude Code sessions in the same active project and assign a bounded role to each. Keep one coordinator. Start only the workers whose tasks can make useful progress; six logical roles do not require six constantly running sessions.

In each terminal, use the actual project path:

```bash
cd '/absolute/path/to/active-contest-project'
claude
```

Check `claude --version` and `claude --help` on the machine where you will run this. If Claude Code is not installed, use Anthropic's current [setup instructions](https://code.claude.com/docs/en/setup); installation is a separate action and is not performed by this document. The official [Claude Code repository](https://github.com/anthropics/claude-code) points to that documentation.

Paste [BOOTSTRAP_PROMPT.md](BOOTSTRAP_PROMPT.md) into the coordinator first. Replace its paths and problem information. The coordinator creates the project control records and prepares assignments. In each worker session, paste the assignment prompt in its role document with the actual task ID, inputs, output paths and deadline. The shared project records are the persistent source of state.

| Session label | Role document | Typical first task |
|---|---|---|
| C | [Coordinator](../roles/coordinator.md) | Requirement map, dependency graph, assignments and checkpoint plan |
| D | [Domain-data](../roles/domain-data.md) | Read statement/attachments; assess data and mechanism evidence |
| M | [Modeler](../roles/modeler.md) | Define baseline, alternatives and distinguishing tests |
| X | [Computation](../roles/computation.md) | Build checkable prototype and baseline once inputs are specified |
| R | [Independent reviewer](../roles/independent-reviewer.md) | Review framing/specification or a pinned result version |
| W | [Writer-visuals](../roles/writer-visuals.md) | Evidence outline and communication requirements; later accepted-result plots |

Use a visible terminal label and record the actual session ID when available. To return to a known conversation, select it explicitly with `claude --resume`; the CLI also accepts a session ID or name. Avoid relying on “continue most recent” when several roles share a directory. These entry points are documented in the [CLI reference](https://code.claude.com/docs/en/cli-reference).

## What is shared and what is not

The sessions can see the same files, subject to their actual access permissions. They do not automatically share every conversation, assumption or decision. A worker must read its assignment and named inputs. A completed file does not wake another terminal or prove that another agent has read it.

Default notification procedure:

1. The worker writes its handoff and reports its path in its own session.
2. The human gives that path to the coordinator: `Read handoffs/T014/computation-r01.md and update the task state.`
3. The coordinator reads the evidence, records acceptance or review needs, and gives the next worker a bounded task.
4. The human relays that assignment to the appropriate session.

Native messaging can later automate the notification, but files remain the durable evidence. Read the [shared-directory protocol](SHARED_DIRECTORY_PROTOCOL.md) before concurrent editing.

## Keep the startup instruction short

The [CLAUDE.md template](CLAUDE.md.template) points sessions to the main document and records a few invariants. Copy it only into the intended active project, adjust its paths, and inspect any existing `CLAUDE.md` before merging. Do not overwrite a user's existing instructions. The complete workflow stays in the working document and role files; it is not converted into a skill.

Claude Code documents `CLAUDE.md` as persistent contextual instruction, not an enforcement mechanism. Sessions begin with separate contexts, so project records and targeted rereading are still necessary. See [memory documentation](https://code.claude.com/docs/en/memory).

## Role boundaries versus tool permissions

“Only write `models/`” is an operating instruction. It is not an operating-system restriction, and a YAML ownership table does not configure Claude Code permissions. Enforce narrower tool or filesystem access separately when needed. The project should work with ordinary permission settings; it does not require bypassing prompts.

The distinction matters for a reviewer: allowing a shell can permit writes even if edit tools are unavailable. A strict document/code inspection can use only read/search tools; an independent computational reproduction needs controlled execution and its own output directory. State which mode the reviewer actually used.

The current CLI distinguishes tools available to the agent from actions pre-approved to run. In particular, `--allowedTools` is not an exclusive tool allowlist; `--tools` restricts built-in tool availability and does not itself remove MCP tools. Inspect the effective configuration and current [permissions documentation](https://code.claude.com/docs/en/permissions) and [CLI reference](https://code.claude.com/docs/en/cli-reference) before relying on a restriction. No permission configuration is installed by these templates.

## Optional: native role definitions

A native subagent is useful for a bounded task inside one coordinator session. Its definition can carry a role prompt and tool choices, while the full working document remains the specification. Current documentation places project definitions in `.claude/agents/`; see [custom subagents](https://code.claude.com/docs/en/sub-agents).

Six inert wrappers are supplied under [optional_native_agents/](optional_native_agents/README.md): coordinator, domain-data, modeler, computation, reviewer and writer-visuals. They reference the complete role documents rather than replacing them with short prompts. If you choose to use the reviewer example:

1. Copy it to `.claude/agents/himcm-reviewer.md` in the intended project.
2. Resolve `DOC_ROOT` in its body, and verify the named tools against your installed version.
3. Ask the coordinator to use that subagent on a specific artifact version and return its report.
4. Save the returned report verbatim with attribution if the read-only tool restriction prevents the reviewer writing it itself.

The example has no shell or write tool. It can inspect available text and source files, but cannot claim to have rerun a numerical experiment. It is optional precisely because a reviewer session with a narrow, controlled execution scope may be more appropriate for computational verification.

The other wrappers expose the tools needed by their role, including execution or writes where appropriate. Their path boundaries remain instructions; a `tools` list does not constrain a write tool to one directory. Use the assignment manifest and appropriate effective permissions. Do not activate all wrappers merely because they exist, and do not assume their presence launches six sessions automatically.

## Optional: native agent teams

As checked on 2026-11-02, Anthropic documents agent teams as experimental and disabled by default. A team supplies coordinated sessions and messaging, while each teammate keeps its own context; the lead's conversation history is not automatically copied. The official documentation also identifies resumption and coordination limitations. See [agent teams](https://code.claude.com/docs/en/agent-teams).

If the human chooses this mode, enable it for the intended launch rather than changing global settings merely to try the workflow:

```bash
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude
```

Check effective settings because existing project or managed configuration may affect behavior. Then ask for a coordinator plus the needed role teammates, give each the same explicit task/paths used in independent-session mode, and preserve the single-writer assignments. Native task status does not replace `control/` or the evidence handoffs. Do not assume native teams isolate files, enforce scientific independence or automatically resolve edit conflicts.

Use native teams when workers need substantial back-and-forth and the installed capability has been tested on a practice problem. Use independent sessions when predictable manual control is sufficient. Neither choice changes the mathematical workflow.

## Practice before a live problem

Run one small historical problem through admission, a baseline, a deliberate failed check, repaired results, independent review, one figure and a final rendered page. Confirm that a fresh session can recover state from files and that no role overwrites another's work. Check current competition rules and the AI-use record described in the main working document before using the arrangement during a live contest. A tool's availability does not establish contest permission.

**Verification status:** documentation and static review only. Claude Code was absent from the authoring environment; no live native-agent/team execution or settings change was performed.
