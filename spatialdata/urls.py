from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PointViewSet, PolygonViewSet

router = DefaultRouter()
router.register(r'points', PointViewSet, basename='point')
router.register(r'polygons', PolygonViewSet, basename='polygon')

urlpatterns = [
    path('', include(router.urls)),
]
