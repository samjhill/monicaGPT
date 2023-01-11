import os
import requests
import json
import subprocess
import openai

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('openai_access_token')

def get_conversation_suggestions(conversation_content):
    intro = f"The following is a conversation I had with my friend. Please suggest a few follow-up questions: "
    prompt = intro + conversation_content

    print(f"prompt: {prompt}")

    # model = "text-ada-001"
    model = "text-davinci-003"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    suggestions = response['choices'][0]['text']

    return suggestions