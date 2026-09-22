from django import forms

from .models import Categoria, Produto


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = [
            'nome',
            'descricao',
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da categoria',
                }
            ),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição da categoria',
                    'rows': 4,
                }
            ),
        }


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto

        fields = [
            'nome',
            'preco_venda',
            'estoque_minimo',
            'categoria',
            'fornecedor',
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome do produto',
                }
            ),

            'preco_venda': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                    'placeholder': '0,00',
                }
            ),

            'estoque_minimo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                    'placeholder': '0,00',
                }
            ),

            'categoria': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),

            'fornecedor': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }