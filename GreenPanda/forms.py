from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import MetodoPago, Proveedor

class ProveedorForm(forms.ModelForm):

    class Meta:
        model= Proveedor
        fields = ['numId', 'Nombre', 'telefono', 'Direccion', 'Email', 'Pais', 'Contrasenna', 'MetodoPago', 'Imagen']
        labels ={
            'numId': 'Número de Identificación',
            'Nombre': 'Nombre Completo',
            'telefono': 'Teléfono',
            'Direccion': 'Dirección',
            'Email': 'Email',
            'Pais': 'País',
            'Contrasenna': 'Contraseña',
            'MetodoPago': 'Metodo de Pago',
        }
        widgets={
            'numId': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese número de Identificación',
                    'id': 'num',
                    'onkeyup': 'myFunction();'
                }
            ),
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre',
                    'id': 'nom',
                    'pattern': '[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+',
                    'onkeyup': 'myFunction();'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese número de Teléfono',
                    'id': 'tel',
                    'pattern': '[0-9\s]+',
                    'onkeyup': 'myFunction();'
                }
            ),
            'Direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Direccion',
                    'id': 'dir'
                }
            ),
            'Email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Email',
                    'id': 'ema'
                }
            ),
            'Pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese País',
                    'id': 'pai',
                    'pattern': '[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+',
                    'onkeyup': 'myFunction();'
                }
            ),
            'Contrasenna': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'con',
                    'readonly':'readonly'
                }
            ),
            'MetodoPago': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'met',
                }
            )
        }