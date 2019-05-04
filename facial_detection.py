import face_recognition
import cv2

def test():
    print("True")

    # path = "static/pics/"
    # os.chdir(path)
    # files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

    # oldest = files[-1]
    # print(oldest)
    # detections = detector.detectObjectsFromImage(input_image = os.path.join(execution_path , f"/code/facial-recognition/object_detection/static/pics/{oldest}"), output_image_path = os.path.join(f"/code/facial-recognition/object_detection/static/pics/{oldest}"))

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    faces = face_cascade.detectMultiScale("obama.jpg", 1.3, 5)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle("static/pics/obama.jpg", (x, y), (x+w, y+h), (255, 0, 0), 2)

