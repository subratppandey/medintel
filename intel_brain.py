import os
from dotenv import load_dotenv
import base64
from groq import Groq

load_dotenv()

#Step1: Setup GROQ API key

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#Step2: Convert image to required format: base64

image_path = "hairfall.jpg"
image_file = open(image_path, "rb")

encoded_image = base64.b64encode(image_file.read()).decode('utf-8')








