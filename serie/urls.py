from django.urls import path
from serie.views import List_serie, Create_serie, search_serie_view, Update_serie, Detail_serie, Delete_serie

urlpatterns =[
    path('', List_serie.as_view(), name = 'list_series'),
    path('crear-series/', Create_serie.as_view(), name = 'create-series'),
    path('buscar-series/', search_serie_view, name = 'search_serie_view'),
    path('detail-serie/<int:pk>/', Detail_serie.as_view(), name = 'detail_serie'),
    path('update-serie/<int:pk>/', Update_serie.as_view(), name = 'update_serie'),
    path('delete-serie/<int:pk>/', Delete_serie.as_view(), name = 'delete_serie'),
]