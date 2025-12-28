import os
import asyncio
import edge_tts

VOICE = "te-IN-ShrutiNeural"

async def _speak(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("audio/output.mp3")

def text_to_speech(text):
    os.makedirs("audio", exist_ok=True)
    asyncio.run(_speak(text))
