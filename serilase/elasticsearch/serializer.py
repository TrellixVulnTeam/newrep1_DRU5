from rest_framework import serializers


class NewsCrawelerSerializer(serializers.Serializer):
    channel = serializers.CharField(max_length=50)
    limit = serializers.IntegerField(max_value=10000)
