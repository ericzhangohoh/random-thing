# A03 implementation repair request

Owner: computation. Actual adversarial evidence: qa/adversarial_implementation/r02/review.md and handoffs/A03/independent-reviewer-r02.md.

F01: selected IDs in a copied frozen-selection receipt can change without changing development scores/CSV hashes, yet final stage accepts and writes selection_changed=false. Repair semantic validation of IDs, eligibility, declared selector/tie rule, scores/metrics and sequential temperature choice; reject inconsistent frozen receipt before final output. This is a consequential stage-integrity defect. It does not show that the actual r02 D/T1-D selection is wrong.
F02: nonpositive CO2 rows become null before diagnostic counting, so a known injected negative path reports nonpositive_co2_count=0. Preserve/count actual failure reasons or raw validity evidence; distinguish nonpositive values from unrelated overflow/missing cases. This is a confirmed failure-diagnostic defect, without impact on the actual positive paths.

Create new source revisions and new run T05-scientific-20261103-r03; retain every closed r02 file/run. No scientific form, split, selector, envelope or source-data change. Add meaningful regression checks for both defects, including independent frozen-field tampering and valid controls. Reconcile current model semantics and all prior tests. Regenerate full primary run using current code, preserve dependencies and replay, compare scientific values with r02 (report provenance-only differences honestly). A03 independently repeats attacks against repaired targets. T10 reviews new identities/chronology and scientific equivalence; no unnecessary repeat of all unchanged mathematics.

Current r02 science remains evidence at its own version, but full execution contract is CHANGES_REQUESTED. G3/final publication waits on repaired-run and claim-version acceptance. Models/interpretation and writer's downstream bindings must use the current accepted release after recheck.
