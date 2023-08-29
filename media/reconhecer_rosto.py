import cv2
import mediapipe as mp
reconhecimento = mp.solutions.face_detection
reconhecer = reconhecimento.FaceDetection()
desenho_rosto = mp.solutions.drawing_utils
img = 'img/joao.jpg'
img = cv2.imread(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgconver = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
resultado = reconhecer.process(imgconver)
if resultado.detections:
    for deteccao in resultado.detections:
        desenho_rosto.draw_detection(imgconver,deteccao)
cv2.imshow('facial recognition', imgconver)
          
cv2.waitKey()