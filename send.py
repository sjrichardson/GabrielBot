import requests
from json import dumps
#send message to the GroupMe chat
def send_message(msg):
    send_url = 'https://api.groupme.com/v3/bots/post'
    send_data = {
        'text' : msg,
        'bot_id' : "d6981906b891bb32c944c96fd3"
    }
    request = requests.post(send_url, data=dumps(send_data))
