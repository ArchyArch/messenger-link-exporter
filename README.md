# messenger-link-exporter

A simple script in Python that exports links from Messenger conversations.

### How to use it?

1. Export your Facebook messages from [here](https://www.facebook.com/dyi).
2. Download your Messenger data and unpack it.
3. Choose one conversation JSON file (it's usually named `messages_1.json`).
4. Run the script in terminal -> `python messenger-link-exporter.py <path to conversation JSON file>` (if you don't provide a path then `messages_1.json` will be opened).
5. A new file named `list_of_links.txt` will be created.
