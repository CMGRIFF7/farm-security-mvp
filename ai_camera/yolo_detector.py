from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel
from ultralytics.nn.modules import Conv
from torch.nn import Sequential, Conv2d, BatchNorm2d, Linear
import torch
import torch.serialization

# ✅ Allowlist trusted global classes for model unpickling
torch.serialization.add_safe_globals({
    DetectionModel: DetectionModel,
    Conv: Conv,
    Sequential: Sequential,
    Conv2d: Conv2d,
    BatchNorm2d: BatchNorm2d,
    Linear: Linear,
})

# ✅ Explicitly set weights_only=False for PyTorch >= 2.6 compatibility
model = YOLO("yolov8n.pt", task="detect")
model.model = torch.load("yolov8n.pt", map_location="cpu", weights_only=False)["model"]
