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
        'server_answer',
    )
    list_display_links = ('cadastral_number',)
    search_fields = ('cadastral_number', )
    list_filter = ('cadastral_number', 'server_answer')
    empty_value_display = '-пусто-'
