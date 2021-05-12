import cv2
import numpy as np


def showMessage(text, frame_size=(500, 700)):
    img = np.ones(frame_size) * 255

    text_offset_y = 50
    
    for split_text in text.split('-'):
        cv2.putText(img, split_text, (50, text_offset_y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        text_offset_y += 50
    
    _, jpeg = cv2.imencode('.jpg', img)
    return (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


def img_to_bytes(frame, text):
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

    _, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()
    

def face_extractor(frame, face_classifier):

    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(frame, 1.3, 5)
    
    if faces is (): return None
    
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face = frame[y:y+h+50, x:x+w+50]

    return cropped_face