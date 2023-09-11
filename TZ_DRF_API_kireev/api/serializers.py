# api/serializers
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