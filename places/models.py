from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.TextField()
    description_long = tinymce_models.HTMLField()
    lat = models.FloatField(blank=True, null=True, verbose_name='Широта')
    lng = models.FloatField(blank=True, null=True, verbose_name='Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место')
    geeks_field = models.PositiveIntegerField(db_index=True,
                                              default=0,
                                              blank=False,
                                              null=False,
                                              verbose_name='Позиция')
    image = models.ImageField('Картинка', unique=True)

    class Meta:
        ordering = ['geeks_field']
        unique_together = ['place', 'geeks_field']



    def __str__(self):
        return f'{self.geeks_field} {self.place.title}'
