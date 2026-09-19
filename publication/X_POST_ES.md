# Hilo para X

## 1/5

Publico el primer piloto abierto y reproducible, en español, que aplica Jev a metadatos jurídicos argentinos.

No para construir otro oráculo, sino para medir qué mejora cuando la IA entrega respuestas tipadas, probabilidades y trazabilidad. 🧵

## 2/5

30 registros públicos de la Corte Suprema argentina. Dos tareas estrechas: área jurídica y vehículo procesal.

Reglas: 96,7% / 100%
Jev: 60% / 96,7%
Kev: 20% / 80%

Un baseline simple venció a los modelos en esta muestra.

## 3/5

El hallazgo más importante: Jev cometió errores de área con confianza 0,99 y 1,00.

Tipar una salida no la vuelve verdadera. La confianza declarada tampoco es calibración. Pero ambas pueden hacer visible el punto exacto donde el procedimiento debe abstenerse o escalar.

## 4/5

La arquitectura que propongo separa:

fuentes → proposiciones → estimaciones probabilísticas → reglas determinísticas → PASS / ESCALATE / BLOCK → revisión profesional → acción autorizada.

La autoridad jurídica sigue en la institución y el profesional.

## 5/5

Código, corpus permitido, resultados, paper y nota técnica quedan abiertos para replicación y crítica:

https://github.com/adrianlerer/jev-legal-instrumentation-latam

#LegalAI #Jev #IAJurídica #Argentina #LatAm
