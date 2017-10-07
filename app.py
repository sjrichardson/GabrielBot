import os
import sys
import bible
import weather

from urllib.parse import urlencode
import requests
from json import dumps

import html2text
from flask import Flask, request

biblekey = "GX2KnKmM5UxrRioM9fcsS7YVTlxo6IwmGfd3TyHU"
app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if "!bible" in data['text']:
        message = bible.bible_handle(data['text'])
    if "!weather" in data['text']:
        message = weather.retrieve_weather(data['text'])
    send_message(message)
    return "ok", 200

#send message to the GroupMe chat
def send_message(msg):
    send_url = 'https://api.groupme.com/v3/bots/post'
    send_data = {
        'text' : msg,
        'bot_id' : "d6981906b891bb32c944c96fd3"
    }
    request = requests.post(send_url, data=dumps(send_data))
