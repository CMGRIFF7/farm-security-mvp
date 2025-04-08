# ai_camera/yolo_detector.py

import cv2
import torch
from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.modules import Conv
from torch.nn import Sequential, Conv2d, BatchNorm2d, Linear
import torch.serialization

# ✅ Allow trusted classes for safe loading
torch.serialization.add_safe_globals({
    DetectionModel: DetectionModel,
    Conv: Conv,
    Sequential: Sequential,
    Conv2d: Conv2d,
    BatchNorm2d: BatchNorm2d,
    Linear: Linear,
})

# ✅ Load the raw YOLOv8 checkpoint directly
ckpt = torch.load("ai_camera/yolov8n.pt", map_location="cpu", weights_only=False)
model = ckpt["model"]
model.eval()

def detect_objects(frame):
    # ✅ Convert frame to PyTorch format
    img = cv2.resize(frame, (640, 640))
    img = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).float() / 255.0

    with torch.no_grad():
        out = model(img)[0]

    boxes = out.cpu().numpy()
    detections = [str(int(cls)) for cls in out[:, 5]]
    return detections, boxes
