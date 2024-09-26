from django import forms
from .models import ComboFamiliar, Pizza, Alitas,  Bebida

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['sabor_1', 'sabor_2']
        
        widgets = {
            'sabor_1': forms.Select(attrs={'class': 'form-select'}),
            'sabor_2': forms.Select(attrs={'class': 'form-select'}),
}
        
        
class AlitaForm(forms.ModelForm):
    class Meta:
        model = Alitas
        fields = ['sabor_1', 'sabor_2']
        
        widgets = {
            'sabor_1': forms.Select(attrs={'class': 'form-select'}),
            'sabor_2': forms.Select(attrs={'class': 'form-select'}),
}
        
class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ['sabor']
        
        widgets = {
            'sabor': forms.Select(attrs={'class': 'form-select'}),
}


# forms.py

class ComboFamiliarForm(forms.ModelForm):
    class Meta:
        model = ComboFamiliar
        fields = ['pizza_sabor_1', 'pizza_sabor_2', 'alita_sabor_1', 'alita_sabor_2', 'bebida_sabor']
        
        widgets = {
            'pizza_sabor_1': forms.Select(attrs={'class': 'form-select'}),
            'pizza_sabor_2': forms.Select(attrs={'class': 'form-select'}),
            'alita_sabor_1': forms.Select(attrs={'class': 'form-select'}),
            'alita_sabor_2': forms.Select(attrs={'class': 'form-select'}),
            'bebida_sabor': forms.Select(attrs={'class': 'form-select'}),
        }
