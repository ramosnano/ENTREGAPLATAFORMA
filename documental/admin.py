from django.contrib import admin
from documental.models import Documental

@admin.register(Documental)
class DocumentalAdmin(admin.ModelAdmin):
    list_display = ['nombre','duracionminutos', 'actores', 'SKU']