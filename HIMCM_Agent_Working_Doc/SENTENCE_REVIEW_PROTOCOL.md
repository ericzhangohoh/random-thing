# Full-sentence review and final artifact protocol

Use this protocol when a paper needs three independent reviewers to inspect every sentence, an additional challenge to the model, author repairs, and a separate review of every final rendered page. It supplements the [execution playbook](EXECUTION_PLAYBOOK.md), [independent-reviewer role](roles/independent-reviewer.md) and [shared-directory protocol](setup/SHARED_DIRECTORY_PROTOCOL.md). It is an executable assignment and evidence convention, not software that launches agents automatically.

This document was authored after the rehearsal review. Authoring it does not extend any independent verdict on that paper. The worked-example receipts below retain their own exact targets and limits.

## 1. Establish the brief and actual reviewers

Record the problem, audience, required answers, accepted scientific evidence, output format and exclusions before dispatch. For the current 2022 Problem B rehearsal, the brief is genuine editable LaTeX compiled to a conventional monochrome academic PDF, with actual Times New Roman text in headings, body, tables, captions and plot labels. Compatible mathematical fonts are allowed only with an explicit disclosure. Do not call a visually similar substitute Times New Roman, silently change fonts, or distribute proprietary font files. Use black/gray, patterns and markers that remain distinguishable without color. These are the current project's requirements, not asserted universal contest rules.

The punctuation target is **zero semicolon symbols**. The final rendered document must contain **at most three combined ASCII `;` (U+003B) and fullwidth `；` (U+FF1B)** across all pages, including captions, references, notes, tables and imported figures. This limit applies to the paper, not to code or this protocol. Preserve an accurate source title or quotation when necessary and count its punctuation. Do not evade the limit with lookalike glyphs or make a sentence less clear merely to hit zero.

“Natural variation” means that sentence length and structure serve the argument and audience. Preserve concise results, longer explanations and necessary qualifications. Do not impose a sentence-length quota, inject mistakes, manipulate data, remove important caveats, or conceal AI involvement to make prose appear human.

| Logical responsibility | Required work | Independent context and ownership |
|---|---|---|
| R1: argument and justification | Read every record and its context, test reasoning and necessity of claims | Fresh reviewer context, own `qa/<R1>/` and handoff |
| R2: facts, evidence and numbers | Read every record, trace factual/numerical claims and their qualifications | Separate fresh reviewer context, own `qa/<R2>/` and handoff |
| R3: readability and coverage | Read every record, inspect meaning, cadence and omitted text | Separate fresh reviewer context, own `qa/<R3>/` and handoff |
| M: additional model attacker | Challenge consequential assumptions, evaluation design and alternatives | Separate context without authorship of the target model, own `qa/<M>/` |
| W: author | Resolve findings and produce new immutable candidate versions | Own manuscript, figure source and author receipts, never reviewers' verdicts |
| V: final artifact reviewer | Inspect every final page, rebuild when feasible and bind the review chain | Independent of target authorship, own `qa/<V>/` and handoff |
| C: coordinator | Assign scope, reconcile findings and accept named deliverables | Own shared control records, not other reviewers' findings |

These are logical responsibilities, not evidence that seven agents ran. Record actual session/context IDs, models if known, authorship history, start/finish status and exact writable paths. Three names in one continuing context do not constitute three independent reviewers. A new context is also insufficient if it merely repeats another verdict. If staffing cannot provide the three requested independent contexts, state the shortfall rather than relabel self-review. Reviewers may work sequentially when concurrency is limited. The coordinator launches contexts only under applicable authorization and tool availability.

Each reviewer forms findings from the target and evidence before reading peer sentence critiques. Prior scientific receipts may define accepted inputs, but are not proof of the new wording. A reviewer who designed, authored or repaired a target must disclose that conflict and cannot independently accept that same work. Later authoring of a protocol does not retroactively alter a closed paper review.

## 2. Freeze the input packet

C releases a version only after W closes its author handoff. Do not review a moving file. The packet contains:

- Exact manuscript source, rendered PDF, sentence register, non-sentence inventory and their SHA-256 hashes.
- Problem/requirements, source definitions, accepted claim/evidence register, numerical output manifest, model specification and known evaluation-access history.
- Included figures and other dependencies with hashes, build command/CWD, compiler and required font availability.
- Named review scope, exclusions, ownership, expected outputs, author receipt and any previous review/delta needed for recheck.

A minimal identity record is:

```json
{
  "packet_id": "paper-rNN",
  "status": "FROZEN_FOR_REVIEW",
  "artifacts": [
    {"role": "source", "path": "paper/manuscript-rNN.tex", "sha256": "<64 hex>"},
    {"role": "pdf", "path": "paper/build-rNN/manuscript-rNN.pdf", "sha256": "<64 hex>"},
    {"role": "register", "path": "paper/sentence-register-rNN.json", "sha256": "<64 hex>"}
  ],
  "evidence_manifest": {"path": "control/accepted-evidence.json", "sha256": "<64 hex>"},
  "author_receipt": {"path": "handoffs/W/author-rNN.md", "sha256": "<64 hex>"},
  "scope": "<named deliverable and exclusions>",
  "reviewer_contexts": {"R1": "<actual ID>", "R2": "<actual ID>", "R3": "<actual ID>"}
}
```

Verify hashes at opening and closure. Record output hashes in a separate receipt or manifest rather than trying to embed a file's own hash inside itself. If any target changes, stop affected conclusions and obtain an immutable revision. Never approve promised future bytes.

## 3. Build the inventory and audit its completeness

Give each prose block and sentence a stable ID. Store exact decoded sentence text, kind, source file/line, block text, section and PDF location. Compute `text_sha256` over the exact UTF-8 sentence string, without normalization. Additions receive new IDs. Retain IDs for edited sentences when their identity is clear and record old/new text. Explain split/merge mappings and removed IDs rather than silently renumbering the entire paper.

Inventory deliberate fragments as records: equation lead-ins, caption fragments, bibliography authors/titles/dates, notes and disclosures. Do not classify them as bad sentences merely because they are not standalone prose. Keep a separate inventory of mathematical displays, table headers/cells, figure axes/legends/ticks/annotations, headings, title, running furniture and contents repetitions. A count of “314 records” need not mean 314 grammatical sentences.

Every sentence reviewer independently checks completeness, not just the provided list:

1. Read the actual source, including included files, custom macros, bibliography and appendices. Match registered blocks to their exact source bodies. A regex over one macro is insufficient if other macros or files emit prose.
2. Extract text from the actual PDF, including imported vector figure text. Map registered text to pages using documented normalization only for matching. Keep exact hashes unnormalized.
3. Examine extracted text left outside the register: unregistered captions, table notes, figure annotations, reference fragments, disclosure text and furniture. Classify each residue rather than deleting it as noise.
4. Inspect relevant rendered regions where extraction is missing or ambiguous. Rasterized or outlined lettering needs visual inspection or checked OCR. An empty extractor result does not establish that text or semicolons are absent.
5. Record coverage, exceptions and missing items. Add missing records through W/C and issue a new register. Inspect paragraph/equation/table context as well as each isolated row.

Remove only identified running heads and terminal page numbers when matching across pages. Do not broadly remove every line containing a header phrase: a bibliography title may contain the same words. Keep raw extraction and the normalization/filter implementation in the review directory.

## 4. Complete the three independent ledgers

Each of R1, R2 and R3 reads **every** record. The three lenses are not permission to divide the manuscript into thirds. Scripts may inventory, hash, compare and format judgments, but may not generate generic PASS rationales as a substitute for reading.

A ledger has top-level reviewer identity, authorship declaration, target source/PDF/register hashes, scope, evidence bindings and one row for every registered ID. Use a schema such as:

```json
{
  "id": "VAL03.03",
  "text_sha256": "<SHA-256 of exact_text UTF-8>",
  "exact_text": "<exact registered text>",
  "kind": "sentence",
  "source": {"path": "paper/manuscript-rNN.tex", "line": 138},
  "pdf_pages": [6],
  "verdict": "PASS",
  "rationale": "<specific explanation of this record's meaning/evidence/clarity>",
  "evidence": [{"path": "<source or output>", "sha256": "<hash>", "locator": "<page, row, claim ID>"}],
  "finding_id": null,
  "repair": null,
  "provenance": {"kind": "personally_read_with_context"}
}
```

Per-record verdicts may be `PASS`, `FRAGMENT_PASS`, `REPAIR`, `SUGGEST` or `UNVERIFIED`. Define any alternative vocabulary and its mapping. Separate a required editorial repair from an optional preference. A specific PASS rationale can be short, but must explain why that record works under the reviewer's lens. If no numerical assertion occurs, R2 still checks scope and wording instead of inventing an evidence citation.

Each finding names location, exact version/text hash, severity, demonstrated problem, evidence, consequence, minimum repair and remaining uncertainty. Send consequential findings promptly while finishing the full ledger. Do not manufacture a quota of defects. A suspicion needs a discriminating check, not a false assertion of error.

Each reviewer returns a complete machine-readable ledger, readable ledger/report, independent completeness and punctuation checks, evidence/scripts actually used, limitations and closed handoff. Overall verdicts are `ACCEPTED_FOR_SCOPE`, `CHANGES_REQUESTED` or `INSUFFICIENT_EVIDENCE`. They are not human approvals or universal correctness certificates.

## 5. Copyable reviewer assignments

Fill all placeholders. Give each R reviewer the common prompt plus exactly one lens. Do not include another sentence reviewer's conclusions in the initial packet.

```text
COMMON FULL-SENTENCE ASSIGNMENT
You are [R1/R2/R3], actual context [ID], reviewing [PROJECT_ROOT].
Read [PROTOCOL_PATH] and the frozen input packet [PATH, SHA256].
Targets: source [PATH, SHA256], PDF [PATH, SHA256], register [PATH, SHA256].
Accepted scientific evidence: [MANIFEST PATH, SHA256].
You did not author or repair these targets. Disclose any contrary history.
Write only [QA DIRECTORY] and [HANDOFF PATH]. Do not edit targets or peers' work.

Personally read every record and its paragraph/equation/table context under
[YOUR LENS BELOW]. Form findings before consulting peer sentence critiques.
Independently search source and PDF for missing prose, fragments, captions,
notes, references, disclosure, table cells and figure text. Inspect extraction
exceptions. Count ASCII and fullwidth semicolons across the entire final PDF:
zero target, combined maximum three. Natural variation must preserve facts,
logic, caveats and AI disclosure. Do not inject errors or use style quotas.

Return a complete exact-ID/exact-text-hash ledger with specific per-record
rationale/verdict/repair, a readable report, completeness/punctuation evidence
and a closed handoff bound to actual target hashes. Report actionable issues
promptly, but finish every record. Distinguish reproduced checks from inspection
and inherited evidence. Rehash inputs at closure. Never approve future bytes.
First acknowledge actual inputs read, owned paths, missing capabilities and
next action. If coverage cannot be completed, report INSUFFICIENT_EVIDENCE.
```

```text
R1 LENS — ARGUMENT AND JUSTIFICATION
For every record ask what work it does in the argument, what premises support
it and whether its conclusion follows. Check model-choice justification,
alternatives, claim strength, causal language, circular reasoning, chronology
and whether limitations survive the summary, conclusion and article. Trace
consequential assertions beyond neighboring prose when needed. Do not mistake
a technically correct calculation for an answer to the requested question.
```

```text
R2 LENS — FACTS, EVIDENCE AND NUMBERS
For every record check factual scope, source applicability, units, baselines,
time windows, numerical values/rounding, ordering, denominators and comparisons.
Trace claims to exact evidence locations. Check data-vintage versus historical
availability, development versus later assessment and any score exposure.
Reproduce only the checks actually authorized and report their finite scope.
Do not call acceptance of a prior run an independent rerun of that computation.
```

```text
R3 LENS — READABILITY AND COVERAGE
For every record check reader meaning, antecedents, terminology, cadence,
necessary detail and whether a fragment is completed by its actual context.
Find undefined internal workflow language, reversed relationships and omitted
qualifications. Preserve useful variation without a length quota. Inspect
whole paragraphs and the standalone summary/article. Independently reconcile
all rendered text with the inventory, including material outside prose macros.
```

## 6. Additional model challenge

The model attacker supplements the sentence reviews. Fluent, correctly copied prose can still rest on weak assumptions. Assign an actual question that could alter the answer, such as aggregation weights, baseline fairness, identifiability, leakage, threshold semantics or an untested horizon. Do not demand that the attacker defeat the model.

```text
MODEL-ATTACK ASSIGNMENT
Act as [M, ACTUAL CONTEXT] for [PROJECT_ROOT]. Targets and scientific inputs:
[EXACT PATHS/HASHES]. Write only [QA PATH] and [HANDOFF]. Do not alter models,
source data, accepted outputs or the selection rule.
Independently challenge consequential assumptions and validation design.
Inspect the specification and evidence, then choose bounded counterexamples
or alternative comparisons that could change the conclusion. State the
objective, assumptions, exact command/derivation and outcomes. Preserve
negative results and distinguish demonstrated failures from hypotheses.
Record which scores you had already seen. Any newly introduced analysis is
post-assessment unless there is evidence otherwise. Do not retroactively
reselect or label the same predictions under a new loss as new validation.
Return findings, evidence, limits and a scoped verdict. New scientific claims
must receive their own evidence review and coordinator decision before W uses
them. This task does not replace three complete sentence ledgers or final
artifact inspection.
```

If M's new diagnostic is proposed for publication, a reviewer other than its author verifies the diagnostic. Update the accepted claim register only through C. The additional evidence then becomes a dependency of affected text reviews.

## 7. Repair without erasing the review history

C consolidates findings into an owner-assigned repair list, retaining reviewer IDs and disagreements. Resolve disagreements by evidence or a recorded scope decision, not majority vote. W writes a new revision and preserves old artifacts and receipts. Accepted numerical evidence is not rewritten to fit a preferred narrative.

```text
AUTHOR-REPAIR ASSIGNMENT
Act as W for [PROJECT_ROOT]. Read frozen candidate [IDENTITIES], consolidated
findings [PATH/HASH] and accepted evidence [PATH/HASH]. Write only [OWNED PATHS].
For each finding implement the smallest sufficient repair or give a supported
response. Preserve all required caveats, results and disclosure. Do not alter
scientific inputs/models/results without a separate authorized task.
Produce new source, PDF, sentence register, non-sentence inventory and hashes.
Provide exact old/new text, changed/added/removed IDs, split/merge mappings,
context changes and figure/table/equation deltas. Build and inspect the export,
including current LaTeX/TNR/monochrome and punctuation requirements.
Close an author receipt listing actual checks, unresolved items and build
instructions. Do not change reviewer reports or claim independent acceptance.
```

For text changes, each of R1–R3 independently verifies the delta and personally reads every changed/added record plus affected context. Check deletions for lost requirements or caveats. Changed assumptions, evidence, definitions or ordering may invalidate unchanged words too. Rerun affected scientific checks when necessary.

Carry forward an unchanged judgment only when ID and exact text hash match, its evidence and interpretation remain applicable, and prior review provenance is retained. Include the prior ledger path/hash, prior row ID/hash and rationale. Reissue a **complete** final ledger, not merely a list of changed rows. Preserve the original receipt rather than editing it into a new verdict.

For a claimed layout-only revision, independently diff the actual source, verify all registered text/IDs and non-sentence contents, inspect included dependency hashes, and classify every change. If truly limited to layout, carry forward sentence judgments with the same provenance rule, then recheck final PDF coverage and punctuation. A new PDF hash always needs a new binding. Mathematical, table, legend or evidence changes are not layout-only simply because sentence IDs stayed constant.

## 8. Review every final page

Release V only after the author handoff and all three final ledgers are closed for the same version. V verifies their bindings, renders the exact final PDF and opens every page at readable scale. Contact sheets are navigation aids, not a substitute for legible inspection of equations, labels and dense references.

```text
FINAL ARTIFACT ASSIGNMENT
Act as V, independent of target authorship, for [PROJECT_ROOT]. Read final
source/PDF/register [PATHS/HASHES], closed author receipt and all three closed
review packages [PATHS/HASHES]. Write only [QA PATH] and [HANDOFF].
Verify every final ledger ID/text hash and provenance against the final register.
Independently extract final PDF text, reconcile coverage and count ASCII plus
fullwidth semicolons. Render and personally inspect EVERY final page, recording
page-level findings and the rendering environment/scale.
Check actual Times New Roman text and plot fonts, disclosed compatible math,
monochrome readability, units/symbols, clipping, collisions, captions, equations,
lead-ins, references, contents destinations, page limits and standalone required
sections. Inspect imported figures, raster text and extraction exceptions.
If feasible, inspect build commands and rebuild in your own fresh directory.
Record actual logs/exits and compare extracted text, pagination and renders.
Do not require binary PDF identity when metadata differs, but explain any
substantive difference. Missing rebuild capability narrows the verdict.
Return exact-byte ACCEPTED_FOR_SCOPE, CHANGES_REQUESTED or INSUFFICIENT_EVIDENCE,
with page coverage, checks, limitations and final rehashes. Do not edit targets,
install dependencies silently, or claim a new numerical rerun from old receipts.
```

V must independently inspect every final page for this protocol's all-page claim. If any changed page is not inspected, state the narrower coverage and do not label it complete. Author page checks are useful evidence but do not replace V's reading. Pixel equality and font reports supplement visual inspection. Font names alone do not establish every glyph's font, and grayscale pixels alone do not establish readable contrast.

## 9. Mechanical closure checks and their limits

Use the project's real schema, or write a documented adapter. The following illustrates basic checks for the ledger schema above, with `register.sentences` containing `id` and `sentence`. It does not perform the personal reading, discover missing register text, validate facts or inspect pages. Run it only with absolute paths to a frozen candidate and exactly three final ledgers.

```python
# python3 verify_bindings.py REGISTER PDF LEDGER_R1 LEDGER_R2 LEDGER_R3
import hashlib, json, pathlib, subprocess, sys
register_path, pdf_path, *ledger_paths = map(pathlib.Path, sys.argv[1:])
assert len(ledger_paths) == 3
register = json.loads(register_path.read_text())
rows = register['sentences']
expected = [(r['id'], r['sentence']) for r in rows]
assert len({r[0] for r in expected}) == len(expected)
for path in ledger_paths:
    ledger = json.loads(path.read_text())
    records = ledger['records']
    assert [(r['id'], r['exact_text']) for r in records] == expected
    for row in records:
        digest = hashlib.sha256(row['exact_text'].encode('utf-8')).hexdigest()
        assert digest == row['text_sha256']
        assert row['rationale'].strip()
        assert row['verdict'] in {'PASS', 'FRAGMENT_PASS'}
        assert not row.get('repair')
    # Also verify actual source/PDF/register and dependency hashes from each
    # ledger's identity manifest, using the declared project schema.
result = subprocess.run(['pdftotext', '-layout', str(pdf_path), '-'],
                        check=True, capture_output=True, text=True)
counts = {label: result.stdout.count(char)
          for label, char in [('ASCII', ';'), ('fullwidth', '；')]}
assert sum(counts.values()) <= 3, counts
print({'records_per_ledger': len(expected), 'semicolon_counts': counts})
```

If accepted ledgers use another verdict vocabulary or retain optional suggestions, adapt the allowed set explicitly and require a recorded disposition for each remaining suggestion. Do not silently treat `UNVERIFIED` or unresolved required repairs as PASS. Count punctuation in both raw and layout PDF extraction where available and inspect image/outlined text. A machine count is a lower bound when text is not extractable.

A finite set of checks establishes only what was checked: hashes identify bytes, sentence matches establish textual presence, a rebuild tests one environment, and a model attack tests named alternatives. None proves universal correctness, future prediction reliability, complete absence of errors or compliance with rules that were not inspected. Agreement among agents is not new empirical evidence.

## 10. Coordinator acceptance and safe public sync

C verifies exact artifacts, closed author receipt, three complete final ledgers, resolved required findings, model-attack disposition, final all-page receipt, evidence dependencies and applicable human authority. Record an acceptance manifest with all hashes, scope, limitations and the release destination. Keep scientific acceptance, sentence acceptance, artifact acceptance, external publication and live submission as distinct decisions.

```text
COORDINATOR-CLOSURE ASSIGNMENT
Read [FINAL PACKET] and all closed receipts. Verify actual target hashes,
complete ledgers, evidence provenance, finding closure and all-page coverage.
Resolve remaining dependencies without rewriting reviewer verdicts. Record
named-scope acceptance or the precise remaining blocker. Preserve the history.
Update current links only to accepted bytes. Publication must follow existing
explicit destination/scope authorization; do not infer live contest submission.
If authorized to sync publicly, use an explicit file allowlist, inspect the
exact proposed publication diff, verify the destination and visibility, exclude
secrets/private material/unlicensed font binaries, publish only that scope, and
verify remote commit/files afterward. Report actual completion or the remaining
failure. No approval is invented and no unavailable operation is claimed.
```

Before public sync, check the authorized destination and what “sync” includes. Existing explicit authorization remains valid for its stated scope; do not repeatedly ask for unchanged permission. If a new destination, sensitive content or expanded scope needs approval, prepare the concrete reviewable package first and explain that precise gap. Remote publication is not authorized merely by this protocol.

Preserve frozen receipts. If sanitization is needed, make a separate public export with a redaction/omission manifest and new hashes, rather than editing accepted evidence in place. Exclude credentials, private chats, personal absolute paths where unnecessary, proprietary font binaries, and source documents without redistribution rights. Confirm relative links survive the public layout. Stage only owned, intended files, inspect staged content and use a normal forward update rather than overwriting unrelated history. Verify the remote revision and file identities after transfer. Local commit success or a pre-push receipt does not prove publication. The reviewer need not perform Git operations, and this document's creation performs none.

## 11. Worked example: exact final 2022 rehearsal

These links point to real local receipts in the sibling rehearsal tree. They will also work in a repository preserving both directories. A standalone copy of this working document must include the authorized example files or identify that the links require the full tree. Do not substitute an earlier PDF's acceptance for the final LaTeX version.

| Evidence | Actual receipt or artifact |
|---|---|
| Author's closed repairs/build account | [T15 writer handoff](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/handoffs/T15/writer-visuals-r02.md) and [author receipt r05](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/paper/latex-r01/author-receipt-r05.json) |
| R1 argument acceptance | [A06 final handoff](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/handoffs/A06/argument-r04.md) |
| R2 evidence acceptance | [A07 final handoff](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/handoffs/A07/sentences-r03-final.md) |
| R3 reader acceptance | [A08 final handoff](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/handoffs/A08/reader-r03-final.md) and [complete final ledger](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/qa/latex-attacks/reader-r01/revised-r03/sentence-ledger.json) |
| Post-assessment diagnostic and limits | [C18 accepted scope](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/control/accepted-claims-latex-r01.json) |
| Independent all-page artifact acceptance | [T16 canonical review](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/qa/latex-pdf-review-r01/review.md) |
| Exact final source and register | [manuscript-r05.tex](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/paper/latex-r01/manuscript-r05.tex) and [sentence-register-r06.json](../HIMCM_Rehearsals/2022_HiMCM_B_2026-11-03/paper/latex-r01/sentence-register-r06.json) |

The final bindings are:

```text
source r05: 1f8259757db5732f38d5cf69b37419c98f1725270559d90b1e82ba8839d92b55
PDF r05:    2ec474ac04debd26d8acbf4b3393ba46e220536415d19e324597770ec7629aac
register r06: 2a7a89c62ceeef6c7aae688a81e506edcc957022110d62411f24ed0bd446bd3c
```

This example has 314 records in 93 prose blocks, plus 54 separately inventoried non-sentence items. The text repair changed 16 records and added three, while 295 judgments carried forward only with exact identity and provenance. Later layout changes preserved all 314 texts. The final PDF has 16 pages, its article occupies page 15, and both semicolon counts are zero. T16 separately inspected every final page and checked all three complete ledger bindings. These counts are evidence of this run, not quotas for another paper.

The example also shows why scope matters: equal target-year weighting used the same predictions under a different loss and was published as a post-assessment diagnostic, not fresh validation or permission to reselect. The final receipts explicitly exclude new numerical validation, causal identification, long-range reliability and live contest submission. Reuse the discipline, not unsupported claims of universal verification.
