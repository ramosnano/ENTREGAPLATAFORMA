from django.urls import path
from serie.views import products, create_serie_view, search_serie_view

urlpatterns =[
    path('', products, name = 'products'),
    path('crear-series/', create_serie_view, name = 'create-series'),
    path('buscar-series/', search_serie_view, name = 'search_series_view'),

    # path('', products),
    # path('crear-peliculas/', create_movie_view),
    # path('buscar-peliculas/', search_movie_view),
]