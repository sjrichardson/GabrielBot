#searches for given passage
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

#sends retrieved scripture to the chat
def bible_handle(passage):
    req = passage.replace('!bible', '')
    try:
        msg = bible_search(req)
        #why 2? I have no idea
        if (len(msg) == 2):
            send_message("Sorry, I couldn't find that passage!")
            return
        if (len(msg) + len(req) + 5 < 1000):
            send_message("{} {} ESV".format(msg,req))
        elif len(msg) + len(req) > 2000:
            send_message("Too much to print...")
        else:
            for chunk in chunks(msg, 1000):
                send_message(chunk)
            send_message("{} ESV".format(req))
    except:
        send_message("Sorry, I couldn't find that passage!")

#splits message (s) into chunks of size n
def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]
