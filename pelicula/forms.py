from django import forms
from pelicula.models import Movie

class Movie_form(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
