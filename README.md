# DuckieTesla
Proyecto Duckietown 2022 de conduccion autonoma mediante Reinforcement Learning

**Archivos:**

 - recorder.py : Este programa graba frames y las velocidades de Duckiebot.

 - reader.py : Este programa permite abrir el conjunto de entrenamiento y leerlo.

 - neural.py : Red neuronal convolucional para entrenar el modelo

 - autoduck.py : Este programa permite mover autónomamente el Duckiebot.

## NECESARIO.
Descargar las librerias de TensorFlow y Keras.
## DATA SET.
El data set se crea con los frames y las velocidades respectivas a cada una. Ejecutar recoder.py en el duckiebot y manejar en las calles de Duckietown, este programa ira guardando las imágenes en la capeta Frames y las velocidades respectivas a cada imagen en el archivo vel.txt.
Una vez hecho esto por el tiempo que se estime conveniente, y en su defecto, para que el entrenamiento tenga sentido, probar con intervalos de 3000 a 20000 fotos. Se recomienda que la cantidad de datos sea equitativa entre las tres acciones (avanzar, izquierda, derecha).
Con el data set ya creado se pasa al entrenamiento de la red neuronal.
## ENTRENAMIENTO.
Con el data set listo se debe importar al computador la carpeta con imágenes y el archivo de velocidades
A continuación, dirigirse a reader.py , modificar el path (si no se ha hecho aun) e indicar el número de datos que se quieren procesar en el entrenamiento.
Ahora, dirigirse a neural.py donde se encontrará la estructura de una red neuronal convolucional, la cual fue utilizada para procesar las imágenes asociadas a sus respectivas velocidades. Una capa de convolución es básicamente un preprocesamiento de los frames, haciéndolos pasar por filtros representados por matrices. Así, se aplica una operación matricial a cada mapa de características, generando nuevas imágenes alteradas que servirán para detectar patrones. Aquí se hacen también operaciones como Max-Pooling, que genera una disminución en las dimensiones de la imagen, quedándose con los pixeles más representativos de la imagen en cuestión. Se aplican funciones de activación, como 'relu', que elimina todos los valores negativos dentro los frames, o 'softmax' que entrega una distribución de probabilidad útil para determinar el valor más relevante en la salida de la Red Neuronal.
En el programa neural.py se debe modificar el path y dar un nombre al modelo (modificar nombre_modelo al final de la arquitectura de la red). Ejecutando neural.py (con librería TensorFlow instalada), se debería apreciar en consola como carga el modelo, entrenado con una cantidad de epocas por defecto. Este programa llama a reader.py, que carga los datos a la memoria RAM para ser utilizados en su conjunto. Cuando termine de cargar, se verá el contador epoch 7/7 y un aviso de que el modelo ya esta listo. Ahora tendrá su modelo en la carpeta models listo para ser usado. Es posible que neural.py no cargue completamente si su ordenador no tiene las características suficientes para correr su modelo. Por esto también se recomienda ejecutar neural.py junto con reader.py en un Google Colab con GPU activada, trasladando las carpetas de frames, models y el archivo de texto vel.txt.
Modificar nuevamente el path de autoduck.py y cambiar el nombre al modelo que se creó. Autoduck.py puede ser ejecutado en el duckiebot ya que necesita trabajar con la librería de tensorflow que no está disponible en Python2, por lo que se debe ejecutar en una terminal de un computador que este conectado a duckiebot.
Si todo sale como fue estipulado, al ejecutar autoduck.py se deberían ver los resultados de su modelo, generando la conducción autónoma del duckiebot.
## RECOMENDACIONES. 
Para poder implementar el trabajo de mejor manera se debe contar con ROS2 en el duckiebot que soporte Python3 para poder trabajar con las librerías de tensorflow y keras desde el duckiebot.

