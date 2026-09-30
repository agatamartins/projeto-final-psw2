from django import forms
from django.contrib.auth.models import Group

from .models import Usuario


class UsuarioForm(forms.ModelForm):

    grupo = forms.ModelChoiceField(
        queryset=Group.objects.order_by('name'),
        label='Grupo',
        empty_label='Selecione um grupo',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    password = forms.CharField(
        label='Senha',
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha',
                'autocomplete': 'new-password',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = not self.instance.pk
        if self.instance.pk:
            self.fields['grupo'].initial = self.instance.groups.first()