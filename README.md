# 🧠 MedIntel: Your Smart Medical Assistant

MedIntel is a multimodal medical chatbot powered by **vision and voice** capabilities. It mimics a real-world medical consultation by analyzing medical images and interpreting spoken symptoms to provide human-like diagnoses and advice — all within an intuitive voice interface.

---

## 🩺 Demo Preview

> 🎤 Speak your symptoms  
> 🖼️ Upload a medical image (X-ray, skin rash, broken leg, etc.)  
> 🤖 Get a voice-based medical opinion instantly

---

## 🚀 Features

- **Multimodal LLM (Text + Image + Voice)**  
- **Realistic voice conversations** powered by `gTTS` and `ElevenLabs`
- **Medical image analysis** using **LLaMA 3 Vision**
- **Speech-to-text transcription** using **OpenAI Whisper (via Groq API)**
- **Gradio-powered UI** for seamless web-based interaction

---

## 🧪 Tools & Technologies

| Tool/Framework    | Purpose                                 |
|------------------|------------------------------------------|
| 🧠 Groq           | Fast inference for Whisper + LLaMA 3     |
| 🦻 Whisper        | Speech-to-text (transcription)           |
| 👁️ LLaMA 3 Vision | Medical image analysis (open-source)     |
| 🗣️ ElevenLabs     | Doctor voice generation (realistic TTS)  |
| 🧾 gTTS           | Backup/optional TTS                      |
| 🎛️ Gradio         | Interactive UI                           |
| 🐍 Python         | Core programming language                |
| 💻 VS Code        | Development environment                  |

---

## 📈 Future Improvements

- 🔍 Fine-tune LLaMA Vision for **medical imaging**
- 🌍 Add multilingual capabilities (Nepali, Spanish, Hindi, etc.)
- 💡 Explore **paid LLMs for higher accuracy**

---

## 🧑‍⚕️ Disclaimer

This project is intended for **educational purposes only**. It does **not replace real medical advice**. Please consult a licensed physician for real health concerns.

---

## 🧑‍💻 Run It Locally

```bash
git clone https://github.com/subratppandey/medintel.git
pipenv shell
cd medintel/frontend
python gradio_app.py
