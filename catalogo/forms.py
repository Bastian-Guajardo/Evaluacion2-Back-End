from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'plataforma', 'precio', 'stock']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: Elden Ring'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control bg-dark text-white border-secondary', 'placeholder': 'Ej: PS5, PC, Switch'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control bg-dark text-white border-secondary'}),
        }

    # Validación personalizada para el precio (Mayor que cero)
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor mayor que cero.")
        return precio

    # Validación personalizada para el stock (No negativo)
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser un número negativo.")
        return stock
