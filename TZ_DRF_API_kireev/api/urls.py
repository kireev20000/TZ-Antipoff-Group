"""Эндпойнты приложения."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GeoListViewSet, GeoCreateViewSet

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('history', GeoListViewSet, basename='geo_list')
router_v1.register('query', GeoCreateViewSet, basename='geo_create')
# router_v1.register(
#     r'recipes/(?P<recipe_id>\d+)/favorite',
#     FavoriteViewSet,
#     basename='favorite'
# )
#
# router_v1.register('tags', TagViewSet, basename='tags')
#
# router_v1.register(
#     r'recipes/(?P<recipe_id>\d+)/shopping_cart',
#     ShoppingCartViewSet,
#     basename='shopping_cart'
# )

urlpatterns = [
    path('', include(router_v1.urls)),
    #path('users/<int:user_id>/subscribe/', SubscribeAddDelView.as_view()),
# "/query" - для получения запроса
# “/result" - для отправки результата
# "/ping" - проверка, что  сервер запустился
# “/history” - для получения истории запросов

]
