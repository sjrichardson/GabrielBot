import os
import sys
import json


import requests

postUrl = 'https://api.groupme.com/v3/bots/post'
r = requests.get("/")
print(r.text)
