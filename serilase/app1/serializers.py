from rest_framework import serializers


class carserializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    model = serializers.CharField(max_length=4)
    number_plate = serializers.IntegerField()
