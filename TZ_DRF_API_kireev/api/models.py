from django.db import models


class GeoData(models.Model):
    cadastral_number = models.CharField(
        'Кадастровый номер',
        max_length=100,
        )
    longitude = models.FloatField()
    latitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    server_answer = models.BooleanField(null=True)

    class Meta:
        ordering = ['-created', ]
        verbose_name = 'Кадастровый номер'
        verbose_name_plural = 'Кадастровые номера'

    def __str__(self):
        return self.cadastral_number
