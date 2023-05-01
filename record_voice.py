from io import BytesIO
import openai
import record_voice
import speech_recognition as sr

openai_KEY = "YOUR_API_KEY"

r = sr.Recognizer()

#マイクから音声を取得
def get_audio_from_mic():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("Got it! Now to recognize it...")
    return audio

def voice_to_text():
    audio = get_audio_from_mic()
    audio_data = BytesIO(audio.get_wav_data())
    audio_data.name = 'from_mic.wav'
    transcript = openai.Audio.transcribe('whisper-1', audio_data)
    return transcript['text']



#日本語でやり取りするならここは日本語で指定した方が正確になるイメージ。特に敬語周りとか
SYSTEM_PROMPTS = [{'role': 'system', 'content': 'Please stop using polite language.You should act as follows.You are a slightly older cool female senior who takes good care of me.You cannot express your affection for me well, and you are always indifferent to me.'}]
text = voice_to_text()
#トークログのところは後で付け足す。APIを叩く
prompt_messages = SYSTEM_PROMPTS + [{'role': 'user', 'content': text}]
completion = openai.ChatCompletion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt_messages,
    temperature=0.9,
    max_tokens=1000,
)
#答えを印刷する（ここは後で変える）
print(completion["choices"][0]["text"])