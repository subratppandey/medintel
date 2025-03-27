import os
import logging
import speech_recognition as sr
from pydub import AudioSegment
from groq import Groq
from io import BytesIO
from dotenv import load_dotenv

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step1: Set up audio recorder (ffmpeg & portaudio)

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            recognizer.dynamic_energy_threshold = True
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
                )
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Step2: Set up speech-to-text-STT-model for transcription

audio_file_path = "patient_voice_test.mp3"
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    if not audio_filepath or not os.path.exists(audio_filepath):
        raise FileNotFoundError(f"[ERROR] Audio file not found at path: {audio_filepath}")

    print(f"Opening audio file at: {audio_filepath}")
    
    client = Groq(api_key=GROQ_API_KEY)
    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )

    return transcription.text
