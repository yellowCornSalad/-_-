import email
from importlib.resources import contents
from statistics import mode
from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add= True)
    
    class  Meta:
        verbose_name_plural = "아티클 작성하기"
    
    def __str__(self):
        return f"{self.title}--{self.name}"