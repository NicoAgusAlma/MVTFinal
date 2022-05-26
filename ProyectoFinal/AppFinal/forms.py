from django import forms

class UsuarioFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    mail=forms.EmailField()
    password=forms.CharField(max_length=40)
    nacimiento=forms.DateField(help_text='mm/dd/aaaa')

class DireccionFormulario(forms.Form):
    pais=forms.CharField(max_length=40)
    provincia=forms.CharField(max_length=40)
    localidad=forms.CharField(max_length=40)
    calle=forms.CharField(max_length=40)
    numero=forms.IntegerField()
    provincia=forms.CharField(max_length=40)

class EstudioFormulario(forms.Form):
    institucion=forms.CharField(max_length=40)
    carrera=forms.CharField(max_length=40)
    tiempoCursado=forms.IntegerField(help_text='Años enteros')
    egresado=forms.BooleanField(required=False)
   