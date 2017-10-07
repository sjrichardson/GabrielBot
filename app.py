import os
import sys
import bible
import weather
from send import send_message
from json import dumps

import html2text
from flask import Flask, request

biblekey = "GX2KnKmM5UxrRioM9fcsS7YVTlxo6IwmGfd3TyHU"
app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if "!bible" in data['text']:
        bible.bible_handle(data['text'])
    if "!weather" in data['text']:
        send_message(weather.retrieve_weather(data['text']))

    return "ok", 200
