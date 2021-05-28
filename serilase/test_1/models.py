from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

#


class student_model(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_reg = models.IntegerField()


class projects(models.Model):
    proj_name = models.CharField(max_length=30)
    info = models.ForeignKey(student_model, on_delete=models.CASCADE, null=True)


class blood_model(models.Model):
    blood_group = models.CharField(max_length=20)
    dep_info = models.OneToOneField(student_model, on_delete=models.CASCADE, null=True)


class subjects(models.Model):
    subject_name = models.CharField(max_length=20)
    subject_info = models.ManyToManyField(student_model)


class company(models.Model):
    company_name = models.CharField(max_length=30)


class employee_model(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_reg = models.IntegerField()
    company_info = models.ForeignKey(company, on_delete=models.CASCADE, null=True)


class assing(models.Model):
    assing_name = models.CharField(max_length=30)
    assing_info = models.ManyToManyField(student_model)


class intern_stu(models.Model):
    name = models.CharField(max_length=20)
    courses = models.IntegerField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
