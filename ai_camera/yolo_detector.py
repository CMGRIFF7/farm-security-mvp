from ultralytics import YOLO
import torch.serialization

# Add safe global for YOLO's DetectionModel class
from ultralytics.nn.tasks import DetectionModel
torch.serialization.add_safe_globals({'ultralytics.nn.tasks.DetectionModel': DetectionModel})

model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame)
    names = results[0].names
    detections = [names[int(cls)] for cls in results[0].boxes.cls]
    return detections, results[0].boxes.xyxy.cpu().numpy()
