import cv2
import mediapipe as mp
from deepface import DeepFace
import matplotlib.pyplot as plt
import face_recognition as fr

webcam = cv2.VideoCapture(0)
reconhecimento = mp.solutions.face_detection
reconhecer = reconhecimento.FaceDetection()
desing = mp.solutions.drawing_utils

detector = ['opencv']
imagem = 'img/joao.jpg'
imagem2 = 'img/aamn.jpg'

while True:
     checker, frame = webcam.read()
     
     rgb_frame = frame[:, :, ::-1]
     
     if not checker:
          break

     rostos_conhecidos = []
     rostos_conhecidos.append(imagem2)
     nome_dos_rostos = []

     list_face = reconhecer.process(frame)

     if list_face.detections:
          for face in list_face.detections:
               desing.draw_detection(frame, face)
               if face in rostos_conhecidos:
                    cv2.putText(frame,f"autenticado {nome_dos_rostos}",(20,450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0), 2)
                    print(nome_dos_rostos)
               else:
                    cv2.putText(frame,"Não Altenticado",(20,450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255), 3)
               



     for detectar in detector:
          obj = DeepFace.verify(imagem, frame, detector_backend= detectar, enforce_detection=False)

          img = DeepFace.detectFace(img_path=imagem, detector_backend= detectar)
          print('**********')
          

     cv2.imshow('facial recognition', frame)

     if cv2.waitKey(5) == 27:
          break

webcam.release()
cv2.destroyAllWindows()