from django import forms
from documental.models import Documental

class Documental_form(forms.ModelForm):
    class Meta:
        model = Documental
        fields = '__all__'