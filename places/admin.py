from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from django.utils.html import format_html

admin.site.register(Image)

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["preview"]
    fields = ('image', 'preview', 'geeks_field')

    def preview(self, obj):
        return format_html("<a>{}</a>",
                    mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')
                    )

@admin.register(Place)
class PlaceForm(admin.ModelAdmin):
    fields = ('title', 'description_short', 'description_long', 'lng', 'lat')
    inlines = [
        ImageInline,
    ]