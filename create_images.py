import numpy as np
import cv2 as cv
from pathlib import Path


def crearImagenes():
    letra = input("Que letra quieres agergar? ")
    Path("abecedario"+letra).mkdir(parents=True, exist_ok=True)
    openCam = cv.VideoCapture(0)
    contador = 0
    while(True):
        ret,frame = openCam.read()
        contador = contador+1
        if contador%5==0:
            cv.imwrite(f'abecedario/{letra}/{str(contador)}.png',frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q') or contador > 500:
            break
    openCam.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
        crearImagenes()
    
