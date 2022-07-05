from unicodedata import name
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

from documental.models import Documental

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class Create_documental(LoginRequiredMixin, CreateView):
    model = Documental
    template_name = 'crear_documentales.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_documental', kwargs={'pk':self.object.pk})


class List_documental(ListView):
    model = Documental
    template_name= 'documentales.html'
    queryset = Documental.objects.all()


class Update_documental(LoginRequiredMixin, UpdateView):
    model = Documental
    template_name = 'update_documental.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_documental', kwargs = {'pk':self.object.pk})


class Detail_documental(DetailView):
    model = Documental
    template_name= 'detail_documental.html'


class Delete_documental(LoginRequiredMixin, DeleteView):
    model = Documental
    template_name = 'delete_documental.html'

    def get_success_url(self):
        return reverse('list-documentales')

def search_documental_view(request):
    print(request.GET)
    products = Documental.objects.filter(nombre__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'buscar_documentales.html', context = context)