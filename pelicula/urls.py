from django.urls import path
from pelicula.views import List_movie, Create_movie, search_movie_view, Update_movie, Detail_movie, Delete_movie

urlpatterns =[
    path('', List_movie.as_view(), name = 'list-peliculas'),
    path('crear-peliculas/', Create_movie.as_view(), name = 'create-peliculas'),
    path('buscar-peliculas/', search_movie_view, name = 'search_movie_view'),
    path('detail-pelicula/<int:pk>/', Detail_movie.as_view(), name = 'detail_pelicula'),
    path('update-pelicula/<int:pk>/', Update_movie.as_view(), name = 'update_pelicula'),
    path('delete-pelicula/<int:pk>/', Delete_movie.as_view(), name = 'delete_pelicula'),
]