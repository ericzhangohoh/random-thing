#!/usr/bin/env python3
"""Report recorded reading coverage without inferring it from extraction."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

DOC = Path(__file__).resolve().parents[1]
PROJECT = DOC.parent


def read_review(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    header = text[:5000]
    source = re.search(r"^- Source:\s*`([^`]+)`", header, re.M)
    sid = re.search(r"^- Source ID:\s*`([^`]+)`", header, re.M)
    if "FULL_TEXT_AND_RELEVANT_VISUALS_REVIEWED" in header:
        status = "full_review_recorded"
    elif re.search(r"Review status:\s*\*\*full\*\*", header, re.I):
        status = "full_review_recorded"
    elif re.search(r"(?:Review status|Coverage):[^\n]*partial", header, re.I):
        status = "partial_review_recorded"
    else:
        status = "review_depth_not_machine_classified"
    return {
        "source_id": sid.group(1) if sid else None,
        "source_relative_path": source.group(1) if source else None,
        "review_path": str(path.relative_to(DOC)),
        "review_status": status,
        "review_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "claim_basis": "Reader-authored explicit coverage statement; not proof of reading or mathematical correctness",
    }


def main() -> None:
    original = json.loads((DOC / "research/corpus.json").read_text())
    scope = json.loads((DOC / "research/scope_exclusions.json").read_text())
    papers = [r for r in original["file_records"] if r["kind"] == "competition_paper"]
    reviews = [read_review(p) for p in sorted((DOC / "research/reviews").rglob("*.md"))]
    by_id = {r["source_id"]: r for r in reviews if r["source_id"]}
    by_source = {r["source_relative_path"]: r for r in reviews if r["source_relative_path"]}
    rows = []
    for p in papers:
        review = by_id.get(p["source_id"]) or by_source.get(p["source_relative_path"])
        rows.append({
            "corpus": "original_mcm_icm_collection",
            "source_id": p["source_id"], "source_relative_path": p["source_relative_path"],
            "year": p.get("year"), "problem": p.get("problem"), "team": p.get("team"),
            "physical_pages": p["physical_pages"],
            "review_status": review["review_status"] if review else "not_reviewed",
            "review_path": review["review_path"] if review else None,
        })
    archive = PROJECT / "HIMCM_备赛资料/03_论文与评审"
    hp = sorted((archive / "HiMCM公开论文").rglob("*.pdf")) + sorted((archive / "作者公开论文").rglob("*.pdf"))
    for p in hp:
        rel = str(p.relative_to(PROJECT))
        review = by_source.get(rel)
        rows.append({"corpus": "himcm_standalone_papers", "source_id": None,
                     "source_relative_path": rel, "year": None, "problem": None, "team": p.stem,
                     "physical_pages": None, "review_status": review["review_status"] if review else "not_reviewed",
                     "review_path": review["review_path"] if review else None})
    for row in rows:
        matches = [rule for rule in scope["known_group_exclusions"]
                   if rule["corpus"] == row["corpus"]
                   and str(row.get("year")) == rule["year"]
                   and str(row.get("problem")) == rule["problem"]]
        for rule in scope.get("known_path_exclusions", []):
            if any(token in row["source_relative_path"] for token in rule["path_contains_any"]):
                matches.append(rule)
        row["research_scope"] = "EXCLUDED_BIOLOGICAL" if matches else "TOPIC_SCREEN_REQUIRED_BEFORE_NEW_READING"
        row["scope_reason"] = "; ".join(rule["reason"] for rule in matches) or "No exclusion matched; not a certified non-biological classification"
    summary = {}
    for group in sorted({r["corpus"] for r in rows}):
        sub = [r for r in rows if r["corpus"] == group]
        summary[group] = {"total": len(sub), **dict(Counter(r["review_status"] for r in sub))}
    stamp = datetime.now(ZoneInfo("Australia/Sydney")).isoformat(timespec="seconds")
    out = {"updated_at": stamp, "status": "SCOPED_WORKFLOW_RESEARCH", "summary": summary,
           "scope_policy": scope,
           "known_excluded_papers": sum(r["research_scope"] == "EXCLUDED_BIOLOGICAL" for r in rows),
           "warning": "Full review labels report reader declarations, not numerical reproduction. Extraction never promotes status.",
           "rows": rows, "review_records": reviews}
    (DOC / "research/review_progress.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    with (DOC / "research/review_progress.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)
    lines = ["# Research Status", "", f"Updated: {stamp}.", "",
             "**Current scope excludes all biology-related papers. The earlier all-paper plan is superseded; see [research scope](SCOPE.md).**", "",
             "This table reports historical archive coverage, not an eligible non-biological denominator or a requirement to finish every archived paper before delivering the workflow.", "",
             f"Known exclusions currently match {out['known_excluded_papers']} papers. This is not exhaustive topic screening; future reading requires a metadata scope check. Existing review records are preserved.", "",
             "## Archived coverage", "", "| Collection | Papers | Full review recorded | Partial review recorded | Other review depth | Not reviewed |",
             "|---|---:|---:|---:|---:|---:|"]
    for group, counts in summary.items():
        lines.append(f"| {group} | {counts['total']} | {counts.get('full_review_recorded',0)} | {counts.get('partial_review_recorded',0)} | {counts.get('review_depth_not_machine_classified',0)} | {counts.get('not_reviewed',0)} |")
    lines += ["", f"The original collection contains {original['file_count']} PDFs, including {len(papers)} competition papers. Award levels, problem labels and one CUMCM item must retain their recorded distinctions; the folder name does not certify every item as MCM/ICM Outstanding.", "",
              "## Meaning of status", "",
              "- **Extracted:** a machine produced page-bounded text. This does not count as reading.",
              "- **Partial review:** a reader examined identified sections; the record states gaps.",
              "- **Full review recorded:** the reader explicitly reports complete available text and relevant visual inspection. This is a review declaration, not a numerical reproduction certificate.",
              "- **Numerical reproduction:** a separate activity, only claimed when actually executed and recorded.", "",
              "The corpus inventory preserves initial extraction status. This progress report joins it with substantive review files; it does not rewrite extraction into scholarship.", "",
              "## Inspectable records", "",
              "- [Original corpus inventory](corpus.csv)",
              "- [Reading queue](reading_queue.md)",
              "- [Per-paper progress](review_progress.csv)",
              "- [Machine-readable progress](review_progress.json)",
              "- [Evidence-to-workflow register](EVIDENCE_REGISTER.md)",
              "- [Review method](REVIEW_METHOD.md)", "", "## Review files", ""]
    for r in rows:
        if r["review_path"]:
            path = Path(r["review_path"]).relative_to("research")
            lines.append(f"- [{Path(r['source_relative_path']).name}]({path.as_posix()}) — {r['review_status']}")
    (DOC / "research/STATUS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": out["status"], "summary": summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
