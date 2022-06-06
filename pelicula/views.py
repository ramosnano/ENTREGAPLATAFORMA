
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from pelicula.models import Movie
from pelicula.forms import Movie_form

# Create your views here.
def products(request):
    print(request.method)
    productos = Movie.objects.all()
    context = {'productos':productos}
    return render(request, 'peliculas.html', context=context)

def create_movie_view(request):
    if request.method == 'GET':
        form = Movie_form()
        context = {'form':form}
        return render(request, 'crear_peliculas.html', context=context)
    else:
        form = Movie_form(request.POST)
        if form.is_valid():
            new_product = Movie.objects.create(
                nombre = form.cleaned_data['nombre'],
                duracionminutos = form.cleaned_data['duracionminutos'],
                actores = form.cleaned_data['actores'],
                creacion = form.cleaned_data['creacion'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context ={'new_product':new_product}
        return render(request, 'crear_peliculas.html', context=context)

def search_movie_view(request):
    print(request.GET)
    #product = Products.objects.get()
    products = Movie.objects.filter(nombre__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'buscar_peliculas.html', context = context)
