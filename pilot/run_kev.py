#!/usr/bin/env python3
"""Run the frozen CSJN metadata set against a local Kev server."""
from __future__ import annotations
import json, time, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
URL="http://127.0.0.1:8009/v1/systemone"
PERMUTE="http://127.0.0.1:8009/v1/systemone/permute"
items=[json.loads(x) for x in (ROOT/"corpus/manifest.jsonl").read_text().splitlines()]
areas={"Laboral":"employment or labor law","Civil - Comercial":"civil or commercial law","Previsional":"social security or pension law","Competencia":"jurisdiction or court competence","Salud":"health coverage or health rights"}
procedures={"queja":"complaint/queja appeal","recurso_directo":"direct judicial review","salto_instancia":"per saltum appeal","otro":"another procedural vehicle"}

def post(url, payload):
    req=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={"content-type":"application/json"})
    with urllib.request.urlopen(req,timeout=120) as r: return json.load(r)

rows=[]
for i,x in enumerate(items,1):
    payload={"state":{"docket":x["docket"],"case_title":x["title"]},"model":"kev-latest","questions":{
      "area":{"type":"choice","instructions":"Classify the principal legal area expressed by this Argentine Supreme Court docket metadata.","criteria":areas},
      "procedure":{"type":"choice","instructions":"Classify the procedural vehicle expressly named in the case title.","criteria":procedures}}}
    started=time.time(); ans=post(URL,payload)
    perm=post(PERMUTE,{"request":payload,"question":"area","n_perm":6,"seed":20260919})
    pred={k:ans["answers"][k]["choice"] for k in ("area","procedure")}
    rows.append({"pilot_id":x["pilot_id"],"system":"kev-0.5b","prediction":pred,"gold":{"area":x["gold_area"],"procedure":x["gold_procedure"]},"correct":{"area":pred["area"]==x["gold_area"],"procedure":pred["procedure"]==x["gold_procedure"]},"answers":ans["answers"],"latency_ms":ans.get("latency_ms"),"wall_ms":round((time.time()-started)*1000,1),"area_permutation":{"argmax_stable":perm["argmax_stable"],"spread":perm["spread"]}})
    print(f"{i:02d}/30 {x['pilot_id']} {pred['area']} {pred['procedure']}",flush=True)

out=ROOT/"results"; out.mkdir(exist_ok=True)
(out/"kev.jsonl").write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
metrics={"n":len(rows),"accuracy":{k:sum(r["correct"][k] for r in rows)/len(rows) for k in ("area","procedure")},"area_argmax_stable_rate":sum(r["area_permutation"]["argmax_stable"] for r in rows)/len(rows),"median_latency_ms":sorted(r["latency_ms"] for r in rows)[len(rows)//2]}
(out/"kev-metrics.json").write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(metrics,ensure_ascii=False))
