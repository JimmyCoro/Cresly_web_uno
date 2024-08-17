from django import forms
from .models import Pizza, Alitas,  Bebida

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