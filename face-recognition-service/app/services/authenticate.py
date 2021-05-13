import cv2
import os
from glob import glob
from PIL import Image
from keras.applications.vgg16 import preprocess_input
import base64
from io import BytesIO
import json
import random
from keras.models import load_model
import numpy as np

from keras.preprocessing import image

from services.misc import img_to_bytes, face_extractor, showMessage

class FacialAuth():
    def __init__(self, username):
        self.count = 1

        self.username = username
        self.user_index = -1
        for folder_name in glob('dataset/images/train/*'):
            if username == folder_name[23:]: self.user_index = int(folder_name[21:23]) - 1
        
        self.face_classifier = cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')
        self.model = load_model('model/facefeatures_new_model.h5')

        self.cap = cv2.VideoCapture(0)


    def auth(self):
        if self.user_index < 0: return showMessage("Dataset not found for this user")
        while True:
            # try:
                

            if self.count <= 10:
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + self.get_frame() + b'\r\n\r\n')
            else:
                self.cap.release()
                yield showMessage("Authentication completed-Redirecting...", (480, 700))
            # except:
            #     self.cap.release()
            #     self.cap = cv2.VideoCapture(0)

    def get_frame(self):
        _, frame = self.cap.read()

        face = face_extractor(frame, self.face_classifier)

        if face is None: return img_to_bytes(frame, "Face not detected")
    
        try:
            name = self.check_face(face)
        except:
            name = "Unknown person"

        return img_to_bytes(frame, name)

    def check_face(self, face):
        face = cv2.resize(face, (224, 224))
        im = Image.fromarray(face, 'RGB')
        
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)
        pred = self.model.predict(img_array)
        
        if(int(pred[0][self.user_index] * 100000) == 100000):
            self.count += 1
            return self.username

        return "Unknown person"