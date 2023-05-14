import threading
import cv2
from deepface import DeepFace


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
"""TAMANHO DO QUADRADO DA CAPTURA"""
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

contador = 0
face_metch = False

img_referencia = cv2.imread("eu.jpg")
"""vai verificar se o fame da camera é uma copia da img"""
def check_face(frame):
    global face_metch
    try:
        if DeepFace.verify(frame,img_referencia.copy())['verified']:
            print(frame.get('verified'))

            face_metch = True
        else:
            face_metch = False
    except ValueError:
        pass

while True:
    retorn,frame = cap.read()
    if retorn:
        if contador % 30 == 0:
            try:
                threading.Thread(target=check_face,args=(frame.copy(),)).start()
            except ValueError:
                pass
        contador += 1

        if face_metch:
            cv2.putText(frame,"Autenticado",(20,450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,"N Autenticado",(20,450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)

        cv2.imshow('Video',frame)

    key = cv2.waitKey(1)
    if cv2.waitKey(5) == 27:
        break



cv2.destroyAllWindows()