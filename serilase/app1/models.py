from django.db import models

# Create your models here.
class car(models.Model):
    name=models.CharField(max_length=30)
    model=models.CharField(max_length=4)
    number_plate=models.IntegerField()

