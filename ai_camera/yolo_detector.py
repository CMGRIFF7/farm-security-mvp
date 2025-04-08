from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.modules import Conv
from torch.nn import Sequential, Conv2d, BatchNorm2d, Linear
import torch.serialization

# ✅ Allowlist trusted globals required for YOLOv8
torch.serialization.add_safe_globals({
    DetectionModel: DetectionModel,
    Sequential: Sequential,
    Conv2d: Conv2d,
    BatchNorm2d: BatchNorm2d,
    Linear: Linear,
    Conv: Conv,
})

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame)
    names = results[0].names
    detections = [names[int(cls)] for cls in results[0].boxes.cls]
    return detections, results[0].boxes.xyxy.cpu().numpy()
