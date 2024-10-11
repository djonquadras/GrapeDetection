from roboflow import Roboflow
import os

rf = Roboflow(api_key="pqWmEUd47vLlriKYHQXr")
project = rf.workspace("grappes-detection").project("grapes-detection-g36ar")
version = project.version(3)
dataset = version.download("yolov5")


if not os.path.exists('yolov5/runs/detect'):
    os.makedirs('yolov5/runs/detect')


if not os.path.exists('yolov5/runs/train'):
    os.makedirs('yolov5/runs/train')


