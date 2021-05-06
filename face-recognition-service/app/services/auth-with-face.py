

def authWithFace(user_id):
    # check for existing users in saved folder
    if len(os.listdir("saved/train")) == 0:
        print("There are no existing users.")
    # TODO: It only works with username "amine". FIX IT
    new_path = os.path.join("saved", "nitesh")
    test_path = os.path.join(new_path, "test")
    print(new_path)
    print(test_path)
    
    # train the model on those images
    classifier = "haarcascade_frontalface_default.xml"
    model = "model_face.h5"
    
    def get_label():
        label = os.listdir("saved/train")
        return label
    
    def get_legend(class_arg):
        label_list = get_label()
        # get label from prediction
        label = label_list[class_arg]
        # create color from each label
        coef = float(class_arg + 1)
        color = coef * np.asarray((20,30,50))
        return color, label
    
    def process_face(roi_gray):
        # resize input model size
        roi_gray = cv2.resize(roi_gray, (128, 128))
        roi_gray = roi_gray.astype("float") / 255.0
        roi_gray = img_to_array(roi_gray)
        roi_gray = np.expand_dims(roi_gray, axis=0)

        return roi_gray
    
    # load haarcascade face classifier
    print("Loading cascade classifier...")
    face_cascade = cv2.CascadeClassifier(classifier)
    # Keras model was trained using the iPython Notebook
    print("Loading Keras model")
    model = load_model(model)

    """
    Open the webcam recognize the face.
    If face recognized print Access Granted.
    Else if face not recognized after 10 seconds Quit and Print
    Access not granted
    """
    # The program will quit when clicking ESC
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Recognizing Face...")

    # clear Terminal
    os.system('cls')
    time.sleep(2)
    print("Recognizing face...")
    img_counter = 0
    #prediction = 0
    # TODO: Change 120 to 10
    t_end = time.time() + 10
    # Run this loop for 10 seconds
    access = False
    # while time.time() < t_end and access != True:
    while True:
        ret, frame = cam.read()
        cv2.imshow("Testing existing Face", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        threshold = 0.5
        # Get faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            roi_face = gray[y:y + h, x:x + w]
            roi_face = process_face(roi_face)
            prediction = model.predict(roi_face)
            print(prediction[0][0])            

            # Get label and color from prediction
            color, label = get_legend(np.argmax(prediction))

            cv2.putText(frame, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            # if(prediction[0][0] >= threshold):
            #     print(prediction[0][0])
            #     print("Access Granted. Welcome!")
            #     access = True
            #     break        
        
            
    if (time.time() > t_end and prediction[0][0] < threshold):
        print("Access Denied.\nFace Not Recognized")
    cam.release()
    cv2.destroyAllWindows()