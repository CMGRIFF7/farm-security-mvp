from ai_camera.event_matcher import match_rfid_to_detection

def should_trigger_alert(tag_id, timestamp, detected_classes):
    return match_rfid_to_detection(tag_id, detected_classes)