from django.contrib import admin
from django.http import HttpResponse
from plataforma.views import index, login_view, logout_view, register_view, about
from users.views import List_profiles
from serie.views import Detail_serie
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),
    path('about/', about, name = 'about'),
    path('peliculas/', include('pelicula.urls')),
    path('series/', include('serie.urls')),
    path('documentales/', include('documental.urls')),

    path('accounts/login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('accounts/signup/', register_view, name = 'register'),
    path('accounts/profile/', List_profiles.as_view(), name = 'profiles'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

