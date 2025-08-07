import os
import re
import subprocess
from pytube import YouTube  # optional, if converting to public link
import requests
from moviepy.editor import VideoFileClip
import whisper

def download_drive_file(drive_url, destination):
    # Extract the file ID
    file_id_match = re.search(r'/d/([^/]+)/', drive_url)
    if not file_id_match:
        raise ValueError("Can't parse file ID from the Drive URL")
    file_id = file_id_match.group(1)
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(destination, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded to {destination}")

def extract_audio(video_path, audio_path):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    clip.close()
    print(f"Extracted audio to {audio_path}")

def transcribe_audio(audio_path, model_size="base"):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    DRIVE_URL = "https://drive.google.com/file/d/1z_kxaAvqMfLtL1kJSHxGW-8-IFkCbJzx/view?usp=sharing"
    VIDEO_PATH = "input_video.mp4"
    AUDIO_PATH = "extracted_audio.wav"

    download_drive_file(DRIVE_URL, VIDEO_PATH)
    extract_audio(VIDEO_PATH, AUDIO_PATH)
    transcript = transcribe_audio(AUDIO_PATH, model_size="base")
    print("Transcript:\n", transcript)
