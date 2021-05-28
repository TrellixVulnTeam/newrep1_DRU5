from django.db import models


# Create your models here.


class engine_model(models.Model):
    cc = models.IntegerField()
    color = models.CharField(max_length=30)


class car_model(models.Model):
    name = models.CharField(max_length=30)
    model_no = models.IntegerField()
    _new = models.OneToOneField(engine_model, on_delete=models.CASCADE, null=True)

#
# class e_mployee(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#
#
# class d_epartment(models.Model):
#     name = models.CharField(max_length=30)
#     location = models.CharField(max_length=30, null=True)
#     _info = models.ForeignKey(e_mployee, on_delete=models.CASCADE, null=True)
#
class employee1(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class department1(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30, null=True)
    _info = models.ForeignKey(employee1, on_delete=models.CASCADE, null=True)
