from django.db import models
from blog.models import Artical

# Create your models here.

class Pinglun(models.Model):
    name = models.CharField(max_length=10,verbose_name="名字")
    pinglun_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=200,verbose_name="内容")
    email = models.EmailField(blank=True,null=True,verbose_name="邮箱")
    url = models.URLField(blank=True,null=True,verbose_name="网址")
    artical = models.ForeignKey(Artical,on_delete=True)