import os
import sys

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    return "ok", 200
