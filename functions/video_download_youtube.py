from pytube import YouTube
import streamlit as st

def DownloadYoutubeWav(url, save_path):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    downloaded_video = video_stream.download(output_path=save_path)
    return downloaded_video

def DownloadYoutubeMP4(url, save_path):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path=save_path)
    return save_path + yt.title + ".mp4"  # Assuming the downloaded file