from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=150, verbose_name="Razão Social")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.razao_social


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    # Relacionamento 1:N (Uma Categoria -> Muitos Produtos)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")
    # Relacionamento 1:N (Um Fornecedor -> Muitos Produtos)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, related_name="produtos")
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de Venda")
    unidade_medida = models.CharField(
        max_length=10, 
        choices=[('KG', 'Quilograma'), ('UN', 'Unidade'), ('L', 'Litro')],
        default='KG'
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.nome} ({self.get_unidade_medida_display()})"


class Lote(models.Model):
    # Relacionamento 1:N (Um Produto -> Muitos Lotes)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="lotes")
    numero_lote = models.CharField(max_length=50, verbose_name="Número do Lote")
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Quantidade em Estoque")
    data_validade = models.DateField(verbose_name="Data de Validade")
    data_entrada = models.DateField(auto_now_add=True, verbose_name="Data de Entrada")

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"

    def __str__(self):
        return f"Lote {self.numero_lote} - {self.produto.nome}"


class Venda(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True, verbose_name="Data/Hora da Venda")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Valor Total")
    # Relacionamento N:N entre Venda e Produto através da tabela intermediária ItemVenda
    produtos = models.ManyToManyField(Produto, through='ItemVenda', related_name="vendas")

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    def __str__(self):
        return f"Venda #{self.id} - {self.data_venda.strftime('%d/%m/%Y %H:%M')}"


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário")

    class Meta:
        verbose_name = "Item da Venda"
        verbose_name_plural = "Itens da Venda"

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} na Venda #{self.venda.id}"
