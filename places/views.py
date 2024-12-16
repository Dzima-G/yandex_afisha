from django.shortcuts import render
from places.models import Place


def index (request):
    places = Place.objects.all()
    features = []
    for place in places:
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

    data = { 'markers': markers }

    return render(request, 'index.html', context=data)
