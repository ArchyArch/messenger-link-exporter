import json
import re
from sys import argv

path_to_json_file = argv.pop()

try:
    script = argv.pop()
except IndexError:
    path_to_json_file = 'message_1.json'

f = open(path_to_json_file, 'r')
conversation = json.load(f)
messages = conversation['messages']
sender_messages = list(filter(lambda x: x['sender_name'] == conversation['participants'][0]['name'], messages))
sender_messages_filtered = list(filter(lambda x: True if 'content' in x else False, messages))
messages_content = list(map(lambda x: x['content'], sender_messages_filtered))
list_of_url = list(map(lambda x: re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x), messages_content))
list_of_url_without_empty_lists = list(filter(lambda x: x != [], list_of_url))

flat_list = [item for sublist in list_of_url_without_empty_lists for item in sublist]
list_of_links = open("list_of_links.txt", 'w')

for item in flat_list:
    list_of_links.write(item)
    list_of_links.write("\n")

list_of_links.close()
