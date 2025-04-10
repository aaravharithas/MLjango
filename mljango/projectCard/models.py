from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image


def upload_rename(instance, filename):
    extension = filename.split('.')[-1]
    format = str(instance.pk) + '.' + str(extension)
    return f'projectImage/{format}'

# Create your models here.
class Project(models.Model):
    projectCode = models.CharField(max_length=10,primary_key=True, null=False)
    title = models.CharField(max_length=100, null=False)
    metaContent = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    background = models.ImageField(default='default.png', upload_to=upload_rename)
    date_created = models.DateTimeField(default=timezone.now)
    github = models.CharField(max_length=250,default='https://github.com/aaravharithas')

    def __str__(self):
        return self.title
    
    def delete(self,*args,**kwargs):
        self.background.delete()
        super(Project,self).delete(*args,**kwargs)