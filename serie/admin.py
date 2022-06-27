from django.contrib import admin
from serie.models import Serie

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracioncapitulos', 'actores', 'SKU']




