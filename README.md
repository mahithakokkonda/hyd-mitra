HYD-MITRA 🇮🇳
Your Hyderabad Local Telugu Voice Assistant

HYD-MITRA is a real-time Telugu voice assistant that works as a Hyderabad city guide.
It accepts Telugu voice or text input and responds with Telugu voice answers related only to Hyderabad places, food, travel, shopping and tourism.

✨ Features

🎤 Real-time Telugu Voice Input

🧠 Gemini AI Powered Reasoning

🔊 Telugu Voice Output

🏙 Hyderabad-Only Knowledge Domain

💬 Chat Interface + Voice Mode

🗺 Optional Google Maps Redirection

⚡ Fast Hybrid AI Design

🛠 Tech Stack

Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Speech-to-Text: Vosk Telugu Model (Offline)
AI Brain: Gemini 2.5 Flash
Text-to-Speech: Gemini TTS

📂 Project Structure
telugu-hyd-voice-assistant/
│
├── app.py
├── services/
│   ├── stt.py
│   ├── llm.py
│   └── tts.py
├── templates/
│   └── index.html
├── models/
├── audio/
├── requirements.txt
├── .env
└── README.md

🔊 Telugu Speech Model Setup

Download Telugu Vosk Model:

https://alphacephei.com/vosk/models/vosk-model-small-te-0.42.zip

Extract and place the folder inside:

models/vosk-model-small-te-0.42

🔐 Environment Setup

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

▶ Run Locally
pip install -r requirements.txt
python app.py


Open in browser:

http://127.0.0.1:5000
