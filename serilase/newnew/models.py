from django.db import models


# Create your models here.
class aeroplane(models.Model):
    cc = models.IntegerField()
    color = models.CharField(max_length=30)
