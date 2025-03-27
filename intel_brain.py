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

client = Groq()
query = "is there something wrong with my head?"
model = "llama-3.2-90b-vision-preview"

messages=[
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

print(chat_completion.choices[0].message.content)





