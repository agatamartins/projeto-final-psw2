from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'cpf', 'rg', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }