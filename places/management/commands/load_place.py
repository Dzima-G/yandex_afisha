import logging
import sys
import time
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help=u'Link to json file with data for adding location'
        )

    def handle(self, *args, **kwargs):
        url = kwargs['url']

        def get_response(url):
            response = requests.get(url)
            response.raise_for_status()
            return response

        def get_image_name(uri):
            path = urlparse(uri).path
            return path.rstrip('/').split('/')[-1]

        def add_place(payload):
            place, created = Place.objects.get_or_create(
                title=payload.get('title'),
                defaults={
                    'short_description': payload.get('description_short'),
                    'long_description': payload.get('description_long'),
                    'lat': payload.get('coordinates').get('lng'),
                    'lng': payload.get('coordinates').get('lat')
                }
            )

            if not created:
                sys.exit('The place has already been added earlier!')

            return place

        def add_image(place_raw, place):
            for number, uri in enumerate(place_raw.get('imgs'), 1):
                image = get_image_name(uri)
                try:
                    photo = get_response(uri)
                    Image.objects.get_or_create(
                        place=place,
                        image=image,
                        position=number,
                        defaults={'image': ContentFile(photo.content, image), }
                    )

                except requests.exceptions.HTTPError as error:
                    print(error, file=sys.stderr)
                    continue
                except requests.exceptions.ConnectionError:
                    logger.warning('Do not connect to the server!!'
                                   ' Reconnecting in 10 seconds.')
                    time.sleep(10)

        try:
            response = get_response(url).json()
            place = add_place(response)
            add_image(response, place)
        except requests.exceptions.HTTPError as error:
            print(error, file=sys.stderr)
        except requests.exceptions.ConnectionError:
            logger.warning('Do not connect to the server!!'
                           ' Reconnecting in 10 seconds.')
            time.sleep(10)
