import socket

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view
)
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GeoData
from .serializers import GeoDataSerializer


@extend_schema(tags=["Запросы"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить историю всех запросов",
        description="Отдает полную историю запросов",
        parameters=[
            OpenApiParameter(
                name='cadastral_number',
                description='Фильтрует запросы по кадастровому номеру',
                required=False,
                type=str
            ),
        ]

    ),
    retrieve=extend_schema(
        summary="Выбрать из базы один запрос по PK",
        description="Выбрать из базы один запрос по PK",
        auth=None,
    ),
)
class GeoListViewSet(viewsets.ModelViewSet):

    queryset = GeoData.objects.all()
    serializer_class = GeoDataSerializer
    http_method_names = ('get',)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('cadastral_number',)


@extend_schema(tags=["Запросы"])
@extend_schema_view(
    create=extend_schema(
        summary="Создать новый запрос",
        description="Принимает на вход кадастровый номер, широту и долготу",
    ),
)
class GeoCreateViewSet(viewsets.ModelViewSet):
    queryset = GeoData.objects.all()
    serializer_class = GeoDataSerializer
    http_method_names = ('post',)


@api_view(['GET'])
def ping_server(request):
    """Проверить пинг внешнего сервера. """
    server, port = 'yandex.ru', 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((server, port))
        s.shutdown(socket.SHUT_RDWR)
        return Response(
            f'{server} Работает',
            status=status.HTTP_200_OK,
        )
    except:
        return Response(
            f'{server} Не пингуется',
            status=status.HTTP_408_REQUEST_TIMEOUT,
        )
    finally:
        s.close()


@api_view(['GET'])
def send_result(request):
    """ Отправляет результат по запросу пользователя. """
    return Response(
        {'success': f'Из задания я не понял что сюда надо слать / отвечать, '
                    f'написал письмо HR который прислал '
                    f'задания, ответа не получил'},
        status=status.HTTP_204_NO_CONTENT,
    )
