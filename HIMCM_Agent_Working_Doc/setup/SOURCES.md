# Setup sources and verification record

Checked **2026-11-02**. Official product documentation is the source for product behavior. Public repository examples supply limited design patterns; they are not authoritative competition rules. No source code or plugin from these repositories was installed or executed.

## Official Claude Code documentation

| Source | Used for |
|---|---|
| [Memory and project instructions](https://code.claude.com/docs/en/memory) | Startup project instructions; contextual guidance versus enforcement |
| [Custom subagents](https://code.claude.com/docs/en/sub-agents) | Optional project subagent definition and distinct task context |
| [Agent teams](https://code.claude.com/docs/en/agent-teams) | Experimental opt-in, separate teammate contexts, coordination and edit conflicts |
| [Permissions](https://code.claude.com/docs/en/permissions) | Tool/access configuration is separate from role prose |
| [CLI reference](https://code.claude.com/docs/en/cli-reference) | Launch/resume commands and tool-availability versus preapproval distinction |
| [Setup](https://code.claude.com/docs/en/setup) | Authoritative installation destination, linked rather than executed |

Feature details may change. Check the installed version and current documentation before using optional features. The independent-session workflow does not depend on native teams, plugins or a particular model name.

## Public GitHub patterns inspected through the connected GitHub tool

The identifiers below are **file blob SHAs returned by the connector**, not repository commit SHAs. URLs point to the inspected default-branch file; those branches may later change.

| Repository file | Returned blob SHA | Limited pattern retained |
|---|---|---|
| [anthropics/claude-code README](https://github.com/anthropics/claude-code/blob/main/README.md) | `70754c523454ad5fd94e5ef910cc347cf69e6f6b` | Official repository points to product documentation and project-directory launch |
| [anthropics/claude-plugins-official code-review README](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-review/README.md) | `42cc8095cd2c54e043f9276224df408dca4f48cc` | Bounded independent review perspectives and actionable findings |
| [github/gitignore Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore) | `6ff7378f20ee9570a320cf59ae0fe9c5b100e722` | Runtime/environment/cache exclusions; no wholesale template copying |
| [drivendataorg/cookiecutter-data-science README](https://github.com/drivendataorg/cookiecutter-data-science/blob/master/README.md) | `ac9eb221225cec566db13334515ef8e3332de8a8` | Raw/derived/source/report separation |

We did not adopt the code-review plugin's confidence-score threshold as mathematical proof, its installation instructions, or its automatic PR-comment behavior. We did not run the Cookiecutter generator. The six-role scopes, scientific evidence requirements and task handoffs are specific to this working document.

## Git and GitHub documentation

- [Ignoring files](https://docs.github.com/en/get-started/git-basics/ignoring-files): repository ignore rules and already-tracked files.
- [Creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository): visibility and initializing a new remote.
- [Git worktree](https://git-scm.com/docs/git-worktree): optional separate checkouts, indices and shared repository data.

## Competition sources

The main working document owns the current-rule snapshot. Setup links to [official HiMCM instructions](https://www.contest.comap.com/highschool/contests/himcm/instructions.html) and defers live-contest decisions to that snapshot and current official material. Product capabilities and public GitHub examples do not establish contest eligibility or permission.

## What was actually verified

- Read current official documentation and the four public repository files above.
- Parsed all six optional definitions and checked their documented fields; the reviewer alone is deliberately restricted to read/search tools.
- Checked local Markdown links, template parseability where applicable, ownership consistency and intended ignore-rule behavior.
- Did not install or execute Claude Code, a native agent team, a third-party plugin, a GitHub Action or a repository generator.
- Did not change user/global settings through this setup work. Repository creation and upload, if performed by the coordinating task, have their own verification record.
