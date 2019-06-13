from django.db import models
from django.contrib.auth.models import User

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
