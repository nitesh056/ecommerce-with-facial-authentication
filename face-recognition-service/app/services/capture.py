import cv2
import os
from glob import glob

from services.misc import img_to_bytes, face_extractor, showMessage
from services.model import create_model

class Capture():
    def __init__(self, username):
        self.count = 1
        self.user_folder = ("0" + str(len(glob('dataset/images/train/*'))))[-2:] + username
        self.face_classifier = cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')
        self.model_created = False

        self.cap = cv2.VideoCapture(0)

        self.create_folder()

    def capture_face(self):
        while True:
            # try:

            if self.count <= 100:
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + self.get_frame() + b'\r\n\r\n')
            else:
                if not self.model_created:
                    self.cap.release()
                    yield showMessage("Capturing Completed!!-Creating model-Please wait...")
                    self.model_created = create_model()
                yield showMessage("Model Created Successfully!!-Reload this page to see the changes")
            # except:
            #     self.cap.release()
            #     self.cap = cv2.VideoCapture(0)


    def get_frame(self):
        _, frame = self.cap.read()

        faces = face_extractor(frame, self.face_classifier)

        if faces is None: return img_to_bytes(frame, "Face not detected")

        face = cv2.resize(faces, (400, 400))

        file_name_path = 'dataset/images/' + ('test/' if self.count % 5 == 0 else 'train/') + self.user_folder + '/' + str(self.count) + '.jpg'
        
        # if self.count % 5 == 0:
        #     file_name_path = 'dataset/images/test/' + self.user_folder + '/' + str(self.count) + '.jpg'
        # else:
        #     file_name_path = 'dataset/images/train/' + self.user_folder + '/' + str(self.count) + '.jpg'

        self.count += 1 if cv2.imwrite(file_name_path, face) else 0

        return img_to_bytes(frame, str(self.count-1))


    def create_folder(self):
        dir_test = 'dataset/images/test/' + self.user_folder
        dir_train = 'dataset/images/train/' + self.user_folder

        if not os.path.exists(dir_test):
            os.makedirs(dir_test)

        if not os.path.exists(dir_train):
            os.makedirs(dir_train)
