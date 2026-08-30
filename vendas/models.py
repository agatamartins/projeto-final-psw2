from django.db import models
from usuarios.models import Usuario
from produtos.models import Produto

class Venda(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='vendas')

    def __str__(self):
        return f"Venda #{self.id} - {self.usuario.username}"

class ItemVenda(models.Model):
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens_venda')

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Venda #{self.venda.id})"