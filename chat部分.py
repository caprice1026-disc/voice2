import record_voice
import openai
import json
import os

openai_KEY = "YOUR_API_KEY"
#日本語でやり取りするならここは日本語で指定した方が正確になるイメージ。特に敬語周りとか
SYSTEM_PROMPTS = [{'role': 'system', 'content': 'Please stop using polite language.You should act as follows.You are a slightly older cool female senior who takes good care of me.You cannot express your affection for me well, and you are always indifferent to me.'}]
text = record_voice.transcript["text"]
#トークログのところは後で付け足す。APIを叩く
prompt_messages = SYSTEM_PROMPTS + [{'role': 'user', 'content': text}]
completion = openai.ChatCompletion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt_messages,
    temperature=0.9,
    max_tokens=1000,
)
print(completion)