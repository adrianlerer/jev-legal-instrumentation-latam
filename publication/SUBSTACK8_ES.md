# Cuando una IA jurídica se equivoca con confianza 1,00

![Arquitectura visual de IA jurídica instrumentada](../assets/ai-instrumentada-editorial-v1.png)

## Un piloto reproducible con Jev, Kev y treinta registros de la Corte Suprema argentina

La confianza 1,00 parece una conclusión. En realidad, puede ser apenas una distribución cerrada sobre opciones mal elegidas.

Esa fue la observación más importante de mi primer piloto con Jev aplicado a metadatos jurídicos argentinos. No buscaba probar que un modelo pudiera “resolver derecho”. Quería estudiar una arquitectura diferente: una inteligencia artificial que no emitiera un dictamen completo, sino proposiciones pequeñas que un procedimiento pudiera validar, combinar, escalar o bloquear.

Congelé treinta registros públicos de la Corte Suprema de Justicia de la Nación. Pregunté por el área jurídica y por el vehículo procesal expresamente mencionado. Comparé reglas determinísticas, Kev 0.5B local y Jev.

Las reglas obtuvieron 96,7% y 100%. Kev, 20% y 80%. Jev, 60% y 96,7%.

La diferencia entre las dos preguntas importa más que el ranking. Reconocer “Recurso Queja” es una tarea casi literal. Clasificar el área jurídica desde una carátula exige una relación semántica más frágil. Jev funcionó bien en la primera y falló cuatro de cada diez casos en la segunda.

Tampoco bastó la confianza. Con un corte de 0,90, Jev acertó doce de dieciséis áreas. Hubo errores con 0,99 y 1,00. En vehículo procesal, el mismo corte retuvo veintiocho casos y acertó todos.

Un threshold no posee un significado jurídico universal. Debe calibrarse por tarea, dominio, idioma y costo del error.

La lección no es abandonar la IA, sino instrumentarla. Las fechas, cálculos, permisos y transiciones deben quedar en código. Las relaciones semánticas pueden estimarse probabilísticamente. Las conclusiones normativas y la valoración probatoria siguen bajo autoridad profesional.

El procedimiento que propongo utiliza tres estados: `PASS`, `ESCALATE` y `BLOCK`. Si falta el texto completo, si la evidencia se contradice o si la vigencia no fue comprobada, el flujo cambia. No basta añadir una advertencia y continuar.

El experimento también respetó una frontera técnica. La descarga directa de los PDF oficiales respondió HTTP 403. No la eludí. La muestra moderna quedó limitada a metadatos. Los treinta pasajes de texto incluidos proceden de un tomo histórico público y sólo sirven para probar mecanismos, no para afirmar derecho vigente.

El siguiente benchmark evaluará soporte de citas: una afirmación y un pasaje deberán clasificarse como apoyados, contradichos o no verificados. Siempre se conservará el pasaje. Allí se juega una diferencia institucional decisiva: poder discutir la proposición sin aceptar el párrafo entero como un oráculo.

El repositorio público contiene corpus permitido, código y resultados. El paper y la nota técnica preservan también el resultado negativo. Porque la innovación útil no consiste en exhibir que una IA acertó. Consiste en construir un procedimiento capaz de mostrar dónde se equivocó y qué debe ocurrir después.

Ignacio Adrián Lerer  
estudio.justitia.com.ar
