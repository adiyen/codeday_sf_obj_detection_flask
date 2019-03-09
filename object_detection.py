from imageai.Detection import ObjectDetection
import os, glob

def storage():
    execution_path = os .getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path , "/code/facial-recognition/object_detection/resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()


    path = "/code/facial-recognition/object_detection/static/pics/"
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

    oldest = files[-1]
    print(oldest)
    detections = detector.detectObjectsFromImage(input_image = os.path.join(execution_path , f"/code/facial-recognition/object_detection/static/pics/{oldest}"), output_image_path = os.path.join(f"/code/facial-recognition/object_detection/static/pics/{oldest}"))

    for eachObject in detections:
        # if eachObject["name"] == wanted_item:
        #     print("Found what you were looking for!")
        #     print(eachObject["name"] , " : " , eachObject["percentage_probability"])
        # else:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"])

    