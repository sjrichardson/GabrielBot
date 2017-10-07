import requests
from json import dumps
#send message to the GroupMe chat
def send_message(msg):
    send_url = 'https://api.groupme.com/v3/bots/post'
    send_data = {
        'text' : msg,
        'bot_id' : "dcea3ad8331995eaed7be6f7e4"
    }
    request = requests.post(send_url, data=dumps(send_data))
