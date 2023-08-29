from cv2 import putText,FONT_HERSHEY_SIMPLEX,VideoCapture,imshow,waitKey,destroyAllWindows
from mediapipe import solutions
from deepface.DeepFace import verify,detectFace
'''import matplotlib.pyplot as plt
import face_recognition as fr'''

webcam = VideoCapture(0)
reconhecimento = solutions.face_detection
reconhecer = reconhecimento.FaceDetection()
desing = solutions.drawing_utils

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
               if face:
                    rostos_conhecidos.append(face)
                    #juntar com a img com o codigo do tarcisio
                    nome_dos_rostos.append(imagem)
                    putText(frame,f"{nome_dos_rostos} ",(20,450), FONT_HERSHEY_SIMPLEX,2,(0,255,0), 2)
                    print(nome_dos_rostos)
               else:
                    putText(frame,"Não Altenticado",(20,450), FONT_HERSHEY_SIMPLEX,2,(0,0,255), 3)
               



          

     imshow('facial recognition', frame)

     if waitKey(5) == 27:
          break

webcam.release()
destroyAllWindows()

'''     for detectar in detector:
          obj = verify(imagem, frame, detector_backend= detectar, enforce_detection=False)

          img = detectFace(img_path=imagem, detector_backend= detectar)
          print('**********')'''