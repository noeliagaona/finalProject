import streamlit as st
from procesar_tiemporeal_mp import mp_en_vivo
import cv2
import pickle #importar el modelo
import numpy as np
import os #trabaja con las rutas del sistema operativo

#devuelve toda la ruta del sistema operativo hasta finalPproject, no hasta dentro
separator = os.path.sep
path_act = os.path.dirname(os.path.abspath(__file__))
dir = separator.join(path_act.split(separator)[:-1])

#especifica la ruta aún más
with open(f'{dir}/modelo/modelo_abecedario.pkl', 'rb') as f:
    model_abc = pickle.load(f)


st.title("Identysigns")
run = st.checkbox('Predice Vocal') #boton mientras que no se le de no se ejecytará lo siguiente
FRAME_WINDOW = st.image([]) #imagen en streamlit
cam = cv2.VideoCapture(0) #instancia de la webcam

while run: #si se la ha dado al boton o no
    _,frame = cam.read() #frame=imagen actual del video
    data = mp_en_vivo(frame) #devuelve los puntos de la imagen del video
    data = np.array(data) #convierte en array
    y_pred = model_abc.predict(data.reshape(-1,63)) #pasamos el modelo para que haga la predicción
    font = cv2.FONT_HERSHEY_SIMPLEX #tipo de letra
    position = (50, 100) #donde aparecerá la letra
    fontScale = 3 #tamaño de la letra
    color = (0, 0, 0) #color en RGB
    thickness = 5 #grosor de la letra
    letter = str(y_pred[0]) #es 0 porque es un array de 1 posicion y solo quiero la letra
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #haciendo la imagen que va a mostrar streamlit
    frame = cv2.putText(frame, letter, position, font, 
                    fontScale, color, thickness, cv2.LINE_AA) #el texto que va a mostrar el streamlit
    FRAME_WINDOW.image(frame) #pintamos la imagen actual del video despues de todas las características que hemos puesto
else: 
    st.write("Has salido de la app") #si el boton no esta puesto
    cam.release()
    cv2.destroyAllWindows() #cierra todo