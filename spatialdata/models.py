from django.db import models
import uuid
from shapely.geometry import Point as ShapelyPoint, Polygon as ShapelyPolygon
import json

class SpatialPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def get_geojson(self):
        """Returns the point in GeoJSON format"""
        point = ShapelyPoint(self.longitude, self.latitude)
        return json.dumps(point.__geo_interface__)  # Convert to GeoJSON

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"


class SpatialPolygon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    coordinates = models.JSONField()  # Stores polygon coordinates as a list of lat/lon pairs

    def get_geojson(self):
        """Returns the polygon in GeoJSON format"""
        try:
            polygon = ShapelyPolygon(self.coordinates)
            return json.dumps(polygon.__geo_interface__)  # Convert to GeoJSON
        except:
            return None  # Return None if polygon is invalid

    def __str__(self):
        return f"Polygon: {self.name}"
