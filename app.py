import os
import sys

from urllib.parse import urlencode
import requests
from json import dumps

from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data['name'] != 'TarkShark':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg)
    return "ok", 200
def send_message(msg):
    send_url = 'https://api.groupme.com/v3/bots/post'
    print(msg)
    send_data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text' : msg,
    }
    request = requests.post(url = send_url, data = dumps(send_data))
    print(request)
