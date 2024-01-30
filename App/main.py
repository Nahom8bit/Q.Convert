import streamlit as st
from moviepy.editor import VideoFileClip
import os
import tempfile

st.title('Video to Audio Converter')
st.subheader('Upload a video file to convert it to audio.')
uploaded_file = st.file_uploader("Choose a video file", type=['mp4', 'avi', 'webm', 'ogv', 'flv', 'mov', 'mkv'])

if uploaded_file is not None:
    video = VideoFileClip(uploaded_file)
    audio = video.audio
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        audio.write_audiofile(tmp.name)
        audio_filename = tmp.name
    st.markdown("Download the audio file [here]({})".format(os.path.abspath(audio_filename)))
    os.remove(audio_filename)
else:
    st.warning("Please upload a video file.")