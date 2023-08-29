import mediapipe
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('joao.jpg')
mp_face_detection = mediapipe.solutions.face_detection
face_detector = mp_face_detection.FaceDetection(min_detection_confidence = 0.6)
resulta = face_detector.process(img) 
resultado = resulta.detections
print(resultado)