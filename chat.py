import requests
import json
import os
import record_voice
import wave
import pyaudio

text = record_voice.completion["choices"][0]["text"]
def post_audio_query(text: str) -> dict:
    params = {'text': text, 'speaker': 1}
    res = requests.post('https://localhost:50021/audio_query', params=params)
    return res.json

def post_synthesis(audio_query_response: dict) -> bytes:
    params = {'speaker': 1}
    headers = {'Content-Type': 'application/json'}
    audio_query_response_json = json.dumps(audio_query_response)
    res = requests.post(
        'https://localhost:50021/synthesis',
        data=audio_query_response_json,
        params=params,
        headers=headers
    )
    return res.content
#再生する
def play_wavfile(mavfile: bytes)
    wr:wave.Wave_read = wave.open(io.BytesIO(wav_file))
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(wr.getsampwidth()),
        channels=wr.getnchannels(),
        rate=wr.getframerate(),
        output=True
    )
    chunk = 1024
    data = wr.readframes(chunk)
    #最後を少し何もしないで終わるようにする
    stream.close()
    p.terminate()

