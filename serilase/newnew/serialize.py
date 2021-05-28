from rest_framework.serializers import ModelSerializer

from newnew.models import aeroplane


class aeroplane_serializer(ModelSerializer):
    class Meta:
        model = aeroplane
        fields = '__all__'
