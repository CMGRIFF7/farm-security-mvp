import cv2

def capture_frame():
    # ✅ Use test image if camera not available
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise Exception("Camera not available")
        ret, frame = cap.read()
        cap.release()
        return frame if ret else None
    except:
        return cv2.imread("test_image.jpg")  # Add this image to your repo
