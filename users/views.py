from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from users.models import User_profile
from django.contrib.auth.mixins import LoginRequiredMixin

class List_profiles(LoginRequiredMixin, ListView):
    model = User_profile
    template_name= 'profiles.html'
    queryset = User_profile.objects.all()