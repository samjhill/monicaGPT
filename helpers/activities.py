import os
from dotenv import load_dotenv
from monicaPython.monica import activities, tasks
from helpers.gpt import get_activity_suggestions

load_dotenv()

MONICA_ACCESS_TOKEN = os.getenv('monica_access_token')

GPT_RESPONSE_MARKER = "RESPONSE FROM GPT:"

def get_activities():
    activity = activities.Activities(MONICA_ACCESS_TOKEN)
    activities_list = activity.list_activities()
    return activities_list["data"]


def add_task_to_contact(response, contact_id):
    print("adding task to contact")
    task = tasks.Task(MONICA_ACCESS_TOKEN)

    title = "Invite this friend to one of these activities"
    description = response

    return task.create_task(title, description, contact_id)


def manage_activities():
    activities_data = get_activities()

    for index, activity in enumerate(activities_data):
        activity_content = activity["description"]

        # if GPT_RESPONSE_MARKER in activity:
        #     print("skipping this call, as it already has a response")
        #     continue

        gpt_response = get_activity_suggestions(activity_content)

        attendees = activity["attendees"]["contacts"]
        for attendee in attendees:
            contact_id = attendee["id"]
            monica_response = add_task_to_contact(gpt_response, contact_id)

        print(f"added task to {contact_id}. {index + 1 / len(activities_data)}%")
    
    print("finished adding activity suggestions")