#!/usr/bin/env python3
"""Build the fixed 30-record CSJN metadata pilot corpus."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "corpus" / "manifest.jsonl"

ROWS = [
 ("8235661","10/09/2026","CNT 065804/2017/1/RH001","Recurso Queja Nº 1 - MARTINEZ, LEANDRO FEDERICO c/ GEFCO ARGENTINA S.A. Y OTROS s/DESPIDO","Laboral","Remisión"),
 ("8247321","10/09/2026","CNT 011822/2017/1/RH001","Recurso Queja Nº 1 - MARINO, CLAUDIO ALEJANDRO c/ ART INTERACCION S.A. s/ACCIDENTE - LEY ESPECIAL","Laboral","Remisión"),
 ("8225201","10/09/2026","CNT 078417/2016/1/RH001","Recurso Queja Nº 1 - LOPEZ VITELLI, IGNACIO c/ GALENO ART S.A. Y OTRO s/ACCIDENTE - ACCION CIVIL","Laboral","Remisión"),
 ("8225221","10/09/2026","CNT 080818/2016/1/RH001","Recurso Queja Nº 1 - LOPEZ PALMA, MARIA ALEJANDRA c/ UNIVERSIDAD DE BUENOS AIRES s/DESPIDO","Laboral","Remisión"),
 ("8321401","10/09/2026","CSJ 001297/2022/RH001","SOCIEDAD ARGENTINA DE AUTORES Y COMP. DE MUSICA (S.A.D.A.I.C.) c/ PONDAL, LUIS MANUEL Y OTRO s/cobro ejecutivo","Civil - Comercial","Remisión"),
 ("8321761","10/09/2026","CIV 057557/2021/2/RH001","Recurso Queja Nº 2 - VIVONA CASASSA, AUGUSTO c/ TORREZ, HUGO ROBERTO s/DAÑOS Y PERJUICIOS(ACC.TRAN. C/LES. O MUERTE)","Civil - Comercial","Inadmisible"),
 ("8247461","10/09/2026","CNT 048165/2017/1/RH001","Recurso Queja Nº 1 - LOPEZ BRUNA, HUGO SANTIAGO Y OTRO c/ ESTADO NACIONAL MINISTERIO DE ENERGIA Y MINERIA s/DIFERENCIAS DE SALARIOS","Laboral","Remisión"),
 ("8321231","10/09/2026","FTU 001359/1988/2/RH001","Recurso Queja Nº 2 - VILLAR RAMON JOSE c/ CAJA NACIONAL DE AHORRO Y SEGURO s/CUMPLIMIENTO DE CONTRATOS","Civil - Comercial","Inadmisible"),
 ("8321771","10/09/2026","CIV 088350/2018/2/RH001","Recurso Queja Nº 2 - LABATE, ADRIÁN ALEJANDRO c/ BARREIRA, LEONEL s/DAÑOS Y PERJUICIOS","Civil - Comercial","Inadmisible"),
 ("8172541","10/09/2026","CNT 009740/2020/1/RH001","Recurso Queja Nº 1 - LEVIN, FERNANDO MATIAS c/ SERVICIO NACIONAL DE SANIDAD Y CALIDAD AGROALIMENTARIA (SENASA) s/JUICIO SUMARISIMO","Laboral","Remisión"),
 ("8313961","03/09/2026","FMP 011502/2024/1/RH001","Recurso Queja Nº 1 - MARTIN, ALICIA BEATRIZ c/ ANSES s/AMPARO por MORA de la ADMINISTRACION","Previsional","Inadmisible"),
 ("8233431","03/09/2026","CSJ 002748/2024/RH001","ZORRILLA, OSVALDO ADRIAN c/ LA SEGUNDA ART S.A. s/RECURSO CONTRA DECISION COMISION MEDICA","Laboral","Inadmisible"),
 ("8316021","03/09/2026","CSJ 001422/2021/RH001","SOSA, EMILIO JAVIER c/ ASOCIART ART S.A. s/ACCIDENTE S/RECURSO EXTRAORDINARIO FEDERAL","Laboral","Inadmisible"),
 ("8251501","03/09/2026","CSJ 000370/2024/RH001","SEREN, SERGIO ENRIQUE c/ DERUDDER HERMANOS S.R.L. s/recurso directo de queja por denegación","Laboral","Inadmisible"),
 ("8312561","03/09/2026","CSJ 000976/2023/RH001","ROLDAN, RUBEN DARIO c/ PREVENCION ART S.A. s/Ordinario - Accidente - Ley de Riesgos","Laboral","Inadmisible"),
 ("8140301","03/09/2026","CNT 024875/2021/6/RH005","Recurso Queja Nº 6 - BOGETTI, EDUARDO FABIAN Y OTRO c/ RAPI ESTANT S.A. (REB) Y OTROS s/DESPIDO","Laboral","Inadmisible"),
 ("8315911","03/09/2026","CCF 005146/2024/CS001","CENCOSUD SA c/ ESTADO NACIONAL MINISTERIO DE ECONOMIA SECRETARIA DE INDUSTRIA Y DESARROLLO PRODUCTIVO s/RECURSO DIRECTO LEY 24.240 - ART 45","Competencia","Remisión"),
 ("8311811","03/09/2026","FGR 000530/2019/CS001","ROSAS HEIN, JUAN VENTURA c/ ADMINISTRACION NACIONAL DE SEGURIDAD SOCIAL (ANSES) s/RECTIFICACION HABER INICIAL","Previsional","Inadmisible"),
 ("8251481","03/09/2026","CNT 040258/2021/2/RH001","Recurso Queja Nº 2 - CABAÑAS, NILDA ESTER c/ PUNTO CRUZ S.A. s/DESPIDO","Laboral","Inadmisible"),
 ("8316371","03/09/2026","CCF 007902/2024/CS001","SANCOR COOPERATIVAS UNIDAS LIMITADA c/ ESTADO NACIONAL MINISTERIO DE ECONOMIA SECRETARIA DE INDUSTRIA Y DESARROLLO PRODUCTIVO s/LEALTAD COMERCIAL - LEY 22802 - ART 22","Competencia","Remisión"),
 ("8312241","27/08/2026","FMZ 029019/2025/CS001","ALTAVILLA OTEO, HORACIO FERNANDO c/ ESTADO PROVINCIAL DE LA PAMPA s/DAÑOS Y PERJUICIOS","Competencia","No informado"),
 ("8312511","27/08/2026","CSS 125228/2018/CS001","DI CIANO MARCELO c/ UNIVERSIDAD DE BUENOS AIRES Y OTRO s/INCONSTITUCIONALIDADES VARIAS","Competencia","No informado"),
 ("8212181","27/08/2026","CSJ 000580/2025/RH001","VEGA, ADRIANA VERONICA c/ LA SEGUNDA A.R.T. S.A s/QUEJA POR REF DENEGADO","Laboral","Inadmisible"),
 ("8313431","27/08/2026","CAF 038066/2017/CS001","SARACENO, MARIANA INES c/ EN-M JUSTICIA DDHH s/PROCESO DE EJECUCION","Laboral","Inadmisible"),
 ("8312931","27/08/2026","FSM 012685/2023/4/1/RH002","S., P. N. EN REP, DE SU HIJA MENOR M.CH.B c/ OBRA SOCIAL DEL PERSONAL DEL AUTOMOVIL CLUB ARGENTINO (OSPACA) Y OTROS s/INC DE MEDIDA CAUTELAR","Salud","Inadmisible"),
 ("8200041","27/08/2026","CNT 046726/2022/1/RS001","Recurso Salto Instancia Nº 1 - BARRIOS, RUBEN DAVID c/ ARGENOVA SOCIEDAD ANONIMA s/DESPIDO","Laboral","Inadmisible"),
 ("8310381","27/08/2026","CNT 021649/2016/5/RH005","Recurso Queja Nº 5 - OCARANZA, SERGIO JAVIER Y OTRO c/ ASOCIART ART S.A. Y OTRO s/ACCIDENTE - LEY ESPECIAL","Laboral","Inadmisible"),
 ("8313081","27/08/2026","FTU 015528/2019/4/RH003","Recurso Queja Nº 4 - T., L. F. Y OTRO c/ OBRA SOCIAL DEL PERSONAL DE PRENSA DE TUCUMAN Y OTROS s/AMPARO LEY 16.986","Salud","No informado"),
 ("8311311","27/08/2026","CNT 022472/2021/3/RH003","Recurso Queja Nº 3 - MELADO, ARIEL c/ ASOCIART ART S.A. s/ACCIDENTE - LEY ESPECIAL","Laboral","Inadmisible"),
 ("8313271","27/08/2026","FLP 115343/2018/4/RH002","Recurso Queja Nº 4 - GIMENEZ, CLARISA ELIZABETH P/D.PRO. Y EN REP.DE HIJOS MEN. c/ MUNICIPALIDAD DE CHACABUCO Y OTROS s/AMPARO LEY 16.986","Laboral","Inadmisible"),
]

def procedure(title: str) -> str:
    t = title.lower()
    if "salto instancia" in t: return "salto_instancia"
    if "recurso queja" in t or "queja por" in t or "queja por denegación" in t: return "queja"
    if "recurso directo" in t or "recurso contra decision" in t: return "recurso_directo"
    return "otro"

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as fh:
    for i, (doc_id, date, docket, title, area, outcome) in enumerate(ROWS, 1):
        item = {
            "pilot_id": f"CSJN-{i:03d}", "document_id": doc_id, "date": date,
            "docket": docket, "title": title, "gold_area": area,
            "gold_outcome": outcome, "gold_procedure": procedure(title),
            "source": "CSJN consulta de fallos (interfaz pública)",
            "source_url": f"https://sjconsulta.csjn.gov.ar/sjconsulta/documentos/verDocumentoByIdLinksJSP.html?idDocumento={doc_id}",
            "acquisition": "metadata_only", "full_text_available_locally": False,
        }
        fh.write(json.dumps(item, ensure_ascii=False) + "\n")
print(f"wrote {len(ROWS)} records to {OUT}")
