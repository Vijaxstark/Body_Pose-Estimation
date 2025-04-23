import cv2
import mediapipe as mp
# import pyttsx3  # Optional: you can uncomment this to use TTS
import numpy as np
import time
import os

# Initialize text-to-speech (optional)
# engine = pyttsx3.init()
last_pose = None
last_speak_time = 0

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Voice assistant function (optional)
def speak(text):
    global last_speak_time
    if time.time() - last_speak_time > 3:
        print(f"Jarvis says: {text}")
        # engine.say(text)
        # engine.runAndWait()
        last_speak_time = time.time()

# Classify pose from key landmarks
def classify_pose(landmarks):
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

    # Hands above shoulders
    if left_wrist.y < left_shoulder.y and right_wrist.y < right_shoulder.y:
        return "Hands Up"

    # T-pose: wrists aligned horizontally with shoulders
    if abs(left_wrist.y - left_shoulder.y) < 0.1 and abs(right_wrist.y - right_shoulder.y) < 0.1:
        return "T-Pose"

    return "Standing"

# Action for each pose (mocked)
def perform_action(pose_label):
    if pose_label == "Hands Up":
        speak("Hello, boss. I would launch your browser now.")
        print("[ACTION] Would launch browser (e.g., Chrome).")

    elif pose_label == "T-Pose":
        speak("Activating security mode.")
        print("[ACTION] Would trigger security system (placeholder).")

    elif pose_label == "Standing":
        print("[ACTION] No specific action. Standing idle.")

# Start Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip and convert image
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        landmarks = results.pose_landmarks.landmark
        current_pose = classify_pose(landmarks)

        # Display current pose
        cv2.putText(frame, f'Pose: {current_pose}', (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Trigger action if pose changed
        if current_pose != last_pose:
            perform_action(current_pose)
            last_pose = current_pose

    cv2.imshow('Jarvis Pose Assistant', frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
