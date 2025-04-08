import json
import os
from datetime import datetime

LOG_DIR = "ai_camera/logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_detection(tag_id, detections):
    log_entry = {
        "tag_id": tag_id,
        "detections": detections,
        "timestamp": datetime.now().isoformat()
    }
    with open(os.path.join(LOG_DIR, "detections.log"), "a") as f:
        f.write(json.dumps(log_entry) + "\n")