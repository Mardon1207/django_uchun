from django.db import models

# Create your models here.
class Talaba(models.Model):
    Ism = models.CharField(max_length=125)
    FISh= models.CharField(max_length=125)
    tel= models.IntegerField()
    haqida= models.TextField()

