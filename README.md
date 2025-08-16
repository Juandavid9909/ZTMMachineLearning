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


## 2. Datos

Podemos tener diferentes tipos de datos, estructurados (como pueden ser Excel, CSV) y no estructurados (como imágenes, audios, correos).

Los datos estáticos son los datos que no cambian con el tiempo, por ejemplo un Excel donde tenemos registros de pacientes en un formato CSV.

Streaming data es la data que se está actualizando constantemente, usualmente en nuestros modelos empezamos con los datos estáticos y si vemos que nuestro modelo empieza a resolver los problemas correctamente, podemos pasar al streaming.


## 3. Evaluación

Es una métrica para identificar qué tan bien predice el futuro un modelo de Machine Learning. Esto básicamente significa cuál es nuestra precisión mínima, por ejemplo para un proyecto que se encarga de obtener las declaraciones de 2 personas identificar quién causó un accidente, y queremos que nuestra precisión sea del 95%.


## 4. Features - características

Se refiere a los distintos datos estructurados y no estructurados. Esto quiere decir que si tenemos un Excel de pacientes con valores del peso, género, rangos y demás, todos estos serán features que podremos usar, y existen 2 tipos:

- **Características numéricas:** Puede ser por ejemplo el peso.
- **Características categóricas:** Por ejemplo el género del paciente.


## 5. Modelamiento

Podemos encontrar 3 pasos a seguir para modelar:

1. Elegir y entrenar un modelo.
2. Ajustar un modelo.
3. Comparar los modelos.

El concepto más importante en Machine Learning es este, el entrenamiento, la validación y los conjuntos de tests (o 3 sets). Para empezar tenemos nuestros datos al inicio de todo, luego los dividimos en 3 partes, donde la parte más grande será para entrenar nuestro modelo, y otras 2 pequeñas partes iguales que irán destinadas a la validación para que nuestro modelo pueda corroborar que funciona correctamente, y el test para nosotros comprobar los resultados. Esto se puede ver como ver clases, donde los materiales del curso son nuestro conjunto de entrenamiento, el examen de práctica nuestro conjunto de validación, y por último el examen final que es nuestro conjunto de test.

Un ejemplo es tener 100 registros de pacientes, para nuestro entrenamiento podemos usar 70 registros (70-80%), luego usar 15 para la validación (10-15%) y por último otros 15 para el test (10-15%).

### 1. Elegir el modelo
Aquí usamos todos los datos de entrenamiento. Actualmente hay muchos modelos Machine Learning que podemos usar, pero debemos tener en cuenta la clase de datos que tenemos. Por ejemplo, si tenemos datos estructurados (en este caso un arbol de decisión), podemos usar CatBoost como nuestra mejor alternativa, y si tenemos data no estructurada, podemos usar Deep Learning, Neural Networks y Transfer Learning.

Una vez hemos seleccionado nuestro modelo entrenamos nuestro modelo, para esto le pasamos nuestros datos de entrada y el dato de salida esperado.

El objetivo en esta etapa es minimizar los tiempos entre los experimentos, es decir que si tenemos 100.000 datos, para iniciar podemos comenzar con 10.000 y ver qué tal va. A su vez, también afecta el tipo de modelo, ya que por ejemplo los modelos profundos como las redes neuronales toman más tiempo en entrenarse comparado a otros tipos de modelos.

### 2. Ajustar el modelo
Aquí usamos nuestros datos de validación, y podemos ajustarlo con diferentes tipos de datos. Todo esto depende del tipo de algoritmo que estemos usando, por ejemplo si usamos Random Forest, podremos ajustar el número de árboles, y para redes neuronales podemos ajustar el número de capas.

### 3. Comparación de modelos
Aquí se utilizan los datos de prueba, y esto es como el examen final para nuestros modelos. Si dividimos nuestros datos correctamente al inicio del proceso, esto debería darnos una guía de cómo nuestro modelo funcionará una vez lo despleguemos a producción.

Cuando se nos presentan problemas de overfitting y underfitting podemos encontrar las siguientes soluciones:

#### Underfitting
- Intentar con un modelo más avanzado.
- Incrementar los hiperparámetros del modelo.
- Reducir la cantidad de features.
- Entrenar más.

#### Overfitting
- Recolectar más datos.
- Intentar con un modelo menos avanzado.


## 6. Experimentación

Aquí validamos si nuestro modelo puede mejorar para obtener mejores resultados, y de ser así siempre podemos volver de aquí al primer paso hasta obtener los resultados esperados.
