from io import BytesIO
import openai
import speech_recognition as sr

openai_KEY = "YOUR_API_KEY"

r = sr.Recognizer()
with sr.Microphone(sample_rate=16_000) as source:
    # 音声を取得
    print("なにか話してください")
    audio = r.listen(source)
    print("音声を取得しました")
# 音声をテキストに変換
audio_data = BytesIO(audio.get_wav_data())
audio_data.name = "from_mic.wav"
transcript = openai.Audio.transcribe("whisper-1", audio_data)
print(transcript["text"])