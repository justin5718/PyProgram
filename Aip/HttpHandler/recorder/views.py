from django.shortcuts import render
from . import translation as trs
from . import testReq as tes
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import timezone
import os
from .models import Wav, text
from django.shortcuts import get_object_or_404
from . import yysb as yysb
from django.urls import reverse
import base64, json, time, random
from googletrans import Translator

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    return render(request, 'recorder/index.html')


# 负责上传
def upaload(request):
    if request.method == 'GET':
        return render(request, 'recorder/error.html')
    elif request.method == 'POST':
        content = request.POST.get('audio', None)
        lan = request.POST.get('language', None)
        if not content:
            return HttpResponse('No file')
        # if not lan:
        # return HttpResponse('choose language')
        # content = request.POST.get('audio', None)
        # return HttpResponse(content)
        wavData = base64.b64decode(content)
        x = random.randint(0, 10000)
        contentName = str(x) + ".wav"
        position = os.path.join(BASE_DIR, contentName)
        f = open(position, 'wb')
        f.write(wavData)
        f.close()
        wav = Wav.objects.create(location=position, filename=contentName)
        t = text.objects.create(wav=wav, language=lan)
        return HttpResponse(wav.id)
    else:
        return HttpResponse('???')


# 翻译
def result(request, id):
    file = get_object_or_404(Wav, pk=id)
    t = text.objects.get(wav_id=id)
    if t.text_raw == "notext":
        txt = yysb.RecognizationProcess(file.location)
        t.text_raw = txt
        t.save()
    ss = t.language
    if t.text_processed == "no procession":
        pro = trs.baidutras(txt, ss)
        t.text_processed = pro
        t.save()
    return render(request, 'recorder/result.html', {
        'wav': t.text_raw,
        'title': file.filename,
        'trans': t.text_processed,
        'lan': ss,
    })


# 查询表格的后台请求，最新10条
def table_list(request):
    list = text.objects.order_by('-id')[:20]
    content = {'latest_text_list': list}
    return render(request, 'recorder/table-list.html', content)


# 前端传入单词表，该视图负责下载发音文件
def download(request):
    if request.method == "GET":
        return render(request, 'recorder/error.html')
    if request.method == "POST":
        lis = request.POST.getlist("wordList", None)
        if not lis:
            return HttpResponse("1")
        for i in lis:
            tes.download(i)
        return HttpResponse("123")



def test(request):
    return render(request, 'recorder/error.html')
