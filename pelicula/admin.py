from django.contrib import admin
from pelicula.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['nombre','duracionminutos','actores', 'SKU']
