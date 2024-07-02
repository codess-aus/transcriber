import azure.cognitiveservices.speech as speechsdk
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up the Azure Speech configuration using environment variables
speech_key = os.getenv("SPEECH_KEY")
service_region = os.getenv("SERVICE_REGION")
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

audio_file = os.getenv("AUDIO_FILE_PATH")

# Set up the audio configuration
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

#Create a speech recognizer object
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

#create an empty list to store the transcription results
transcriptions = []

#define an event handler for continuous recognition
def continuous_recognition_handler(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        transcriptions.append(evt.result.text)

#start continuous recognition
speech_recognizer.recognized.connect(continuous_recognition_handler)
speech_recognizer.start_continuous_recognition()

#wait for the recognition to complete
timeout_seconds = 600
timeout_expiration = time.time() + timeout_seconds

# Adjust the sleep duration as needed
while time.time() < timeout_expiration:
    time.sleep(1)

#stop continuous recognition
speech_recognizer.stop_continuous_recognition()

# Combine transcriptions into a single string
transcription = ' '.join(transcriptions)

# Write the transcription to a file
output_file = "transcription.txt"
with open(output_file, "w") as file:
    file.write(transcription)

print("Transcription saved to: " + output_file)
