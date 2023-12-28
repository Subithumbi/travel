from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    desc=models.TextField()

def __str__(self):
    return self.name

class Contributor(models.Model):
    names=models.CharField(max_length=250)
    imgs = models.ImageField(upload_to='pic')
    descs = models.TextField()

def __str__(self):
    return self.name
