from .models import  employee1
from rest_framework.serializers import ModelSerializer



class employee12_serializer(ModelSerializer):
    class Meta:
        model = employee1
        fields = '__all__'
