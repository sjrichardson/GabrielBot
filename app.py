import os
import sys
import json


import requests

postUrl = 'https://api.groupme.com/v3/bots/post'
r = requests.get("/")
if r.status_code == 200
    q = request.post(postUrl, data = {'text': 'yay', 'bot_id' : 'd6981906b891bb32c944c96fd3'})
