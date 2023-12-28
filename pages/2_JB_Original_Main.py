import streamlit as st
import plotly
import pandas as pd
import pygwalker as pyg
import tempfile
from IPython.display import display, Image, Audio
import cv2
import base64
import time
#from openai import OpenAI
import os
import requests

#client = OpenAI()
st.write('Welcome to your Athlete Analysis dashboard')

video_files = st.file_uploader("Upload a video file", type=['.mp4', '.avi', '.mov', '.mkv'], accept_multiple_files=True)

for video_file in video_files:
    # Save the uploaded video file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
        tmp_file.write(video_file.read())
        tmp_file_path = tmp_file.name

    # Display the video
    st.video(tmp_file_path)

    # Load the video using OpenCV
    video = cv2.VideoCapture(tmp_file_path)

    # Get the total number of frames
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the slider with the total number of frames as the max value
    frame_number = st.slider('the number of frames listed below are the total number of frames in the video you provided. Scroll for closer inspection.', 0, total_frames - 1, key=video_file.name)

    # Set the video to the selected frame
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = video.read()
    if success:
        # Convert the frame to an image displayable in Streamlit
        _, buffer = cv2.imencode('.jpg', frame)
        st.image(buffer.tobytes(), channels="BGR")

    video.release()


