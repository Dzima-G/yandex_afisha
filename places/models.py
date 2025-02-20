from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Заголовок')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    long_description = tinymce_models.HTMLField(blank=True, verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта', default=0.00,)
    lng = models.FloatField(verbose_name='Долгота', default=0.00,)

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
    image = models.ImageField('Картинка', unique=True)

    class Meta:
        ordering = ['position']
        unique_together = ['place', 'position']



    def __str__(self):
        return f'{self.position} {self.place.title}'
