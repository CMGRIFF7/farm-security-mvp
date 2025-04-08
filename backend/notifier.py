import cv2
import os

ALERT_IMAGE_DIR = "alerts"
os.makedirs(ALERT_IMAGE_DIR, exist_ok=True)

def send_alert(tag_id, image=None):
    print(f"[ALERT] Asset ID {tag_id} triggered an alert.")
    if image is not None:
        filepath = os.path.join(ALERT_IMAGE_DIR, f"{tag_id}_{int(time())}.jpg")
        cv2.imwrite(filepath, image)
        print(f"Alert image saved to {filepath}")