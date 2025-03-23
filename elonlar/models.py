from django.db import models

# Create your models here.
class Elon(models.Model):
    title = models.CharField(max_length=125) #E'lin nomi
    malumot = models.TextField() #Malumot
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) #narxi
    yaratilgan= models.DateTimeField(auto_now=True) #yaratilgan vaqti
    yangilangan= models.DateTimeField(auto_now=True) #yangilangan vaqti

def __str__(self):
    return self.title
