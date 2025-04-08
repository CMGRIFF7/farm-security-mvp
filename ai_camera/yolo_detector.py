from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel
import torch.serialization

# ✅ Register the class object, not a string
torch.serialization.add_safe_globals({DetectionModel: DetectionModel})

# Now you can load the model safely
model = YOLO("yolov8n.pt")

def detect_objects(frame):
    results = model(frame)
    names = results[0].names
    detections = [names[int(cls)] for cls in results[0].boxes.cls]
    return detections, results[0].boxes.xyxy.cpu().numpy()
