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


while True:
     checker, frame = webcam.read()
     
     rgb_frame = frame[:, :, ::-1]
     
     if not checker:
          break

     rostos_conhecidos = []
     nome_dos_rostos = []
     list_face = reconhecer.process(frame)

     if list_face.detections:
          for face in list_face.detections:
               desenho = desing.draw_detection(frame, face)
          for detectar in detector:
               img = DeepFace.detectFace(img_path=imagem, detector_backend= detectar)
               obj = DeepFace.verify(imagem, frame, detector_backend= detectar, enforce_detection=False)
               rostos_conhecidos.append(face)
               nome_dos_rostos.append(imagem)
               
               if obj.get('verified') == True:

                    cv2.putText(frame,f"{nome_dos_rostos} ",(20,450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0), 2)
                    print(nome_dos_rostos)
               else:
                    cv2.putText(frame,"Nao Autenticado",(20,450), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255), 3)
               
               print(obj.get('verified'))




          print('**********')
          

     cv2.imshow('facial recognition', frame)

     if cv2.waitKey(5) == 27:
          break

webcam.release()
cv2.destroyAllWindows()