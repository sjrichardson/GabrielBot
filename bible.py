import requests
from send import send_message
import json
import html2text
import os
import re

biblekey = os.getenv("BIBLE_KEY")
#searches for given passage
def bible_search(reference):
    header = { 'Authorization' : os.getenv('BIBLE_KEY')}
    payload = {
        "q" : reference
    }

    res = requests.get(os.getenv('BIBLE_URL'), headers=header, params=payload)
    response = res.json()
    passage = response['passages'][0].split('\n\nFootnotes')[0]
    passage = re.sub(r'\(\d+\)', '', passage)
    passage = passage.replace('\n\n', '\n').replace('(ESV)','')
    return (passage)

#sends retrieved scripture to the chat
def bible_handle(passage):
    req = passage.replace('!bible', '')
    try:
        msg = bible_search(req)
        print (msg)
        #why 2? I have no idea
        if (len(msg) == 2):
            send_message("Sorry, I couldn't find that passage!")
            return
        if (len(msg) + len(req) + 5 < 1000):
            send_message("{} (ESV)".format(msg))
        elif len(msg) + len(req) > 2000:
            send_message("Too much to print... shorten your search")
        else:
            for chunk in chunks(msg, 1000):
                send_message(chunk)
             send_message("(ESV)")
    except:
        send_message("Sorry, I couldn't find that passage!")

#splits message (s) into chunks of size n
def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]
