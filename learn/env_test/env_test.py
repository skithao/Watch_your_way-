import cv2
import supervision as sv
from ultralytics import YOLO

input_path = "learn/env_test/test_photos/test.jpeg"
output_path = "learn/env_test/result_outputs/test_annotated.jpeg"

# 加载图像和模型
image = cv2.imread(input_path)
model = YOLO('yolov8s.pt')

# 进行目标检测
result = model(image)[0]
detections = sv.Detections.from_ultralytics(result)

# 可视化结果
detections
box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(
    scene=image.copy(),
    detections=detections
)

# 保存结果
cv2.imwrite(output_path, annotated_frame)

# 显示结果
cv2.imshow("Result", annotated_frame)
cv2.waitKey(0)
