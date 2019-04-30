from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import timezone
import os
from .models import Wav
from django.shortcuts import get_object_or_404
from . import yysb as yysb
from django.urls import reverse
import base64, json
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    return render(request, 'recorder/index.html')


#负责上传
def upaload(request):
    if request.method == 'GET':
        return render(request, 'recorder/error.html')
    elif request.method == 'POST':
        content = request.POST.get('audio', None)
        if not content:
            return HttpResponse('No file')
        #content = request.POST.get('audio', None)
        #return HttpResponse(content)
        wavData = base64.b64decode(content)
        contentName = "test.wav"
        position = os.path.join(BASE_DIR, contentName)
        f = open(position, 'wb')
        f.write(wavData)
        f.close()
        wav = Wav.objects.create(location=position, filename=contentName)
        return HttpResponse(wav.id)
    else:
        return HttpResponse('???')

#翻译
def result(request, id):
    file = get_object_or_404(Wav,pk=id)
    text = yysb.RecognizationProcess(file.location)

    return render(request, 'recorder/result.html', {
        'wav': text,
        'title': file.filename,
    })

def test(request):
    return render(request, 'recorder/error.html')