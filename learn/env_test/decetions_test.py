import cv2
import supervision as sv
from ultralytics import YOLO

input_path = "learn/env_test/test_photos/test.jpeg"
YOLO_path = "/home/sunsky/codes/Watch_your_way-/yolov8s.pt"

model = YOLO(YOLO_path)
image = cv2.imread(input_path)
results = model(image, verbose=False)[0]

detections = sv.Detections.from_ultralytics(results)

detections