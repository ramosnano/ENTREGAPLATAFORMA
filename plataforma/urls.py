from django.contrib import admin
from plataforma.views import index
from django.urls import path, include

urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('peliculas/', include('pelicula.urls')),
    path('series/', include('serie.urls')), #ACA
    path('documentales/', include('documental.urls')),

]