from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'data-icon': 'bi-lock'  # Añadir un atributo personalizado para el icono
        })
    )
    
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'data-icon': 'bi-envelope'  # Icono para correo electrónico
        })
    )
    
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre',
            'data-icon': 'bi-person'  # Icono para nombre
        })
    )
    
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido',
            'data-icon': 'bi-person'  # Icono para apellido
        })
    )

    class Meta:
        model = Cliente
        fields = ['correo', 'nombre', 'apellido', 'password']
