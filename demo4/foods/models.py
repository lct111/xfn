from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyUser(User):
    telephone = models.CharField(max_length=11)

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Foods(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    pic = models.ImageField(upload_to='ads')
    price = models.FloatField(max_length=20)
    creat_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Adss(models.Model):
    pic = models.ImageField(upload_to='adss')
    msg = models.CharField(max_length=20,blank=True,null=True)


