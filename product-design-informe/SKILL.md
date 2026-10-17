---
name: product-design-informe
description: Variante local de product-design con dos añadidos: (1) un workflow para ARRANCAR proyectos que abren un estándar o producto dependiente de terceros (bancos, procesadores, comercios, reguladores) y (2) la producción de un INFORME PDF de estudio de mercado, MOAT y estrategia (portada, índice con páginas, tablas, gráficos, fuentes numeradas, marcas de confianza) con un generador ReportLab incluido. Úsala cuando el usuario pida un informe/PDF/documento de estrategia o estudio de mercado, quiera arrancar un proyecto de este estilo, o cuando aplique product-design. Guía el proceso completo de product design, del problema al spec listo para desarrollo. Úsala siempre que el usuario hable de diseñar un producto, feature, app o flujo, definir el problema, user stories, journeys, wireframes, mockups, prototipos, design specs, PRD, UX/UI, análisis de mercado o competidores, monetización, pricing, posicionamiento o diferenciación, priorizar, simplificar o recortar alcance, iterar más rápido, planificar tareas de un prototipo, o pida revisar o mejorar un diseño, aunque no diga "product design". También en inglés (product design, UX, UI, user flow, wireframe, design critique, design handoff).
---

# Product Design

Acompaña al usuario por el proceso de diseño de producto y entrega, en cada fase, algo que pueda usar. Adapta la profundidad a la petición: una idea suelta pide empezar por el problema; un flujo ya definido pide ir directo a pantallas o spec. No recorras todas las fases por inercia.

## Cómo trabajar

1. **Ubica la fase.** Identifica en qué punto está el usuario (idea, problema definido, flujo, UI, handoff, revisión) y empieza ahí. Saltarse una fase cuyo resultado ya existe ahorra tiempo; saltarse una que falta genera diseños sin base.
2. **Pregunta lo mínimo.** Si falta contexto decisivo (usuario objetivo, objetivo de negocio, plataforma), haz una sola pregunta corta. Si no es decisivo, asume lo razonable y declara la suposición en una línea.
3. **Entrega por fases.** Muestra un primer borrador pronto para que el usuario pueda redirigir, en vez de un entregable enorme al final.
4. **Cuestiona y borra antes de construir.** Pasa lo que vas a producir por el algoritmo de 5 pasos y por la velocidad de iteración (más abajo): lo más rápido es no hacer lo que sobra.
5. **Responde en el idioma del usuario.**

## Principios base de diseño

Aplícalos en todas las fases; son el filtro con el que se decide qué diseñar y qué descartar.

### Moverse a donde están los usuarios
Diseña para que el producto llegue al usuario, no para que el usuario venga al producto. Cambiar de hábitos, herramientas o canales es un coste alto, y la mayoría de los usuarios no lo paga.
- Identifica dónde ya trabajan y se comunican (apps, canales, dispositivos, momentos del día) y plantea el producto ahí: integraciones, notificaciones en su canal habitual, formatos que ya usan, sin cuenta ni instalación cuando sea posible.
- Reduce lo que se les pide cambiar: reutiliza patrones y datos que ya tienen, importa en lugar de pedir que reintroduzcan, y evita flujos que exijan salir de su contexto.
- En cada propuesta, responde explícitamente: "¿qué tiene que cambiar el usuario para usar esto?". Si la respuesta es mucho, busca una versión que se acerque más a su contexto actual.
- Una mejora que obliga a migrar de herramienta debe aportar mucho más valor que el coste de moverse; si no, rediseña el punto de entrada.

### M.O.A.T. (ventaja competitiva defendible)
Un buen diseño no solo resuelve el problema: construye una ventaja que a la competencia le cueste copiar. Para cada producto o feature importante, pregúntate cuál es su moat y diseña para reforzarlo.
- Fuentes típicas: efectos de red, datos propios que mejoran el producto con el uso, costes de cambio, integración profunda en el flujo del usuario, marca y confianza, experiencia que se vuelve hábito.
- Distingue ventaja real de ventaja frágil: una funcionalidad copiable en semanas no es un moat; los datos acumulados, la integración en el flujo y los costes de cambio sí.
- Une ambos principios: estar donde están los usuarios (integración en su flujo) suele crear costes de cambio y datos propios, es decir, moat.
- En el framing (fase 1), en el análisis de mercado (fase 2) y en el spec (fase 7) incluye una línea: "Moat: qué lo hace difícil de replicar y cómo lo refuerza este diseño".

### Algoritmo de 5 pasos (cuestionar, borrar, simplificar, acelerar, automatizar)
Aplícalo a cualquier requisito, feature, flujo, proceso o tarea antes de diseñarlo o construirlo. El orden importa: es un error común optimizar, acelerar o automatizar algo que no debería existir.
1. **Cuestiona los requisitos.** Cada requisito debe tener un dueño con nombre (una persona o un dato, no "alguien lo pidió") y una razón comprobable. Los requisitos más peligrosos son los que parecen obvios o vienen de alguien inteligente: cuestiónalos igual. Pregunta "¿quién lo necesita y qué pasa si no está?".
2. **Borra partes o pasos innecesarios.** Elimina antes de mejorar. Si después no tienes que volver a añadir al menos una décima parte de lo que borraste, no borraste lo suficiente. Aplica a funciones, campos, pantallas, pasos del usuario, tareas y documentos.
3. **Simplifica y optimiza.** Solo después de borrar, simplifica lo que queda: menos pasos, menos opciones, menos actores. Optimizar algo que no debía existir es el desperdicio más caro.
4. **Acelera el ciclo.** Acorta el tiempo entre una idea y la evidencia de si funciona (ver abajo, "Velocidad de iteración"). Acelera solo lo que sobrevivió a los pasos 1 a 3.
5. **Automatiza.** Lo último, y solo lo que ya es simple, estable y se repite: pruebas, generación de datos, despliegues, comprobaciones. Automatizar antes de simplificar fija un proceso malo.

Cómo usarlo en la práctica:
- En definición y alcance (fase 3), pasa cada requisito por los pasos 1 y 2 y deja explícito qué se borró y por qué.
- En flujos y UI (fases 4 y 5), cuenta los pasos del usuario y borra los que no aporten valor directo.
- En el plan de trabajo, ordena las tareas según los 5 pasos: primero preguntas y borrados, al final la automatización.
- En el modo revisión, pregunta siempre "¿qué se puede borrar?" antes de proponer añadidos.

### Velocidad de iteración
El producto mejora tantas veces como ciclos completes de idea, versión mínima, evidencia y decisión. Diseña el trabajo para maximizar ciclos por semana, no para pulir cada versión.
- **Versión más pequeña que dé evidencia.** Define qué hipótesis prueba cada entregable y construye solo lo necesario para probarla. Un prototipo desechable que responde en un día vale más que uno pulido que responde en un mes.
- **Primero lo que más reduce la incertidumbre.** Ordena el trabajo por el riesgo que elimina, no por lo fácil o lo vistoso. Ataca pronto la suposición que, si falla, invalida todo.
- **Ciclos cortos con una pregunta cada uno.** Cada iteración tiene una pregunta, un criterio de éxito y un límite de tiempo. Al terminar, decide: seguir, cambiar o borrar.
- **Elimina esperas.** Detecta qué hace esperar a cada ciclo (aprobaciones, datos reales, dependencias externas) y sustitúyelo por algo local: datos sintéticos, simuladores, mocks, stubs. Lo que depende de terceros se lanza en paralelo desde el principio.
- **Trabaja en paralelo.** Lo independiente (investigación, diseño, prototipo, validación) avanza a la vez; reserva lo secuencial para lo que realmente depende de un resultado anterior.
- **Mide el propio ciclo.** Anota cuánto tarda cada iteración y dónde se pierde el tiempo; esa es la métrica del proceso, aparte de la del producto.
- **Decisiones reversibles, rápido.** Si se puede deshacer con poco coste, decide con la información que hay. Detente y consulta solo en lo difícil de revertir.
- **Entrega de forma incremental** y deja siempre algo que se pueda ver y probar al final de cada paso.

## Fases y qué producir

### 1. Descubrimiento y framing del problema
Por qué importa: un diseño bueno de un problema equivocado no sirve.
- Quién es el usuario y en qué situación está (contexto, no demografía).
- El problema en una frase: "[Usuario] necesita [objetivo] pero [obstáculo], lo que causa [consecuencia]".
- Alternativas actuales y por qué fallan.
- Hipótesis y riesgos clave; cómo validarlos barato.
- Métrica de éxito (una principal, máximo dos de apoyo).
- Dónde están hoy los usuarios y qué tendrían que cambiar para usar el producto.
- Moat potencial: qué ventaja defendible puede construir el producto.

### 2. Mercado, competencia y monetización
Por qué importa: saber quién más resuelve el problema, cómo gana dinero y dónde puedes ser distinto evita construir algo sin hueco de mercado o sin modelo de negocio. Busca información actual en la web (precios, funciones, noticias) y cita las fuentes. No inventes cifras: marca como estimación lo que no puedas verificar.
- **Mercado:** quién paga y quién usa (a veces son distintos), tamaño aproximado del problema (usuarios, frecuencia, valor por usuario), tendencias y cambios regulatorios o tecnológicos relevantes.
- **Competidores y sustitutos:** directos, indirectos y "no hacer nada" o soluciones manuales. Para cada uno: qué hace, a quién sirve, cómo monetiza, puntos fuertes y débiles, y dónde está el usuario cuando lo usa. Resume en una tabla comparativa con las dimensiones que le importan al usuario, no solo la lista de funciones.
- **Monetización:** modelos posibles (suscripción, comisión por transacción, licencia B2B, freemium, publicidad o datos, servicios sobre un estándar abierto, cuotas de miembros). Para cada uno: quién paga, por qué pagaría, qué ingresos cabe esperar y qué riesgos tiene (por ejemplo, el conflicto de confianza al monetizar datos del usuario). Recomienda un modelo principal y explica por qué.
- **Diferenciación y posicionamiento:** en una frase, "A diferencia de [alternativa], nosotros [diferencia] para [usuario] porque [razón]". Contrasta con los principios base: ¿llega a donde está el usuario mejor que ellos?, ¿cuál es el moat frente a cada competidor y cuánto tardaría en copiarse?
- **Conclusión:** huecos reales del mercado, riesgos de la competencia y qué validar antes de invertir más.

### 3. Definición
- 3–5 user stories o jobs-to-be-done, priorizadas (Must / Should / Could).
- Alcance explícito: qué entra en la v1 y qué se deja fuera a propósito.
- Requisitos cuestionados y borrados: para cada uno, quién lo necesita y por qué; lista lo que se eliminó y el motivo.
- Plan de iteración: el ciclo más corto que prueba la suposición más arriesgada, con su pregunta, criterio de éxito y límite de tiempo.
- Casos límite: vacío, error, carga, permisos, primera vez vs recurrente.

### 4. Flujos y arquitectura de información
- Mapa del flujo principal (feliz) y de los caminos alternativos y de error.
- Pantallas o estados necesarios y cómo se navega entre ellos.
- Si ayuda, un diagrama (Mermaid o similar) en lugar de describirlo en texto.

### 5. Diseño de interfaz
- Empieza en baja fidelidad (estructura y jerarquía) antes de estilo.
- Jerarquía visual clara: una acción primaria por pantalla.
- Reutiliza componentes y patrones conocidos; innova solo donde aporta valor.
- Cubre todos los estados (vacío, carga, error, éxito), no solo el feliz.
- Accesibilidad desde el inicio: contraste (WCAG AA), tamaños táctiles ≥ 44px, no depender solo del color, etiquetas claras, foco visible.
- Si hay tokens o design system, úsalos; si no, propón uno mínimo (color, tipografía, espaciado, radio).
- Para mockups visuales, apóyate en la skill `frontend-design` o en el tipo de artefacto de diseño si está disponible.

### 6. Validación
- Plan de prueba breve: 5 usuarios, 3 tareas, qué se observa y qué cuenta como fallo.
- Preguntas que evitan sesgo (no "¿te gusta?" sino "¿qué esperas que pase si pulsas aquí?").

### 7. Handoff a desarrollo
Spec con: objetivo, user stories, flujos, pantallas y estados, componentes, comportamiento e interacciones, copy, reglas de validación, criterios de aceptación, analítica a medir, dudas abiertas, y una línea de moat (qué lo hace difícil de replicar), de puntos de entrada (en qué contexto del usuario vive) y de diferenciación frente a las alternativas.

## Modo revisión de diseños
Cuando el usuario comparta un diseño o flujo para criticar:
1. Resume en una frase qué intenta lograr (para confirmar que lo entiendes).
1b. Pregunta qué se puede borrar (campos, pasos, pantallas) antes de proponer añadidos.
2. Evalúa con heurísticas de Nielsen, jerarquía, consistencia, accesibilidad y carga cognitiva.
3. Prioriza los hallazgos: **Bloqueante / Importante / Detalle**, cada uno con el porqué y una propuesta concreta.
4. Comprueba los principios base: ¿exige que el usuario se mueva o va a donde está?, ¿refuerza algún moat?, ¿en qué se diferencia de las alternativas que ya existen?
5. Señala también lo que funciona bien, para que no se pierda en la iteración.

## Formato de salida
Elige según el caso, sin preguntar si es obvio:
- **Documento** (PRD, spec, plan de investigación, análisis de mercado): ideal para fases 1, 2, 3, 6 y 7. Entrégalo como doc o markdown, con las fuentes citadas en el análisis de mercado.
- **Mockup o prototipo HTML**: ideal para fase 5. Una sola página autocontenida, responsive.
- **Diagrama**: para flujos y arquitectura (fase 4) y para el posicionamiento frente a competidores (matriz de dos ejes).
- **Respuesta en chat**: para dudas puntuales, críticas rápidas o decisiones de diseño.

## Principios
- Decide con el usuario final en mente; cada elemento debe justificar su sitio.
- Prefiere lo simple: menos pasos, menos opciones, lenguaje claro.
- Explica el porqué de las decisiones de diseño en una línea; así el usuario aprende y puede discutirlas.
- Distingue lo que sabes de lo que supones, y propón cómo validar lo segundo.

## Workflow: arrancar un proyecto que depende de terceros
**Cuándo usarlo.**

Proyectos que intentan **abrir un estándar o producto que depende de terceros** (bancos, procesadores, comercios, reguladores) y que no se pueden validar del todo sin ellos: protocolos, integraciones, marketplaces, datos compartidos entre empresas. Si el producto lo controla un solo equipo y se puede probar solo con usuarios, basta con las fases normales de la skill.


Cada paso termina con algo que se puede ver, ejecutar o leer. No saltes al código sin los pasos 1 a 4.

### 1. Una página de contexto (`CLAUDE.md`)
Objetivo y 3 cosas que debe demostrar; **qué NO es**; principios de diseño (aquí van "moverse a donde están los usuarios" y "M.O.A.T."); riesgos y suposiciones abiertas; preguntas abiertas. Se mantiene actualizado cuando cambia una decisión. Regla fija: nada se presenta como validado si no lo está.

### 2. Estudio de lo que ya existe, antes de construir
Competidores, sustitutos, intentos previos que fracasaron y marco regulatorio, con **fuente, fecha y nivel de confianza** (alto/medio/bajo) y separando hecho de inferencia. Después, contrastar de forma independiente las 2-3 afirmaciones que más mueven el pitch. En un proyecto real este paso mostró que la suposición "no existe nada parecido" era falsa y reorientó el posicionamiento.

### 3. Mapa de dependencias de terceros
Lista qué hay que confirmar con cada tercero y escríbelo como **preguntas concretas** (no "hablar con un procesador"). Esas conversaciones se lanzan **en paralelo desde el primer día**, porque son lo más lento. Todo lo que no dependa de ellos se construye con simuladores, datos sintéticos con semilla y mocks.

### 4. Puertas de decisión
Identifica de antemano qué decisiones son **difíciles de revertir** (esquema, formato de mensajes, clave de identificación, valores por defecto con efecto en privacidad). Para cada una: resumir 2-3 opciones, dar una recomendación y **preguntar al usuario** antes de implementar. Las reversibles se deciden con la información disponible y se anotan.

### 5. Backlog en issues, con prioridad y criterio de "hecho"
P0 núcleo técnico, P1 necesario para la demo, P2 validación y salida. Cada tarea con un "hecho cuando" que se demuestre con una prueba o una ejecución reproducible. Etiqueta aparte las que dependen de terceros.

### 6. Simular primero, medir una métrica principal
El primer entregable es el flujo extremo a extremo simulado y **una métrica principal** medible (p. ej., en un proyecto de pagos, la tasa de emparejado entre dos mensajes). Los parámetros inventados se rotulan como tales en cada tabla y cada frase: una simulación no es evidencia del mundo real.

### 7. Orquestación por niveles de modelo
Un orquestador reparte el trabajo y no escribe código salvo lo trivial:
1. Modelo grande: planificar, diseñar interfaces, analizar decisiones y revisar.
2. Modelo medio: escribir código y pruebas (TDD: la prueba primero y verla fallar).
3. Modelo pequeño: leer archivos, tareas mecánicas, README y CI.

Reglas: contratos mínimos primero (firmas y modelos) para que los agentes en paralelo no se pisen; **cada agente es dueño de sus archivos**; un integrador cablea la CLI y la documentación; el orquestador verifica la suite y hace **un commit por tarea**.

### 8. Revisión adversarial periódica
Tras cada bloque, una revisión independiente que **confirme cada hallazgo ejecutándolo** (no especulaciones), con reproducción mínima. Después: pruebas de propiedades sobre lo crítico y comprobación en un navegador real de lo que sea interfaz. En un proyecto real la revisión encontró un falso casado y un fallo de detección de datos de tarjeta que las pruebas del propio autor no veían. Desconfía de pruebas que "pasan" porque se apagó el caso difícil.

### 9. Privacidad y seguridad desde el P0
Opt-in revocable, minimización, ROPA y DPIA simplificados como **borradores sin validación legal**, modelo de amenazas, y una política de revocación decidida por el usuario. Lo que queda sin resolver se documenta como riesgo residual y se deja visible en una prueba `xfail`.

### 10. Salida para terceros
Guion de demo de 2 minutos con "qué NO decir", propuesta de piloto con alcance mínimo y métricas como hipótesis, y un kit para validar con personas (consentimiento, anonimización, protocolo de 5 usuarios y 3 tareas).

### 11. Higiene
Commits pequeños con propósito claro, issues cerradas con enlace al commit y comentario honesto de qué quedó fuera, `CLAUDE.md` y documentos de decisiones al día, y una lista pública de lo que el prototipo **no** demuestra.

### Plantillas rápidas

**Issue:** contexto · hecho cuando (reproducible) · depende de · ¿decisión difícil de revertir? (sí/no) · riesgos.

**Decisión difícil de revertir:** opciones (2-3) con pros y contras · recomendación · qué se rompe si cambia · quién decide.

**Hallazgo de revisión:** severidad · archivo:línea · reproducción mínima · arreglo propuesto · ¿cambia un contrato?

**Afirmación de pitch:** frase · fuente · fecha · confianza · hecho o inferencia.

### Errores que este workflow evita
- Construir contra un mercado que se supone vacío sin comprobarlo.
- Esperar a un tercero para empezar, cuando podía lanzarse la conversación el primer día.
- Presentar cifras de una simulación como si fueran resultados reales.
- Cambiar un esquema o un valor por defecto sin preguntar.
- Dar por buena una prueba que solo confirma la implementación.


## Informe de estudio de mercado y estrategia (PDF)

Cuando el usuario pida un informe, un PDF o un documento de estudio de mercado, competencia, MOAT y estrategia, produce un PDF con el generador incluido en esta skill. Es el entregable de la fase 2 (mercado) y de la conclusión de la fase 1 y 3.

### Proceso
1. **Reúne la base.** Lee los documentos del proyecto (contexto, precedentes, riesgos, métricas). Si ya hay estudios previos con fuentes, parte de ellos y cítalos; no los repitas.
2. **Investiga y contrasta.** Con búsqueda web, contrasta de forma independiente las 6-8 cifras o hechos que más pesan (competidores que cerraron, tamaño del problema, regulación, formato abierto existente). Cada dato lleva fuente, fecha y confianza. Lo que no se pueda contrastar conserva la confianza de su origen y se dice.
3. **Escribe el contenido en JSON** con el esquema de `scripts/ejemplo.json` (portada, secciones, bloques, fuentes numeradas). Una sola idea por párrafo; cifras en tabla o gráfico, no enterradas en prosa.
4. **Genera y REVISA el PDF.** `python3 scripts/generar_informe.py contenido.json salida.pdf` (necesita `reportlab`; el generador valida el JSON y da errores claros). Renderiza las páginas a imagen y míralas: índice con números de página, sin títulos solos al final de página, tablas legibles, gráficos con título y fuente, acentos y ñ correctos.
5. **Pasa la lista de comprobación** (abajo) y entrega el PDF con un resumen de 5 líneas y las decisiones que quedan para el usuario.

### Estructura (12 secciones + fuentes)
1. Resumen para decidir en un minuto (recuadro "En una frase" + problema, mercado, competencia, MOAT, estrategia).
2. El problema y a quién sirve (quién usa y quién paga, cómo se resuelve hoy y por qué falla).
3. Los principios que guían el diseño (ir a donde están los usuarios, M.O.A.T., algoritmo de 5 pasos, velocidad de iteración; cómo se aplican).
4. El mercado (embudo con método y supuestos, rangos, fiabilidad de cada cifra, "Límite honesto").
5. La competencia (tabla: competidor, qué ofrece, cómo cobra, punto fuerte, punto débil; incluir "no hacer nada" y a los que ya cerraron; mapa de dos ejes).
6. Cómo ganar dinero (tabla de modelos con quién paga, ingreso esperado como ESTIMACIÓN y riesgo; recomendación en recuadro).
7. Posicionamiento (qué ya existe en el producto y qué todavía no, verificado contra el código o el prototipo).
8. El MOAT (fuentes del moat con fuerza hoy, por qué protege y cómo se refuerza; qué parece moat y no lo es).
9. Borrar antes de construir (los 5 pasos aplicados; qué se borra y por qué).
10. Plan de validación rápida (calendario de semanas, responsable, criterio de seguir / cambiar / parar, preguntas sin sesgo para entrevistas).
11. Riesgos y lo que aún no sabemos (tabla con gravedad y qué se hace; plan de contingencia de la prueba más arriesgada).
12. Conclusión (estrategia en una frase, tabla de decisión por ejes, "qué nos haría cambiar de opinión", veredicto) y, al final, Fuentes numeradas.

### Formato (referencia, A4)
- Portada: banda superior azul marino #14213d y franja dorada #b08d3c, título 30 pt, subtítulo dorado 14 pt, tagline 12 pt, bloque Fecha / Método / Estado; sin pie.
- Texto: Helvetica, cuerpo 10,5 pt (#222222), H1 18 pt azul marino numerado con línea dorada, H2 12,5 pt, tablas 8,8 pt con cabecera azul marino y filas alternas #f2f0eb, notas 8,5 pt gris.
- Recuadros con fondo beige y barra dorada para "En una frase", "Recomendación", "Estrategia en una frase". Pie con título y "Página N" desde la página 2.
- Etiquetas de confianza en línea: Dato verificado, Dato antiguo, Estimación, Hipótesis, Inferencia. Todo dato no verificado se rotula como estimación.

### Reglas de contenido
- Distingue hecho citado, inferencia y estimación; no inventes cifras ni nombres; no afirmes que ninguna empresa esté interesada ni cumplimiento legal; lo no validado se dice.
- Cada cifra con referencia numerada [n] a la lista de fuentes (nombre, URL, fecha, confianza). Marca las fuentes interesadas.
- Incluye siempre: un cálculo del tamaño del problema con método y rangos, "Límite honesto", qué demuestra y qué no el prototipo, "qué nos haría cambiar de opinión" y un plan de contingencia.
- Mínimo 3 gráficos cuando haya datos (embudo, mapa de posicionamiento, barras) y ninguno decorativo.
- Tono "nosotros", frases cortas, vocabulario sencillo; explica cada sigla la primera vez.

### Lista de comprobación antes de entregar
- [ ] Índice con números de página; ningún título solo al final de una página; sin líneas huérfanas.
- [ ] Erratas y acentos (Cómo/Como, ¿ ¡, ñ, tildes); términos explicados.
- [ ] Todas las [n] existen y todas las fuentes se citan; URLs válidas y fecha de consulta.
- [ ] Las cifras de simulación o inventadas están rotuladas como tales.
- [ ] El PDF abre bien, pesa poco y tiene título y autor en los metadatos.
- [ ] Se han visto las páginas como imagen, no solo el texto.

### Generador
`scripts/generar_informe.py` (ReportLab; usa el `python3` que tenga `reportlab`) y `scripts/ejemplo.json` con todos los tipos de bloque: párrafo, subtítulo, viñetas, recuadro, nota, tabla, salto de página y gráficos (barras, mapa de dos ejes, embudo). Si falta `reportlab`: `python3 -m pip install reportlab`.
