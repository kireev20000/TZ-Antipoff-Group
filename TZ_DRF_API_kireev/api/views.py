from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .models import GeoData
from .serializers import GeoDataSerializer

class GeoListViewSet(viewsets.ModelViewSet):

    queryset = GeoData.objects.all()
    serializer_class = GeoDataSerializer
    http_method_names = ('get', )
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('cadastral_number', )

class GeoCreateViewSet(viewsets.ModelViewSet):

    queryset = GeoData.objects.all()
    serializer_class = GeoDataSerializer
    http_method_names = ('post', )

