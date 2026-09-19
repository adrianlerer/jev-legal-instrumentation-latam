#!/usr/bin/env python3
"""Measure Jev area-label sensitivity under six deterministic option orders."""
from __future__ import annotations
import argparse, json, os, random, sys
from pathlib import Path
from typesafe_sdk import Choice, TypeSafeClient

p=argparse.ArgumentParser(); p.add_argument("--max-usd",type=float,required=True); a=p.parse_args()
if a.max_usd>0.50: sys.exit("budget cap exceeds approved USD 0.50")
if not os.getenv("TYPESAFE_API_KEY"): sys.exit("BLOCKED: TYPESAFE_API_KEY absent")
ROOT=Path(__file__).resolve().parents[1]
items=[json.loads(x) for x in (ROOT/"corpus/manifest.jsonl").read_text().splitlines()]
areas={"Laboral":"employment or labor law","Civil - Comercial":"civil or commercial law","Previsional":"social security or pension law","Competencia":"jurisdiction or court competence","Salud":"health coverage or health rights"}
rows=[]; total_in=total_out=0
with TypeSafeClient() as client:
  for n,x in enumerate(items,1):
    runs=[]; keys=list(areas)
    for j in range(6):
      order=list(keys); random.Random(20260919+j).shuffle(order)
      r=client.system_one(state={"docket":x["docket"],"case_title":x["title"]},questions={"area":Choice(instructions="Classify the principal legal area expressed by this Argentine Supreme Court docket metadata.",criteria={k:areas[k] for k in order})})
      ans=r.choices["area"]; total_in+=r.usage.input_tokens or 0; total_out+=r.usage.output_tokens or 0
      runs.append({"order":order,"choice":ans.choice,"confidence":ans.confidence,"probabilities":ans.probabilities})
    stable=len({r["choice"] for r in runs})==1
    rows.append({"pilot_id":x["pilot_id"],"gold_area":x["gold_area"],"argmax_stable":stable,"choices":[r["choice"] for r in runs],"runs":runs})
    print(f"{n:02d}/30 {x['pilot_id']} stable={stable}",flush=True)
out=ROOT/"results"; (out/"jev-permutations.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
metrics={"n":len(rows),"orders_per_record":6,"argmax_stable_rate":sum(r["argmax_stable"] for r in rows)/len(rows),"input_tokens":total_in,"output_tokens":total_out,"approved_max_usd":a.max_usd}
(out/"jev-permutation-metrics.json").write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(metrics,ensure_ascii=False))
