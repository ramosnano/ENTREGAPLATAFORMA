from django.urls import path
from documental.views import products, create_documental_view, search_documental_view

urlpatterns =[
    path('', products, name = 'products'),
    path('crear-documentales/', create_documental_view, name = 'create-documentales'),
    path('buscar-documentales/', search_documental_view, name = 'search_documental_view'),
]