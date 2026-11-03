# T05 computation handoff r01 — ingestion ready

Role/session: computation, /root/rehearsal_computation. Status: ingestion complete and ready for independent review; full T05 remains pending explicit G2 release. This is not scientific acceptance.

Question: faithfully transform the frozen supplied XLSX to year-keyed tables and prove execution/recovery without fitting models.

## Inputs consumed

Acknowledged before substantive work in computation-r00.md: complete problem text, T01 r01 dictionary/quality/checks and source inventory, exact admitted XLSX SHA-256 `73a4c73433d530cdbd3bb7509131bea528eeffd52d1a66b2ddeddf44543a2a4a`, task/role/core workflow and run-retention protocols. The source/definition limitations remain: annual Mauna Loa proxy, temperature baseline 1951–1980, no post-2021/live-revised observations. Model_spec-r01.md was later read for planning only; T02 is not treated as released and no historical model fit was executed.

## Fixed outputs and identity

| Path | SHA-256 |
|---|---|
| `code/data/ingest_r01.py` | `efe066f5e0175657e3d73ac39cf0e6ccbf3d57c93bda62678ff3d313144b2ece` |
| `code/data/ingestion_config-r01.json` | `15c901e6433d1c1e93cf26b05e1fc460fba3222715c6f2b87a762c15934469ec` |
| `code/data/ingestion_schema-r01.json` | `e01859b64494a9984e6e0d969f5202fbfab44a4bf44faf62cce780158d74165c` |
| `code/qa/test_ingestion_r01.py` | `ea6216ca83bed48b0de6ede4386b55bfb7758074de6b83d541ed49e18e905d49` |
| `code/qa/retrieve_retained_r01.py` | `864887a852c0d295b697035d94d5539db562f6a6a95eb9d16ff32f31a22d9921` |
| `code/experiments/run_ingestion_r01.py` | `a7e77eb158f707e7f2101f26da740c0fe7ef3f55771ab9d658a2161d73437499` |
| `data/processed/co2-r01.csv` | `fbc29861bf3c76df99752b920bfb35476945195905cd6c59029e40bb9511ea7f` |
| `data/processed/temperature-r01.csv` | `fbef7efc1761da9f76058b5b60d22d50d79aa023536908666c874a3c60296855` |
| `data/processed/joined-r01.csv` | `61ee5eaea9f7e0143006feee49c7985f5bdb0dd036be8c2b7152a305acd6563e` |
| `runs/T05-ingestion-20261103-r02/manifest.json` | `82fcb8ad41592412a28e98fdb7880d0e57ad493566bd14e9f2da6e760960a4b5` |
| `runs/T05-ingestion-20261103-r02/execution.log` | `6a428b562a4f39b86151e32c7468e7931695f222e8b2f8330ca57082f7a88a1b` |
| `runs/T05-ingestion-20261103-r02/reproduction-check.json` | `ffa85a1ab9b0431c6b0321237046a173dab25707f5ff605c921f2b02b4f34a39` |
| `runs/T05-ingestion-20261103-r02/isolated-recovery/retrieval-receipt.json` | `56196ad26c6e62c3ad68bc0f1c74bc1d11b7a6e72d7d25b623d75dc482907c54` |

All code and run dependencies have exact snapshot bytes under `runs/T05-ingestion-20261103-r02/reproduction/`; the manifest inventories them. Data/processed copies have the same hashes as run-local CSVs. Closed runs are immutable. No other role's artifacts were edited.

## Actual execution and checks

Executed command (exit 0):

```
/Users/ericzhang/.venvs/default/bin/python3 code/experiments/run_ingestion_r01.py --project-root /Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03 --run-id T05-ingestion-20261103-r02
```

Working directory is PROJECT_ROOT. Environment, version lock, per-subprocess commands, start/end times and stdout/stderr are retained. Per-subprocess limit 60 seconds; single BLAS/OpenMP threads. No optimizer/solver applied; solver status NOT_APPLICABLE.

Computed checks: 63 CO2 records for 1959–2021; 64 temperature records for 1958–2021; 63 inner-joined records for 1959–2021. Temperature-only year is 1958. Zero missing values, duplicate keys, formulas or unexpected populated cells. Negative temperature anomalies remain valid. Source schema/identity and complete year sets are mandatory; no imputation, value replacement, baseline shift or extra observations occurs. Numeric values are emitted at the supplied hundredth precision; raw reader representations are retained for every source row, maximum normalization delta in this reader was zero.

Nine unit tests passed: shuffled year join with an extra temperature year; valid negative/zero temperatures; binary-tail normalization; duplicate keys rejected; missing/future keys rejected; None/text/NaN/infinity/boolean values rejected; fractional/boolean/null years rejected; unsupported precision rejected; empty intersection produces no invented rows. The shuffled test is a counterexample to a row-position join.

Actual retrieval: all 16 inventoried dependencies copied into a new isolated directory and verified against hashes. A second ingestion from recovered code/config/input, with that isolated directory as CWD, produced five byte-identical output files. Recovery receipt and output-hash comparisons are pinned above. This proves local dependency recoverability and deterministic ingestion in the recorded available environment; it does not certify mathematical models or bundle Python/package binaries.

After closure, the same runner invocation with the same run ID was executed deliberately: exit 1 / FileExistsError, and manifest hash remained `82fcb8ad41592412a28e98fdb7880d0e57ad493566bd14e9f2da6e760960a4b5`. Both original input hashes were rechecked unchanged. No accepted result was overwritten.

## Preserved failure and environment repair

`runs/T05-ingestion-20261103-r01/` is retained as FAILED. Shell `python3` unexpectedly selected CLT Python 3.9 and failed while recording package versions because SciPy was absent. No tests or ingestion/processed export occurred. Its 14 prepared source/input/spec/config snapshots and error log remain intact. Full environment capture and retention recovery were not reached in that failed preparation; no reproducibility success is claimed for it. The app-bundled Python also lacked SciPy, discovered by a read-only import probe. No package was installed. The explicit existing default virtual environment provided Python 3.12 and numpy 2.5.3, scipy 1.18.1, pandas 3.0.5, openpyxl 3.1.5, and was used successfully for r02. Future tasks should use that explicit interpreter rather than ambiguous python3.

## Limits and next action

No fits, forecasts, model selection, threshold estimates or causal inference were executed. Ingestion tests and a successful exit do not establish scientific accuracy. Alternatives deferred: live data replacement, row-position joining, using 1958 in a CO2 pair, hidden cleaning and inventing unapproved equations.

Coordinator: pin r02 ingestion and request independent review as appropriate. When T02/G2 is explicitly released, send the exact accepted spec/experiment/interface paths and hashes. Computation will then acknowledge the accepted revision, implement the supplied known-answer and failure tests, and run the full numerical task in a new immutable directory. Reviewer: inspect the three CSVs against source and challenge the extraction/retention contract. Writer should use no scientific claims from this ingestion-only packet.
