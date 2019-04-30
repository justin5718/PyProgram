from aip import AipSpeech
import datetime


""""sdk"""

APP_ID = '16000621'
API_KEY = 'XYY2APwmNGFnr0VGxiGqNaDZ'
SECRET_KEY = 'QCilx9RGfHEzG0S8n4nGCV9MRln9Bb7m'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()

def RecognizationProcess(files):
    result = client.asr(get_file_content(files), 'wav', 16000, {
        'dev_pid': '1536', })
    if result['err_no'] == 0:
        text = result['result'][0]
    else:
        text = "err_no:" + str(result['err_no'])
    return text