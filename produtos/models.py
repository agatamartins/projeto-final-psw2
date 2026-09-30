from django.db import models

from fornecedores.models import Fornecedor


class Categoria(models.Model):

    nome = models.CharField(max_length=100)

    descricao = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):

    nome = models.CharField(max_length=150)

    preco_venda = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estoque_minimo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    fornecedores = models.ManyToManyField(
        Fornecedor,
        blank=True,
        related_name='produtos'
    )

    def __str__(self):
        return self.nome