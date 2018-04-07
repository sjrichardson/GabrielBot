import requests
from json import dumps
import os
#send message to the GroupMe chat
def send_message(msg):
    send_url = 'https://api.groupme.com/v3/bots/post'
    send_data = {
        'text' : msg,
        'bot_id' : os.getenv('TARK_ID')
    }
    request = requests.post(send_url, data=dumps(send_data))
