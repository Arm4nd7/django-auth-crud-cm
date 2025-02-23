from django import forms
from .models import Mueble
from .models import Cliente

class MuebleForm(forms.ModelForm):
    class Meta:
        model = Mueble
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'material': 'Material',
            'style': 'Estilo',
            'picture': 'Imagen'
            
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'style': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'dni': 'Cedula',
            'email': 'Correo',  
            'gender': 'Genero'          
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={"class": 'form-control'}),
            'gender' : forms.Select(attrs={'class': 'form-control'}),
        }