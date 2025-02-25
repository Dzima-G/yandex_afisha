from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Заголовок')
    short_description = models.TextField(
        blank=True,
        verbose_name='Краткое описание')
    long_description = tinymce_models.HTMLField(
        blank=True,
        verbose_name='Полное описание')
    lat = models.FloatField(unique=True, verbose_name='Широта')
    lng = models.FloatField(unique=True, verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    position = models.PositiveIntegerField(
        db_index=True,
        default=0,
        blank=False,
        null=False,
        verbose_name='Позиция'
    )
    image = models.ImageField(verbose_name='Картинка')

    class Meta:
        ordering = ['position']
        unique_together = ['place', 'position', 'image']

    def __str__(self):
        return f'{self.position} {self.place.title}'
