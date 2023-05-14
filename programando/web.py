import face_recognition as fr
import cv2
import numpy as np
from engine import get_rosto

rostos_conhecidos, nomes_dos_rostos = get_rosto()

video_capture = cv2.VideoCapture(0)
while True:
     ret, frame = video_capture.read()

     rgb_frame = frame[:, :, ::-1]

     localizar_rosto = fr.face_locations(rgb_frame)
     rostos_desconhecidos = fr.face_encodings(rgb_frame,localizar_rosto)

     for(top,right, bottom, left),rostos_desconhecidos in zip(localizar_rosto,rostos_desconhecidos):
          resultados = fr.compare_faces(rostos_conhecidos, rostos_desconhecidos)
          print(resultados)
          
          face_distaces = fr.face_distance(rostos_conhecidos,rostos_desconhecidos)

          melhor_id = np.argmin(face_distaces)
          if resultados[melhor_id]:
               nome = nomes_dos_rostos[melhor_id]
          else:
               nome = 'desconhecido'

          cv2.rectangle(frame, (left,top), (right, bottom), (0,0,255), 2)
          
          cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0,0,255), cv2.FILLED)
          font = cv2.FONT_HERSHEY_SIMPLEX

          cv2.putText(frame, nome, (left + 6, bottom -6), font, 1.0, (255,255,255), 1)

     if cv2.waitKey(5) == 27:
          break

video_capture.release()
cv2.destroyAllWindows()