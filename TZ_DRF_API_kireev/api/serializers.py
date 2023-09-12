from random import randint, getrandbits
from time import sleep

import requests
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers
from .models import GeoData

@extend_schema_serializer(
    examples=[
         OpenApiExample(
            'Пример запроса',
            summary='Создаем запрос по API',
            description='Отправляем кадастровый номер, широту, долготу.',
            value={
                "cadastral_number": "50:21:0100208",
                "longitude": 48.707103,
                "latitude": 44.516939,
            },
            request_only=True
         ),
    ]
)
class GeoDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoData
        read_only_fields = ('id', 'server_answer', 'created')
        fields = (
            "id",
            'cadastral_number',
            'longitude',
            'latitude',
            'created',
            'server_answer',
        )

    def create(self, validated_data):
        """ Функция делает запрос на удаленный сервер и создает объект модели.

            В данном случае генерируем случайное значение ответа,
            и ждем рандомное время (в пределах минуты) до отправки ответа.
        """
        # запрос реверсирует место из широты и долготы, для примера, он работает
        # просто не был уверен что это нужно.

        # url = "https://geocode.maps.co/reverse"
        # query = {
        #          "lat": validated_data.get('longitude'),
        #          "lon": validated_data.get('latitude')
        #          }
        # response = requests.get(url, params=query)

        result = bool(getrandbits(1))
        sleep(randint(1, 59))
        validated_data['server_answer'] = result
        return GeoData.objects.create(**validated_data)
