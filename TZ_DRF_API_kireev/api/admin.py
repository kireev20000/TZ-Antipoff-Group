from django.contrib import admin

from .models import GeoData


@admin.register(GeoData)
class GeoDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cadastral_number',
        'longitude',
        'latitude',
        'created',
    )
    list_display_links = ('cadastral_number',)
    search_fields = ('cadastral_number',)
    list_filter = ('cadastral_number',)
    empty_value_display = '-пусто-'
