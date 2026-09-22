from django import forms

from .models import Usuario


class UsuarioForm(forms.ModelForm):

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha',
            }
        )
    )

    class Meta:
        model = Usuario

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'cpf',
            'rg',
            'password',
        ]

        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'cpf': 'CPF',
            'rg': 'RG',
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o usuário',
                }
            ),

            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o nome',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o sobrenome',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o e-mail',
                }
            ),

            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o CPF',
                }
            ),

            'rg': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite o RG',
                }
            ),
        }