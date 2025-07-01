import cv2

def detect_objects():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return []

    # Placeholder for YOLO/detection pipeline
    return ["Katze", "Hund", "Ball"]  # Simulierte Detektion