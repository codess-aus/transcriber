from moviepy.editor import *

video_file = r"C:\Users\codess-aus\Downloads\DevBoxSH.mp4"
output_file = r"C:\Users\codess-aus\Downloads\DevBoxSH.wav"

# Load the video clip 
video = VideoFileClip(video_file)

# Extract the audio from the video
audio = video.audio

# Set the desired audio parameters
audio_params = {
    "codec": "pcm_s16le",
    "fps": 16000,  # Set the desired sampling rate: 16000 Hz
    "nchannels": 1,  # Mono audio
    "bitrate": "16k"  # Set the desired bitrate
}

audio.write_audiofile(output_file, codec=audio_params["codec"], fps=audio_params["fps"], nbytes=2, bitrate=audio_params["bitrate"])
