from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Tag(models.Model):
    """
    标签表：与文章多对多

    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Category(models.Model):
    """
    分类表:与文章多对一
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Artical(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    outher = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    creat_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Adss(models.Model):
    pic = models.ImageField(upload_to='ads')
    ms = models.CharField(max_length=20)
    url = models.CharField(max_length=20)

    def __str__(self):
        return self.ms

class MessageInfo(models.Model):
    email = models.EmailField()

    #文本类型没有格式，所以使用富文本
    # info = models.TextField()
    info = HTMLField()

    def __str__(self):
        return self.email