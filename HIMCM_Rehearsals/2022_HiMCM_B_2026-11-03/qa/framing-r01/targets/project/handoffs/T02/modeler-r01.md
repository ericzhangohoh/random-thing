# Handoff — T02 — modeler — r01

Producer: `/root/rehearsal_modeler`; date: 2026-11-03. Recipient: coordinator `/root`, then independent reviewer and computation. Status: complete for pre-computation specification scope; ready for independent review, not self-accepted.

Question answered: how to cover every official requirement with a practicable, justified and auditable mathematical experiment before calculating historical model results.

## Inputs actually read

Initial exact paths/hashes and scope acknowledgment are in `handoffs/T02/modeler-r00.md`. Read the complete original four-page PDF directly, WORKING_DOC Sections 1–5 (and relevant modeling stages), modeler role, full approach/justification document, shared-directory protocol, coordination, task/control inputs and relevant templates. No historical solution paper or biological source was read. This role did not parse the XLSX or independently browse source pages; T01 owns that evidence.

Additional T01 provisional packet actually read:

- `handoffs/T01/domain-data-r01.md` — `24ce4ba3f834d057e4402cf4593134db419e21aa8e0c0e51d48504c608a955b3`
- `research/data-dictionary-r01.md` — `7b3d932b653b835431b068f857f540ca28bc1ab66dfab6c3e72a81a072c27028`
- `research/data-quality-r01.md` — `3a73e4241c5a872f6782735efac5ab7081d62ee5ab8ee3e5245c7e27db3cfb1a`
- `research/source-register-r01.md` — `9efcc164ce5e11aa7aec725fa8895c88d632b40e2846db0fd76eefa9bbb2be75`

`control/state.md` was reread and still described pending admission at inspection. The coordinator's message confirms that explicit delegated-practice authority is being recorded; this role does not claim a human approval or edit control.

## Outputs and pinned identities

| Artifact | SHA-256 |
|---|---|
| `models/framing-r01.md` | `1b1ccb4007c43ef937ba67da2a79cf1782c6499b8321fdcf1b5b6822e108a75b` |
| `models/model_spec-r01.md` | `4c3de3faa1234fe8e9add94fe2b6c7a655808ceb351b6c2dfea775d894f3c7da` |
| `models/model_decision-r01.md` | `c6d0779939cab9349102b97235f2e203f78d17dc71ee9c881ed3247f36cd4bb4` |
| `models/experiment_plan-r01.md` | `e2209d5a21c601445ac11d46a738c125be94efde02c16f4bf12f594e3eb781c6` |
| `models/assumptions-r01.md` | `824af993532cd8a35204fa8c137db490c8f2cec0345c6b08454825ebe24c77e9` |
| `models/model_interface-r01.md` | `12d9084979d7d5c65479a41a124d106a769dc9ce86a37500413293f0eafcb611` |
| `models/toy_selfcheck-r01.py` | `327c64a9ecfbb2608102f9db894b5db3c90c34d5348311d1e8c356bfe7e8f336` |
| `models/toy_checks-r01.json` | `ebd63a9df5125d7d19fd60b4ba12f9faaf7fc827c8e59c4b439c620cf2314652` |
| `models/artifact-hashes-r01.json` | `d5051bbb0ceda4562a6ac0e3dc6893227a803c6fe7fb23ad3a9683d3ff27bc16` |

All writes were limited to `models/` and this role's `handoffs/T02/modeler-rNN.md`. No code/, data/, control/, other-role, archive or Git mutation occurred. The toy script lives in models as an author self-check, not the target implementation.

## Proposed decisions and findings

The architecture retains three CO2 paths: anchored ten-year drift baseline D, quadratic Q and exponential E. It compares temperature-time T0 with an empirical log-CO2 T1 path, tests shared trends/differences, and extends T1 using predicted CO2. No parameter estimates, empirical forecast scores, selected winner or future crossing year have been invented.

Development uses fixed origins 1981/1986/1991/1996/2001, horizons 1–10, all targets through 2011. The selected CO2 and temperature rules must be persisted before final 2012–2021 assessment from origin 2011. Final errors cannot choose a new winner. Unchanged rules may subsequently refit through 2021 for projections. The full official table was visible in the statement, so this is computationally untouched final assessment, not concealed human exposure.

T01 source semantics are incorporated provisionally: supplied annual CO2 cannot directly verify March, and the OECD 685-ppm value is CO2-equivalent. Keep the requested pure-CO2 685-ppm exercise without falsely testing a different quantity. Temperature thresholds retain the 1951–1980 baseline. Year-key join and supplied vintage are mandatory.

First threshold passage means integer annual central-path year after 2021, with explicit already-at-origin, non-crossing-through-2300 and invalid-path statuses. Beyond 2031 is outside maximum tested horizon and is conditional extrapolation. Empirical historical-error envelopes are restricted to tested horizons and have no promised coverage probability; structural and last30-window spreads are sensitivity, not confidence intervals. No causal parameter or policy effect is identified.

Alternatives deferred: unsupported saturation/logistic parameters, high-degree polynomial extrapolation, externally calibrated carbon-cycle mechanisms, large Monte Carlo/searches and causal claims unavailable from two annual series. These reasons are recorded in model_decision-r01, rather than hidden by selecting only a preferred algorithm.

## Checks actually executed versus inspected

Executed: `python3 models/toy_selfcheck-r01.py`; 17 synthetic checks passed, no supplied observations used. Checks cover ten-year interval/ties, drift, quadratic/exponential/time/log-CO2 coefficient recovery, log-reference invariance, fractional and exact annual crossings, constant non-crossing, already-above origin, nonmonotone first passage and invalid log inputs. Exact code, software versions, spec/script hashes and numeric outputs are retained. Rerun after the final specification wording update passed identically. This is modeler self-check, not computation implementation validation and not independent review.

Executed: file existence and SHA-256 inventory; toy result passed/count/source-data flags; current spec/script identity matches toy result. Inspected: complete official coverage, mathematical units/definitions, time availability, failure statuses, no arbitrary OECD-agreement selection, no fictional empirical winner. No actual-data model fit, empirical forecast score, independent numerical review, final PDF generation or visual QA was performed by this role.

## Consumer receipt and unresolved dependencies

T01 r01 was read and its exact paths/hashes are above. Agreed interface: annual Mauna Loa CO2 ppm, global annual anomaly against 1951–1980, CO2 1959–2021 (63 rows), temperature 1958–2021 (64), 63 matched years by integer key, supplied vintage only. Source-context values and later observations remain excluded from fitting.

This is a **provisional-consumption receipt**, not a claim that T01 was accepted: the state available to this role still showed pending admission. Coordinator must release the accepted T01 packet; computation must acknowledge exact accepted hashes before fitting. If T01 changes units/rows/source interpretation, these specifications and all affected downstream evidence need review. No remaining mathematical input is knowingly missing, but implementation/reviewer feedback may reveal an ambiguity requiring a new revision.

## Requested next action

Coordinator: pin T02 r01 and assign independent framing/specification review, including the source-meaning caveats, split/freeze order, forecast-input leakage, horizon claims and model/interface consistency. Record G1/G2 as delegated practice decisions only after the required review and exact toy evidence. Then computation should acknowledge accepted source/spec hashes, independently implement E01–E07, reproduce arithmetic and retain real failure/repair evidence. Reviewer must not repair this author's artifacts in place. Return findings to modeler for a new revision. This role will await feedback.
