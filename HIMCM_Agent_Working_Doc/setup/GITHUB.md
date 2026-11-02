# GitHub and local versioning

## Chosen arrangement for this project

The user has explicitly chosen **one private repository for the complete substantive project**, including the original PDF libraries, archives, downloaded reference materials, this working document, research notes and code. The chosen target is [ericzhangohoh/himcm](https://github.com/ericzhangohoh/himcm). This supersedes the lighter original suggestion to keep the PDF library outside Git.

Keep source manifests, source URLs, retrieval records and original licensing/provenance information with the materials. The chosen full-project upload also retains the extracted text and extraction metadata used for corpus reading. Exclude credentials, local machine state, temporary files and disposable build/runtime caches. Do **not** use a blanket `*.pdf`, `*.zip`, `*.xlsx`, extraction-directory or library-folder exclusion. Private repository storage is the selected distribution scope; it does not change the original materials' provenance.

This guide is not a repository-creation or push receipt. The executing coordinator must verify the actual remote, private visibility and uploaded commit before reporting success. No remote operation is performed merely by reading this document.

## What belongs in the repository

| Include | Exclude by default |
|---|---|
| Original downloaded papers, problem statements, attachments and archives | Access tokens, `.env` secrets, private keys and local credentials |
| Working document, role instructions, setup templates and historical reading records | OS metadata such as `.DS_Store` and `__MACOSX/` |
| Source manifests, extracted text/metadata, source classification and reading-coverage records | Disposable temporary page renders and debug screenshots |
| Original code, model specifications, experiment configs and environment lockfiles | Virtual environments, `node_modules/`, Python bytecode and test caches |
| Meaningful result tables, run receipts/logs, validation records and final figures | Temporary export/build intermediates and incomplete download fragments |
| Manuscript sources, bibliography and deliberately retained delivery snapshots | Machine-specific Claude settings, local session data and worktree internals |

Do not confuse an execution log needed for evidence with a disposable application cache. This is why the supplied [`.gitignore` template](gitignore.template) does not ignore every `*.log`, every result directory, every PDF or every image. Review unusually large derived outputs individually; preserve their reproducible recipe and evidence if they are excluded.

Git's ignore rules apply to untracked files. They do not remove a previously committed secret or large file from history. Inspect the staged paths before committing; changing `.gitignore` after a mistaken commit is not a complete remedy. See [GitHub's ignore-file guidance](https://docs.github.com/en/get-started/git-basics/ignoring-files).

## Start with one local writer for Git operations

Several agents can work in disjoint owned directories, but a shared checkout has a shared Git index and current branch. The coordinator alone stages, commits, switches branches and integrates changes. A modeler should not switch the shared branch while computation is running or stage a writer's unfinished manuscript.

Use explicit file/path staging after checking current changes. A useful checkpoint contains a coherent, reviewable unit: an accepted model specification, a validated experiment with its receipt, or a manuscript revision tied to accepted results. Commit messages identify the concrete change and reason. A commit hash provides a version reference; it is not a scientific validation certificate.

Before a checkpoint, the coordinator checks:

```bash
git status --short
git diff --stat
git diff --cached --stat
git diff --cached --name-only
```

Read the relevant staged changes rather than accepting the statistics alone. Verify that the original library remains included, caches are excluded as intended, and no secrets or unrelated personal files were staged. Preserve original files rather than editing them to make a repository smaller.

## Connecting or verifying the private remote

Repository creation and publication are separate from the modeling workflow. The current user has authorized the full private upload for this project. The coordinator should inspect whether the target already exists and whether the local remote already points to it before creating or changing anything. Do not create a second repository because an earlier command's outcome was unclear.

For an existing checkout/remote, these are useful inspection commands:

```bash
git remote -v
git status --short
git log -1 --oneline
gh repo view ericzhangohoh/himcm --json nameWithOwner,visibility,url
```

If creating a new repository in another project, choose private visibility and avoid prepopulating a conflicting README/history when importing an existing local repository. The official [repository creation guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) explains the choices. Do not copy account names, remote URLs or prior authorization from this project into an unrelated future project.

After a push, verify the remote branch points to the intended local commit and that representative substantive files are present. Report the repository URL, visibility, commit and any genuinely excluded material. Do not infer a completed upload from a local commit or a partially transmitted pack.

## Optional later: branches and worktrees

The initial workflow uses one checkout and explicit file ownership. Add separate worktrees when experiments need overlapping code changes or branch switching would disturb another worker. Each worktree has its own working files and index while sharing repository objects; see [Git's worktree manual](https://git-scm.com/docs/git-worktree).

Use one branch/worktree per substantial experimental route. Give the agent its actual worktree root, input versions and output scope. Do not assume uncommitted files from the main checkout appear in the new worktree. Ignored local datasets/caches may also need an explicit read-only source path or regeneration. Record the integration base and final commit in the handoff.

The coordinator reviews and integrates a finished branch, resolves model/result dependencies, and reruns affected checks. Retain the last accepted version while evaluating a candidate. Never use force-reset, force-push or worktree deletion as a routine way to resolve a conflict or discard another agent's work.

## Competition boundary

Use the repository for private preparation and the team's permitted work. During a live HiMCM contest, follow the current rules restricting discussion/sharing to the registered team; do not turn on public issues/PRs, outside reviewers, public Pages or external AI review integrations as an incidental convenience. Private storage is a project choice, **not a statement that COMAP approves every possible cloud service or sharing arrangement**. The coordinator's current-rule snapshot and AI-use reporting procedure in the main working document govern the live project. See the [official HiMCM instructions](https://www.contest.comap.com/highschool/contests/himcm/instructions.html).

## Public patterns used in this design

The design borrows limited ideas rather than installing a framework:

- [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science): separate immutable raw data, derived data, code and reports. The local ownership and handoff rules here are our own design.
- [GitHub's gitignore collection](https://github.com/github/gitignore/blob/main/Python.gitignore): ignore environments and generated caches while retaining dependency lockfiles where useful.
- [Anthropic's code-review plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review): give independent reviewers bounded perspectives and demand actionable evidence. Its numerical confidence threshold, automatic comments and plugin installation are not adopted.

Sources were inspected on 2026-11-02; exact fetched-file identifiers are recorded in [SOURCES.md](SOURCES.md). No third-party framework is required by the working document.
