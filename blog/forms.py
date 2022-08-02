from django import forms
from django.db import models



class FormLibro(forms.Form):
    titulo = forms.CharField(max_length=30)
    editorial = forms.CharField(max_length=30)
    fecha_de_publicación = forms.DateField(required=False)


    

    
class busquedaLibro(forms.Form):
    titulo= forms.CharField(max_length=30, required=False)
 