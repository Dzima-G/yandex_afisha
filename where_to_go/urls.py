from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('tinymce/', include('tinymce.urls')),
                  path('', views.index),
                  path('places/<int:places_id>/', views.place_view, name='places_id'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
