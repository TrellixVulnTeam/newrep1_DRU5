from rest_framework.serializers import ModelSerializer
from .models import employee_model, department_model,student,projects

class department1_serialzer(ModelSerializer):
    class Meta:
        model = department_model
        fields = '__all__'


class employee1_serializer(ModelSerializer):
    class Meta:
        model = employee_model
        fields = '__all__'
        depth=1


class student_serializer(ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        depth=1


class project_serializer(ModelSerializer):
    class Meta:
        model = projects
        fields = '__all__'

