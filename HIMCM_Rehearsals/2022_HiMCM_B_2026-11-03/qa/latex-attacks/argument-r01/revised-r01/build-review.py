from pathlib import Path
import collections, hashlib, json, re, subprocess, unicodedata

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'paper/latex-r01/manuscript-r02.tex'
PDF = ROOT / 'paper/latex-r01/build-r02/manuscript-r02.pdf'
REGISTER = ROOT / 'paper/latex-r01/sentence-register-r03.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

expected = {
    SOURCE: 'f9f60adb63996ae83d2bffeec43e4e3b9e04cc10d9e85cbd1c3f452db8bed35b',
    PDF: 'c0e4a245b2b5013effbd7fcca5262db2114ab5b48e3162b5a7482707e2137e8e',
    REGISTER: '80e9e581927f4483cf99a3038dea6fb387ba9a903edec7b9b36cd69b8e940e7e',
}
assert all(sha(p) == h for p, h in expected.items())
reg = json.loads(REGISTER.read_text())
notes = {}
for line in (OUT / 'manual-notes.txt').read_text().splitlines():
    ident, verdict, rationale = line.split('|', 2)
    assert ident not in notes
    notes[ident] = (verdict, rationale)
assert set(notes) == {s['id'] for s in reg['sentences']}

# Independent Poppler extraction. The author's extraction script is not imported.
for option, name in [('-raw', 'rendered-raw.txt'), ('-layout', 'rendered-layout.txt')]:
    subprocess.run(['pdftotext', option, str(PDF), str(OUT / name)], check=True)
raw = (OUT / 'rendered-raw.txt').read_text()
layout = (OUT / 'rendered-layout.txt').read_text()
clean = re.sub(r'2022 HiMCM Problem B\s*Retrospective practice', '', raw)
clean = re.sub(r'(?m)^\d+\s*\f', '', clean)

def normalized(text):
    return ''.join(c.lower() for c in unicodedata.normalize('NFKD', text) if c.isalnum())

remainder = normalized(clean)
ledger, unmatched = [], []
for s in reg['sentences']:
    key = normalized(s['sentence'])
    matched = key in remainder
    if matched:
        remainder = remainder.replace(key, '', 1)
    else:
        unmatched.append(s['id'])
    verdict, rationale = notes[s['id']]
    ledger.append({
        'id': s['id'], 'exact_registered_text': s['sentence'],
        'text_sha256': hashlib.sha256(s['sentence'].encode()).hexdigest(),
        'source_line': s['source_line'], 'block_id': s['block_id'],
        'register_kind': s['kind'],
        'reviewer_classification': 'fragment_or_caption_label' if verdict == 'FRAGMENT_PASS' else 'sentence',
        'checked_dimensions': ['argument_role', 'natural_cadence', 'precision_and_qualifiers', 'surrounding_TeX_context', 'rendered_text_presence'],
        'verdict': verdict, 'specific_rationale_or_repair': rationale,
        'independent_pdf_match': matched,
    })
assert not unmatched
(OUT / 'normalized-remainder.txt').write_text(remainder)

# Independent balanced-brace inventory of visible prose macros.
tex = SOURCE.read_text()
body_start = tex.index('\\begin{document}')
body = tex[body_start:]
def group_at(text, pos):
    assert text[pos] == '{'
    depth, start = 1, pos + 1
    pos += 1
    while depth:
        if text[pos] == '\\':
            pos += 2
            continue
        if text[pos] == '{': depth += 1
        elif text[pos] == '}': depth -= 1
        pos += 1
    return text[start:pos-1], pos

spans, blocks = [], []
for match in re.finditer(r'\\(?:p|txt)\{', body):
    ident, after_id = group_at(body, match.end()-1)
    value, end = group_at(body, after_id)
    blocks.append(ident)
    spans.append((match.start(), end))
assert set(blocks) == {s['block_id'] for s in reg['sentences']}
masked = list(body)
for start, end in spans:
    masked[start:end] = ['\n' if c == '\n' else ' ' for c in body[start:end]]
residue = ''.join(masked)
residue = re.sub(r'\\begin\{(equation|align|tabular)\}.*?\\end\{\1\}', '', residue, flags=re.S)
(OUT / 'unregistered-source-residue.tex').write_text(residue)

stats = {
    'status': 'REPAIR_REQUESTED_FOR_VINTAGE_QUALIFICATION',
    'target_hashes': {str(p.relative_to(ROOT)): sha(p) for p in expected},
    'additional_claim_register_sha256': sha(ROOT / 'control/accepted-claims-latex-r01.json'),
    'records_individually_reviewed': len(ledger),
    'unique_manual_notes': len(notes),
    'verdict_counts': dict(collections.Counter(x['verdict'] for x in ledger)),
    'prose_macro_blocks_independently_found': len(blocks),
    'independent_pdf_unmatched_records': unmatched,
    'source_ascii_semicolons': tex.count(';'),
    'source_fullwidth_semicolons': tex.count('；'),
    'pdf_raw_ascii_semicolons': raw.count(';'),
    'pdf_raw_fullwidth_semicolons': raw.count('；'),
    'pdf_layout_ascii_semicolons': layout.count(';'),
    'pdf_layout_fullwidth_semicolons': layout.count('；'),
    'method_limits': 'Normalization verifies text presence, not layout. All manual rationales were authored after reading the complete register and surrounding TeX. The source and normalized PDF remainder were inspected for omitted prose. No numerical rerun or font audit is claimed.',
}
for filename, obj in [('ledger.json', {'review': stats, 'records': ledger}), ('verification.json', stats)]:
    temp = OUT / (filename + '.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    temp.replace(OUT / filename)
md = ['# A06 per-record sentence ledger', '', 'Every row contains an individually authored contextual rationale. FRAGMENT_PASS explicitly classifies reviewed caption labels, bibliographic fragments and equation lead-ins. NOTE is optional editorial polish. REPAIR rows share the one supplied-vintage issue.', '', '| ID | Exact registered text | Verdict | Specific rationale / repair |', '|---|---|---|---|']
for x in ledger:
    cells = [x['id'], x['exact_registered_text'], x['verdict'], x['specific_rationale_or_repair']]
    md.append('| ' + ' | '.join(c.replace('|', '\\|') for c in cells) + ' |')
temp = OUT / 'ledger.md.tmp'
temp.write_text('\n'.join(md) + '\n')
temp.replace(OUT / 'ledger.md')
assert all(sha(p) == h for p, h in expected.items())
print(json.dumps(stats, indent=2))
