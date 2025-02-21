from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SpatialPoint, SpatialPolygon
from .serializers import PointSerializer, PolygonSerializer

class PointViewSet(viewsets.ModelViewSet):
    queryset = SpatialPoint.objects.all()
    serializer_class = PointSerializer

    def list(self, request):
        points = self.get_queryset()
        serializer = self.get_serializer(points, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            point = self.get_object()
            serializer = self.get_serializer(point)
            return Response(serializer.data)
        except SpatialPoint.DoesNotExist:
            return Response({"error": "Point not found"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            point = self.get_object()
            serializer = self.get_serializer(point, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SpatialPoint.DoesNotExist:
            return Response({"error": "Point not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            point = self.get_object()
            point.delete()
            return Response({"message": "Point deleted"}, status=status.HTTP_204_NO_CONTENT)
        except SpatialPoint.DoesNotExist:
            return Response({"error": "Point not found"}, status=status.HTTP_404_NOT_FOUND)


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = SpatialPolygon.objects.all()
    serializer_class = PolygonSerializer

    def list(self, request):
        polygons = self.get_queryset()
        serializer = self.get_serializer(polygons, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            polygon = self.get_object()
            serializer = self.get_serializer(polygon)
            return Response(serializer.data)
        except SpatialPolygon.DoesNotExist:
            return Response({"error": "Polygon not found"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            polygon = self.get_object()
            serializer = self.get_serializer(polygon, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SpatialPolygon.DoesNotExist:
            return Response({"error": "Polygon not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            polygon = self.get_object()
            polygon.delete()
            return Response({"message": "Polygon deleted"}, status=status.HTTP_204_NO_CONTENT)
        except SpatialPolygon.DoesNotExist:
            return Response({"error": "Polygon not found"}, status=status.HTTP_404_NOT_FOUND)
