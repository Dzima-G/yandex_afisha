import sys
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help=u'Ссылка на json файл с данными для добавления локации')

    def handle(self, *args, **kwargs):
        url = kwargs['url']

        def get_response(url):
            response = requests.get(url)
            response.raise_for_status()
            return response


        def get_image_name(uri):
            path = urlparse(uri).path
            return path.rstrip("/").split("/")[-1]

        def add_place(geo_json):
           Place.objects.get_or_create(
                title=geo_json.get('title'),
                short_description=geo_json.get('description_short'),
                long_description=geo_json.get('description_long'),
                lat=geo_json.get('coordinates').get('lng'),
                lng=geo_json.get('coordinates').get('lat'),
            )


        def add_image(geo_json, place):
            for number, uri in enumerate(geo_json.get('imgs'), 1):
                photo = get_response(uri)
                content = ContentFile(photo.content)
                image = Image.objects.create(place=place, position=number)
                image.image.save(get_image_name(uri), content, save=True)


        try:
            response = get_response(url).json()
            add_place(response)
            place = Place.objects.get(title=response.get('title'))
            add_image(response, place)
        except requests.exceptions.HTTPError as error:
            print(error, file=sys.stderr)
