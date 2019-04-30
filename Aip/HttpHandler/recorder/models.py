from django.db import models

# Create your models here.


class Wav(models.Model):
    location = models.CharField(max_length=200,default='NofilePath')
    pub_time = models.DateTimeField('date up', auto_now=True)
    filename = models.CharField(max_length=20,default='NoName')

class text(models.Model):
    text_raw = models.CharField(max_length=200,default="notext")
    text_processed = models.CharField(max_length=200,default="no procession")
    language = models.CharField(max_length=20,default="en")
    wav = models.ForeignKey(Wav, on_delete=models.CASCADE)