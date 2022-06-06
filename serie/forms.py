from django import forms
from serie.models import Serie

class Serie_form(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'
