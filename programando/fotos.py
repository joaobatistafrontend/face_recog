import face_recognition as fr

from engine import reconhecer_rosto,get_rosto

desconhce = reconhecer_rosto('eu.jpg')
if (desconhce[0]):
     rosto_desconhecido = desconhce[1][0]
     rosto_conhecido, nome_dos_rostos = get_rosto()
     resultados = fr.compare_faces(rosto_conhecido,rosto_desconhecido)
     print(resultados)

     for i in range(len(rosto_conhecido)):
          resultado = resultados[i]
          if(resultado):
               print('rosto do ',nome_dos_rostos[i],'foi reconhecido')


else:
     print('desconhecida')