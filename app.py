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
    send_data = {
        'text' : msg,
        'bot_id' : "d6981906b891bb32c944c96fd3"
    }
    request = requests.post(send_url, params=send_data)
    print(request.text)
    print(request.url)
