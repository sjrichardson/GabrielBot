import os
import sys
import json


import requests

postUrl = 'https://api.groupme.com/v3/bots/post'
r = requests.get('tarksharkbot.herokuapp.com/')
q = request.post(postUrl, data = {'text': r.status_code, 'bot_id' : 'd6981906b891bb32c944c96fd3'})
