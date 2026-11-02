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

Reviewed papers distinguish author reports, reviewer interpretation, static checks and numerical reproduction. Full numerical reconstruction of every historical paper has not been performed. Complete-corpus synthesis remains unfinished until the required readings and cross-paper analysis are complete.
