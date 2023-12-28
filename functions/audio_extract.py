import streamlit as st
import moviepy.editor as mp

def ExtractAudio(varVideoPath):
    try:
        video = mp.VideoFileClip(varVideoPath)
        audio = video.audio
        audiofile = audio.write_audiofile("full_audio.wav")
        return audiofile
    except Exception as e:
        errormessage = st.error(f"Error extracting audio: {str(e)}")
        return None
    
    