import os
import subprocess
from cartesia import Cartesia
from dotenv import dotenv_values


def speak(text):
    config = dotenv_values(".env")


    client = Cartesia(api_key=config["CARTESIA_API_KEY"])

    data = client.tts.bytes(
        model_id="sonic-preview",
        transcript="One way to think about the function e to the t is to ask what properties does it have?",
        voice_id="3790cf58-070e-48ec-8dbe-6a037065b413",  # Barbershop Man
        # You can find the supported `output_format`s at https://docs.cartesia.ai/api-reference/tts/bytes
        output_format={
            "container": "wav",
            "encoding": "pcm_f32le",
            "sample_rate": 44100,
        },
    )
    with open("sonic.wav", "wb") as f:
        f.write(data)

    # Play the file
    subprocess.run(["ffplay", "-autoexit", "-nodisp", "sonic.wav"])