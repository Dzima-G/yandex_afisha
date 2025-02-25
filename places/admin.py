from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Image, Place


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)


class ImageInline(SortableTabularInline, admin.TabularInline):
    model = Image
    readonly_fields = ['preview']
    fields = ('image', 'preview', 'position')

    def preview(self, obj):
        return format_html(
            '<a>{}</a>',
            mark_safe(
                f'<img src="{obj.image.url}"'
                f' style="max-height: 200px; max-width: 200px;">'))

    def get_extra(self, request, obj=None, **kwargs):

        return 1


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('title', 'short_description', 'long_description', 'lng', 'lat')
    inlines = [
        ImageInline,
    ]
