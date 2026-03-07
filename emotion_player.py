import cv2
from fer import FER
import pygame
pygame.mixer.init()
EMOTION_MUSIC = {
    "happy": "music/happy.mp3",
    "sad": "music/sad.mp3",
    "angry": "music/angry.mp3",
    "neutral": "music/neutral.mp3"
}
detector = FER(mtcnn=True)
camera = cv2.VideoCapture(0)
current_emotion = None

print("AI Emotion Music Player Started...")
print("Press 'Q' to exit.")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to access webcam.")
        break
    detected_emotions = detector.detect_emotions(frame)

    if detected_emotions:
        emotion, score = max(
            detected_emotions[0]["emotions"].items(),
            key=lambda item: item[1]
        )

        if emotion != current_emotion and emotion in EMOTION_MUSIC:
            pygame.mixer.music.load(EMOTION_MUSIC[emotion])
            pygame.mixer.music.play(-1) 
            current_emotion = emotion

        cv2.putText(
            frame,
            f"Emotion: {emotion}",
            (40, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("AI Emotion Music Player", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()

print("Application closed.")