from django.contrib import admin
from django.http import HttpResponse
from plataforma.views import index, login_view, logout_view, register_view, about
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('about/', about, name = 'about'),
    path('peliculas/', include('pelicula.urls')),
    path('series/', include('serie.urls')), #ACA
    path('documentales/', include('documental.urls')),

    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

