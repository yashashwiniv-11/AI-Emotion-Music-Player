import cv2
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not access the camera.")
    exit()

print("Camera started successfully. Press 'q' to quit.")
while True:
    success, frame = camera.read()

    if not success:
        print("Failed to capture image from camera.")
        break
    cv2.imshow("Camera Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()