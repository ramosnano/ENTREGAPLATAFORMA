from django.urls import path
from pelicula.views import products, create_movie_view, search_movie_view

urlpatterns =[
    path('', products, name = 'products'),
    path('crear-peliculas/', create_movie_view, name = 'create-peliculas'),
    path('buscar-peliculas/', search_movie_view, name = 'search_movie_view'),

    # path('', products),
    # path('crear-peliculas/', create_movie_view),
    # path('buscar-peliculas/', search_movie_view),
]