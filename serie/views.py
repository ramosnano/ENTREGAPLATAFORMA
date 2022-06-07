from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from serie.models import Serie
from serie.forms import Serie_form

# Create your views here.
def products(request):
    print(request.method)
    productos = Serie.objects.all()
    context = {'productos':productos}
    return render(request, 'series.html', context=context)

def create_serie_view(request):
    if request.method == 'GET':
        form = Serie_form()
        context = {'form':form}
        return render(request, 'crear_series.html', context=context)
    else:
        form = Serie_form(request.POST)
        if form.is_valid():
            new_serie = Serie.objects.create(
                nombre = form.cleaned_data['nombre'],
                duracioncapitulos = form.cleaned_data['duracioncapitulos'],
                actores = form.cleaned_data['actores'],
                creacion = form.cleaned_data['creacion'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context ={'new_serie':new_serie}
        else:
            context = {'errors':form.errors}
        return render(request, 'crear_series.html', context=context)

def search_serie_view(request):
    print(request.GET)
    #product = Products.objects.get()
    products = Serie.objects.filter(nombre__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'buscar_series.html', context = context)