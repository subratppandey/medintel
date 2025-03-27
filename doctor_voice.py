import os
import elevenlabs
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from gtts import gTTS
import subprocess
import platform

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Step1: Set up text-to-speech-model (gTTs)

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )

    audioobj.save(output_filepath)

# Step1b: Set up text-to-speech-model with ElevenLabs

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.generate(
        text = input_text,
        voice = "Aria",
        output_format = "mp3_22050_32",
        model = "eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)

# Step 2: Use Model for text output to voice

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )

    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

elevenlabs_input_text = "I am your good doctor, always ready to help!"

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.generate(
        text = input_text,
        voice = "Aria",
        output_format = "mp3_22050_32",
        model = "eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

