import base64
import streamlit as st

# Function to encode the image
def EncodeImage(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')