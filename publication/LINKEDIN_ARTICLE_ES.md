# La IA jurídica no necesita otro oráculo

![Arquitectura visual de IA jurídica instrumentada](../assets/ai-instrumentada-editorial-v1.png)

## Probé Jev y Kev con fallos argentinos. El resultado más importante no fue cuál modelo ganó, sino dónde la automatización debía detenerse.

Un modelo puede devolver una respuesta perfectamente tipada y estar perfectamente equivocado.

Esa frase resume el primer piloto público y reproducible en español que realicé con Jev sobre metadatos de la Corte Suprema de Justicia de la Nación. Quería comprobar una idea concreta: si reemplazamos el párrafo persuasivo por decisiones acotadas, probabilidades visibles y reglas explícitas, ¿obtenemos una arquitectura jurídica más confiable?

La respuesta es incómoda y, por eso mismo, útil.

Congelé treinta registros públicos de la CSJN. Formulé dos preguntas: cuál era el área jurídica principal y qué vehículo procesal aparecía expresamente en la carátula. Comparé tres sistemas: reglas determinísticas, Kev 0.5B ejecutado localmente y Jev.

Los resultados fueron:

| Sistema | Área jurídica | Vehículo procesal |
|---|---:|---:|
| Reglas | 96,7% | 100% |
| Kev | 20% | 80% |
| Jev | 60% | 96,7% |

Jev fue muy superior a Kev. Pero las reglas simples fueron superiores a ambos en las dos tareas. Eso no significa que la IA no sirva. Significa que no conviene usar una estimación semántica donde una regla clara resuelve mejor el problema.

El dato más serio apareció al mirar la confianza. En clasificación de área, Jev cometió errores con confianza 0,99 y 1,00. Entre los dieciséis casos con confianza igual o superior a 0,90, acertó doce. En vehículo procesal, en cambio, acertó los veintiocho casos retenidos por ese mismo umbral.

La misma cifra de confianza no tenía el mismo valor institucional según la pregunta.

Tipar una salida no vuelve determinística a la inteligencia artificial. La parte determinística puede estar en el código que valida el tipo, calcula una fecha, aplica un threshold o bloquea una acción. La estimación del modelo sigue siendo probabilística.

Por eso propongo pasar de la IA como oráculo a la IA instrumentada:

```text
fuentes
→ proposiciones ancladas
→ estimaciones probabilísticas
→ reglas determinísticas
→ PASS / ESCALATE / BLOCK
→ revisión profesional
→ verificación de vigencia
```

La incertidumbre deja de ser una frase prudente al final del informe. Se convierte en un estado capaz de detener el procedimiento.

El piloto tuvo límites deliberados. La descarga automatizada de los PDF oficiales respondió HTTP 403 y no intenté eludirlo. La capa moderna quedó limitada a metadatos. No evalué holding, vigencia, autoridad, razonamiento judicial ni resultados de expedientes. Tampoco envié información privada. El costo estimado de Jev fue de aproximadamente USD 0,0042; el costo importante fue el trabajo humano de diseñar, congelar, revisar y auditar.

La próxima prueba será más exigente:

**afirmación + pasaje del fallo → supported / contradicted / unverified**

El pasaje deberá conservarse siempre para revisión humana. Un resultado “no verificado” no se convertirá automáticamente en falso. Y ningún puntaje decidirá qué es derecho vigente.

Publiqué el corpus permitido, el código, las preguntas y las salidas crudas para que el experimento pueda discutirse y replicarse. Mi conclusión provisional es `ADAPT / EVAL-FIRST`: adoptar la instrumentación, no automatizar la decisión jurídica.

En América Latina necesitamos menos demostraciones cerradas y más experimentos que permitan localizar el error.

Ignacio Adrián Lerer  
estudio.justitia.com.ar
