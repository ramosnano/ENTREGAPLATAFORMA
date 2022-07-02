from unicodedata import name
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

from pelicula.models import Movie
from pelicula.forms import Movie_form

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class Create_movie(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'crear_peliculas.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_pelicula', kwargs={'pk':self.object.pk})


class List_movie(ListView):
    model = Movie
    template_name= 'peliculas.html'
    queryset = Movie.objects.all()


class Update_movie(UpdateView):
    model = Movie
    template_name = 'update_pelicula.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_pelicula', kwargs = {'pk':self.object.pk})


class Detail_movie(DetailView):
    model = Movie
    template_name= 'detail_pelicula.html'


class Delete_movie(DeleteView):
    model = Movie
    template_name = 'delete_pelicula.html'

    def get_success_url(self):
        return reverse('list-peliculas')


def search_movie_view(request):
    print(request.GET)
    #product = Products.objects.get()
    products = Movie.objects.filter(nombre__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'buscar_peliculas.html', context = context)
    