# Optional native role wrappers

These files are **templates**, not active `.claude/agents/` definitions. The default remains independent sessions using the plain role documents. If the human chooses native definitions, copy the needed template to `.claude/agents/<name>.md` inside the intended active project, replace `DOC_ROOT` in its body with the absolute working-document path, and inspect the available tools in the installed Claude Code version.

| Template | Role | Tools intentionally available |
|---|---|---|
| [himcm-coordinator](himcm-coordinator.md.template) | Coordinator | Read/search, local edits/execution and delegation |
| [himcm-domain-data](himcm-domain-data.md.template) | Research and source admission | Read/search, web research, local writes/execution |
| [himcm-modeler](himcm-modeler.md.template) | Mathematical specification | Read/search and local edits; computation delegated |
| [himcm-computation](himcm-computation.md.template) | Implementation and runs | Read/search, edits and execution |
| [himcm-reviewer](himcm-reviewer.md.template) | Strict read-only review | Read/search only; returns its review in text |
| [himcm-writer-visuals](himcm-writer-visuals.md.template) | Manuscript, plots and export | Read/search, edits and execution |

Tool availability and path ownership are different. Except for the deliberately strict reviewer, these definitions do not provide an OS-enforced write sandbox. The full role instructions and task-specific manifest still apply. The reviewer template cannot execute tests; use an explicitly scoped reviewer session when independent numerical checks are needed.

No template pins a particular paid model; `model: inherit` follows the caller's selected model. No template changes permission mode, installs a plugin, enables experimental teams or adds a background schedule. Current fields and project location were checked against [official subagent documentation](https://code.claude.com/docs/en/sub-agents) on 2026-11-02. Native execution has not been live-tested in the authoring environment.
