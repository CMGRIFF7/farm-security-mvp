from flask import Flask, jsonify, request
from flask_socketio import SocketIO
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
from time import time, localtime

from notifier import send_alert
from alert_engine import should_trigger_alert
from ai_camera.camera_stream_handler import capture_frame
from ai_camera.yolo_detector import detect_objects
from rfid.movement_logger import log_movement
from rfid.rfid_reader_interface import read_rfid_tag
from rfid.geofence_logic import is_within_allowed_hours

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/api/assets")
def get_assets():
    with open("rfid/asset_registry.json") as f:
        return jsonify(json.load(f))

@app.route("/api/logs")
def get_logs():
    path = "rfid/movement_log.json"
    if not os.path.exists(path):
        return jsonify([])
    with open(path) as f:
        logs = f.readlines()
        return jsonify([json.loads(line) for line in logs])

@app.route("/api/simulate", methods=["GET"])
def simulate_rfid_event():
    tag_id, timestamp = read_rfid_tag()
    log_movement(tag_id, timestamp)

    socketio.emit("asset_update", {"tag_id": tag_id, "timestamp": timestamp})
    socketio.emit("log", f"Simulated movement for tag {tag_id}")

    if not is_within_allowed_hours(localtime(timestamp)):
        try:
            frame = capture_frame()
            detected_classes, _ = detect_objects(frame)
        except Exception as e:
            print("[WARNING] Frame capture or detection failed:", e)
            detected_classes = []
            frame = None

        if should_trigger_alert(tag_id, timestamp, detected_classes):
            send_alert(tag_id, frame)
            socketio.emit('alert', {
                "tag_id": tag_id,
                "detections": detected_classes
            })
            return {"status": "ALERT", "tag_id": tag_id, "detections": detected_classes}

    return {"status": "OK", "tag_id": tag_id}

@socketio.on('connect')
def handle_connect():
    print("[Socket] Client connected")

@socketio.on("disconnect")
def on_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)

