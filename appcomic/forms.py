from django import forms

class BusquedaComic(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)