import json
import re
from sys import argv
from sys import exit

def show_participant_selection_menu(conversation):
    participants = conversation['participants']
    participant_number = 0

    for participant in participants:
        print(f'{participant_number}. {participant["name"]}')
        participant_number = participant_number + 1
    print("E. Everyone")

    print("Choose option:")
    choice = input()

    return [choice, participants]

path_to_json_file = argv.pop()

try:
    script = argv.pop()
except IndexError:
    path_to_json_file = 'message_1.json'

f = open(path_to_json_file, 'r')
conversation = json.load(f)
messages = conversation['messages']

while True:
    choice, participants = show_participant_selection_menu(conversation)
    try:
        if choice == "e" or choice == "E":
            sender_messages_filtered = list(filter(lambda x: True if 'content' in x else False, messages))
        else:
            choice = int(choice)
            participant_name = participants[choice]['name']
            sender_messages = list(filter(lambda x: x['sender_name'] == participant_name, messages))
            sender_messages_filtered = list(filter(lambda x: True if 'content' in x else False, sender_messages))

        messages_content = list(map(lambda x: x['content'], sender_messages_filtered))
        list_of_url = list(map(lambda x: re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x), messages_content))
        list_of_url_without_empty_lists = list(filter(lambda x: x != [], list_of_url))

        flat_list = [item for sublist in list_of_url_without_empty_lists for item in sublist]
        list_of_links = open("list_of_links.txt", 'w')

        for item in flat_list:
            list_of_links.write(item)
            list_of_links.write("\n")

        list_of_links.close()
        exit()
    except ValueError:
        print("Choose a valid option!")
