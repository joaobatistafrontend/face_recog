import mediapipe as mp
from deepface import DeepFace
import cv2
import os
import time

#base_dir = os.path.dirname(os.path.abspath(__file__))
#image_dir = os.path.join(base_dir, "img")
#listra das img dentro do arquivo 
#list_imgs = os.listdir(image_dir)

webcam = cv2.VideoCapture(0)
reconhecimento = mp.solutions.face_detection
reconhecer = reconhecimento.FaceDetection()
desenho_rosto = mp.solutions.drawing_utils
img = 'img/joao.jpg'
detector_rosto = ['opencv',]

#vai rodar quando a deteccao do rosto for 70%
with reconhecimento.FaceDetection(min_detection_confidence=0.70) as face_detection:
     #como se fosse o if not ret
     while webcam.isOpened():
          ret, frame = webcam.read()
          frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
          resultado = face_detection.process(frame)
          # frame = cv2.resize(frame, (500, 500))
          # start = time.time()
          
          #fazendo a deteccao
          #quantos rosto foi identificado 
          if resultado.detections:
               for id, deteccao in enumerate(resultado.detections):
                    desenho_rosto.draw_detection(frame,deteccao)

                    caixa = deteccao.location_data.relative_bounding_box
                    h, w, c = frame.shape  #porcentagem de deteccao do frame 
                    #mostra quantos % ta sendo detectado o face
                    delimitador = int(caixa.xmin * w), int(caixa.ymin * h), int(caixa.width * w), int(caixa.height * h)
                    cv2.putText(frame, f'{int(deteccao.score[0]*100)}%', (delimitador[0], delimitador[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    
          #fazer um verificador da img com o frame      
          img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          imgconvertida = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
          resultado = reconhecer.process(imgconvertida)
          if resultado.detections:
               for deteccao in resultado.detections:
                    desenhoimg = desenho_rosto.draw_detection(imgconvertida,deteccao)

          obj = DeepFace.verify(imgconvertida, frame)
          print(obj)



          #fazer um verificador da img com o frame
          #for detectar in detector_rosto:
               #obj = DeepFace.verify(img, frame, detector_backend= detector_rosto[0], enforce_detection=False)
               #print(obj)
               #if verificar['']











          # endtime = time.time()
          # totaltime = endtime - start
          # fps = 2 / totaltime
          # cv2.putText(frame, f'FPS: {int(fps)}', (20,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)



          cv2.imshow('facial recognition', frame)
          
          if cv2.waitKey(1) == 27:
               break

webcam.release()
cv2.destroyAllWindows()
