"""Эндпойнты приложения."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GeoCreateViewSet, GeoListViewSet, ping_server, rates_converter

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('history', GeoListViewSet, basename='geo_list')
router_v1.register('query', GeoCreateViewSet, basename='geo_create')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('ping/', ping_server),
    path('rates/', rates_converter)
]

