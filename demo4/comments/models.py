from django.db import models
from foods.models import Foods

# Create your models here.

class Comments(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    com_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    food = models.ForeignKey(Foods,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Com(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    com_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    cc = models.ForeignKey(Comments,on_delete=models.CASCADE)


