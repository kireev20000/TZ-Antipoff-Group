# api/serializers
from random import randint, getrandbits
from time import sleep

import requests
from rest_framework import serializers
from .models import GeoData


class GeoDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoData
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
