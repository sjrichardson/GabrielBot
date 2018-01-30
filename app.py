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
    data['text'] = data['text'].lower()
    if "!bible" in data['text']:
        bible.bible_handle(data['text'])
    if "!weather" in data['text']:
        send_message(weather.retrieve_weather(data['text']))
    if "hello there" in data['text']:
        send_message("General Kenobi!")
    return "ok", 200
