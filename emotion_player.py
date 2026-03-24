import cv2
from fer import FER
import pygame
import os
import time
import random
pygame.mixer.init()
emotion_map = {
    "happy": "happy",
    "sad": "sad",
    "angry": "angry",
    "neutral": "neutral",
    "surprise": "excited",
    "fear": "stressed",
    "disgust": "thinking"
}
cooldown_time = 10
last_song_time = 0
emotion_history = []
history_size = 5
current_song = ""


def play_music(mood):
    global last_song_time, current_song

    current_time = time.time()
    if current_time - last_song_time < cooldown_time:
        return
    music_files = {
         "happy": ["music/happy.mp3"],
         "sad": ["music/sad.mp3"],
         "angry": ["music/angry.mp3"],
         "neutral": ["music/neutral.mp3"],
         "excited": ["music/excited.mp3"],
         "stressed": ["music/stress.mp3"],
         "thinking": ["music/thinking.mp3"]
    }
    if mood not in music_files:
        print("No music available for:", mood)
        return
    song_path = random.choice(music_files[mood])
    if not os.path.exists(song_path):
        print("File not found:", song_path)
        return

    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

        last_song_time = current_time
        current_song = os.path.basename(song_path)

        print(f"Now playing: {current_song} (Mood: {mood})")

    except Exception as e:
        print("Error while playing music:", e)
camera = cv2.VideoCapture(0)
detector = FER()

current_mood = None

print("Emotion Music Player started...")
print("Press Q to quit | P to pause | R to resume")
while True:
    success, frame = camera.read()

    if not success:
        print("Camera not working")
        break
    results = detector.detect_emotions(frame)

    if results:
        face = results[0]
        emotions = face["emotions"]

        detected_emotion = max(emotions, key=emotions.get)
        confidence = emotions[detected_emotion]
        mood = emotion_map.get(detected_emotion, "neutral")
        if confidence < 0.5:
            mood = "neutral"
        x, y, w, h = face["box"]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"{mood} ({round(confidence, 2)})",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )
        emotion_history.append(mood)
        if len(emotion_history) > history_size:
            emotion_history.pop(0)
        stable_mood = max(set(emotion_history), key=emotion_history.count)
        if stable_mood != current_mood:
            print("Stable mood detected:", stable_mood)
            current_mood = stable_mood
            play_music(stable_mood)
    cv2.putText(
        frame,
        f"Playing: {current_song}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )
    cv2.imshow("Emotion Music Player", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('p'):
        pygame.mixer.music.pause()
        print("Music paused")
    elif key == ord('r'):
        pygame.mixer.music.unpause()
        print("Music resumed")
camera.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()

print("Program exited successfully")