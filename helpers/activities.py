import os
from dotenv import load_dotenv
from monicaPython.monica import activities
from helpers.gpt import get_activity_suggestions

load_dotenv()

MONICA_ACCESS_TOKEN = os.getenv('monica_access_token')

GPT_RESPONSE_MARKER = "RESPONSE FROM GPT:"

def get_activities():
    activity = activities.Activities(MONICA_ACCESS_TOKEN)
    activities_list = activity.list_activities()
    return activities_list["data"]


def add_task_to_contact(content, response, contact_id, called_at):
    print("adding gpt response to contact")
    call = calls.Calls(MONICA_ACCESS_TOKEN)

    updated_call_log = content + GPT_RESPONSE_MARKER + response
    return call.update_call(updated_call_log, contact_id, called_at)


def manage_activities():
    activities_data = get_activities()

    for index, activity in enumerate(activities_data):
        activity_content = activity["description"]

        # if GPT_RESPONSE_MARKER in activity:
        #     print("skipping this call, as it already has a response")
        #     continue

        gpt_response = get_activity_suggestions(activity_content)

        attendees = activity["attendees"]
        for attendee in attendees:
            monica_response = add_gpt_response_to_call(call_content, gpt_response, contact_id, called_at)

        print(f"added GPT response to {contact_id}. {index + 1 / len(calls_data)}%")
    
    print("finished adding responses to calls")