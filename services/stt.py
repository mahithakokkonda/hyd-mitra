import json
import wave
from vosk import Model, KaldiRecognizer

model = Model(r"C:/vosk-model-te/vosk-model-small-te-0.42")

def speech_to_text(audio_file_path):
    wf = wave.open(audio_file_path, "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in (8000,16000):
        import subprocess
        fixed = "audio/fixed.wav"
        subprocess.call([
            "ffmpeg","-y","-i",audio_file_path,
            "-ar","16000","-ac","1","-sample_fmt","s16",fixed
        ])
        wf = wave.open(fixed, "rb")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    final_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part = json.loads(rec.Result()).get("text","")
            final_text += " " + part

    final = json.loads(rec.FinalResult()).get("text","")
    final_text += " " + final

    final_text = final_text.strip()
    print("USER SPOKE:", final_text)   # DEBUG

    return final_text
