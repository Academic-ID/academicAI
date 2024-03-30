import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
import requests
from elevenlabs.client import ElevenLabs
from elevenlabs import save, play
import time
import json

from config import ELEVEN_API_KEY

client = ElevenLabs(
  api_key=ELEVEN_API_KEY
)

CHUNK_SIZE = 1024

async def get_voice_id(desired_voice):
    if desired_voice == '' or desired_voice is None:
        return 'itSbi8no4w0rxFMKGz5o'
    # set_api_key(ELEVEN_API_KEY)
    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": ELEVEN_API_KEY
    }
    response = requests.get(
        'https://api.elevenlabs.io/v1/voices', headers=headers)
    
    voices = response.json()['voices']
    
    voice_id = next((voice['voice_id']
                    for voice in voices if voice['name'] == desired_voice), None)
    
    if voice_id is None:
        voice_id = desired_voice
    
    return voice_id

async def get_audio(text, DESIRED_VOICE):
    voice_id = await get_voice_id(DESIRED_VOICE)
    audio = client.generate(text=text, model='eleven_multilingual_v2', voice=voice_id)
    play(audio)
    timestamp = time.strftime('%Y_%m_%d--%H_%M_%S')

    if not os.path.exists('generated voice'):
        os.makedirs('generated voice')

    save(audio, f'generated voice/{timestamp}.mp3')

    json_filename = "generated voice/00. Generated voice record.json"

    if not os.path.exists(json_filename):
        with open(json_filename, 'w') as f:
            f.write('[]')

    # Load existing data
    with open(json_filename, 'r') as f:
        try:
            data = json.load(f)
            # Ensure data is a list
            if not isinstance(data, list):
                data = [data]
        except json.JSONDecodeError:
            data = []

    # Append new data
    data.append({'prompt': text,
                 'filename': f'generated voice/{timestamp}.mp3',
                 'voice_id': voice_id,
                 'timestamp': timestamp,
                 })

    # Write updated data
    with open(json_filename, 'w') as f:
        json.dump(data, f)
