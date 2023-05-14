import face_recognition as fr


def reconhecer_rosto(url_ft):
     foto = fr.load_image_file(url_ft)
     rostos = fr.face_encodings(foto)
     if (len(rostos) > 0):
        return True,rostos
     
     return False,[]
def get_rosto():
     rostos_conhecidos = []
     nome_dos_rostos = []
     joao1 = reconhecer_rosto('eu.jpg')
     if (joao1[0]):
          rostos_conhecidos.append(joao1[1][0])
          nome_dos_rostos.append('joao')

     elon = reconhecer_rosto('elon.jpg')
     if (joao1[0]):
          rostos_conhecidos.append(elon[1][0])
          nome_dos_rostos.append('elon')
     
     return rostos_conhecidos,nome_dos_rostos