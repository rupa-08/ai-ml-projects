import streamlit as st
from src.service.detection_service import DetectionService
from src.service.audio_service import AudioService
import numpy as np
import cv2
import tempfile

from config import DEFULT_CAMERA


detection_service = DetectionService()
audio_service = AudioService()

st.title("Secure Helmet")
st.subheader("Upload your image/video or use you webcam to detect helmet. If helmet is detected beep sound is produced and atm is locked")

st.sidebar.subheader("Input Settings")

input_type = st.sidebar.radio("Input type", ("Image","Video","Camera"))


def process_image(image):
    frame, detection_classes = detection_service.detect(image)

    if "helmet" in detection_classes:
        # st.error("Helmet detected so atm is locked.")
        audio_service.play_beep()

    return frame

def process_camera(source):
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        st.error("could not open camera")
        return
    
    stframe = st.empty()

    while True:
        ret, frame = cap.read()

        if not ret:
            st.error("Error loading frame.")
            break
        processed_frame = process_image(frame)
        stframe.image(processed_frame, channels="BGR")

    cap.release()
    cv2.destroyAllWindows()

def process_video(file):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(file.read())
    video_path = tfile.name

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        st.error("Error loading video")
        return
    
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            st.error("Error capturing frame.")
            break
        processed_frame = process_image(frame)
        stframe.image(processed_frame, channels="BGR")

    cap.release()
    cv2.destroyAllWindows()

    
if input_type == "Image":

    upload_file = st.sidebar.file_uploader("Upload image: ", type=["jpg","jpeg","png"])

    if upload_file is not None:
        image = np.asarray(bytearray(upload_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        processed_image = process_image(image)
        st.image(processed_image, caption="Processed Image")

if input_type == "Camera":
    camera_source = st.sidebar.text_input("Camera source: ", str(DEFULT_CAMERA))

    camera_source = int(camera_source) if camera_source.isdigit() else camera_source
    process_camera(camera_source)

if input_type == "Video":
    video = st.sidebar.file_uploader("Upload video: ", type=['mov','mp4'])

    if video is not None:
        processed_video = process_video(video)
        st.video(processed_video, caption="Processed Video")