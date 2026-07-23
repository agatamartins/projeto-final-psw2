from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.razao_social

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    codigo_barras = models.CharField(max_length=50, unique=True)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome

class Lote(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='lotes')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, related_name='lotes')
    quantidade = models.IntegerField()
    data_entrada = models.DateField(auto_now_add=True)
    data_validade = models.DateField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Lote {self.id} - {self.produto.nome}"

    @property
    def status_validade(self):
        """Retorna a situação de risco do lote para uso nas cores do Dashboard."""
        hoje = date.today()
        dias_restantes = (self.data_validade - hoje).days

        if dias_restantes < 0:
            return {'status': 'Vencido', 'cor': 'danger', 'dias': dias_restantes} # Vermelho
        elif dias_restantes <= 7:
            return {'status': 'Crítico', 'cor': 'warning', 'dias': dias_restantes} # Amarelo/Laranja
        else:
            return {'status': 'Ok', 'cor': 'success', 'dias': dias_restantes}     # Verde

class Venda(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Venda #{self.id} em {self.data_venda.strftime('%d/%m/%Y')}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)