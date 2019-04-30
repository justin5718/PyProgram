import requests, _md5, random, json

APP_ID = "20190413000287584"

KEY = "tTSzz6Lowa9YOwJGJNt4"


def baidutras(text,lan):
    my_url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    salty = random.randint(32768, 65536)

    q = text
    fromlan = 'zh'
    tolan = lan
    sign = APP_ID+q+str(salty)+KEY
    m1 = _md5.md5()
    m1.update(sign.encode("utf8"))
    sign = m1.hexdigest()
    params = {
        'appid': APP_ID,
        'q': text,
        'from': fromlan,
        'to': tolan,
        'salt': str(salty),
        'sign': sign,
    }

    response = requests.get(my_url, params=params)
    data = json.loads(response.content.decode())
    return data['trans_result'][0]['dst']





