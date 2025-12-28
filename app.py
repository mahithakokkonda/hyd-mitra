import os
from flask import Flask, render_template, request, jsonify, send_file
from services.stt import speech_to_text
from services.llm import get_llm_response
from services.tts import text_to_speech
from services.maps import maps_link
from services.maps_utils import needs_map, make_map_link
from services.filter import hyd_filter
import uuid

BASE = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE,"templates"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    audio = request.files["audio"]

    raw_path = os.path.join(BASE, "audio", f"{uuid.uuid4()}.webm")
    wav_path = raw_path.replace(".webm", ".wav")

    audio.save(raw_path)
    os.system(f'ffmpeg -y -i "{raw_path}" -ar 16000 -ac 1 -sample_fmt s16 "{wav_path}"')

    user_text = speech_to_text(wav_path)
    if not user_text.strip():
        user_text = "[వాయిస్ గుర్తించలేకపోయాను]"

    map_url = None   # ← SAFE initialization

    if not hyd_filter(user_text):
        ai_text = "క్షమించండి, నాకు హైదరాబాద్ నగరానికి సంబంధించిన సమాచారమే తెలుసు."
    else:
        ai_text = get_llm_response(user_text)

        if needs_map(user_text):
            map_url = make_map_link(ai_text)

    text_to_speech(ai_text)

    return jsonify({
        "user": user_text,
        "ai": ai_text,
        "audio": "/audio/output.mp3",
        "map": map_url
    })


@app.route("/askText", methods=["POST"])
def ask_text():
    user_text = request.json["text"]
    if not user_text.strip():
        user_text = "[వాయిస్ గుర్తించలేకపోయాను]"

    map_url = None   # ← SAFE initialization

    if not hyd_filter(user_text):
        ai_text = "క్షమించండి, నాకు హైదరాబాద్ నగరానికి సంబంధించిన సమాచారమే తెలుసు."
    else:
        ai_text = get_llm_response(user_text)

        if needs_map(user_text):
            map_url = make_map_link(ai_text)

    text_to_speech(ai_text)

    return jsonify({
        "user": user_text,
        "ai": ai_text,
        "audio": "/audio/output.mp3",
        "map": map_url
    })


@app.route("/audio/output.mp3")
def serve_audio():
    return send_file(os.path.join(BASE, "audio", "output.mp3"))


if __name__ == "__main__":
    os.makedirs(os.path.join(BASE,"audio"), exist_ok=True)
    app.run(debug=False)
