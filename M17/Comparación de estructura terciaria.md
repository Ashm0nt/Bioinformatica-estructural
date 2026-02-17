# Comparación de estructura tercearia

La **estructura terciaria** corresponde al arreglo espacial completo de todos los átomos de una proteína, es decir, cómo los elementos de estructura secundaria (hélices α, láminas β, giros y lazos) se organizan en el espacio para formar una conformación compacta y funcional.

Esta organización no es arbitraria: está determinada por **principios fisicoquímicos** que gobiernan el plegamiento y la estabilidad de la proteína. Este nivel estructural es el que realmente define la geometría molecular responsable de la actividad biológica.

## Conservación estructural y comparación entre proteínas
Aunque la secuencia primaria puede divergir considerablemente a lo largo del tiempo evolutivo, la estructura terciaria tiende a conservarse con mucha mayor fuerza. Esto ocurre porque:

- La función depende directamente de la forma tridimensional.
- El núcleo estructural suele estar compuesto por residuos cuya sustitución está fuertemente restringida.
- Muchas mutaciones son toleradas siempre que no alteren el empaquetamiento global.
- Existen múltiples combinaciones de aminoácidos capaces de estabilizar una misma arquitectura tridimensional.

En términos evolutivos, el plegamiento representa una **solución estructural robusta** que puede mantenerse incluso cuando la secuencia cambia.

Por ello, dos proteínas pueden presentar:

- Muy baja identidad de secuencia (< 20%).
- Diferencias extensas en regiones periféricas.
- Inserciones o deleciones en bucles.

y aun así compartir:

- El mismo núcleo estructural.
- La misma topología de hélices y láminas β.
- La misma organización de dominios.
- Un sitio activo con geometría equivalente.

### ¿Por qué la estructura se conserva más que la secuencia?

1. **Redundancia en el código estructural**  
   Muchos aminoácidos pueden sustituirse por otros con propiedades fisicoquímicas similares sin alterar el plegamiento global.

2. **Restricción funcional**  
   La actividad catalítica, unión a ligandos o interacción con otras macromoléculas depende de la geometría tridimensional, no de la identidad exacta de cada residuo.

3. **Limitación del espacio de plegamientos**  
   El número de arquitecturas estables posibles es finito.  
   La evolución tiende a reutilizar plegamientos exitosos en diferentes contextos funcionales.

4. **Conservación del núcleo hidrofóbico**  
   El núcleo estructural suele ser más conservado que las regiones superficiales, que toleran mayor variabilidad.

### Implicaciones para evolución y filogenia de proteínas

Dado que la secuencia puede divergir rápidamente mientras que el plegamiento se mantiene, la comparación estructural se convierte en una herramienta más potente para detectar:

- Homología remota.
- Ancestros comunes antiguos.
- Relaciones evolutivas profundas.
- Superfamilias estructurales.

En etapas evolutivas muy separadas, la señal de similitud en la secuencia puede perderse por acumulación de mutaciones (saturación evolutiva). Sin embargo, la arquitectura tridimensional puede seguir revelando un origen común.

Por ello, desde el punto de vista filogenético:

- La secuencia es informativa en divergencias recientes.
- La estructura es más informativa en divergencias profundas.

En resumen, mientras que la secuencia refleja la historia local de mutaciones,  
la estructura refleja la historia conservada del plegamiento y la función.  
Y es precisamente esta estabilidad del plegamiento lo que permite reconstruir relaciones evolutivas que serían invisibles si solo analizáramos secuencias.


### PROBLEMA

Disponemos de las coordenadas tridimensionales de dos proteínas A y B y queremos calcular cuánto se parecen sus estructuras.

Cada proteína puede representarse como un conjunto de puntos en el espacio (por ejemplo, las coordenadas de los átomos Cα). Sin embargo, comparar directamente estas coordenadas no es trivial porque:

- Las proteínas pueden tener distinta longitud.
- Puede haber inserciones o deleciones.
- No existe necesariamente una correspondencia uno-a-uno entre residuos.
- Las moléculas pueden estar rotadas y trasladadas arbitrariamente en el espacio.

Por tanto, el problema no es solo medir distancias, sino determinar:

1. Qué regiones son estructuralmente equivalentes.
2. Cómo superponerlas de forma óptima.
3. Cómo cuantificar objetivamente la similitud obtenida.

En términos formales, buscamos una medida que capture similitud geométrica independientemente de la orientación espacial inicial.


### SOLUCIÓN

Buscar las subestructuras de máximo tamaño subA y subB que minimicen la distancia entre átomos equivalentes.

Esta solución implica tres componentes fundamentales:

#### 1. Identificación de subestructuras comunes

No necesariamente se alinean las proteínas completas.  
El objetivo es encontrar el **núcleo estructural compartido más grande posible**, es decir:

- Un conjunto de residuos en A.
- Un conjunto correspondiente en B.
- Que mantengan la misma organización tridimensional.

Estas subestructuras suelen corresponder a dominios conservados o al plegamiento central de la proteína.


#### 2. Superposición rígida óptima

Una vez identificados los pares equivalentes, se aplica una transformación geométrica que incluye:

- Una rotación.
- Una traslación.

Esta transformación no deforma la estructura; únicamente cambia su posición y orientación en el espacio para maximizar la coincidencia espacial.

Matemáticamente, se busca minimizar:

\[
\sum_i \| R A_i + t - B_i \|^2
\]

donde:

- \(A_i\) y \(B_i\) son pares de átomos equivalentes.
- \(R\) es una matriz de rotación.
- \(t\) es un vector de traslación.


#### 3. Minimización de la distancia estructural

El criterio habitual es minimizar la desviación cuadrática media (RMSD), que cuantifica cuánto se separan en promedio los átomos equivalentes tras la superposición.

El objetivo completo puede resumirse como:

> Encontrar la región común más grande posible cuya superposición produzca la menor desviación geométrica.


### Interpretación biológica

Si existe una subestructura extensa con baja desviación espacial, esto sugiere:

- Conservación de un plegamiento.
- Posible homología evolutiva.
- Mantenimiento de un núcleo funcional.

En cambio, si solo pequeñas regiones pueden alinearse correctamente, la similitud puede deberse a:

- Motivos estructurales recurrentes.
- Restricciones geométricas universales.
- Convergencia estructural.


## Algoritmos fundamentales para comparar estructura terciaria

La comparación estructural puede abordarse desde distintas perspectivas:  
geométrica directa, conversión a representaciones abstractas, comparación de matrices o enfoques basados en teoría de la información. A continuación repasamos algunos algoritmos representativos y sus ideas centrales.


### 1. Conversión de estructura a secuencia estructural  
(Foldseek, FoldMason)

Estos métodos transforman la información tridimensional en una **representación lineal discreta**, utilizando un alfabeto estructural diseñado a medida.

Idea principal:

- Cada residuo no se representa por su identidad química.
- Se representa por su **entorno geométrico local** o por la relación espacial con residuos vecinos.
- La estructura completa se convierte en una “secuencia estructural”.

Ventaja:

- Permite usar algoritmos rápidos de alineamiento de secuencias.
- Escala bien a bases de datos masivas.
- Reduce drásticamente el coste computacional frente al alineamiento 3D directo.

Limitación:

- Simplifica la información geométrica.
- Puede perder precisión fina en comparación con métodos puramente espaciales.

Este enfoque es especialmente útil para búsquedas rápidas a gran escala.

### 2. Alineamiento estructural iterativo  
(STAMP)

STAMP combina información de secuencia y estructura en un proceso iterativo.

Flujo general:

1. Se genera un alineamiento preliminar usando matrices de sustitución de aminoácidos (por ejemplo, BLOSUM).
2. Se calcula la superposición tridimensional correspondiente.
3. Se identifican como equivalentes los residuos cuya distancia espacial cae por debajo de un umbral.
4. Se recalcula el alineamiento usando solo estos residuos.
5. El proceso se repite hasta que el RMSD deja de mejorar.

Características clave:

- Integra información evolutiva (secuencia) con información geométrica.
- Refina progresivamente el conjunto de residuos equivalentes.
- Busca convergencia hacia un núcleo estructural estable.

Conceptualmente, este método refleja la idea de que la similitud estructural puede emerger gradualmente tras eliminar regiones mal alineadas.


### 3. Doble programación dinámica  
(SSAP – Sequential Structure Alignment Program)

SSAP utiliza una estrategia en dos niveles basada en programación dinámica.

Paso 1:  
Se identifican fragmentos localmente similares entre ambas estructuras.

Paso 2:  
Se selecciona el subconjunto óptimo de fragmentos que produce la mejor superposición global.

En lugar de comparar únicamente coordenadas directas, SSAP compara **vectores de distancias internas**, capturando la geometría relativa de cada residuo respecto al resto.

Ventajas:

- Detecta similitudes no triviales.
- Es robusto frente a inserciones y reordenamientos.

Es especialmente adecuado para comparar dominios estructurales completos.


### 4. Comparación de matrices de distancias/contactos  
(DALI)

DALI adopta un enfoque diferente: en vez de trabajar directamente con coordenadas 3D, transforma cada estructura en una **matriz de distancias internas**.

Cada entrada de la matriz representa la distancia entre pares de residuos dentro de la misma proteína.

Luego:

- Se comparan las matrices entre sí.
- Se buscan patrones similares en las relaciones internas de distancia.

Ventajas conceptuales:

- Es independiente de la orientación espacial.
- No requiere calcular rotaciones durante la comparación inicial.
- Captura la geometría global de la proteína.

DALI es especialmente potente para detectar homología estructural remota.



### 5. Minimización de información (mmligner)

Este enfoque se basa en el principio de **mínima longitud de descripción (Minimum Message Length, MML)**.

Idea central:

- Si dos estructuras son similares, describir una usando la otra debería requerir poca información adicional.
- El mejor alineamiento es aquel que minimiza la cantidad total de información necesaria para reconstruir una estructura dada la otra.

Ventajas:

- Evita la elección arbitraria de umbrales de distancia.
- Proporciona un criterio formal y bien definido para la superposición óptima.
- Integra alineamiento y evaluación estadística en un mismo marco teórico.

Es un enfoque más formal y menos heurístico que muchos métodos clásicos.



### 6. Superposición de factores de transcripción  
(TFcompare)

Este método está orientado a proteínas que interactúan con ADN.

Idea principal:

- Superponer estructuras de factores de transcripción.
- Deducir el alineamiento correcto de sus sitios de unión cis en el ADN.
- Comparar no solo la proteína, sino también la geometría del complejo proteína–ADN.

Es un ejemplo de cómo la comparación estructural puede extenderse a complejos macromoleculares y no limitarse a proteínas aisladas.

### Diversidad de métodos y ambigüedades

Existen numerosos programas para la comparación estructural de proteínas, y es común que distintos investigadores prefieran herramientas diferentes.  
La razón principal es que **no existe una definición única y totalmente satisfactoria de lo que constituye el alineamiento estructural “correcto”**.

Todos los algoritmos intentan optimizar alguna función objetivo (minimizar distancias, maximizar residuos alineados, maximizar probabilidad estadística, minimizar información, etc.), pero:

- No hay un criterio universal que capture simultáneamente geometría, topología, relevancia evolutiva y significado funcional.
- Diferentes métodos priorizan distintos aspectos (similitud local vs global, tamaño del núcleo alineado, penalización de huecos, etc.).
- El resultado puede variar según los umbrales elegidos y las heurísticas utilizadas.

Por ello, distintos investigadores pueden preferir distintos programas según el tipo de problema que estén abordando.


### Más complicaciones... 

#### Taxonomías estructurales
Esta ambigüedad también afecta a las clasificaciones estructurales clásicas, como **CATH** y **SCOP**, que durante décadas han organizado el espacio de plegamientos en categorías como:

- Clase
- Arquitectura
- Fold
- Superfamilia

Estas taxonomías han sido extremadamente útiles, pero surge una pregunta importante:

> ¿Reflejan realmente la historia evolutiva de los plegamientos?

Diversos estudios han sugerido que la evolución estructural:

- No es completamente discreta.
- Puede presentar transiciones graduales entre arquitecturas.
- Puede generar relaciones intermedias difíciles de clasificar.
- Puede reutilizar módulos estructurales en distintos contextos.

Si el espacio estructural es parcialmente continuo, entonces imponer categorías rígidas puede simplificar en exceso la realidad evolutiva.

Precisamente por estas limitaciones se desarrolló **SCOP2**, que:

- Introduce relaciones más flexibles.
- Permite múltiples conexiones entre dominios.
- Refleja mejor la complejidad evolutiva del espacio estructural.

Más recientemente, **TED: The Encyclopedia of Domains (2024)** amplió el repertorio de dominios estructurales conocidos tras la explosión de modelos generados por AlphaFold, lo que demuestra que el espacio estructural sigue expandiéndose y refinándose.


#### Permutaciones circulares
La definición de alineamiento estructural se complica aún más por fenómenos como las **permutaciones circulares**.

En estos casos:

- El orden secuencial de los elementos de estructura secundaria cambia.
- La topología tridimensional global puede mantenerse esencialmente igual.

Desde el punto de vista geométrico, las estructuras son equivalentes.  
Desde el punto de vista secuencial, parecen diferentes.

Esto desafía a los algoritmos que asumen correspondencia lineal directa y muestra que la equivalencia estructural no siempre coincide con la equivalencia secuencial.

#### Conceptos operativos

A pesar de todas estas complicaciones, en la práctica se utilizan definiciones operativas:

- Una **superfamilia** es un clúster de estructuras que pueden superponerse con buena calidad aunque su secuencia sea muy divergente.
- Un **plegamiento (fold)** agrupa varias superfamilias que comparten una topología general de estructura secundaria.

Estas categorías no son perfectas desde el punto de vista evolutivo, pero resultan útiles para organizar y comparar proteínas.

#### Evaluación comparativa de métodos

Dado que no existe un criterio absoluto de alineamiento correcto, la validación de nuevos métodos se basa en comparaciones con algoritmos preexistentes.

Estas comparaciones, si son:

- Rigurosas,
- Reproducibles,
- Basadas en bases de datos de referencia,

permiten evaluar:

- Sensibilidad para detectar homología remota.
- Robustez frente a inserciones y reordenamientos.
- Calidad estadística de la puntuación.
- Escalabilidad computacional.

La elección del método adecuado depende entonces del problema biológico concreto.


##### MAMMOTH

MAMMOTH fue uno de los algoritmos más exitosos en la era pre-AlphaFold y ejemplifica cómo se combinan similitud local, coherencia global y evaluación estadística.


1. A partir del trazado de Cα, se calcula el U-RMS entre todos los pares de heptapéptidos (fragmentos de 7 residuos).

Esta medida:

- Es sensible a la geometría local.
- No depende de la orientación global.
- Permite identificar bloques estructurales similares.

2. La matriz de similitudes locales se utiliza en un alineamiento global tipo Needleman–Wunsch (con huecos terminales sin penalización).Se obtiene así un alineamiento preliminar basado en fragmentos estructuralmente compatibles.

3. Se identifica el subconjunto máximo de fragmentos alineados cuyos Cα estén a ≤ 4.0 Å en el espacio cartesiano.

4. Este paso, inspirado en MaxSub, define el núcleo estructural común más consistente.

5. Se estima la probabilidad de obtener por azar la proporción observada de residuos alineados (E-value o Z-score), ajustando la distribución a valores extremos. Esto permite distinguir similitudes reales de coincidencias fortuitas.



 ## Más allá del RMSD: TM-score y métricas alternativas

 El RMSD ha sido durante décadas la métrica estándar para cuantificar similitud estructural.  
Sin embargo, presenta limitaciones importantes:

- Da el mismo peso a todas las regiones alineadas.
- Penaliza fuertemente desviaciones locales grandes.
- Es sensible a la longitud de las proteínas comparadas.
- Puede aumentar artificialmente si pequeñas regiones divergentes están incluidas en el alineamiento.

En particular, el RMSD no distingue entre:

- Desviaciones en el núcleo estructural (core), que son biológicamente relevantes.
- Desviaciones en regiones flexibles o periféricas, que pueden no afectar al plegamiento global.

### TM-score

Para superar estas limitaciones, Zhang y Skolnick (2004) propusieron el **TM-score (Template Modeling score)**.

La idea central del TM-score es:

> Reducir progresivamente la contribución de pares de residuos que están a mayor distancia.

En lugar de penalizar cuadráticamente la distancia (como en el RMSD), el TM-score utiliza una función de ponderación suave que disminuye el peso de las desviaciones grandes.

La fórmula general es:

\[
TM\text{-}score =
\max \left[
\frac{1}{L_Q}
\sum_{i=1}^{L_T}
\frac{1}{1 + \left(\frac{d_i}{d_0}\right)^2}
\right]
\]

donde:

- **max** es el valor máximo obtenido entre todas las superposiciones evaluadas.
- \(L_Q\) es la longitud de la proteína *query*.
- \(L_T\) es el número de residuos alineados con la proteína *template*.
- \(d_i\) es la distancia entre el par \(i\) de residuos equivalentes.
- \(d_0\) es un factor de escala dependiente de la longitud, que normaliza la puntuación.

#### Propiedades importantes

1. **Normalización por longitud**  
   El TM-score es menos sensible al tamaño absoluto de las proteínas.

2. **Rango acotado**  
   Toma valores entre 0 y 1.

3. **Interpretación estructural clara**
   - TM-score ≈ 1 → estructuras casi idénticas.
   - TM-score > 0.5 → generalmente mismo plegamiento.
   - TM-score < 0.2 → similitud comparable al azar.

4. **Menor penalización de regiones divergentes**  
   Las desviaciones grandes contribuyen poco al valor total.

Por estas razones, el TM-score se ha convertido en uno de los estándares modernos para evaluar similitud estructural.

El algoritmo **TM-align** permite calcularlo de manera eficiente y optimizada, buscando directamente la superposición que maximiza el TM-score.



### Métricas sin superposición explícita: lDDT

Aunque el TM-score mejora el RMSD, sigue dependiendo de una superposición óptima.  
Esto implica que:

- El resultado depende del alineamiento elegido.
- Puede verse afectado por decisiones heurísticas.

Para evitar esta dependencia, se han propuesto métricas que no requieren superposición global, como **lDDT (local Distance Difference Test)**.

#### Idea central de lDDT

En lugar de evaluar la desviación tras superponer dos estructuras, lDDT:

- Compara distancias locales entre pares de átomos vecinos.
- Evalúa si esas distancias se conservan dentro de ciertos radios.
- Calcula la fracción de distancias locales correctamente reproducidas.

Características:

- No requiere rotación ni traslación explícita.
- Es robusta frente a errores globales de orientación.
- Se centra en la consistencia geométrica local.

#### Rango e interpretación

- Toma valores entre 0 y 1.
- Valores altos indican alta concordancia estructural.
- Valores bajos indican discrepancias significativas en la organización local.

lDDT puede calcularse considerando:

- Todos los átomos (incluyendo cadenas laterales).
- Solo el esqueleto peptídico.
- Subconjuntos específicos según el análisis deseado.


### Comparación conceptual

| Métrica   | Requiere superposición | Sensible a longitud | Penaliza regiones divergentes | Enfoque |
|------------|------------------------|----------------------|-------------------------------|----------|
| RMSD       | Sí                     | Sí                   | Fuertemente                   | Global |
| TM-score   | Sí                     | Mucho menos          | Débilmente                    | Global ponderado |
| lDDT       | No                     | No directamente      | Evalúa coherencia local       | Local |


La evolución de las métricas refleja una transición conceptual:

- Del énfasis en desviación global (RMSD),
- A medidas normalizadas y más robustas (TM-score),
- Hasta métricas locales independientes de superposición (lDDT).

Cada una responde a una pregunta ligeramente distinta sobre qué significa que dos estructuras “se parezcan”.

Por ello, la elección de la métrica debe alinearse con el objetivo del análisis:

- Comparación de plegamiento global → TM-score.
- Evaluación detallada de calidad estructural → lDDT.
- Medida geométrica clásica → RMSD.

