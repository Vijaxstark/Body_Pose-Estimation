# 🧍 Pose Estimation Jarvis Assistant

This project uses **MediaPipe** and **OpenCV** to build a real-time pose recognition system that mimics a virtual assistant (like Jarvis). It detects user poses such as "Hands Up", "T-Pose", and "Standing", and optionally triggers actions like launching apps or speaking messages.

## 📌 Features

- Real-time webcam-based pose estimation
- Recognizes poses: Hands Up, T-Pose, and Standing
- Custom actions mapped to each pose
- Text-to-speech support (optional using `pyttsx3`)
- MediaPipe pose detection with OpenCV overlay

## 🔧 How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the script:

```bash
python pose_estimation.py
```

> Make sure your webcam is connected and accessible.

3. (Optional) Enable voice feedback:
   - Uncomment lines related to `pyttsx3` for text-to-speech.

## 🕹️ Pose Actions

| Pose       | Action                                      |
|------------|---------------------------------------------|
| Hands Up   | Greets the user and suggests launching a browser |
| T-Pose     | Activates mock security system              |
| Standing   | No action, idle state                       |

## 🧰 Dependencies

- `mediapipe` for pose estimation
- `opencv-python` for webcam and display
- `numpy` for computations
- `pyttsx3` for text-to-speech (optional)

## 📹 Sample View

Pose annotations and classification are displayed live on webcam feed.

---

**Author**: Vijay Krishna RV  
**Script**: `pose_estimation.py`