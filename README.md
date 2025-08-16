# Cheat Sheet de Python

Toda la documentación sobre Python la podremos encontrar [aquí](https://zerotomastery.io/cheatsheets/python-cheat-sheet/).


# ¿Qué es Inteligencia Artificial?

Es el gran padre de todos los conceptos, y básicamente es una máquina que actúa como un humano.


## Narrow AI

Son esas máquinas que pueden hacer una cosa muy bien, no son muy buenas en tareas múltiples.


## Machine Learning

Es un subconjunto de IA, y es una técnica de inteligencia artificial implementada en sistemas que pueden encontrar patrones basados en un conjunto de datos. Es la ciencia de hacer que las máquinas actúen sin programarlas de forma explícita. Es permitir a las máquinas tomar decisiones sobre los datos.

### Tipos de Machine Learning
- **Supervisado:** La data que recibimos tiene categorías, y esta categorización es denominada **clasificación**, por ejemplo si estamos categorizando manzanas y peras. Por otra parte, tenemos **regresión**, el cual está basado en datos continuos como pueden ser años de experiencia para contratar ingenieros y demás.
- **No supervisado:** Cuando nuestros datos no tienen labels o grupos, este tipo de Machine Learning es muy usado, y tenemos 2 tipos, primero el **clustering** donde creamos grupos (o los crea la máquina por nosotros) para hacer el proceso, y también tenemos el **aprendizaje de reglas de asociación** donde asociamos por ejemplo diferentes cosas para predecir lo que un cliente podría comprar en el futuro.
- **Reforzado:** Es básicamente enseñarle a la máquina a través de prueba y error, mediante recompensas y castigos. Por ejemplo un programa que aprende un juego mientras intenta millones de veces hasta que obtiene el puntaje más alto.


## Deep Learning - Deep Neural Networks

Es una técnica para implementar Machine Learning, usando varias capas de aprendizaje para llevar a un objetivo.


## Data Science

No tiene una clara diferencia con el Machine Learning, ya que su definición es el análisis de datos, buscando data útil para después hacer algo con ella.


# ¿Cómo se trabajará el proceso de desarrollo?

Para nuestros proyectos de Machine Learning seguiremos la siguiente línea:

1. Recolección de datos.
2. Modelamiento de datos.
	1. **Definición del problema:** ¿Cuáles son los problemas que intentamos resolver?
	2. **Datos:** ¿Qué datos tenemos?
	3. **Evaluación:** ¿Qué define el éxito de nuestro modelo?
	4. **Características:** ¿Qué características debemos modelar?
	5. **Modelamiento:** ¿Qué tipo de modelo deberíamos usar?
	6. **Experimentos:** ¿Qué hemos intentado y qué más podemos intentar?
3. Despliegue.


## 1. Definición del problema

No siempre funciona usar Machine Learning para solucionar un problema, para saber si lo solucionará debemos hacernos la siguiente pregunta:

- ¿Funcionará un sistema simple basado en instrucciones codificadas a mano?

Si esto es afirmativo, tal vez no necesitemos hacer trabajo demás en modelar un modelo de Machine Learning para cumplir con la tarea.

### Aprendizaje supervisado
Es llamado así porque tenemos datos y etiquetas, ya que el modelo de Machine Learning tratará de usar los datos para predecir la etiqueta (label), y si se equivoca lo intentará nuevamente hasta que acierte.

- **Clasificación:** Es básicamente predecir si algo es una cosa u otra, por ejemplo si queremos predecir si un paciente podrá (o no) tener un paro cardíaco basado en sus registros médicos, o qué tipo de raza de perro tenemos en una imagen la clasificación es la ruta que usaremos. Si tenemos sólo 2 opciones, es llamado clasificación binaria, y si tenemos muchas opciones tenemos clasificación multiclase. Para predecir el paro cardíaco tenemos una clasificación binaria ya que nuestras opciones son sí o no. Y para el ejemplo de las razas es una clasificación multiclase ya que hay muchísimas razas de perro.
- ** Regresión:** Se encargan de predecir un valor numérico, usualmente dicen que es un número continuo, por ejemplo podríamos intentar predecir el valor de una casa basado en la cantidad de habitaciones, área, cantidad de baños.

### Aprendizaje no supervisado
Es cuando tenemos datos pero no etiquetas, y entonces debemos proveer las etiquetas para hacer la clasificación, por ejemplo si queremos encontrar qué personas usarían ropa de verano, pero no tenemos etiquetas, lo que hacemos es clasificar nuestra ropa en ropa de verano y ropa de invierno, y con base a esto el modelo clasificará e intentará ver en qué lugar de la clasificación entraría una persona basado en sus compras verificando características en común.

### Transferencia de aprendizaje
Este aprovecha lo que un modelo de Machine Learning ha aprendido en otro modelo de Machine Learning, por ejemplo, digamos que estamos intentando predecir qué raza de perro aparece en una foto, y supongamos que tenemos un modelo que se encarga de validar el tipo de carro hay. ¿Por qué sería esto útil? Porque puede ser una tarea muy costosa el encontrar patrones en los datos, y aunque hace una clasificación distinta el punto es que cumple con una función parecida y el principio fundamental es el mismo, entonces podemos usar este modelo y usar estos patrones para nuestro problema de la raza de los perros.

### Aprendizaje reforzado
Se enfoca en tener un programa de computadora ejecutando algunas acciones en un espacio definido, y dándole un premio si lo hace bien o dar un "castigo" si lo hace mal. Esto puede ser por ejemplo un modelo para jugar ajedrez, y darle un punto positivo cada que gana una partida, y un punto negativo cada que pierde, ya que el objetivo de nuestro modelo será maximizar el puntaje obtenido.
