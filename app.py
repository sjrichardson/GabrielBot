import os
import sys

from urllib.parse import urlencode
import requests
from json import dumps

from flask import Flask, request

biblekey = "GX2KnKmM5UxrRioM9fcsS7YVTlxo6IwmGfd3TyHU"
app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if "!bible" in data['text']:
        data['text'].replace('!bible', '')
        msg = bible_search(data['text'])
    return "ok", 200
def send_message(msg):
    send_url = 'https://api.groupme.com/v3/bots/post'
    send_data = {
        'text' : msg,
        'bot_id' : "d6981906b891bb32c944c96fd3"
    }
    request = requests.post(send_url, data=dumps(send_data))

def bible_search(reference):
    payload = {
        'q[]': reference,
        'version': 'ESV'
    }
    bible_url = "https://bibles.org/v2/passages.js"
    res = requests.get(bible_url, auth=(biblekey, 'X'), params=payload)
    print(res.request)
    response = res.json()
    passage = response['response']['search']['result']['passages']
    print(passage)
