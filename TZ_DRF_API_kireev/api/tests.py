from django.test import RequestFactory, TestCase

from .models import GeoData
from .views import GeoListViewSet


class TestApiListGeodata(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        GeoData.objects.create(
            cadastral_number="50:21:0100208",
            longitude=48.707103,
            latitude=44.516939,
        )
        GeoData.objects.create(
            cadastral_number="20:21:0100208",
            longitude=58.707103,
            latitude=64.516939,
        )
        GeoData.objects.create(
            cadastral_number="10:21:0100208",
            longitude=98.707103,
            latitude=14.516939,
        )

    def test_api_list_status(self):
        request = self.factory.get("/api/history")
        response = GeoListViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)


    def test_api_list_data(self):
        request = self.factory.get("/api/history")
        response = GeoListViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(len(response.data), 3)

