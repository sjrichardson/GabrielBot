import os
import sys
import bible
import weather
from send import send_message
from json import dumps

from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if "!bible" in data['text']:
        bible.bible_handle(data['text'])
    if "!weather" in data['text']:
        send_message(weather.retrieve_weather(data['text']))
    if "!kill" in data['text'] and "Sam Richardson" in data['name']:
        sys.exit()

    return "ok", 200
