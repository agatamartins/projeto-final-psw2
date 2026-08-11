from django import forms
from .models import Produto  # Subsitua pelo nome real do seu Model se for diferente

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  # Exibe todos os campos do Model no formulário