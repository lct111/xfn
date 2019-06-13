from django.db import models
from blog.models import Artical

# Create your models here.

class Pinglun(models.Model):
    name = models.CharField(max_length=10)
    pinglun_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=200)
    email = models.EmailField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    artical = models.ForeignKey(Artical,on_delete=True)