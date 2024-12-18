from django.shortcuts import render
from places.models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def index(request):
    features = []
    for place in Place.objects.all():
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lat, place.lng]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "static/places/moscow_legends.json"
            }
        })

    markers = {
        "type": "FeatureCollection",
        "features": features
    }

    data = {'markers': markers}

    return render(request, 'index.html', context=data)


def place_view(request, places_id):
    place = get_object_or_404(Place, pk=places_id)
    place_images = Image.objects.filter(place=place)
    serialize_place = {
        "title": place.title,
        "imgs": [img.image.url for img in place_images],
        "description_short": place.description_short,
        "description_long": place.description_long,
            "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(serialize_place, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
