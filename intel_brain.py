import os
from dotenv import load_dotenv
import base64
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def encode_image(image_path):
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

query = "is there something wrong with my head?"
model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq()  
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]

    chat_completion = client.chat.completions.create(
        messages = messages,
        model = model
    )

    return chat_completion.choices[0].message.content


