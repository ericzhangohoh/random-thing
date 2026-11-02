# Historical Paper Review Method

## Scope and priority

The original MCM/ICM collection is the central archive. Its inventory retains every independent paper and its award/category distinctions, but [current research scope](SCOPE.md) excludes all biology-related papers from further work. Screen title/problem metadata before reading; defer uncertain topics and choose clearly non-biological cases. Eligible HiMCM papers, official problems and commentary provide complementary context.

The unit of review is an actual document, not a filename. Match paper identity to its cover and content. Pair it with the official problem where available. If the original statement is missing, identify that limitation; a paper's restatement does not independently establish full requirement coverage.

## Reading procedure

Apply the scope screen before this procedure. Full reading below concerns an admitted, eligible paper; it does not override the user's exclusions or require exhaustive archive completion before workflow delivery.

1. Check source hash, page count, identity, claimed award provenance and available problem statement.
2. Read every available page in bounded, untruncated batches, including references, appendices and code.
3. Inspect text extraction coverage. Empty, scrambled or implausibly short pages require OCR and/or direct visual inspection. Formula extraction needs special care even when surrounding prose is readable.
4. Inspect substantive figures, tables, diagrams and image-encoded equations at a readable scale. Text extraction alone cannot establish their content.
5. Write a substantive review with physical-page references, separating author reports, reviewer inference, static consistency checks and executed reproduction.
6. Record missing appendices, inaccessible attachments or unresolved visual passages. Reading all available pages is different from reconstructing unavailable material.
7. Preserve both strengths and weaknesses. The aim is to learn modeling architecture, reasoning and communication, with critical checks supporting responsible transfer.

## Required analytical coverage

- Actual task and paper response map.
- Model architecture and information flow between components.
- Representation, solver and validation as distinct layers.
- Explicit selection rationale, alternatives and unreported justifications.
- Data, parameters, proxies, weights and consequential assumptions.
- Actual validation design and the strength of claims it supports.
- Strong mathematical, experimental and expository moves.
- Consistency of summary, body, equations, figures, code and recommendations.
- Transferable principles, triggering conditions and limits for HiMCM.

## Research synthesis

Compare papers solving the same problem before treating different method names as meaningful differences. Compare task structure, data, objectives, feasibility conditions, baselines and validation design. Then compare recurring reasoning patterns across problems and years.

Every proposed workflow rule is categorized as official requirement, observed practice, conditional modeling advice or project coordination design. Record supporting cases and counterexamples. Do not infer causal reasons for award outcomes from a selected set of successful papers.

## Progress integrity

`tools/build_corpus.py` inventories and extracts. `tools/update_review_status.py` reports explicit reader coverage declarations from review records. Neither script performs the intellectual review. Numeric reproduction remains separately labeled.

The main workflow may be usable before full research is complete, but it must remain labeled as an operational edition with research in progress until all required readings, synthesis and quality checks are complete.
