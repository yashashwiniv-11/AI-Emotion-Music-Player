import cv2
from fer import FER
import pygame

# Initialize music player
pygame.mixer.init()

emotion_music = {
    "happy": "music/happy.mp3",
    "sad": "music/sad.mp3",
    "angry": "music/angry.mp3",
    "neutral": "music/neutral.mp3"
}

cap = cv2.VideoCapture(0)
detector = FER()

current_emotion = None

print("AI Emotion Music Player Started...")
print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect emotion
    result = detector.detect_emotions(frame)

    if result:
        face = result[0]
        emotions = face["emotions"]

        detected_emotion = max(emotions, key=emotions.get)

        (x, y, w, h) = face["box"]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(frame,
                    detected_emotion,
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2)

        if detected_emotion != current_emotion:
            current_emotion = detected_emotion

            if detected_emotion in emotion_music:
                pygame.mixer.music.load(emotion_music[detected_emotion])
                pygame.mixer.music.play()

                print("Detected emotion:", detected_emotion)

    cv2.imshow("Emotion Music Player", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()