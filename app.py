import os
import sys
import json

import requests

postUrl = 'https://api.groupme.com/v3/bots/post'
r = requests.post(postUrl, data = {'text': 'hi', 'bot_id' : 'd6981906b891bb32c944c96fd3'})
