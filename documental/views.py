from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from documental.models import Documental
from documental.forms import Documental_form

# Create your views here.
def products(request):
    print(request.method)
    productos = Documental.objects.all()
    context = {'productos':productos}
    return render(request, 'documentales.html', context=context)

def create_documental_view(request):
    if request.method == 'GET':
        form = Documental_form()
        context = {'form':form}
        return render(request, 'crear_documentales.html', context=context)
    else:
        form = Documental_form(request.POST)
        if form.is_valid():
            new_docu = Documental.objects.create(
                nombre = form.cleaned_data['nombre'],
                duracionminutos = form.cleaned_data['duracionminutos'],
                actores = form.cleaned_data['actores'],
                creacion = form.cleaned_data['creacion'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context ={'new_docu':new_docu}
        return render(request, 'crear_documentales.html', context=context)

def search_documental_view(request):
    print(request.GET)
    #product = Products.objects.get()
    products = Documental.objects.filter(nombre__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'buscar_documentales.html', context = context)