import sys
import os
import gradio as gr

# Added the project root directory to Python path to resolve import issues
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from intel_brain import encode_image, analyze_image_with_query
from patient_voice import record_audio, transcribe_with_groq
from doctor_voice import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt = """
            You have to act as a professional doctor.
            What's in this image? Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. NEVER add any numbers, special characters, symbols and signs in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). 
            No preamble, start your answer right away please."""

def process_inputs(audio_filepath, image_filepath):
    # Handle Gradio audio input as filepath (sometimes dict)
    if isinstance(audio_filepath, dict):
        audio_filepath = audio_filepath.get('name') or audio_filepath.get('path')

    # Check if audio filepath exists
    if not audio_filepath or not os.path.exists(audio_filepath):
        return "No audio recorded", "Please record audio first", None

    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY = os.getenv("GROQ_API_KEY"), 
        audio_filepath = audio_filepath,
        stt_model = "whisper-large-v3"
        )

  # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output, 
            encoded_image=encode_image(image_filepath), 
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "Please provide me an image to analyze"

    voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor

# Create the user interface

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("Temp.mp3")
    ],
    title="MedIntel: Your Reliable AI Doctor"
)

iface.launch(debug=True)

