import sys
import uuid
import requests
import hashlib
import time, json

#youdao tranlation detail
YOUDAO_URL = 'http://openapi.youdao.com/api'
APP_ID = "3de4b4207bc5dd42"
APP_KEY = "7N2gEi3lzDkrubcZjrm40jUeSwgTydIu"

def encrypt(signstr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signstr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]

def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def connect():
        q = 'pennis'
        data = {}
        data['from'] = 'EN'
        data['to'] = 'zh-CHS'
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signstr = APP_ID + truncate(q) + salt + curtime + APP_KEY
        sign = encrypt(signstr)
        data['q'] = q
        data['salt'] = salt
        data['appKey'] = APP_ID
        data['sign'] = sign

        response = do_request(data)
        data = json.loads(response.content.decode())
        print(data['web'])
        #print(type(response.content))
        #for ls in response:
            #print(ls)

if __name__ == '__main__':
    connect()





