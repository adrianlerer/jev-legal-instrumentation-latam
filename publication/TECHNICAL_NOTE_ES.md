# Nota técnica: piloto CSJN con Jev y Kev

## Propósito

Documentar un experimento reproducible sobre dos clasificaciones acotadas aplicadas a treinta metadatos públicos de la CSJN. No es un benchmark jurídico general.

## Datos

- 30 registros modernos, metadata-only.
- 30 pasajes históricos OCR para pruebas de mecanismo.
- PDF moderno no descargado: el servidor respondió HTTP 403 y no se eludió.
- Hash del manifiesto: `d12cf13ca2ea39e3c1a989d0195db22dd6e61906b3ecb357426e1d58d677ecb1`.

## Preguntas congeladas

1. Área: Laboral, Civil-Comercial, Previsional, Competencia o Salud.
2. Vehículo: queja, recurso directo, salto de instancia u otro.

## Resultados

| Sistema | Área | Vehículo | Orden |
|---|---:|---:|---:|
| Reglas | 96,7% | 100% | n/a |
| Kev | 20% | 80% | 93,3% estable |
| Jev | 60% | 96,7% | 93,3% estable |

Con confianza Jev ≥0,90, área fue correcta en 12/16 casos. Se observaron errores con 0,99 y 1,00. Vehículo fue correcto en 28/28 casos retenidos.

## Costo y privacidad

Tokens de entrada registrados: 16.787 en el lote principal y 82.722 en permutaciones, más una consulta inicial no registrada. Costo estimado: ~USD 0,0042. Sólo se enviaron metadatos públicos. La clave quedó fuera del repositorio.

## Reproducción

```bash
python3 pilot/build_corpus.py
python3 pilot/run_baseline.py
python3 pilot/run_kev.py
python3 pilot/run_jev.py --max-usd 0.50
python3 pilot/run_jev_permutations.py --max-usd 0.50
```

## Estado

`PASS` como experimento técnico reproducible. `ESCALATE` para cualquier conclusión jurídica. `BLOCK` para expedientes reales, información privilegiada o decisiones automatizadas.

