from django.db import models

# Create your models here.

class Database1(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    collage = models.CharField(max_length=50, default="")
    year = models.IntegerField(max_length=5,default='2019')
    course = models.CharField(max_length=100,default='')