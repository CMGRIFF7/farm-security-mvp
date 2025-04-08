import cv2

def capture_frame():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Camera not accessible")
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None