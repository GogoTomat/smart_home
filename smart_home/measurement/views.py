from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import sensor, measurement
from .serializers import sensorSerializer, SensorDetailSerializer, measurementSerializer


class SensorsView(ListCreateAPIView):
    queryset = sensor.objects.all()
    serializer_class = sensorSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    queryset = measurement.objects.all()
    serializer_class = measurementSerializer
