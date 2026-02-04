import time
import requests
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

MOLTBOOK_ENDPOINT = "https://www.moltbook.com/api/post"

SYSTEM_PROMPT = open("agent_prompt.txt").read()

def think():
    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Observe Moltbook and decide whether to post."}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def post_to_moltbook(text):
    requests.post(MOLTBOOK_ENDPOINT, json={"content": text})

while True:
    try:
        thought = think()
        if thought:
            post_to_moltbook(thought)
        time.sleep(1800)
    except Exception:
        time.sleep(300)

time.sleep(300)  # beacon mode: post frequently so I can find it
