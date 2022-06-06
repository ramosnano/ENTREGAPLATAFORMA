from django.db import models

class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    duracioncapitulos = models.IntegerField()
    temporadas = models.IntegerField()
    actores = models.CharField(max_length=100)
    creacion =  models.IntegerField()
    SKU = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'serie'
        verbose_name_plural = 'series'