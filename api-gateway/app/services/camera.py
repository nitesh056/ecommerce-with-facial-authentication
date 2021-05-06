import cv2
import numpy as np
import os
import random
import time
from keras.preprocessing.image import img_to_array
from keras.models import load_model

def run_frame(cam):
    _, img = cam.read()
    imgc = img.copy()

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # cam = cv2.VideoCapture(0)
    cv2.namedWindow("Save New Face")
    img_counter = 0

    # Username
    username = input("Username: ")
    create_folder(username)
    try:
        os.makedirs(os.path.join("saved/train", username))
    except:
        pass
    new_path = os.path.join("saved", username)
    train_path = os.path.join(new_path, "train")
    user_path = os.path.join(train_path, username)

    i, j = 0, 0

    print("Turn your head in different positions and click space bar with every position")
    # TODO: Take pictures for 10 seconds to capture all the sides of the face
    num = 100
    while img_counter < num:
        ret, frame = cam.read()
        cv2.imshow("Save New Face", frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.2, 5)

        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

        # TODO: Make it take pictures automatically
        for x, y, w, h in face:

            # Get face in grayscale
            roi_gray = gray[y:y + h, x:x + w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), 1)
            gray_face = cv2.resize(roi_gray, (128, 128))

            # Capture only 20% of the face

            # Split data in train and test set to be 80%/20%
            if j % 5 == 0:
                cv2.imwrite('saved/test/' + username + '/face_'
                            + username + '_' + str(j) + '.png', gray_face)
            else:
                cv2.imwrite('saved/train/' + username + '/face_'
                            + username + '_' + str(j) + '.png', gray_face)

            j += 1

            os.system("cls")
            print(f"{img_counter+1}/{num} Face Saved!")
            time.sleep(0.1)
            img_counter += 1

    ret, jpeg = cv2.imencode('.jpg', imgc)
    return jpeg.tobytes()