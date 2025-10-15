from django import forms
from django.core.validators import RegexValidator

class CustomerForm(forms.Form):
    name = forms.CharField(
        label="Nombre y Apellido",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded'})
    )
    phone = forms.CharField(
        label="Número de Teléfono (con código de país, ej: +543834653289)",
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+\d{8,15}$',
                message="Ingresa un número de teléfono válido con código de país (ej: +543834653289)."
            )
        ],
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': '+543834653289'})
    )
