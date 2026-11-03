# T05 computation acknowledgment r00

Task/session: T05; computation; /root/rehearsal_computation. Status: acknowledged for pre-G2 ingestion only.

Question: Can the frozen supplied workbook be transformed reproducibly into unambiguous year-keyed tables without altering values or admitting future observations?

Read: DOC_ROOT WORKING_DOC sections 1–5, computation role, COORDINATION, shared-directory and retention/run-manifest contracts; T05, intake/state; T01 closed r01 handoff, dictionary, quality, checks and inventory; entire four-page problem text. Spreadsheets skill applied to read-only handling. No workbook authoring, model fits or source-network retrieval are planned.

PROJECT_ROOT: `/Users/ericzhang/Desktop/himcm/HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03`.
DOC_ROOT: `/Users/ericzhang/Desktop/himcm/HIMCM_Agent_Working_Doc`.

## Input bytes acknowledged

| Path | SHA-256 |
|---|---|
| `control/intake.md` | `8b04f0cf2402212f7f3a6c5ee1be5fafd2b2bb4a730ee63dafa61adea2a13c2a` |
| `control/state.md` | `d3a5e2501f06dd1991f07b814b82e07f6aaa1d937b72d90f09ac2957e394b114` |
| `control/tasks/T05.md` | `81596e3ada8ec452b3451a9b663f16387c3bf397c4ea5aeec53234117c5cb08b` |
| `handoffs/T01/domain-data-r01.md` | `24ce4ba3f834d057e4402cf4593134db419e21aa8e0c0e51d48504c608a955b3` |
| `research/data-dictionary-r01.md` | `7b3d932b653b835431b068f857f540ca28bc1ab66dfab6c3e72a81a072c27028` |
| `research/data-quality-r01.md` | `3a73e4241c5a872f6782735efac5ab7081d62ee5ab8ee3e5245c7e27db3cfb1a` |
| `research/data-checks-r01.json` | `b83a1a998c964e7340a4691d7b439dc19d7eba514f0fd38c4cb2ea06c55965f3` |
| `research/problem-fulltext-r01.txt` | `bd2bff98f4c9d92bdd33328ae046dcc9a27b87379d8c828b54955220032979bf` |
| `research/artifact-hashes-r01.json` | `4c4161752d7eac5dd01a01d35be18e7b10a65701f77cdcf6b66e943fd5d68451` |
| `inputs/2022_HiMCM_Data.xlsx` | `73a4c73433d530cdbd3bb7509131bea528eeffd52d1a66b2ddeddf44543a2a4a` |
| `inputs/2022_HiMCM_Problem_B.pdf` | `fb9000006eb0402d24c4e810a0e6d4cd69f26f94181a48adbfe9c795d6669ece` |

The T01 supplied-vintage contract is consumed: annual Mauna Loa CO2 ppm (63 years 1959–2021), annual global temperature anomaly relative to 1951–1980 (64 years 1958–2021), 63 matched records by integer year; 1958 retained in standalone temperature. Original negative anomalies and hundredth-unit precision remain valid. Current web values are definition evidence only and never ingestion inputs. The annual/March and OECD CO2-equivalent caveats are understood.

Owned paths only: code/data/, code/modeling/, code/experiments/, code/qa/, data/processed/, unique runs/T05-*/, handoffs/T05/computation-rNN.md. No code/visualization, original input/raw, model, research, control, reviewer, paper, other handoff or Git writes.

First action: implement read-only extraction to explicit schema and year-keyed CSVs; independent input/negative checks; immutable run-local code/input/dictionary/config/environment snapshots and actual isolated recovery. Source originals will be hashed before/after. Runs refuse existing directories.

Missing dependency: T02 closed accepted model/experiment/interface revisions and explicit coordinator G2 release. No full historical fitting, forecasting, scientific selection or inferred equations until those arrive. Current state.md is stale relative to T01 completion; dispatch/task packet gives bounded pre-G2 authority, and root must reconcile control state.

Expected handoff: handoffs/T05/computation-r01.md pins ingestion run, processed data hashes, executed checks and limitations. Root/R next action is review ingestion and release pinned mathematics only when G2 is recorded. A successful ingestion is not scientific acceptance.
