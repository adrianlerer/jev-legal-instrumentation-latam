#!/usr/bin/env python3
"""Deterministic baseline and common result format for the pilot."""
from __future__ import annotations
import json, re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
items = [json.loads(x) for x in (ROOT / "corpus/manifest.jsonl").read_text().splitlines()]

def predict(x):
    title, docket = x["title"].lower(), x["docket"].upper()
    if "obra social" in title: area = "Salud"
    elif "anses" in title or "haber inicial" in title: area = "Previsional"
    elif docket.startswith("CCF") or docket.endswith("/CS001") and ("estado provincial" in title or "inconstitucionalidades" in title): area = "Competencia"
    elif docket.startswith("CIV") or "daños y perjuicios" in title or "cobro ejecutivo" in title: area = "Civil - Comercial"
    else: area = "Laboral"
    if "salto instancia" in title: procedure="salto_instancia"
    elif "recurso queja" in title or "queja por" in title: procedure="queja"
    elif "recurso directo" in title or "recurso contra decision" in title: procedure="recurso_directo"
    else: procedure="otro"
    return {"area": area, "procedure": procedure}

rows=[]
for x in items:
    p=predict(x)
    rows.append({"pilot_id":x["pilot_id"],"system":"rules","prediction":p,"gold":{"area":x["gold_area"],"procedure":x["gold_procedure"]},"correct":{"area":p["area"]==x["gold_area"],"procedure":p["procedure"]==x["gold_procedure"]}})
out=ROOT/"results"; out.mkdir(exist_ok=True)
(out/"rules.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
metrics={k:sum(r["correct"][k] for r in rows)/len(rows) for k in ("area","procedure")}
(out/"rules-metrics.json").write_text(json.dumps({"n":len(rows),"accuracy":metrics,"area_distribution":Counter(x["gold_area"] for x in items)},ensure_ascii=False,indent=2,default=dict)+"\n")
print(json.dumps(metrics))
