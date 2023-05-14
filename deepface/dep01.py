from deepface import DeepFace
import matplotlib.pyplot as plt
import time

imagem = 'joao.jpg'
imagem2 = 'aman.jpg'
"""'opencv', 'ssd', """
detctores = ['mtcnn']

for detectar in detctores:
    
     obj = DeepFace.verify(imagem, imagem2, detector_backend= detectar)



     tic = time.time()
     img1 = DeepFace.detectFace(img_path=imagem, detector_backend= detectar)
     img2 = DeepFace.detectFace(img_path=imagem2, detector_backend= detectar)
     toc = time.time()

     plt.imshow(img1)
     plt.show()

     print(obj)
     plt.imshow(img2)
     plt.show()
     print('brackend' , tic-toc, 'segundos')
     print('**********************')
     if(obj.get('verified') == False):
          print('nao atualizado')