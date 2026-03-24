# AI Emotion Music Player

This project is a simple AI-based music player that can understand a user’s emotion through a webcam and play music that matches that mood.

The main goal of this project is to make music listening more interactive. Instead of choosing songs manually, the system automatically detects facial expressions and selects suitable music.

---

## Features

- Detects face and emotions in real time using a webcam  
- Recognizes emotions such as happy, sad, angry, neutral, excited, stressed, and thinking  
- Automatically plays music based on the detected mood  
- Uses a predefined song for each emotion  
- Includes a cooldown system to prevent songs from changing too quickly  
- Easy to understand and beginner-friendly project  

---

## Technologies Used

- **Python** – used for writing the main logic of the project  
- **OpenCV** – used to access the webcam and display video frames  
- **FER (Facial Emotion Recognition)** – used to detect emotions from facial expressions  
- **Pygame** – used to play music files  
- **NumPy** – used for handling data and backend processing  

---

## Project Structure
The project is organized in a simple way:

Emotion-Music-Player/  
│  
├── emotion_player.py (main program)  
├── requirements.txt (libraries used)  
├── README.md (project description)  
│  
└── music/  
  ├── happy.mp3  
  ├── sad.mp3  
  ├── angry.mp3  
  ├── neutral.mp3  
  ├── excited.mp3  
  ├── stress.mp3  
  ├── thinking.mp3  
  ├── confidence.mp3  
  ├── romantic.mp3  
  └── relax.mp3  

Each music file represents a specific emotion or mood.

---
=======
##  How to Run
## 🎥 Demo Video

Watch the working demo of the Emotion Music Player here:
https://drive.google.com/file/d/1EZ9o1U3Kb2CYviP0A-sGUIXQDllCnIG0/view?usp=drive_link
###  Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Emotion-Music-Player.git
