from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from django.contrib.auth.models import Group
# g2 = Group.objects.create(name='superroup')


class employee1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
