from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    palace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место')
    geeks_field = models.PositiveIntegerField(verbose_name='Расположение')
    image = models.ImageField('Картинка')

    def __str__(self):
        return f'{self.geeks_field} {self.palace.title}'