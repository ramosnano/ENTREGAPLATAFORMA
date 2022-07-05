from django.urls import path
from documental.views import Delete_documental, Detail_documental, List_documental, Create_documental, Update_documental, search_documental_view

urlpatterns =[
    path('', List_documental.as_view(), name = 'list-documentales'),
    path('crear-documentales/', Create_documental.as_view(), name = 'crear-documentales'),
    path('buscar-documentales/', search_documental_view, name = 'search_documental_view'),
    path('detail-documental/<int:pk>/', Detail_documental.as_view(), name = 'detail_documental'),
    path('update-documental/<int:pk>/', Update_documental.as_view(), name = 'update_documental'),
    path('delete-documental/<int:pk>/', Delete_documental.as_view(), name = 'delete_documental'),
]