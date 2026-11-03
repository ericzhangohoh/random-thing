# T09 recovery execution receipt

**Status: executed checks complete; independent review required.**

This directory is the replacement computation agent's isolated recovery of `T05-scientific-20261103-r03`. The agent reconstructed the objective, delegated practice authority, current release, quiescence and next action from durable records before executing. Its first acknowledgment is `handoffs/T09/computation-r00.md`. The session is `/root/early_mcm_continue`, an existing agent previously uninvolved in this rehearsal, not a new empty thread. No other agent supplied the numerical answers or executable commands used for recovery.

## What ran

The original manifest hash is `7bc6e1fe3498302d247b45fa97c4d13498edfbf5366cddd078ff7ebfaff4bc00`; producer handoff r05 hash is `ca0853e2b5433f1ed79fe9ccc5332150bb31dcb80e0a16ffdcca2761f48c2006`. Both were checked against coordinator state. The retained retrieval program recovered and verified all 88 dependencies into `recovered/`. All 23 identities in the retained G2 release matched. Scientific code was loaded from those recovered files, not current mutable project code.

The original wrapper was inspected, not rerun: it creates T05 run IDs and snapshots files from its project root. Instead, this recovery executed its recorded tests, workbook ingestion and separate development/final/production commands in the recovered directory. All writes, including temporary test directories, were confined to this T09 subtree. Original retained files, original run outputs, model records, inputs and control files were not modified.

The absolute interpreter `/Users/ericzhang/.venvs/default/bin/python3` was checked in this session: Python 3.12.14, NumPy 2.5.3, SciPy 1.18.1, pandas 3.0.5 and openpyxl 3.1.5 match the retained environment. Each child command used the recorded single-thread settings, disabled bytecode writes, and had a 60-second timeout. Package binaries were available locally; none were installed or bundled.

Commands from PROJECT_ROOT:

```text
/Users/ericzhang/.venvs/default/bin/python3 -B runs/T09-recovery-20261103-r02/recovery_driver.py
/Users/ericzhang/.venvs/default/bin/python3 -B runs/T09-recovery-20261103-r02/check_frozen_decision.py
```

These commands were actually executed. The driver deliberately creates new artifacts with exclusive writes, so running it again in this closed directory is not a supported retry. Use a new T09 directory and retained intake bytes for another attempt. Exact child argv, working directories, environment, timestamps, exit codes and stdout/stderr are in `commands/` and `execution_report.json`.

## Reproduction results

- The recovered ingestion, model and repair suites passed 9, 28 and 7 unittest methods respectively, including the repair suite's mutation subcases.
- Reingesting the retained official XLSX reproduced all three admitted year-keyed CSVs exactly.
- Development, final assessment and production ran in separate processes in that order.
- All 32 deterministic output files are byte-identical to the original manifest's hash-verified reference outputs.
- The other three files are timestamped receipts. Every field other than the explicitly listed timestamps and dependent receipt digests matches exactly. The new digest links were then checked against the actual new receipt bytes; local chronology and selected IDs also match. No numerical field was excluded from comparison.
- All 12 recorded postrun checks pass. There is no claim that rerunning the same checks supplies independent empirical validation.
- A separate standard-library calculation read only the 350 development-forecast rows, reconstructed absolute errors and pooled MAEs, checked origin/horizon/availability, and applied the specification's fixed tie and sequential selection rules. It confirms D followed by T1-D. It imports no original model/analysis module and reads no final forecast/metric table, but it still uses the reproduced predictions rather than independently validating their mathematics.
- Before/after hashes for the original manifest, 88 retained dependencies, 35 outputs and producer handoff match: 125 records unchanged.

The retained configuration keeps the original logical run ID so deterministic outputs can be compared byte-for-byte. The physical execution, commands and timestamps belong to this T09 directory. This is reproduction of the original scientific run, not a new model-selection experiment under a disguised identity.

## Controlled stale-dependency probes

Both probes are operational fixtures on copies, never changed official observations or new scientific conclusions.

1. **Tampered retained dependency.** A copied joined table changes its first CO2 value from 315.98 to 316.98 while retaining the original expected digest. The actual recovered retrieval program exits 1 with `Recovered artifact hash mismatch: data/processed/joined-r01.csv` and creates no success receipt. The invalid copy and failed retrieval remain inspectable. A separately versioned valid copy retrieves successfully with the original digest.
2. **Wrong frozen-output reference.** A copy of the genuine development-stage outputs changes only `development_metrics_sha256` in its frozen receipt to an incorrect digest. The actual retained final-stage command exits 1 with `Development evidence changed after freeze` before producing any `final_*` artifact. A new versioned directory receives the valid six-file development bundle; final and production then complete and reproduce the same 32 deterministic outputs and receipt semantics.

See `stale_probe_receipt.json`, the failed-command logs and `probes/valid-output-reference-v02/comparison.json`. These checks demonstrate rejection of these concrete stale dependencies and recovery of valid versions. They do not prove security against coordinated forgery, OS permission enforcement, or scientific correctness.

## Preserved failed attempt

`../T09-recovery-20261103-r01/` remains a failed recovery-harness attempt. Its primary reproduction and two rejection probes had succeeded. The harness then selected development inputs by filename prefix, accidentally including `development_error_samples.csv`, which is generated later by production. The recovered program correctly refused to overwrite it. The failure is in the recovery agent's fixture assembly, not in the original scientific computation.

The retry changed only the harness's file list to the six exact files emitted by development. Original scientific source, config and data bytes were unchanged. The failed r01 log, partial outputs and `failure_closure.json` remain preserved; r02 does not relabel that attempt as successful. The r02 intake is a byte-verified copy of the original r01 intake snapshots, preserving what was read at recovery start even if live coordinator state later advances.

## Scope and next action

G1/G2 authority is delegated practice, not an invented human reply. G3 and PDF completion were pending in the intake state and did not block this explicitly authorized verification. The original prior final-score exposure remains disclosed; local selection-before-final chronology does not establish global blindness. The recovery does not change any selector, numerical claim, model interpretation or gate.

This is actual Codex/file/runtime work, not a Claude-native launch, six-agent orchestration validation or contest submission. No Git operation, installation, global setting change, biological research or old solution-paper reading occurred. The coordinator should assign independent review of the pinned recovery artifacts before recording a recovery pass or releasing dependent claims. Scientific, claim and PDF acceptance remain separate responsibilities.
