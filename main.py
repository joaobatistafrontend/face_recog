import math
import face_recognition
import cv2
import os, sys
import numpy  as  np

def face(distancia,limite_corespondente=0.6):
     faixa = (1.6 - limite_corespondente)
     linha = (1.0 - limite_corespondente) / (faixa * 2.0)


     if distancia> limite_corespondente:
          return str(faixa(linha * 100, 2)) +'%'
     else:
          valor = (linha + ((1.0 - linha) * math.pow((linha - 0.5) * 2, 0.2))) * 100
          return str(faixa(valor, 2)) + '%'

class reconhecimento:
     face_localizadas = []
     face_codificadas = []
     face_nomes = []
     face_conhecidas = []
     nomes_conhecidos = []
     processar_quadro = True

     def __int__(self):
        self.codificar_face()

     def codificar_face(self):
          for imagem in os.listdir('img'):
               face_img = face_recognition.load_image_file(f'img/{imagem}')
               reconhecer_rosto = face_recognition.face_encodings(face_img)[1]

               self.face_conhecidas.append(reconhecer_rosto)
               self.nomes_conhecidos.append(imagem)
          print(self.nomes_conhecidos)

     def reconhecer():
          webcam = cv2.VideoCapture(0)

          if not webcam.isOpened():
               sys.exit('Video nao encontrado...')

          while True:
               quadro, frame = webcam.read()

               if self.processar_quadro:
                    redirecionar_quadro = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
                    rgb_frame = redirecionar_quadro[:, :, :: - 1]

               self.face_localizadas = face_recognition.face_locations(rgb_frame)
               self.face_codificadas = face_recognition.face_encodings(rgb_frame, self.face_localizadas)

               self.face_nomes = []
               for facesCodificadas in self.face_codificadas:
                    metcher = face_recognition.compare_faces(self.faces_conhecidas, facesCodificadas)
                    nome = 'desconhecido'
                    autorizado = 'desconhecido'

                    distancia_facial = face_recognition.face_distance(self.faces_conhecidas,facesCodificadas)
                    index_sublinhado = np.argmin(distancia_facial)

                    if metcher[index_sublinhado]:
                         nome = self.nomes_conhecidos[index_sublinhado]
                         autorizado = face


reconhecimento()