# De la IA oráculo a la IA instrumentada

## Proposiciones auditables, incertidumbre y decisión institucional: un piloto reproducible con Jev, Kev y metadatos de la Corte Suprema argentina

**Ignacio Adrián Lerer**  
Attorney (UBA), Executive MBA (IAE, Universidad Austral).  
Buenos Aires, Argentina.  
adrian@lerer.com.ar  
ORCID 0009-0007-6378-9749  

19 de septiembre de 2026

## Resumen

Este trabajo propone sustituir la imagen de la inteligencia artificial como oráculo que emite conclusiones por una arquitectura instrumentada que produce proposiciones limitadas, trazables y revisables dentro de un procedimiento institucional. Tipar una respuesta no vuelve determinístico al modelo ni convierte su confianza en verdad. Permite, en cambio, separar estimaciones semánticas probabilísticas, reglas ejecutadas en código, umbrales de abstención, revisión profesional y autoridad decisoria. Para someter esta tesis a una primera prueba, se construyó un piloto reproducible con treinta registros públicos de la Corte Suprema de Justicia de la Nación. Se compararon reglas determinísticas, Kev 0.5B local y Jev sobre dos tareas estrechas: área jurídica y vehículo procesal. Las reglas obtuvieron 96,7% y 100%; Kev, 20% y 80%; Jev, 60% y 96,7%. Ambos modelos mantuvieron el argmax de área en 93,3% de los casos bajo seis permutaciones, pero esa estabilidad no aseguró corrección. Jev cometió errores de área con confianza 0,99 y 1,00. El resultado apoya una conclusión acotada: las interfaces tipadas pueden mejorar instrumentación y auditoría, pero no eliminan la necesidad de baselines determinísticos, calibración por tarea, fuentes completas y revisión jurídica. El piloto no evalúa holding, vigencia ni autoridad de los fallos.

**Palabras clave:** inteligencia artificial jurídica; Jev; decisiones tipadas; calibración; abstención; Corte Suprema; auditoría algorítmica.

## 1. El problema del oráculo

Una respuesta jurídica en prosa puede ocultar varias operaciones bajo una misma superficie lingüística. Extrae hechos, relaciona pasajes, calcula plazos, infiere consecuencias, interpreta normas y recomienda decisiones. El texto puede ser claro y persuasivo sin permitir reconstruir cuál de esas operaciones falló. La fluidez se convierte así en una forma de agregación: un resultado único reemplaza la secuencia de proposiciones, fuentes y decisiones que lo produjo.

La alternativa desarrollada aquí no consiste en pedir una prosa más cauta. Consiste en cambiar la unidad de trabajo. En lugar de solicitar una conclusión institucional completa, el procedimiento formula preguntas limitadas sobre evidencia identificable. El modelo estima relaciones semánticas. El código resuelve fechas, aritmética, opciones permitidas y transiciones de estado. Un profesional conserva la autoridad para valorar prueba, interpretar estándares controvertidos y decidir.

La arquitectura propuesta es:

```text
fuentes y evidencia
  -> proposiciones ancladas
  -> estimaciones semánticas probabilísticas
  -> reglas y derivaciones determinísticas
  -> PASS / ESCALATE / BLOCK
  -> revisión profesional
  -> verificación del estado vigente
  -> acción autorizada
```

Los estados no son advertencias retóricas. `PASS` habilita el siguiente paso previsto; `ESCALATE` exige evidencia o revisión; `BLOCK` impide actuar. Una conclusión seguida por una cláusula genérica de cautela no gobierna incertidumbre si el sistema continúa igual.

## 2. Tipar no es determinar

Jev, de TypeSafe AI, recibe un estado y preguntas acotadas de elección, puntaje o sí/no. Devuelve valores estructurados y probabilidades. Esto permite que un programa valide el esquema y aplique reglas explícitas. No permite afirmar que el modelo sea determinístico. La salida sigue siendo una estimación probabilística y puede ser incorrecta.

La distinción es importante porque “type-safe” describe el espacio formal de salida, no su relación con el mundo. Un modelo puede respetar perfectamente el tipo y elegir la opción equivocada. También puede asignar alta probabilidad a un error. La calibración exige comprobar empíricamente, en una tarea y población definidas, si las probabilidades corresponden a frecuencias de corrección. No se deriva de la arquitectura ni del nombre del campo `confidence`.

Kev permite inspeccionar parte del mecanismo. Es una reconstrucción abierta inspirada en Jev, construida sobre Qwen2.5-0.5B con LoRA y una cabeza de lectura. No es Jev. Su repositorio ofrece código, pesos, suite congelada, hashes y pruebas de aislamiento, permutación, alternativas irrelevantes y falsificación de delimitadores. Es valioso como harness y baseline local, pero su propio model card lo define como prototipo de investigación en inglés y excluye decisiones jurídicas o crediticias de producción.

## 3. La proposición como unidad

La unidad útil deja de ser el párrafo persuasivo y pasa a ser una proposición con alcance limitado. Debe conservar fuente, localizador, versión, condiciones de aplicabilidad y estado de revisión. Esta estructura permite distinguir cinco operaciones que suelen mezclarse:

1. extracción de un dato explícito;
2. relación semántica entre afirmación y pasaje;
3. cálculo determinístico;
4. inferencia causal;
5. conclusión normativa.

No todas admiten el mismo tratamiento. Fechas, distancias y umbrales deben resolverse mediante código cuando sea posible. La causalidad exige un diseño y supuestos explícitos. La conclusión normativa requiere autoridad institucional. La estimación semántica puede ayudar a identificar candidatos, contradicciones o insuficiencias, pero no transforma una probabilidad en estándar de prueba.

La dependencia entre proposiciones tampoco puede ignorarse. Tres respuestas basadas en el mismo pasaje no constituyen tres evidencias independientes. Multiplicar sus probabilidades puede fabricar certeza. Un procedimiento auditable debe registrar fuentes comunes, precedencia, excepciones y derrotadores. Cuando esa dependencia no puede modelarse, corresponde escalar.

## 4. Método

### 4.1 Corpus y frontera de adquisición

Se congelaron treinta registros modernos de la interfaz pública de consulta de fallos de la CSJN, correspondientes a tres fechas de acuerdos de agosto y septiembre de 2026. Cada registro conserva identificador, carátula, fecha, enlace oficial, área y resultado exhibido por la Corte. La descarga automatizada de los PDF oficiales respondió HTTP 403. El control no fue eludido y la muestra moderna quedó limitada a metadatos.

Como fixture de texto se preservaron treinta pasajes de un tomo histórico público. Ese material sirve para probar segmentación y trazabilidad. No se utiliza para determinar derecho vigente.

La distinción entre texto completo, sumario oficial, análisis documental y comentario posterior es sustantiva. El sumario selecciona y condensa. El comentario interpreta. Ninguno sustituye silenciosamente el razonamiento completo del tribunal.

### 4.2 Preguntas

Se midieron dos tareas:

- clasificación del área entre Laboral, Civil-Comercial, Previsional, Competencia y Salud;
- identificación literal del vehículo procesal: queja, recurso directo, salto de instancia u otro.

No se intentó predecir el resultado del recurso desde la carátula. Esa información no está contenida allí y pedirla habría convertido el piloto en adivinación.

### 4.3 Sistemas

El baseline determinístico utilizó patrones explícitos sobre carátula y número de expediente. Kev fue ejecutado localmente. Jev fue ejecutado mediante el SDK oficial con datos públicos, clave local protegida y tope de gasto de USD 0,50. Las opciones y preguntas fueron las mismas. La sensibilidad al orden de las cinco áreas se midió con seis permutaciones determinísticas.

### 4.4 Métricas y reproducibilidad

Se registraron predicción, gold, corrección, probabilidades, confianza, uso y latencia cuando estaban disponibles. El manifiesto moderno quedó congelado con SHA-256 `d12cf13ca2ea39e3c1a989d0195db22dd6e61906b3ecb357426e1d58d677ecb1`. Código, corpus permitido y resultados crudos se publican con este trabajo.

## 5. Resultados

| Sistema | Área | Vehículo procesal | Estabilidad del argmax de área |
|---|---:|---:|---:|
| Reglas determinísticas | 29/30, 96,7% | 30/30, 100% | No aplica |
| Kev 0.5B local | 6/30, 20,0% | 24/30, 80,0% | 28/30, 93,3% |
| Jev | 18/30, 60,0% | 29/30, 96,7% | 28/30, 93,3% |

Kev colapsó principalmente hacia Civil-Comercial. Su resultado procesal fue mejor porque la tarea podía resolverse en gran medida mediante fórmulas literales. Jev mejoró claramente respecto de Kev, pero permaneció muy por debajo del baseline determinístico para el área.

La estabilidad frente al orden tampoco garantizó acierto. Con confianza Jev igual o superior a 0,90, el área tuvo 12 aciertos sobre 16 casos. Hubo errores con confianza 0,99 y 1,00. En vehículo procesal, los 28 casos retenidos por ese umbral fueron correctos. El mismo umbral produjo, por tanto, significados prácticos distintos según la pregunta.

Las treinta consultas principales consumieron 16.787 tokens de entrada y las permutaciones 82.722, más una consulta inicial no registrada por un error local. A la tarifa mostrada de USD 0,042 por millón de tokens, el costo estimado total fue aproximadamente USD 0,0042. Este costo no incluye el trabajo humano de diseño, etiquetado, revisión y auditoría.

## 6. Discusión

El resultado negativo de área no invalida las decisiones tipadas. Delimita su utilidad. Para campos literales y reglas conocidas, el código ordinario puede ser más preciso, barato y transparente. Para relaciones semánticas, un modelo puede agregar valor, pero debe competir contra ese baseline y conservar abstención y revisión.

También aparece una objeción más profunda: la complejidad jurídica que desaparece de la salida reaparece en la descomposición y en el código que combina predicados. Formular las preguntas, definir las opciones y decidir cómo se propagan respuestas incorpora juicio humano. La arquitectura no elimina ese juicio. Lo externaliza y vuelve auditable.

El próximo benchmark debe abandonar los metadatos y evaluar soporte de citas sobre texto completo:

```text
afirmación + pasaje recuperado
  -> SUPPORTED / CONTRADICTED / UNVERIFIED
```

Cada clasificación debe conservar el pasaje y el localizador para revisión humana. `UNVERIFIED` debe cubrir ausencia, insuficiencia o ambigüedad; no equivale a falsedad. El corpus debe incluir evidencia incompleta, contradictoria, adversarial, OCR deteriorado, español jurídico y cambios de dominio.

## 7. Relación con EPT/EGT

La conexión con mis teorías es condicional. Un procedimiento de preguntas, thresholds y estados puede funcionar como ambiente selectivo: vuelve visibles algunas proposiciones, deriva otras y bloquea ciertas variantes. Pero no basta esa analogía para afirmar selección evolutiva. Habría que identificar unidad de variación, portador, mecanismo de retención, población, transmisión y persistencia diferencial, además de rivales como poder, costo, costumbre o simple rendimiento técnico.

La hipótesis nueva es que una arquitectura instrumentada reduce la “pérdida de instrumentación”: la información material que desaparece cuando fuentes, proposiciones, dependencias e incertidumbres se comprimen en una recomendación monolítica. El benchmark futuro deberá medir si esa descomposición mejora la detección y corrección de errores, incluso cuando no aumenta la exactitud bruta.

## 8. Límites

La muestra es pequeña y no aleatoria. Las etiquetas de área provienen de la interfaz oficial, no de una adjudicación independiente. La capa moderna es metadata-only. El tomo histórico no representa derecho vigente. No se midieron holding, fuerza vinculante, calidad argumentativa, vigencia, sesgo demográfico ni desempeño sobre expedientes. El piloto compara sistemas completos, no aísla causalmente arquitectura, entrenamiento o prompt. Sus resultados no autorizan uso profesional ni producción.

## 9. Conclusión

El valor de una IA jurídica no reside en que hable menos ni en que entregue JSON. Reside en que sus proposiciones puedan ser discutidas, sus errores localizados y su incertidumbre capaz de detener el procedimiento. El piloto muestra que una interfaz tipada puede reconocer bien una fórmula procesal y fallar una clasificación jurídica con confianza extrema. Muestra también que reglas simples pueden superar a modelos especializados cuando la tarea ya admite una descripción determinística.

La recomendación es `ADAPT / EVAL-FIRST`: adoptar el harness, la congelación, los hashes, los estados y las pruebas adversariales; no adoptar todavía pesos, thresholds ni automatización jurídica. La autoridad sobre la decisión final permanece donde siempre debió estar: en la institución y en el profesional responsable.

## Referencias seleccionadas

- Geifman, Y. y El-Yaniv, R. (2019). “SelectiveNet: A Deep Neural Network with an Integrated Reject Option”. ICML.
- Gu, Z. y Hopkins, M. (2023). “On the Evaluation of Neural Selective Prediction Methods for Natural Language Processing”. ACL.
- Guo, C. et al. (2017). “On Calibration of Modern Neural Networks”. ICML.
- NIST (2023). *AI Risk Management Framework 1.0*.
- Palmer, J. (2026). *kev: a laptop-scale reconstruction of a Jev-style decision model*.
- TypeSafe AI (2026). “Introducing System One Models & Jev”.

## Declaración de asistencia de IA

Se utilizó asistencia de IA para estructuración, edición y generación de código bajo revisión del autor. La selección de la pregunta, los límites jurídicos, la interpretación de resultados y la responsabilidad final corresponden al autor. El uso de Jev se limitó a metadatos públicos y a las tareas documentadas.

