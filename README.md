# JEV Legal Instrumentation LATAM

Primer piloto público y reproducible, en español, sobre decisiones tipadas aplicadas a metadatos jurídicos argentinos.

## Resultado principal

Sobre 30 registros públicos de la Corte Suprema de Justicia de la Nación:

| Sistema | Área jurídica | Vehículo procesal | Argmax estable ante 6 órdenes |
|---|---:|---:|---:|
| Reglas determinísticas | 96,7% | 100% | No aplica |
| Kev 0.5B local | 20,0% | 80,0% | 93,3% |
| Jev | 60,0% | 96,7% | 93,3% |

La confianza no equivale a corrección. En área jurídica, Jev acertó 12 de 16 casos con confianza igual o superior a 0,90 y cometió errores con confianza 0,99 y 1,00.

## Qué demuestra y qué no

El piloto demuestra que el experimento puede reproducirse con corpus, preguntas, opciones, resultados y código visibles. También muestra que una tarea literal puede funcionar bien mientras una clasificación jurídica falla.

No demuestra comprensión jurídica, holding, vigencia, autoridad, calidad profesional ni aptitud para automatizar decisiones. La muestra moderna contiene metadatos, no el texto completo de los fallos.

## Reproducción

Requisitos: Python 3.12+. El baseline determinístico no necesita dependencias externas.

```bash
python3 pilot/build_corpus.py
python3 pilot/run_baseline.py
```

Para Kev se requiere un servidor local compatible en `127.0.0.1:8009`. Para Jev se requiere el SDK oficial, una clave propia y aprobación de gasto:

```bash
python3 pilot/run_kev.py
python3 pilot/run_jev.py --max-usd 0.50
python3 pilot/run_jev_permutations.py --max-usd 0.50
```

Los runners se detienen si falta la clave y rechazan un tope superior a USD 0,50. Nunca incluya credenciales en el repositorio.

## Estructura

- `corpus/manifest.jsonl`: 30 registros modernos y etiquetas oficiales.
- `corpus/historical-fixtures.jsonl`: pasajes OCR históricos para pruebas de mecanismo, no derecho vigente.
- `pilot/`: construcción del corpus y runners.
- `results/`: salidas crudas y métricas del piloto del 19 de septiembre de 2026.
- `publication/`: paper, nota técnica y piezas editoriales.

## Frontera jurídica y de privacidad

- Sólo fuentes públicas o fixtures sintéticos.
- No enviar expedientes reales, comunicaciones privilegiadas, datos de clientes o información financiera a servicios externos.
- Un modelo no decide holding, vigencia, fuerza vinculante ni resultado.
- Toda incertidumbre material debe cambiar el flujo a `ESCALATE` o `BLOCK`.

## Autor

Ignacio Adrián Lerer  
Attorney (UBA), Executive MBA (IAE, Universidad Austral)  
Buenos Aires, Argentina  
ORCID 0009-0007-6378-9749  
https://estudio.justitia.com.ar

## Licencia

Código: MIT. Textos: CC BY 4.0. Los documentos fuente conservan sus propios términos y procedencia.

