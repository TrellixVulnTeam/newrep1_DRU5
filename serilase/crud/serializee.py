from rest_framework.serializers import ModelSerializer
from .models import student


class student_serializer(ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
