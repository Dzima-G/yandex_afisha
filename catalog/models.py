from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField()
    published_date = models.DateField()

    def __str__(self):
        return self.title