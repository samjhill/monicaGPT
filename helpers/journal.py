import os
from dotenv import load_dotenv
from monicaPython.monica import journal
from helpers.gpt import get_journal_entry_suggestions

load_dotenv()

MONICA_ACCESS_TOKEN = os.getenv('monica_access_token')

GPT_RESPONSE_MARKER = "\n RESPONSE FROM AI THERAPIST: \n"

def get_journal_entries():
    journals = journal.Journal(MONICA_ACCESS_TOKEN)
    entries_list = journals.list_journal()
    entries_data = entries_list["data"]
    return entries_data


def add_gpt_response_to_journal_entry(title, content, response, journal_entry_id):
    print("adding gpt response to journal entry")
    journals = journal.Journal(MONICA_ACCESS_TOKEN)

    updated_journal_entry = content + GPT_RESPONSE_MARKER + response
    return journals.update_journal_entry(title, updated_journal_entry, journal_entry_id)


def manage_journal_entries():
    journals_data = get_journal_entries()

    for index, journal_entry in enumerate(journals_data):
        journal_content = journal_entry["post"]

        if GPT_RESPONSE_MARKER in journal_content:
            print("skipping this journal entry, as it already has a response")
            continue

        entry_id = journal_entry["id"]
        entry_title = journal_entry["title"] or "No title"

        gpt_response = get_journal_entry_suggestions(journal_content)

        monica_response = add_gpt_response_to_journal_entry(entry_title, journal_content, gpt_response, entry_id)

        print(f"added GPT response to {entry_id}. {index + 1 / len(journals_data)}%")
    
    print("finished adding responses to journals")