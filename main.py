import json
import sys
import random
import requests

def customizer():
    #Getting random bot name
    with open('bot_name.txt', 'r') as f:
         name_data = f.read()
    name_data = name_data.split("\n")
    bot_name = random.choice(name_data)

    #Getting random slack emoji
    with open('emoji_id.txt', 'r') as f:
         emoji_data = f.read()
    emoji_data = emoji_data.split("\n")
    emoji_id = random.choice(emoji_data)

    #Generating random hex color code
    hex_number = random.randint(1118481, 16777215)
    hex_number = str(hex(hex_number))
    hex_number = '#' + hex_number[2:]

    return bot_name, emoji_id, hex_number

if __name__ == '__main__':
    url = "https://hooks.slack.com/services/xxxxx/xxxxxx/xxxxxxx"
    bot_name, emoji_id, hex_number = customizer()
    message = ("A Sample Message")
    title = (f"New Incoming Message {emoji_id}")
    slack_data = {
        "username": bot_name,
        "icon_emoji": emoji_id,
        "channel": "#random",
        "attachments": [
            {
                "color": hex_number,
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)