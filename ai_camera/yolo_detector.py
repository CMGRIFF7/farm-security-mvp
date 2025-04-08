# ai_camera/yolo_detector.py

from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.modules import Conv
from torch.nn import Sequential, Conv2d, BatchNorm2d, Linear
import torch
import torch.serialization
import cv2

# ✅ Allowlist all required global classes for model unpickling
torch.serialization.add_safe_globals({
    DetectionModel: DetectionModel,
    Conv: Conv,
    Sequential: Sequential,
    Conv2d: Conv2d,
    BatchNorm2d: BatchNorm2d,
    Linear: Linear,
})

model = YOLO("yolov8n.pt")
model.model = torch.load("yolov8n.pt", map_location="cpu", weights_only=False)["model"]

def detect_objects(frame):
    results = model(frame)
    names = results[0].names
    detections = [names[int(cls)] for cls in results[0].boxes.cls]
    return detections, results[0].boxes.xyxy.cpu().numpy()
