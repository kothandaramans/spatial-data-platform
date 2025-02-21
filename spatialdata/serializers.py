from rest_framework import serializers
from .models import SpatialPoint, SpatialPolygon

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialPoint
        fields = '__all__'

class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpatialPolygon
        fields = '__all__'
