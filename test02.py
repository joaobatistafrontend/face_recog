import cv2
from deepface import DeepFace
import mediapipe as mp
webcam = cv2.VideoCapture(0)
recognition = mp.solutions.face_detection
recognize = recognition.FaceDetection()
desing = mp.solutions.drawing_utils
img = cv2.imread('eu.jpg')
img2 = cv2.imread('elon.jpg')

models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib", "SFace"]
resul = DeepFace.verify(img,img2, model_name = models[1])
print(resul.get('verified'))










"""facial = DeepFace.verify(img,img2)
print(facial.items())
print(facial.get('verified')) """