# A03 full implementation reviewer r02

**CHANGES_REQUESTED** on closed scientific-r02 negative-path safeguards, not a finding that ordinary forecast numbers are wrong. Exact review: `qa/adversarial_implementation/r02/review.md`; pinned targets `r02/pins.json`; pre-probe plan `r02/strategy.md`.

F01/P2: changing only selected IDs in copied frozen receipt to Q/T1-Q leaves verified development tables intact but actual final stage accepts and writes COMPLETED/selection_changed=false. Receipt then contradicts original scores/eligible temperature pair. Validate freeze semantics against verified development evidence and rule; require exact tamper rejection before output.

F02/P3: completed production with injected D=-1 at2023 emits NONPOSITIVE_CO2/null and invalid_count278 but nonpositive_co2_count0. Count violations before nulling or from statuses; one evaluated direct violation should count1. Ordinary positive actual paths unaffected.

Successful challenges: all44 artifacts recovered,32 numerical outputs independently byte-identical; future-only perturbation invariance; predictedCO2 response; dev/final table tamper rejection; crossing-before-invalid, invalid-before-crossing and negative-temperature semantics. Original target hashes unchanged. Full results and preserved failed reviewer fixture are documented; corrected diagnostic fixture completes successfully.

Owner X/root notified early. New versioned code/run required for safeguards, preserving r02. Await repairs for scoped recheck; no scientific selector change or global holdout reset. Same reviewer as prior A02/A03 assignments.
