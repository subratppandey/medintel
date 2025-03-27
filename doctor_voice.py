import os
import elevenlabs
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from gtts import gTTS

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Step1: Set up text-to-speech-model (gTTs)

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )

    audioobj.save(output_filepath)

input_text = "Hi, this is your friend Subrat Pandey"
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_test.mp3")

# Step1b: Set up text-to-speech-model with ElevenLabs

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.generate(
        text = input_text,
        voice = "Aria",
        output_format = "mp3_22050_32",
        model = "eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_test.mp3")

# Step 2: Use Model for text output to voice



