# Estructura Cuaternaria

La **estructura cuaternaria** es el nivel de organización proteica en el que **dos o más cadenas polipeptídicas (subunidades)** se ensamblan para formar un complejo funcional.  
La estructura cuaternaria describe cómo **varias moléculas interactúan entre sí** para desempeñar una función biológica.

Estas interacciones pueden ser:

- Proteína–proteína  
- Proteína–DNA  
- Proteína–ligando  

En la célula, las proteínas rara vez actúan de forma aislada. Su estado funcional habitual suele ser **formando complejos moleculares**, lo que convierte a la estructura cuaternaria en un nivel crucial para entender la función biológica.

## Interfases Moleculares

Una **interfaz molecular** es la región específica de contacto entre dos moléculas que interactúan.  
No implica toda la superficie de la proteína, sino un conjunto particular de residuos que:

- Establecen contactos físicos
- Determinan especificidad
- Permiten reconocimiento molecular

- El reconocimiento de ligandos por receptores (como en inmunoglobulinas).
- La unión de factores de transcripción a secuencias reguladoras del DNA.


### Conservación 

Como ya se ha mencionado anteriormente la **estructura tridimensional se conserva más que la secuencia** a lo largo de la evolución. Este tipo de análsis de relaciones entre la secuencia y estrutura se extendió posteriormente a las interfases molecualres. Al estudiar las interfaces proteína–proteína y observaron patrones similares: las regiones implicadas en interacción tienden a estar evolutivamente conservadas.  Estudios posteriores encontraron tendencias análogas en interfaces proteína–DNA.

Las interfaces moleculares están sometidas a presión evolutiva porque son esenciales para la función.  Si una mutación altera significativamente una interfaz crítica, la interacción puede perderse y con ello la función biológica. Por esta razón, muchas regiones de interfaz muestran grados importantes de conservación estructural.

A partir de los estudios sobre conservación estructural, se ha propuesto una generalización importante:

> **Proteínas con secuencias similares tienden a formar interfaces similares cuando participan en complejos.**

Esto significa que si dos proteínas están evolutivamente relacionadas (son homólogas), no solo conservarán en muchos casos su plegamiento global, sino también la manera en que interactúan con otras moléculas.

### Diseño de proteínas

Estas observaciones han servido como base para desarrollar algoritmos de:

- Predicción de interacciones proteína–proteína
- Modelado de complejos
- Diseño racional de interfaces

Muchos métodos de diseño estructural parten de la idea de que, si conocemos cómo interactúa una proteína con su socio, podemos:

- Modificar residuos en la interfaz para cambiar afinidad.
- Rediseñar especificidad.
- Crear nuevas interacciones artificiales.

Esto es especialmente relevante porque gran parte de las funciones biológicas dependen de interacciones moleculares:
- Señalización celular
- Regulación génica
- Respuesta inmune
- Ensamblaje de complejos macromoleculares

### Limitaciones

Sin embargo, centrarse únicamente en la interfaz es una simplificación.

La función de una proteína no depende solo del "parche" de contacto, sino también de:

- Su estabilidad global.
- Su dinámica conformacional.
- Cambios alostéricos.
- Regulación postraduccional.

En algunos casos, mutaciones alejadas de la interfaz pueden tener efectos funcionales más importantes que cambios directos en la región de contacto.


## Optimización de cadenas laterales en interfaces

Cuando dos proteínas tienen **alta similitud de secuencia**, es razonable asumir que su **esqueleto peptídico (backbone)** no cambia drásticamente.  

Si el backbone se mantiene relativamente fijo, entonces podemos centrarnos en lo que sí cambia con facilidad: 
> **Las cadenas laterales (side chains)**

Esto permite rediseñar proteínas modificando únicamente las cadenas laterales para alterar:

- Estabilidad
- Afinidad por un ligando
- Actividad enzimática
- Especificidad de reconocimiento

Un **rotámero** es una conformación preferente de la cadena lateral basada en ángulos torsionales χ (chi).
El backbone restringe qué rotámeros son posibles, pero las cadenas laterales aún pueden rotar dentro de ciertos estados energéticamente favorables.

### Diseño basado en rotámeros

El procedimiento general consiste en:

1. Seleccionar posiciones en la interfaz.
2. Mutarlas de manera sistemática.
3. Para cada mutación, explorar una **biblioteca de rotámeros**.
4. Evaluar cuál conformación es energéticamente más favorable.

La lógica es:

> Si cambio residuos en la interfaz y optimizo sus rotámeros, puedo modificar la afinidad sin alterar el esqueleto global.

#### SCWRL

- Mantiene fijo el backbone (ángulos ϕ y ψ).
- Explora rotámeros de una biblioteca derivada del PDB
- Selecciona la combinación de cadenas laterales con menor energía y menor choque estérico.

Más particular:

- Toma la geometría local.
- Considera las conformaciones de residuos vecinos.
- Evalúa combinaciones posibles de rotámeros.
- Devuelve la configuración más probable.
- Se puede hacer mutagénesis también, y se recalculan los rotámeros 


Aunque podría asumirse que la geometría del esqueleto proteico se ve poco afectada al cambiar rotámeros, estudios previos muestran que el muestreo de cadenas laterales puede inducir pequeños cambios conformacionales locales.

Estos cambios pueden modelarse mediante el algoritmo *backrub* , que introduce ajustes locales del esqueleto para acomodar nuevas conformaciones laterales.

## Interacciones no covalentes: puentes de hidrógeno en la interfaz

El estudio experimental y teórico de las interacciones proteína–proteína (*protein–protein interactions*) ha sido clave para comprender los mecanismos que determinan la especificidad del reconocimiento molecular. 

Este reconocimiento es un proceso termodinámico complejo donde intervienen múltiples factores de afinidad y especificidad. Sin embargo, en muchas interfaces los protagonistas principales son los **puentes de hidrógeno**, cuya formación depende directamente de la secuencia (estructura primaria), ya que no todos los aminoácidos pueden actuar como donadores o aceptores.

la geometría del esqueleto peptídico o de la doble hélice de DNA varía muy poco cuando se sustituyen un número reducido de cadenas laterales o bases. No solo es necesario muestrear conformaciones, sino también **evaluar la especificidad del reconocimiento en las interfaces modeladas**, por ejemplo estimando la formación de puentes de hidrógeno.

### Puentes de hidrógeno

Un **puente de hidrógeno (H-bond)** es una interacción no covalente direccional que ocurre cuando:

- Un átomo electronegativo actúa como **donador (D)** y está covalentemente unido a un hidrógeno.
- Otro átomo electronegativo cercano actúa como **aceptor (A)**.
- El hidrógeno participa en la interacción: D–H···A.

En proteínas y complejos proteína–DNA, los átomos más comunes involucrados son **N** y **O**.


### Criterios geométricos

Para identificar computacionalmente un puente de hidrógeno se utilizan criterios geométricos, ya que la mayoría de los archivos PDB no contienen información energética explícita.

Los parámetros más habituales son:

1. **Distancia donador–aceptor (D–A):**  
   Generalmente ≤ 3.5 Å.

2. **Distancia hidrógeno–aceptor (H–A):**  
   Generalmente ≤ 2.5–2.7 Å.

3. **Ángulo D–H···A:**  
   Debe ser cercano a la linealidad (≥ 120°–150°).  
   Cuanto más próximo a 180°, más fuerte y direccional es el puente.

Estos criterios reflejan que los puentes de hidrógeno son interacciones altamente **direccionales**, no simples contactos por proximidad.


### Importancia en interfaces proteína–DNA

En complejos como el de **dnaA–DNA (PDB: 1J1V)**, los puentes de hidrógeno:

- Contribuyen a la **afinidad** del complejo.
- Determinan la **especificidad de secuencia**, ya que ciertos aminoácidos pueden reconocer bases concretas mediante patrones complementarios de donadores y aceptores.
- Estabilizan la orientación correcta del dominio proteico sobre el DNA.

Por ejemplo:

- La guanina ofrece múltiples sitios aceptores y donadores en el surco mayor.
- Aminoácidos como Arg, Lys, Asn o Gln pueden establecer redes específicas de H-bonds con estas bases.


### Evaluación computacional

Programas como HBPLUS identifican puentes de hidrógeno evaluando automáticamente:

- Distancias interatómicas.
- Ángulos geométricos.
- Tipos de átomos involucrados.

Este análisis permite comparar:

- Interfaces experimentales.
- Modelos estructurales generados por mutagénesis.
- Cambios en la red de interacciones tras sustituciones de residuos.



### Consideración termodinámica

Aunque los puentes de hidrógeno son clave para la especificidad, su contribución a la estabilidad global depende también de:

- El entorno (solvatación).
- Efectos cooperativos.
- Reorganización estructural local.

Por ello, no basta con contar puentes de hidrógeno: es importante analizar su geometría y contexto estructural.


## Interfaces entre proteína, DNA y RNA: endonucleasas CRISPR-Cas guiadas por RNA

En algunos casos no es necesario modelar una interfaz molecular desde cero, sino comprender su arquitectura para diseñar experimentos de edición genética. Este es el caso de las endonucleasas CRISPR-Cas, herramientas de edición genómica que resultan, en general, más sencillas de utilizar que tecnologías previas como TALEN o las nucleasas con dominios Zinc Finger (ZFN).

Estos sistemas se han empleado, por ejemplo, para inducir mutaciones heredables en loci específicos de plantas, incluso en especies poliploides como el trigo panadero (Wang et al., 2014; Lawrenson et al., 2015).


### Arquitectura de la interfaz proteína–DNA–RNA

Las endonucleasas Cas (Stella, Alcon y Montoya, 2017) son proteínas grandes, de más de 1000 aminoácidos, que forman un complejo ternario con:

- La proteína Cas
- El RNA guía (sgRNA)
- El DNA diana

La especificidad del sistema no depende únicamente de complementariedad de secuencia, sino también de la arquitectura estructural de la interfaz.

Un elemento esencial es el **PAM (Protospacer Adjacent Motif)**:

- Secuencia corta de 3–5 nucleótidos.
- Debe estar adyacente a la región diana.
- Es reconocida directamente por la proteína Cas.
- Sin PAM correcto, no ocurre el corte.

El reconocimiento ocurre en varias etapas:
1. Unión inicial al PAM.
2. Desenrollamiento local del DNA.
3. Hibridación del RNA guía con la hebra complementaria.
4. Activación conformacional del dominio catalítico.
5. Corte de ambas hebras.


### Especificidad y efectos fuera de objetivo

Además del diseño bioinformático de la secuencia guía (buscando regiones únicas en el genoma), es necesario evaluar:

- La tasa de cortes fuera de objetivo (*off-target*).
- Qué regiones del sgRNA son más sensibles a desajustes.
- La estabilidad de la hibridación RNA–DNA.

Estudios experimentales in vitro e in vivo han mostrado que ciertas posiciones del RNA guía toleran mismatches, mientras que otras son críticas para la actividad catalítica (Cisse, Kim y Ha, 2012; Zheng et al., 2017).


### Modelado y dinámica molecular

Además de estructuras cristalográficas y de cryo-EM, se han empleado modelos de dinámica molecular para estudiar:

- Cambios conformacionales tras reconocimiento del PAM.
- Flexibilidad del complejo.
- Mecánica del proceso de corte.

Estos estudios permiten entender cómo pequeñas variaciones en secuencia pueden afectar la eficiencia y especificidad del sistema (W. Zheng, 2017).


Las endonucleasas CRISPR-Cas representan un ejemplo paradigmático de interfaz proteína–DNA–RNA altamente regulada, donde:

- La secuencia,
- La estructura tridimensional,
- Y la dinámica conformacional

actúan de manera integrada para garantizar reconocimiento específico y corte preciso.


## Modelando interfaces moleculares por homología

Las observaciones estructurales previas permiten estudiar u optimizar una interfaz molecular tomando como referencia la estructura de moléculas similares. Este enfoque, conocido como **modelado por homología**, se basa en la conservación estructural entre proteínas evolutivamente relacionadas.

Existen múltiples herramientas para modelar interfaces proteína–proteína o proteína–DNA:

- Herramientas simples como InterPreTS o PPI3D, que mantienen fija la geometría del molde.
- Protocolos más complejos que incluyen refinamiento por *docking*.
- Herramientas especializadas como InteractomeINSIDER (mutaciones asociadas a enfermedad).
- Métodos de diseño estructural como los utilizados en ingeniería de anticuerpos.

### Fundamento conceptual

En el contexto de interfaces proteína–proteína o proteína–DNA:

- Los residuos que participan en el reconocimiento suelen estar parcialmente conservados.
- La geometría global del complejo tiende a mantenerse.
- Las diferencias en secuencia pueden traducirse en cambios en interacciones específicas (puentes de hidrógeno, interacciones electrostáticas, contactos hidrofóbicos).

El modelado por homología permite:

- Transferir la geometría del complejo molde.
- Conservar la disposición relativa de las moléculas.
- Evaluar cómo mutaciones o variaciones afectan la red de interacciones.

### Tipos de herramientas

Existen distintos enfoques para modelar interfaces:

- **Modelado rígido:**  
  Se mantiene la geometría del complejo molde sin modificar el acoplamiento.

- **Modelado con refinamiento:**  
  Se permiten ajustes locales en cadenas laterales o regiones flexibles.

- **Docking estructural:**  
  Se recalcula el acoplamiento completo entre moléculas.

- **Herramientas especializadas:**  
  Algunas se centran en mutaciones asociadas a enfermedades o en diseño de anticuerpos.


## Modelado de interfaces moleculares mediante docking

Cuando no disponemos de una estructura molde para aplicar modelado por homología, el estudio de interfaces moleculares requiere explorar directamente cómo interactúan dos macromoléculas. Este problema se aborda mediante **docking molecular**.

El docking intenta predecir la pose (orientación y posición relativa) que adoptan dos moléculas cuando forman un complejo.

### Complejidad del problema

El docking es computacionalmente costoso porque:

- Existen múltiples grados de libertad (rotaciones, traslaciones y flexibilidad interna).
- Muchos átomos pueden moverse simultáneamente.
- El espacio conformacional crece exponencialmente.

Para reducir este coste, los algoritmos emplean estrategias de optimización como:

- Uso de transformadas rápidas de Fourier (FFT) para explorar orientaciones.
- Simplificación energética inicial (scoring grueso).
- Muestreo jerárquico (búsqueda global seguida de refinamiento local).


### Tipos de docking

1. **Docking rígido**  
   Ambas moléculas se consideran cuerpos rígidos.

2. **Docking semirrígido**  
   Se permiten ajustes en cadenas laterales o regiones flexibles.

3. **Docking flexible**  
   Se consideran cambios conformacionales significativos.

4. **Docking enzima–sustrato**  
   Caso particular donde la información funcional o genómica (por ejemplo, operones) puede ayudar a restringir el espacio de búsqueda.

### Evaluación de los modelos

El resultado de un protocolo de docking es un conjunto de posibles complejos.  
Cada pose se evalúa mediante funciones de puntuación (*scoring functions*) que consideran:

- Complementariedad geométrica.
- Interacciones electrostáticas.
- Contactos hidrofóbicos.
- Puentes de hidrógeno.
- Energía estimada del complejo.

Sin embargo, no todas las poses con buena puntuación son biológicamente relevantes.  
La interpretación requiere:

- Conocimiento estructural.
- Información funcional previa.
- Análisis comparativo.


### Validación y benchmarking

Desde 2001 existe el experimento colectivo **CAPRI** (Critical Assessment of PRedicted Interactions), donde distintos grupos evalúan sus algoritmos prediciendo complejos cuya estructura experimental aún no ha sido publicada.

CAPRI funciona como un banco de pruebas independiente para comparar:

- Precisión estructural.
- Capacidad de discriminación.
- Robustez de los algoritmos

#### Idea clave

El docking no garantiza encontrar la interfaz “correcta”, sino que genera hipótesis estructurales plausibles.  

Su éxito depende de:

- La calidad del muestreo.
- La función de puntuación utilizada.
- El análisis experto posterior.

Por ello, el docking es tanto un problema computacional como interpretativo.

# AlphaFold3

AlphaFold3 (AF3) representa una evolución sustancial respecto a AlphaFold2 (AF2). Mientras AF2 revolucionó la predicción de estructuras proteicas individuales, AF3 amplía el alcance hacia complejos moleculares completos y adopta un enfoque generativo más directo.

## Cambios principales respecto a AF2

### 1. Soporte para múltiples tipos de moléculas

AF3 no se limita a proteínas. Puede modelar:

- Proteínas
- ADN
- ARN
- Pequeños ligandos
- Iones y cofactores

Esto permite predecir directamente:

- Estructuras cuaternarias
- Interfaces proteína–proteína
- Interfaces proteína–ADN
- Interfaces proteína–ARN
- Complejos proteína–ligando

AF3 ya no es solo un predictor de plegamiento, sino un modelo de ensamblaje molecular.


### 2. Menor dependencia de alineamientos múltiples (MSA)

AF2 dependía fuertemente de información evolutiva extraída de alineamientos múltiples de secuencias (MSA).

AF3:

- Reduce el procesamiento intensivo de MSA.
- Se apoya más en aprendizaje profundo directo.
- Puede trabajar mejor en casos con baja señal evolutiva.

Esto lo hace más robusto para proteínas con pocos homólogos conocidos.

### 3. Predicción directa de coordenadas atómicas

AF2 trabajaba sobre representaciones internas basadas en:

- Residuos
- Marcos locales
- Restricciones geométricas

AF3 introduce un **módulo de difusión generativa**, que:

- Modela directamente la distribución tridimensional de átomos.
- Genera coordenadas atómicas completas.
- No necesita reconstruir cadenas laterales como paso posterior.

En lugar de “plegar” una proteína paso a paso, AF3 aprende a **generar la estructura completa como una muestra coherente en 3D**.


## Pipeline
### Entrada multimolecular

AF3 recibe:

- Secuencias proteicas
- Secuencias de ADN o ARN
- Información de ligandos
- Opcionalmente MSA

Todo se codifica en una representación conjunta del sistema.

No trata cada molécula por separado, sino que construye una representación integrada desde el inicio.


### Embedding estructural unificado

Las moléculas se convierten en vectores en un espacio latente compartido.

Este embedding captura:

- Relaciones espaciales potenciales
- Compatibilidad química
- Información evolutiva (cuando existe)
- Contexto multimolecular

Es como crear un “mapa probabilístico” del complejo antes de que exista en 3D.



### Modelo generativo por difusión

Aquí está la gran innovación.

AF3 utiliza un **modelo de difusión**, similar a los usados en generación de imágenes:

1. Se parte de una nube de átomos en posiciones casi aleatorias.
2. El modelo aprende a eliminar progresivamente el “ruido”.
3. En cada paso refina posiciones atómicas.
4. Converge hacia una estructura físicamente coherente.

En términos simples:

AF2 optimizaba una estructura.
AF3 **la genera**.

Es un cambio de paradigma: de predicción determinista a modelado probabilístico generativo.


### Evaluación interna y confianza

El modelo produce:

- Coordenadas atómicas completas
- Métricas de confianza estructural
- Estimaciones de precisión en interfaces

Esto permite evaluar qué regiones del complejo son más fiables.

