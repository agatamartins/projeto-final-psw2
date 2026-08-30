from django.db import models
from django.conf import settings
from produtos.models import Produto

class Venda(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Relacionamento 1:N com o Usuario customizado
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='vendas'
    )

    def __str__(self):
        return f"Venda #{self.id} - {self.data_venda.strftime('%d/%m/%Y')}"

class ItemVenda(models.Model):
    quantidade = models.IntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Tabela intermediária para a relação N:N entre Venda e Produto
    venda = models.ForeignKey(
        Venda, 
        on_delete=models.CASCADE, 
        related_name='itens'
    )
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.PROTECT, 
        related_name='itens_venda'
    )

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Venda #{self.venda.id})"