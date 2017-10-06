import os
import sys

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
        req = data['text'].replace('!bible', '')
        msg = bible_search(req)
        if (len(msg) + len(req) + 5 < 1000):
            send_message("{} {} ESV".format(msg,req))
        else:
            for chunk in chunks(msg, 1000):
                send_message(chunk)
            send_message("{} ESV".format(req))
        if (len(msg) == 0):
            send_message("Sorry, I couldn't find that passage!")

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
    print(payload)
    response = res.json()
    passage = response['response']['search']['result']['passages'][0]['text']
    h = html2text.HTML2Text()
    h.ignore_links = True
    ret = h.handle(passage)
    return ret
def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]
