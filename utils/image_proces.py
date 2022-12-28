import cv2
import mediapipe as mp
import numpy as np 

def process_img(ruta):
    
    # leer imagen de una ruta
    hand_img = cv2.imread(ruta)

    # Procesamiento de imagen
    # 1. Convertir de BGR a RGB
    img_rgb = cv2.cvtColor(hand_img, cv2.COLOR_BGR2RGB)

    # 2. Mueve la imagen al ege Y
    img_flip = cv2.flip(img_rgb, 1)

    # Acceso a MediaPipe de manos
    mp_hands = mp.solutions.hands

    # Inicializar Hands
    hands = mp_hands.Hands(static_image_mode=True,
    max_num_hands=1, min_detection_confidence=0.7) # Margen de error

    # Resultados
    output = hands.process(img_flip)

    hands.close() # Cerramos Mediapipe porque ya no lo necesitamos

    try:

        #Limieza de los datos

        data = output.multi_hand_landmarks[0] 
        print(data)

        data = str(data)

        data = data.strip().split('\n')

        delete = ['landmark {', '}']

        keep = []

        for i in data:
            if i not in delete:
                keep.append(i)

        clean = []

        for i in keep:
            i = i.strip()
            clean.append(i[2:])

        for i in range(0, len(clean)):
            clean[i] = float(clean[i])

        return(clean)

    except:

        # Sino devuelve un array de 0
        return(np.zeros([1,63], dtype=int)[0])

if __name__ == "__main__":
    process_img()
















