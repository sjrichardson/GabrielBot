import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen


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
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'text' : msg,
        'bot_id' : os.getenv('TARKSHARK_BOT_ID')
    }
    #equest = requests.post("https://api.groupme.com/v3/bots/post", data = dumps(send_data))
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
    #print(request.text)
    #print(request.url)
