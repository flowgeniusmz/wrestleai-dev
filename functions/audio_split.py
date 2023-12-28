import streamlit as st
from pydub import AudioSegment as AS 

def SplitAudio(varAudioFilePath, varSegmentLength=6000):            #6000 = 1 min
    audio = AS.from_wav(varAudioFilePath)
    audiolength = len(audio)
    start = 0
    parts = []
    while start < audiolength:
        end = min(start + varSegmentLength, audiolength)
        chunk = audio[start:end]
        chunkpath = varAudioFilePath.replace(".wav", f"_{start//1000}.wav")
        chunkexport = chunk.export(chunkpath, format="wav")
        parts.append(chunkpath)
        start += varSegmentLength
    return parts
