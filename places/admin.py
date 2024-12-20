from django.contrib import admin
from .models import Place, Image


admin.site.register(Image)

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'geeks_field')

@admin.register(Place)
class PlaceForm(admin.ModelAdmin):
    fields = ('title', 'description_short', 'description_long', 'lng', 'lat')
    inlines = [
        ImageInline,
    ]