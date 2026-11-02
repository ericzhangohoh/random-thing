#!/usr/bin/env python3
"""Read-only source inventory and page-preserving extraction; never claims human review."""
from __future__ import annotations
import argparse, concurrent.futures, csv, hashlib, json, re, subprocess, sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

DOC_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = DOC_ROOT.parent
SOURCE_ROOT = WORKSPACE / "MCM-ICM-master"
RESEARCH = DOC_ROOT / "research"
EXTRACTED = RESEARCH / "extracted" / "mcm_original"

def classify(path: Path, first: str):
    name, rel = path.name, str(path.relative_to(SOURCE_ROOT))
    low = name.lower()
    compact = re.sub(r"\s+", " ", first)
    if re.search(r"judg|commentary|comment|评委|点评|评阅", low):
        kind, basis = "commentary", "filename and first-page content"
    elif re.search(r"results?|press|获奖名单", low) or re.search(r"press release|COMAP is pleased to announce the results", compact[:1800], re.I):
        kind, basis = "results_announcement", "result/press filename or actual first-page press-release text"
    elif re.search(r"(?:mcm|icm).{0,6}problems?|problems?[_ -]+[a-f](?:\b|_)|题目|赛题", low):
        kind, basis = "problem_statement", "filename and first-page content"
    elif re.search(r"policy|instructions|rules|guidelines", low):
        kind, basis = "policy_or_instructions", "filename and first-page content"
    elif re.search(r"^[a-f][- _]*\d+", low) or re.search(r"team\s*(?:control\s*)?(?:number|#)|summary\s*sheet|team\s*\d{2,}", compact, re.I):
        kind, basis = "competition_paper", "team/summary identifier or team-coded filename"
    else:
        kind, basis = "unclassified_article", "manual content classification required"
    ym = re.search(r"(?:19|20)\d{2}", rel)
    year = int(ym.group()) if ym else None
    pm = re.search(r"^([A-F])(?:[-_ ]|\d)", name, re.I)
    if not pm:
        pm = re.search(r"([A-F])题", rel, re.I)
    if not pm:
        pm = re.search(r"problem\s*(?:chosen\s*)?[:：]?\s*([A-F])\b", compact, re.I)
    problem = pm.group(1).upper() if pm else None
    tm = re.search(r"^[A-F][- _]*(\d{2,})", name, re.I)
    if not tm:
        tm = re.search(r"team\s*(?:control\s*)?(?:number|#)\s*[:#]?\s*(\d{2,})", compact, re.I)
    if not tm:
        tm = re.search(r"team\s*(\d{2,})", compact, re.I)
    team = tm.group(1) if tm else None
    family = None
    if problem:
        family = "MCM" if problem in "AB" or (problem == "C" and year and year >= 2016) else "ICM"
    if kind != "competition_paper":
        if "ICM" in name.upper() and "MCM" not in name.upper(): family = "ICM"
        elif "MCM" in name.upper() and "ICM" not in name.upper(): family = "MCM"
    award = None
    for label in ["Outstanding", "Finalist", "Meritorious", "Honorable", "Successful", "Unsuccessful"]:
        if label.lower() in low:
            award = label
            break
    if award:
        award_basis = "Explicit source filename label; not independently verified"
    elif kind == "competition_paper" and "特等奖" in rel and "其他奖项" not in rel:
        award = "Outstanding (collection claim)"
        award_basis = "Parent collection directory label only; not independently verified"
    else:
        award_basis = "No award verified; do not infer from collection name"
    return dict(kind=kind, classification_basis=basis, classification_review_required=kind == "unclassified_article",
                family=family, year=year, problem=problem, team=team, award_label=award, award_basis=award_basis)

def process(path: Path):
    blob = path.read_bytes()
    sha = hashlib.sha256(blob).hexdigest()
    source_id = "mcm_" + sha[:12]
    cache = EXTRACTED / (source_id + ".json")
    textfile = EXTRACTED / (source_id + ".txt")
    error = None
    try:
        if cache.exists():
            extracted = json.loads(cache.read_text())
            pages = extracted["pages"]
        else:
            proc = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"], capture_output=True, timeout=150)
            if proc.returncode:
                raise RuntimeError(proc.stderr.decode(errors="replace")[:500])
            content = proc.stdout.decode("utf-8", errors="replace")
            parts = content.split("\f")
            if parts and not parts[-1].strip(): parts.pop()
            pages = [dict(physical_page=i+1, text=t, nonspace_characters=len(re.sub(r"\s", "", t)),
                          low_extraction=len(re.sub(r"\s", "", t)) < 180) for i,t in enumerate(parts)]
            extracted = dict(source_id=source_id, sha256=sha, extractor="Poppler pdftotext -layout; page boundaries retained",
                             warning="Extraction is not reading, formula verification, figure review, or numeric reproduction.", pages=pages)
            cache.write_text(json.dumps(extracted, ensure_ascii=False, indent=2))
            textfile.write_text("\n\n".join(f"=== PHYSICAL PAGE {p['physical_page']} ===\n{p['text']}" for p in pages))
        for p in pages:
            bad = sum(ord(c) < 32 and c not in "\n\r\t" for c in p["text"])
            p["encoding_suspect"] = bad / max(1, len(p["text"])) > .01 or p["text"].count("\ufffd") > 10
        extracted["pages"] = pages
        cache.write_text(json.dumps(extracted, ensure_ascii=False, indent=2))
        first = "\n".join(p["text"] for p in pages[:3])
        status = "extracted_not_reviewed"
    except Exception as e:
        pages, first, status, error = [], "", "extraction_failed", str(e)
    row = dict(source_id=source_id, source_relative_path=str(path.relative_to(WORKSPACE)),
               source_path=str(path), bytes=len(blob), sha256=sha, physical_pages=len(pages),
               extraction_status=status, extracted_text_path=str(textfile.relative_to(DOC_ROOT)),
               extracted_pages_path=str(cache.relative_to(DOC_ROOT)),
               low_extraction_pages=[p["physical_page"] for p in pages if p["low_extraction"]],
               encoding_suspect_pages=[p["physical_page"] for p in pages if p.get("encoding_suspect")],
               actual_review_status="not_reviewed", numeric_reproduction_status="not_reproduced", extraction_error=error,
               first_page_excerpt=first[:2200])
    row.update(classify(path,first))
    return row

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--workers",type=int,default=4)
    parser.add_argument("--ocr-source-id",action="append",default=[],help="OCR every physical page of a source, retaining a separate non-authoritative transcription")
    args=parser.parse_args()
    RESEARCH.mkdir(exist_ok=True); EXTRACTED.mkdir(parents=True,exist_ok=True)
    if args.ocr_source_id:
        existing=json.loads((RESEARCH/"corpus.json").read_text())["file_records"]
        for sid in args.ocr_source_id:
            record=next(r for r in existing if r["source_id"]==sid)
            ocrdir=EXTRACTED/(sid+"_ocr");ocrdir.mkdir(exist_ok=True)
            def one_page(n):
                textpath=ocrdir/f"page_{n:03}.txt"
                if textpath.exists(): return dict(physical_page=n,text=textpath.read_text())
                img=subprocess.run(["pdftoppm","-f",str(n),"-l",str(n),"-scale-to","2200","-singlefile","-png",record["source_path"]],capture_output=True,check=True,timeout=60).stdout
                proc=subprocess.run(["tesseract","stdin","stdout","-l","eng","--psm","3"],input=img,capture_output=True,check=True,timeout=120)
                txt=proc.stdout.decode(errors="replace");textpath.write_text(txt)
                return dict(physical_page=n,text=txt)
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
                pages=list(pool.map(one_page,range(1,record["physical_pages"]+1)))
            out=dict(source_id=sid,warning="OCR transcription is not full review and may misread formulas, labels and symbols; visually check before relying on it.",pages=pages)
            (ocrdir/"pages.json").write_text(json.dumps(out,ensure_ascii=False,indent=2))
            (ocrdir/"full_text.txt").write_text("\n\n".join(f"=== PHYSICAL PAGE {p['physical_page']} ===\n{p['text']}" for p in pages))
            print(f"OCR cached for {sid}: {len(pages)} pages; not reviewed",flush=True)
        return
    paths=sorted(SOURCE_ROOT.rglob("*.pdf")); rows=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for n,row in enumerate(pool.map(process,paths),1):
            rows.append(row)
            if n % 25 == 0: print(f"Extracted {n}/{len(paths)} files (not reviewed)",flush=True)
    # Preserve explicit manual inventory corrections in a separate data file.
    overrides_path=RESEARCH/"corpus.overrides.json"
    overrides=json.loads(overrides_path.read_text()) if overrides_path.exists() else {}
    for row in rows:
        row.update(overrides.get(row["source_relative_path"],{}))
    by_hash={}
    for row in rows: by_hash.setdefault(row["sha256"],[]).append(row["source_relative_path"])
    for row in rows:
        row["duplicate_paths"] = by_hash[row["sha256"]]
        row["is_canonical_copy"] = row["source_relative_path"] == by_hash[row["sha256"]][0]
    queue=[r for r in rows if r["is_canonical_copy"] and r["kind"] in ("competition_paper","unclassified_article")]
    data=dict(generated_at=datetime.now(timezone.utc).isoformat(), scope="All PDFs in the original MCM-ICM-master collection",
              review_warning="Machine inventory/extraction only. actual_review_status is not_reviewed until a reader records complete coverage and an evidence-backed review.",
              file_count=len(rows),unique_sha256_count=len(by_hash),counts_by_kind=dict(Counter(r["kind"] for r in rows)),
              file_records=rows)
    (RESEARCH/"corpus.json").write_text(json.dumps(data,ensure_ascii=False,indent=2))
    fields=["source_id","source_relative_path","kind","classification_basis","classification_review_required","family","year","problem","team","award_label","award_basis","physical_pages","sha256","extraction_status","low_extraction_pages","encoding_suspect_pages","extracted_text_path","extracted_pages_path","actual_review_status","numeric_reproduction_status","is_canonical_copy","duplicate_paths","extraction_error"]
    with (RESEARCH/"corpus.csv").open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader()
        for row in rows:w.writerow({**row,"low_extraction_pages":json.dumps(row["low_extraction_pages"]),"duplicate_paths":json.dumps(row["duplicate_paths"],ensure_ascii=False)})
    (RESEARCH/"reading_queue.json").write_text(json.dumps(queue,ensure_ascii=False,indent=2))
    lines=["# Original MCM/ICM reading queue","","This is a machine inventory, not a record of completed reading. Each unique paper requires a real full review; unclassified articles remain in the queue until resolved.","",f"{len(rows)} file occurrences; {len(by_hash)} unique hashes; {len(queue)} queued paper/article records.","","| ID | Year | Family/problem | Team | Pages | Low-extraction pages | Source |","| --- | --- | --- | --- | --- | --- | --- |"]
    for r in queue:
        lines.append(f"| {r['source_id']} | {r['year']} | {r['family'] or '?'} {r['problem'] or '?'} | {r['team'] or '?'} | {r['physical_pages']} | {','.join(map(str,r['low_extraction_pages'])) or '—'} | {r['source_relative_path']} |")
    (RESEARCH/"reading_queue.md").write_text("\n".join(lines)+"\n")
    print(json.dumps({"files":len(rows),"unique_hashes":len(by_hash),"kind_counts":data["counts_by_kind"],"queued":len(queue),"failed":sum(r["extraction_status"]=="extraction_failed" for r in rows)},ensure_ascii=False),flush=True)

if __name__ == "__main__": main()
