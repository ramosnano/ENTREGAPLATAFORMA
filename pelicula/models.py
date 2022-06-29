from django.db import models

class Movie(models.Model):
    nombre = models.CharField(max_length=40)
    duracionminutos = models.IntegerField()
    actores = models.CharField(max_length=100)
    creacion =  models.IntegerField()
    SKU = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'pelicula', blank=True, null=True)
    class Meta:
        verbose_name = 'pelicula'
        verbose_name_plural = 'peliculas'

# class Genero(models.Model):
#     tipogenero = models.CharField(max_length=40)

#     class Meta:
#         verbose_name = 'genero'
#         verbose_name_plural = 'generos'

# class Resume(models.Model):
#     sinopsis = models.CharField(max_length=200)

#     class Meta:
#         verbose_name = 'resumen'
#         verbose_name_plural = 'resumen'