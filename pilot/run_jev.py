#!/usr/bin/env python3
"""Run the frozen public CSJN metadata set through Jev with a hard spend cap."""
from __future__ import annotations
import argparse, json, os, sys, time
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument("--max-usd",type=float,required=True)
args=p.parse_args()
if args.max_usd > 0.50:
    sys.exit("budget cap exceeds the approved USD 0.50")
if not os.getenv("TYPESAFE_API_KEY"):
    sys.exit("BLOCKED: TYPESAFE_API_KEY is absent; no key was created and no credits were purchased")

try:
    from typesafe_sdk import Choice, TypeSafeClient
except ImportError:
    sys.exit("BLOCKED: install the pinned typesafe-sdk environment before execution")

ROOT=Path(__file__).resolve().parents[1]
items=[json.loads(x) for x in (ROOT/"corpus/manifest.jsonl").read_text().splitlines()]
areas={"Laboral":"employment or labor law","Civil - Comercial":"civil or commercial law","Previsional":"social security or pension law","Competencia":"jurisdiction or court competence","Salud":"health coverage or health rights"}
procedures={"queja":"complaint/queja appeal","recurso_directo":"direct judicial review","salto_instancia":"per saltum appeal","otro":"another procedural vehicle"}
rows=[]
with TypeSafeClient() as client:
    for i,x in enumerate(items,1):
        started=time.time()
        response=client.system_one(
            state={"docket":x["docket"],"case_title":x["title"]},
            questions={
                "area":Choice(instructions="Classify the principal legal area expressed by this Argentine Supreme Court docket metadata.",criteria=areas),
                "procedure":Choice(instructions="Classify the procedural vehicle expressly named in the case title.",criteria=procedures),
            },
        )
        a=response.choices["area"]; q=response.choices["procedure"]
        pred={"area":a.choice,"procedure":q.choice}
        def answer_dict(value):
            return {"choice":value.choice,"confidence":value.confidence,"probabilities":value.probabilities}
        rows.append({"pilot_id":x["pilot_id"],"system":"jev","prediction":pred,"gold":{"area":x["gold_area"],"procedure":x["gold_procedure"]},"correct":{"area":pred["area"]==x["gold_area"],"procedure":pred["procedure"]==x["gold_procedure"]},"answers":{"area":answer_dict(a),"procedure":answer_dict(q)},"usage":{"input_tokens":response.usage.input_tokens,"output_tokens":response.usage.output_tokens},"wall_ms":round((time.time()-started)*1000,1)})
        print(f"{i:02d}/30 {x['pilot_id']} {pred['area']} {pred['procedure']}",flush=True)
out=ROOT/"results"; out.mkdir(exist_ok=True)
(out/"jev.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False,default=str)+"\n" for r in rows))
metrics={"n":len(rows),"accuracy":{k:sum(r["correct"][k] for r in rows)/len(rows) for k in ("area","procedure")},"approved_max_usd":args.max_usd}
(out/"jev-metrics.json").write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(metrics,ensure_ascii=False))
