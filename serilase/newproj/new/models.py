from django.db import models


# Create your models here.

class employee_model(models.Model):
    name_1 = models.CharField(max_length=30)
    age = models.IntegerField()


class department_model(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30, null=True)
    _info = models.ForeignKey(employee_model, on_delete=models.CASCADE, null=True)


class student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class projects(models.Model):
    project_name = models.CharField(max_length=30)
    _info = models.ManyToManyField(student)
