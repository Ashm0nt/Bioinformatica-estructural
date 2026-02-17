# Fundamentos estructurales de proteínas

Las **proteínas** son macromoléculas esenciales que convierten la información genética en acción molecular dentro de la célula. Aunque el ADN y el ARN almacenan y transmiten la información, son las proteínas las que *ejecutan* las funciones biológicas.

Para entender cómo realizan estas funciones, es fundamental comprender su **estructura molecular**, ya que la estructura determina su función. En bioinformática, no deben considerarse entidades abstractas, sino moléculas cuya actividad depende directamente de su conformación estructural.


Las **proteínas deben plegarse** en una conformación tridimensional específica y relativamente estable para desempeñar su función biológica. Esta conformación, llamada **estructura nativa**, se mantiene gracias a una red de **interacciones no covalentes**. Cuando se pierde esta estructura tridimensional (desnaturalización o despliegue), generalmente también se pierde la función.

Sin embargo, existen **proteínas intrínsecamente desordenadas (IDPs)** que no presentan una estructura fija en estado libre. Estas pueden:

- Plegarse al unirse a un ligando.
- Formar parte de complejos proteicos.
- Desempeñar funciones importantes sin una estructura rígida estable.

El estudio del plegamiento, el desorden estructural y los cambios conformacionales es fundamental para comprender:

- La relación entre estructura y función.
- Los mecanismos de enfermedades asociadas al mal plegamiento (como los priones).
- El uso de modelos estructurales de proteínas en estudios a gran escala.

## Conformación de las proteínas

Las **proteínas** están formadas por 20 aminoácidos estándar. Cada aminoácido posee:

- Un grupo amino.
- Un grupo carboxilo.
- Un carbono α (Cα) al que se une una **cadena lateral (R)**.

La **cadena lateral R** es la que diferencia a los aminoácidos y determina sus propiedades químicas, influyendo directamente en la estructura y función de las proteínas.

Los aminoácidos se unen mediante **enlaces peptídicos**, formando **cadenas polipeptídicas**. 

### Enlace peptídico

El **enlace peptídico** es el enlace covalente que une aminoácidos en una proteína. Se forma entre:

- El **grupo carboxilo (-COOH)** de un aminoácido.
- El **grupo amino (-NH₂)** del siguiente aminoácido.

Esta reacción es una **reacción de condensación**, ya que se libera una molécula de agua (H₂O). El resultado es un enlace tipo **amida** (-CO–NH-). Algunas de las características del doble enlace son:

1. **Carácter parcial de doble enlace**
   - Debido a la **resonancia**, el enlace C–N del grupo amida tiene carácter parcial de doble enlace.
   - Esto lo hace **más corto y más rígido** que un enlace simple típico.

2. **Planaridad**
   - Los átomos involucrados (Cα–C=O–N–H–Cα) quedan en un mismo plano.
   - Esto restringe la rotación alrededor del enlace peptídico.

3. **Configuración trans predominante**
   - La mayoría de los enlaces peptídicos adoptan configuración **trans**, ya que minimiza la repulsión estérica entre cadenas laterales.
   - Una excepción relevante ocurre con **prolina**, donde la forma cis es más frecuente que en otros aminoácidos.
  
La rigidez del enlace peptídico limita la flexibilidad de la proteína. Además la conformación de la cadena no depende del enlace peptídico en sí (que es plano), sino de la rotación alrededor de los ángulos diedros: **ϕ (phi)** → rotación alrededor del enlace N–Cα y **ψ (psi)** → rotación alrededor del enlace Cα–C. Estas restricciones geométricas son fundamentales para la formación de estructuras secundarias como hélices α y láminas β.

El enlace peptídico define la **estructura primaria** de la proteína. Su estabilidad química permite que las proteínas mantengan su integridad estructural. Al mismo tiempo, puede ser hidrolizado por **proteasas**, permitiendo regulación y degradación controlada.


### Interacciones hidrofóbicas

- Ocurren entre **residuos apolares** en medio acuoso.
- No son una “atracción” directa, sino el resultado del efecto del agua: los grupos hidrofóbicos tienden a agruparse para minimizar la perturbación de la red de puentes de hidrógeno del solvente.
- Son el **principal motor del plegamiento proteico**, promoviendo la formación de un núcleo hidrofóbico interno.

**Importancia estructural:**  
Dirigen el colapso inicial de la cadena polipeptídica y estabilizan la estructura terciaria.


### Interacciones de van der Waals

- Surgen entre átomos no cargados cuando están a distancias muy cortas.
- Se deben a **dipolos instantáneos e inducidos**.
- Son débiles individualmente, pero muy numerosas.

**Importancia estructural:**  
Contribuyen al empaquetamiento preciso del núcleo proteico y a la complementariedad en interacciones proteína–proteína y proteína–ligando.


### Interacciones electrostáticas (puentes salinos)

- Ocurren entre **residuos con carga opuesta** (por ejemplo, cadenas laterales ácidas y básicas).
- Su intensidad depende inversamente de la distancia y del entorno dieléctrico.
- En proteínas se denominan frecuentemente **puentes salinos**.

**Importancia estructural y funcional:**  
- Estabilizan estructuras terciarias y cuaternarias.
- Participan en reconocimiento molecular.
- Son sensibles a cambios de pH e ionicidad.

### Puentes de hidrógeno

- Interacciones direccionales entre un **donador de hidrógeno** (como -NH) y un **aceptor** (como O=C).
- Tienen una longitud y geometría relativamente definidas.
- En proteínas son comunes entre grupos del esqueleto peptídico y entre cadenas laterales polares.

**Importancia estructural:**
- Fundamentales en la formación de **estructura secundaria** (hélices α y láminas β).
- Contribuyen a la especificidad estructural y al reconocimiento molecular.


Las interacciones no covalentes:

- Son reversibles.
- Actúan de manera cooperativa.
- Determinan la estabilidad, dinámica y función de las proteínas.

La estructura nativa de una proteína es el resultado del equilibrio energético entre todas estas interacciones.


## Estructura de Proteínas

La estructura de las proteínas puede analizarse de forma jerárquica en **cuatro niveles**: primaria, secundaria, terciaria y cuaternaria. Cada nivel representa un grado mayor de organización estructural.

### Estructura Primaria
La **estructura primaria** corresponde a la **secuencia lineal de aminoácidos** en una cadena polipeptídica, determinada por la información genética.

- Se representa mediante una secuencia de letras, donde cada letra corresponde a un aminoácido.
- La cadena tiene **direccionalidad**, desde el **extremo amino-terminal (N-terminal)** hacia el **carboxilo-terminal (C-terminal)**.
- Cada aminoácido en la cadena se denomina **residuo**, ya que ha perdido los elementos de agua durante la formación del enlace peptídico.


```
MFSQHNGAAVHGLRLQSLLIAAMLTAAMAM...
```

La estructura primaria es la base de la organización proteica. La secuencia de aminoácidos no solo define la composición química de la proteína, sino que condiciona su plegamiento y, por tanto, su función biológica. [Depende*]


### Estructura secundaria
La **estructura secundaria** describe el plegamiento local y regular del esqueleto peptídico. Se forma para **maximizar los puentes de hidrógeno** entre los grupos polares del backbone (C=O y N–H), lo que estabiliza la cadena.

Este plegamiento es posible gracias a la **rotación alrededor de los ángulos diedros ϕ (phi) y ψ (psi)**, ya que el enlace peptídico es plano y rígido.


#### α-hélice

- Generalmente **dextrógira**.
- Presenta un puente de hidrógeno entre el residuo *i* y el residuo *i+4*.
- Las cadenas laterales apuntan hacia el exterior de la hélice.
- Es una estructura compacta y estable.

#### Lámina β

- Conformación **extendida**.
- Se estabiliza mediante puentes de hidrógeno entre segmentos distintos de la cadena.
- Puede ser:
  - **Paralela**
  - **Antiparalela**
- Las cadenas laterales alternan arriba y abajo del plano de la lámina.

#### Giros y regiones coil

- Permiten cambios de dirección en la cadena.
- Conectan hélices y láminas.
- Algunos giros están estabilizados por puentes de hidrógeno.

#### Clasificación extendida

- **G** → Hélice 3₁₀  
- **H** → Hélice α  
- **I** → Hélice π  
- **T** → Giro estabilizado por puente de H  
- **E** → Hebra β extendida  
- **B** → Puente β  
- **S** → Giro sin puente de H  
- **C** → Otras conformaciones  

Esta asignación se basa en **patrones geométricos y de puentes de hidrógeno**.


#### Diagrama de Ramachandran

Cada tipo de estructura secundaria ocupa regiones específicas en el **diagrama de Ramachandran**, que representa los valores permitidos de los ángulos ϕ y ψ.

- Hélice α → región característica bien definida.
- Lámina β → región distinta, correspondiente a conformación extendida.
- Giros → regiones intermedias.


La estructura secundaria:

- Es el primer nivel de organización tridimensional.
- Surge de restricciones geométricas y energéticas del backbone.
- Contribuye significativamente a la estabilidad global de la proteína.
- Sirve como base para la formación de la **estructura terciaria**.

En resumen, la estructura secundaria refleja cómo la geometría del esqueleto peptídico y los puentes de hidrógeno organizan localmente la cadena polipeptídica.



### Estructura Terciaria

La **estructura terciaria** describe la organización tridimensional completa de una cadena polipeptídica. 

La mayoría de las proteínas se pliegan formando **glóbulos compactos**, compuestos por:

- Elementos de estructura secundaria (hélices α y láminas β).
- Lazos o *loops* que conectan estos elementos.

[Revisar proteínas fibrilares y de membrana]

Durante el plegamiento:

- Las **cadenas laterales hidrofóbicas** tienden a ubicarse en el interior.
- Las regiones más polares y los *loops* suelen quedar expuestos al solvente.

Esta organización minimiza la energía libre del sistema y estabiliza la proteína en medio acuoso.

En casos poco frecuentes, algunas proteínas pueden:

- Formar **nudos topológicos**.
- Agregarse en estructuras fibrilares como **amiloides**.



#### Dominios proteicos

Las unidades globulares de plegamiento se denominan **dominios**.

Un dominio suele caracterizarse por:

- **Autonomía estructural** (puede plegarse independientemente).
- **Autonomía funcional** (realiza una función específica).
- **Historia evolutiva propia**.

Desde la secuencia primaria, un dominio puede identificarse mediante el alineamiento de proteínas que lo contienen.

Las clasificaciones estructurales de proteínas suelen hacerse a nivel de **dominio**, agrupándolos según su arquitectura tridimensional y relaciones evolutivas.

Estas clasificaciones se basan en:

- Organización de elementos secundarios.
- Topología global.
- Patrones de contactos internos.

Algunas propuestas consideran como unidad básica una combinación compacta de elementos de estructura secundaria sostenida por una red de contactos que coevoluciona.


#### Matrices de contacto
La estructura terciaria también puede representarse mediante **matrices de contactos (contact maps)**.

- Son matrices donde ambos ejes representan la secuencia.
- Cada punto indica si dos residuos están en contacto espacial.
- Normalmente se excluyen contactos entre residuos vecinos inmediatos en la secuencia.

Estas matrices permiten:

- Visualizar patrones estructurales.
- Identificar hélices (bandas cercanas a la diagonal).
- Detectar interacciones entre hebras β (patrones característicos fuera de la diagonal).
- Comparar estructuras sin necesidad de superposición tridimensional.


## Alineamientos y superposición 

El trabajo pionero de Chothia y Lesk estableció una relación cuantitativa entre:

- **Conservación de secuencia (estructura primaria)**  
- **Divergencia estructural (estructura terciaria)**  

La observación principal fue que, en general, **a mayor identidad de secuencia, menor divergencia estructural**, aunque esta relación depende de dónde ocurran las mutaciones:

- Mutaciones en el **core (núcleo hidrofóbico)** → mayor impacto estructural.
- Mutaciones en la **superficie** → menor impacto estructural.


### RMSD

La diferencia entre dos estructuras se cuantifica mediante el **RMSD (Root Mean Square Deviation)**, que mide la desviación promedio entre posiciones equivalentes de átomos (usualmente Cα):

\[
RMSD = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( dist(Cα_i^A - Cα_i^B) \right)^2}
\]

Donde:

- \( n \) = número de residuos equivalentes
- \( Cα_i^A \) y \( Cα_i^B \) = coordenadas del carbono alfa en cada proteína

Un RMSD bajo indica estructuras muy similares.

Estudios posteriores demostraron que:

- La **estructura se conserva más que la secuencia** a lo largo de la evolución.
- Es raro que secuencias similares adopten estructuras muy distintas.
- Sin embargo, secuencias con baja identidad pueden conservar el mismo plegamiento.

Esto implica que la estructura es una propiedad evolutivamente más robusta que la secuencia.


### Alineamiento de secuencia

- Compara posiciones en la **estructura primaria**.
- Establece qué residuos ocupan posiciones equivalentes en la secuencia.
- Puede realizarse sin conocer la estructura tridimensional.
- Puede contener errores cuando la identidad es baja.

### Superposición estructural

- Compara posiciones equivalentes en el **espacio tridimensional**.
- Requiere coordenadas atómicas.
- Identifica **residuos equivalentes estructurales**.
- Permite calcular el RMSD.

#### Algoritmos de superposición

Los algoritmos clásicos de superposición estructural:

- Minimizar la distancia cuadrática entre coordenadas equivalentes.
- Utilizar métodos matemáticos como la **descomposición en valores singulares (SVD)**.
- Determinar la rotación y traslación óptimas que alinean ambas estructuras.

Cambios en el alineamiento de secuencia alteran los pares de residuos equivalentes, lo que modifica la superposición y el RMSD resultante.


## Métodos experimentales para estudiar estructura

La estructura tridimensional de las proteínas puede determinarse mediante diversas técnicas experimentales que proporcionan información a distinta resolución y sobre distintos aspectos estructurales y dinámicos.

### 1. Microscopía electrónica (EM)

Especialmente la **crio-microscopía electrónica (crio-EM)**:

- Permite estudiar **grandes complejos proteicos**.
- No requiere cristalización.
- Ha alcanzado resoluciones casi atómicas.
- Es especialmente útil para complejos que no cristalizan fácilmente (por ejemplo, grandes ensamblajes multiproteicos).



### 2. Cristalografía de rayos X

- Proporciona estructuras **estáticas de alta resolución**.
- Requiere cristales de proteína.
- Es el método que históricamente ha producido más estructuras proteicas.
- Las fuentes XFEL permiten estudiar cristales pequeños y proteínas de membrana.

Ventaja: alta precisión atómica.  
Limitación: requiere cristalización y no capta bien la dinámica.



### 3. SAXS (Small-Angle X-ray Scattering)

- No requiere cristales.
- Se realiza en solución.
- Proporciona información de **forma global y tamaño**.
- Muy útil para estudiar **proteínas desordenadas o flexibles**.


### 4. Resonancia Magnética Nuclear (NMR)

- Se realiza en solución.
- Permite estudiar **dinámica molecular**, interacciones y movimientos.
- Genera conjuntos de estructuras compatibles con los datos experimentales.
- Especialmente útil para proteínas pequeñas o medianas.

La comparación entre estructuras obtenidas por NMR y cristalografía muestra que son **complementarias**, revelando diferencias sutiles relacionadas con la dinámica.



### 5. Dicroísmo Circular (CD)

- Técnica rápida y accesible.
- Permite estimar el **contenido de estructura secundaria** (α-hélice, β-lámina).
- No proporciona estructura tridimensional detallada.
- Útil para estudiar cambios conformacionales.



### 6. Espectrometría de masas con entrecruzamiento

- Detecta proximidad espacial entre residuos.
- Proporciona **restricciones estructurales**.
- Muy útil para modelar **complejos proteicos**.



### 7. Aproximaciones indirectas

- Ultrasecuenciación para analizar mutantes y diseñar proteínas.
- Ensayos masivos para identificar regiones desordenadas.
- Métodos de biología molecular que aportan restricciones funcionales y estructurales.

### Repositorios y validación estructural

Las estructuras experimentales se almacenan en el **Protein Data Bank (PDB)**, generalmente en formato PDB.

Cada estructura incluye:

- Coordenadas atómicas.
- Resolución experimental.
- Indicadores de calidad.

Para evaluar calidad estructural se emplean herramientas como:

- Visualización y edición de mapas experimentales.
- Plataformas de validación geométrica y estereoquímica.


### Complementariedad metodológica

- La cristalografía proporciona precisión estructural estática.
- NMR revela flexibilidad y dinámica.
- Crio-EM permite estudiar grandes ensamblajes.
- SAXS describe conformaciones globales en solución.

La comparación entre métodos permite identificar:

- Regiones flexibles.
- Proteínas intrínsecamente desordenadas.
- Cambios conformacionales o cambios de plegamiento.


## PDB

El **Protein Data Bank (PDB)** es el repositorio internacional que almacena las **estructuras tridimensionales de proteínas** (y otras macromoléculas), determinadas experimentalmente.

Cada estructura incluye:

- Coordenadas cartesianas de los átomos.
- Información experimental.
- Indicadores de calidad estructural.


Hasta 2022, el formato estándar fue el **formato PDB**.

Características principales:

- Archivo de texto plano con columnas fijas.
- Cada estructura se identificaba con un código de **4 caracteres** (ej. `1LFU`).
- Registra:
  - Coordenadas atómicas (x, y, z).
  - Ocupancia.
  - **B-factor** (factor de temperatura).
 
#### B-factor (factor térmico)

- Indica el grado de movilidad o desorden de un átomo.
- Valores altos (>50) suelen corresponder a:
  - Regiones flexibles.
  - Superficie expuesta al solvente.
  - Zonas mal definidas en la densidad electrónica.

El formato PDB sigue siendo ampliamente compatible con muchos programas.


### Formato mmCIF (estándar actual)

El estándar actual es **mmCIF (Macromolecular Crystallographic Information File)**.

Ventajas:

- No tiene las limitaciones de columnas fijas del PDB.
- Permite describir **estructuras grandes y complejas**.
- Maneja mejor estructuras cuaternarias con múltiples cadenas.
- Soporta mayor cantidad de metadatos.

Debido al crecimiento del repositorio, los nuevos identificadores siguen un esquema ampliado (ej. `pdb_00001lfu`).

Herramientas como **gemmi** permiten convertir entre formatos PDB y mmCIF.


### Visualización de estructuras proteicas

Los archivos estructurales pueden visualizarse con programas como:

- **PyMOL**
- **Chimera**
- **Jmol**
- **RasMol**

Estos programas permiten:

- Analizar estructura secundaria y terciaria.
- Visualizar dominios.
- Examinar interacciones.
- Inspeccionar B-factors y calidad estructural.

### Coordenadas cartesianas vs coordenadas internas

Las estructuras en PDB/mmCIF se almacenan en **coordenadas cartesianas (x, y, z)**.

Sin embargo, en algunas aplicaciones computacionales se prefieren **coordenadas internas** (ángulos y distancias):

- Más eficientes para simulaciones.
- Útiles para modelado conformacional.
- Permiten manipular directamente ángulos ϕ y ψ.
