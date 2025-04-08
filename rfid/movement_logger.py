import json
from datetime import datetime

LOG_PATH = "rfid/movement_log.json"

def log_movement(tag_id, timestamp):
    entry = {
        "tag_id": tag_id,
        "timestamp": datetime.fromtimestamp(timestamp).isoformat()
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")