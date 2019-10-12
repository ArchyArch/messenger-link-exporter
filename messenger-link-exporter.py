import json
import re
f = open('message_1.json', 'r')
conversation = json.load(f)
print(conversation['participants'])
messages = conversation['messages']   
zajac_messages = list(filter(lambda x: x['sender_name'] == conversation['participants'][0]['name'], messages))
zajac_messages_filtered = list(filter(lambda x: True if 'content' in x else False, messages))
messages_content = list(map(lambda x: x['content'], zajac_messages_filtered))
print(messages_content[0])
list_of_url = list(map(lambda x: re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x), messages_content))
list_of_url_without_empty_lists = list(filter(lambda x: x != [], list_of_url))

flat_list = [item for sublist in list_of_url_without_empty_lists for item in sublist]
for item in flat_list:
    print(item)
