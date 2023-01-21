import os
import requests
import json
import subprocess
import openai
import time
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('openai_access_token')

def get_openai_response(prompt):
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
    response = response['choices'][0]['text']
    time.sleep(2)
    return response


def get_conversation_suggestions(conversation_content):
    split_content = conversation_content.splitlines()
    suggestions = []

    for line in split_content:
        if len(line) < 1:
            continue

        intro = f"The following is a conversation I had with my friend. Please give me advice about it, and then suggest a few follow-up questions and topics of conversation: "
        prompt = intro + line

        print(f"prompt: {prompt}")
        
        suggestions.append(get_openai_response(prompt))

    return "\n".join(suggestions)


def get_activity_suggestions(activity_content):
    intro = f"The following is an activity I did with my friend. Please suggest three other similar activies we may like to do together: "
    prompt = intro + activity_content

    print(f"prompt: {prompt}")

    suggestions = get_openai_response(prompt)

    return suggestions


def get_journal_entry_suggestions(entry_content):
    split_content = entry_content.splitlines()

    suggestions = []

    for line in split_content:
        if len(line) < 1:
            continue

        intro = f"The following is a journal entry I wrote. Please assume the role of my therapist and give me your thoughts, advice, and suggestions based on what you read: "
        prompt = intro + line

        print(f"prompt: {prompt}")

        suggestions.append(get_openai_response(prompt))

    return "\n".join(suggestions)