import socket

from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.decorators import api_view

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


@api_view(['GET'])
def ping_server(request):
    """ping server"""
    server, port = 'kaidzen-deploy.vercel.app', 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((server, port))
        s.shutdown(socket.SHUT_RDWR)
        return Response(f'{server} Работает')
    except:
        return Response(f'{server} Не пингуется')
    finally:
        s.close()
