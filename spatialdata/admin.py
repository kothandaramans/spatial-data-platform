from django.contrib import admin
from .models import SpatialPoint, SpatialPolygon

admin.site.register(SpatialPoint)
admin.site.register(SpatialPolygon)