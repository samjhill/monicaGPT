import os
from dotenv import load_dotenv
from monicaPython.monica import calls
from gpt import get_conversation_suggestions

load_dotenv()

MONICA_ACCESS_TOKEN = os.getenv('monica_access_token')

GPT_RESPONSE_MARKER = "\n RESPONSE FROM GPT: \n"

def get_calls():
    call = calls.Calls(MONICA_ACCESS_TOKEN)
    calls_list = call.list_calls()
    calls_data = calls_list["data"]
    return calls_data


def add_gpt_response_to_call(content, response, contact_id, called_at):
    print("adding gpt response to contact")
    call = calls.Calls(MONICA_ACCESS_TOKEN)

    updated_call_log = content + GPT_RESPONSE_MARKER + response
    return call.update_call(updated_call_log, contact_id, called_at)


calls_data = get_calls()

for call in calls_data:
    call_content = call["content"]

    if GPT_RESPONSE_MARKER in call_content:
        print("skipping this call, as it already has a response")
        continue

    contact_id = call["id"]
    called_at = call["called_at"]

    gpt_response = get_conversation_suggestions(call_content)
    print(gpt_response)

    monica_response = add_gpt_response_to_call(call_content, gpt_response, contact_id, called_at)

    print(monica_response)