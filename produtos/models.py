from django.db import models
from fornecedores.models import Fornecedor

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Relacionamentos 1:N
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='produtos'
    )
    fornecedor = models.ForeignKey(
        Fornecedor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='produtos'
    )

    def __str__(self):
        return self.nome