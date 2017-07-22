import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

def log(msg):
    print(str(msg))
    sys.stdout.flush()

@app.route('/v3/bots/post', methods=['POST'])
def webhook():
    data = request.get_json()
    log('Received {}'.format(data))

    #ensure message is not from self
    if data['name'] != 'TarkShark':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg)

    return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'text'   : msg,
          'bot_id' : os.getenv('TARKSHARK_BOT_ID'),
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
