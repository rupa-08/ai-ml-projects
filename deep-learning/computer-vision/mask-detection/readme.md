# Face Mask Detection System

A real-time **face mask detection** system built using **YOLOv8** and a clean **Streamlit UI**. This project simulates an intelligent monitoring system that can detect if a person is:

- Wearing a mask correctly 
- Not wearing a mask 
- Wearing a mask incorrectly 

When someone is detected wearing a mask correctly, a **beep sound** is played (as a demo alert), showing the system is actively monitoring.

---

## Features

- Detects face mask usage (3 categories).
- Uses YOLOv8 for fast and accurate detection.
- Accepts **Image**, **Video**, and **Webcam** input.
- Plays a **beep sound** when someone is wearing a mask.
- Clean and interactive UI built with **Streamlit**.
- Modular code with separate services for detection and sound.

---

## Dataset Information

Dataset Source: [Kaggle – Face Mask Detection](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection)

### Preprocessing Steps:
- Uploaded dataset to **Roboflow**
- Annotated 3 classes:
  - `with_mask`
  - `without_mask`
  - `mask_worn_incorrectly`
- Exported in **YOLOv8 format**
- Splits:
  - **Train:** 70%
  - **Validation:** 20%
  - **Test:** 10%

---

## Summary

This project helped me apply **computer vision** techniques to a real-world use case. I built this project to:

- Learn and implement **YOLOv8 object detection**
- Build **deployable UI applications** using **Streamlit**
- Simulate a **real-time mask detection system** like those used during the pandemic

---
