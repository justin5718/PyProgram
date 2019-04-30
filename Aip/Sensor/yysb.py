from aip import AipSpeech
import datetime
from Sensor import translation as trs

""""sdk"""

APP_ID = '16000621'
API_KEY = 'XYY2APwmNGFnr0VGxiGqNaDZ'
SECRET_KEY = 'QCilx9RGfHEzG0S8n4nGCV9MRln9Bb7m'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filepath):
        with open(filepath, 'rb') as fp:
                return fp.read()

def AipTest():
        result = client.asr(get_file_content('test.wav'), 'wav', 16000, {
            'dev_pid': '1536',})
        if result['err_no'] == 0:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + result['result'][0])
                #print(type(result['result'][0]))
                trs.Process(result['result'][0])
                #translation
        else:
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + "err_no:" + str(result['err_no']))