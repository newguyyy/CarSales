from rest_framework import serializers

class car_serializer(serializers.Serializer):
    Color = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=20)

