from django.db import models
from django.utils import timezone

# Create your models here.
class Image_Post(models.Model):
    title = models.CharField(max_length=200, default="")
    uploaded_date = models.DateTimeField(default = timezone.now)
    image_file = models.ImageField(upload_to = 'img/')

class Audio_Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    #uploaded_date = models.DateTimeField(auto_now_add=True)
    audiofile = models.FileField(upload_to = 'audio/')