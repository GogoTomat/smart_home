from rest_framework import serializers
from .models import sensor, measurement


class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor
        fields = ['id', 'name', 'des']


class measurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = measurement
        fields = ['sensor', 'temp', 'image', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = measurementSerializer(read_only=True, many=True)

    class Meta:
        model = sensor
        fields = ['id', 'name', 'description', 'measurements']
