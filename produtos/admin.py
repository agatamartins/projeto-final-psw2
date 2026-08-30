from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Em vez de 'fornecedores', chamamos o método 'exibir_fornecedores'
    list_display = ('nome', 'preco_venda', 'estoque_minimo', 'categoria', 'exibir_fornecedores')

    # Método que pega os fornecedores e junta em uma string (ex: "Fornecedor A, Fornecedor B")
    def exibir_fornecedores(self, obj):
        return ", ".join([f.razao_social for f in obj.fornecedores.all()])
    
    # Define o nome que aparecerá no cabeçalho da coluna no admin
    exibir_fornecedores.short_description = 'Fornecedores'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')