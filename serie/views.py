from unicodedata import name
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

from serie.models import Serie
from serie.forms import Serie_form

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class Create_serie(LoginRequiredMixin, CreateView):
    model = Serie
    template_name = 'crear_series.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_serie', kwargs={'pk':self.object.pk})

class List_serie(ListView):
    model = Serie
    template_name= 'series.html'
    queryset = Serie.objects.all()

class Update_serie(LoginRequiredMixin, UpdateView):
    model = Serie
    template_name = 'update_serie.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_serie', kwargs = {'pk':self.object.pk})
    
class Detail_serie(DetailView):
    model = Serie
    template_name= 'detail_serie.html'

class Delete_serie(LoginRequiredMixin, DeleteView):
    model = Serie
    template_name = 'delete_serie.html'

    def get_success_url(self):
        return reverse('list_series')

def search_serie_view(request):
    print(request.GET)
    series = Serie.objects.filter(nombre__contains = request.GET['search'])
    context = {'products':series}
    return render(request, 'buscar_series.html', context = context)