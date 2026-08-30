from django import forms
from .models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco_venda', 'estoque_minimo', 'categoria', 'fornecedores']

        widgets = {
            'fornecedores': forms.CheckboxSelectMultiple(),
        }