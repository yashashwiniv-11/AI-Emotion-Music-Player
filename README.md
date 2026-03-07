# AI Emotion Music Player 

The **AI Emotion Music Player** is a Python-based project that detects a user's facial emotion using a webcam and automatically plays music that matches the detected emotion.

This project combines **Artificial Intelligence, Computer Vision, and Multimedia Processing** to create an interactive music experience.

---

## Features

* Real-time **facial emotion detection**
* Automatic **music playback based on emotion**
* Webcam-based live video processing
* Displays detected emotion on screen
* Supports multiple emotions

Supported emotions:

* Happy 😊
* Sad 😢
* Angry 😠
* Neutral 😐

---

##  Technologies Used

* **Python** – Programming language used to build the project
* **OpenCV** – Captures webcam video and processes frames
* **FER (Facial Emotion Recognition)** – Detects facial emotions
* **Pygame** – Plays music files based on detected emotion
* **MTCNN** – Improves face detection accuracy

---

##  Project Structure

AI-Emotion-Music-Player
│
├── emotion_player.py
├── requirements.txt
├── README.md
│
└── music
    ├── happy.mp3
    ├── sad.mp3
    ├── angry.mp3
    └── neutral.mp3

---

##  Installation

Install the required Python libraries using the following command:

pip install -r requirements.txt

---

## How to Run the Project

Run the following command inside the project folder:

python emotion_player.py

After running:

1. Your webcam will open.
2. The system detects your facial emotion.
3. The program plays music that matches your emotion.

Press **Q** on your keyboard to close the application.

---

## Example Workflow

Step 1: Webcam captures your face
Step 2: Emotion detection model analyzes your facial expression
Step 3: The dominant emotion is detected
Step 4: The system plays the corresponding music

Example mapping:

Emotion → Music Played

Happy → happy.mp3
Sad → sad.mp3
Angry → angry.mp3
Neutral → neutral.mp3

---

## Future Improvements

Possible upgrades for this project:

* Add more emotions (surprise, fear, disgust)
* Create a **Graphical User Interface (GUI)**
* Integrate **Spotify API for online music**
* Build an **Emotion Analytics Dashboard**
* Convert the project into a **desktop application**
* Deploy as a **web application**

---

## Author

Developed by **Veerabomma Yashashwini**.

This project was created as a learning project to explore **Artificial Intelligence, Computer Vision, and Emotion Recognition using Python**.