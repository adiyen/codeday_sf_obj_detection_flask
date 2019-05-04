import matplotlib; matplotlib.use("Agg")

from imageai.Detection import ObjectDetection
import os, glob

def runner():
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()


    path = "static/pics/"
    files = os.listdir(path)

    oldest = files[-1]
    print(oldest)
    detections = detector.detectObjectsFromImage(input_image = os.path.join(execution_path , f"static/pics/{oldest}"), output_image_path = os.path.join(f"static/pics/{oldest}"))

    for obj in detections:
#         # if eachObject["name"] == wanted_item:
#         #     print("Found what you were looking for!")
#         #     print(eachObject["name"] , " : " , eachObject["percentage_probability"])
#         # else:
        print(obj["name"] , " : " , obj["percentage_probability"])

runner()

# from imageai.Detection import VideoObjectDetection
# import os
# import cv2

# execution_path = os.getcwd()

# camera = cv2.VideoCapture(0)


# detector = VideoObjectDetection()
# detector.setModelTypeAsYOLOv3()
# detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
# detector.loadModel()

# video_path = detector.detectObjectsFromVideo(camera_input=camera,
#     output_file_path=os.path.join(execution_path, "camera_detected_video")
#     , frames_per_second=2, log_progress=True, minimum_percentage_probability=30)

# cv2.imshow(video_path)

# print(video_path)
# def runner():

#     counter = 0
#     while True:
#         ret, img = camera.read()
#         counter+=1
#         cv2.waitKey(100)
#         detections = detector.detectObjectsFromVideo(camera_input = camera)
#         for obj in detections:
#         #     cv2.imwrite("pics/" + str(name) + "." + str(counter) + ".jpg", img)
#             cv2.waitKey(100)
#         #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#         cv2.imshow("Face", img)
#         # k = cv2.waitKey(1)
#         if counter > 50:
#             break

#     cam.release()
# cv2.destroyAllWindows()

# runner()