# 🛡️ ATM Secure Helmet Detection System

A real-time helmet detection system using YOLOv8 integrated with Streamlit UI. This project simulates an ATM security system where access is **denied (ATM locked)** and a **beep sound** is played if a person is detected **wearing a helmet**.

## Features

- Detects helmets using YOLOv8 model.
- Supports **image**, **video**, and **webcam** input.
- Automatically plays a beep and displays lock message if helmet is detected.
- Clean and interactive **Streamlit UI**.
- Modular structure with separate services for detection and audio.

## Use Case

In ATMs or secure areas, users must remove helmets for facial verification. This system:
- Scans incoming frames from webcam/video/image.
- Detects presence of helmet.
- If a helmet is detected:
  - Plays a **beep sound**.
  - Simulates ATM **lock** for access denial.

## UI Input Options

| Input Type | Description                    |
|------------|--------------------------------|
| Image      | Upload an image for detection. |
| Video      | Upload a video for frame-wise detection. |
| Camera     | Use your webcam for live detection. |