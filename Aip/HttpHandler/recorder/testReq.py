import os
import requests

BASE_DIR = os.getcwd().replace("\\",'/')

def download(word):

    url = "https://dict.youdao.com/dictvoice"
    key = {
        "type": '2',
        "audio": word,
    }
    r = requests.get(url, params=key, stream=True)
    filename = word + ".mp3"
    dis = '/recorder/static/mp3/'
    pos = BASE_DIR + dis + filename
    with open(pos, "wb") as mp3:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp3.write(chunk)





