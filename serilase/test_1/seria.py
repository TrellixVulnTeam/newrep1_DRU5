from rest_framework.serializers import ModelSerializer
from .models import student_model, projects, blood_model, subjects, employee_model, company, assing, intern_stu
from rest_framework import serializers


class stu_serializer(ModelSerializer):
    class Meta:
        model = student_model
        fields = '__all__'


class proj_serializer(ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'


class blood_serializer(ModelSerializer):
    class Meta:
        model = blood_model
        fields = '__all__'


class subject_serializer(ModelSerializer):
    class Meta:
        model = subjects
        fields = '__all__'


class employee_serializer(ModelSerializer):
    class Meta:
        model = employee_model
        fields = '__all__'


class company_serializer(ModelSerializer):
    class Meta:
        model = company
        fields = '__all__'


class assing_serializer(ModelSerializer):
    class Meta:
        model = assing
        fields = '__all__'


class intern_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    courses = serializers.IntegerField()



