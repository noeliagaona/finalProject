# Proyecto Final - Identysigns 
 
<p imagen = "center">
  <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7U1MvSoXlaScXdiZFTlML6HOF0oQgayqE1g&usqp=CAU" width = "400">
</p>

Con este proyecto tengo el objetivo de crear y entrenar una red neuronal para la identificación de signos en imagenes en tiempo real de la lengua de signos española. Empezaré con las vocales hasta conseguir el abecedario completo. Uno de los objetivos a medio-largo plazo es poder identificar los signos de videos largos y subtitularlos de manera simultanea.

El dataset creado no se subirá por el gran peso que tiene.

## Problemas que he encontrado:
- No encontrar un dataset que encajara dentro de los parametros que necesitaba, por lo tanto lo cree.
- Instalación de Mediapipe.


Pasos para la realización del proyecto:
+ Crear la conexion con la webcam.
+ Crear el dataset con imagenes generadas a traves de la webcam del ordenador con CV2.
+ Procesar las imagenes.
+ Instalación y procesamiento con Mediapipe.
+ Gracias a las imagenes creamos una archivo csv que nos proporciona unos puntos para poder realizar el entrenamiento.
+ Realizamos el entrenamiento.
+ Se crea el modelo.
+ Procesamos las imagenes en tiempo real.
+ Creación de un Dashboard con Streamlit.



