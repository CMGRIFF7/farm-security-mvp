def match_rfid_to_detection(tag_id, detected_classes):
    return any(cls in detected_classes for cls in ["person", "vehicle"])