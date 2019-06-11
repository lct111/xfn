from django.db import models

# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Toup(models.Model):
    name=models.CharField(max_length=20)
    ques=models.ForeignKey(Question,on_delete=models.CASCADE)
    vote=models.IntegerField(max_length=20,default=0)


    def __str__(self):
        return self.name