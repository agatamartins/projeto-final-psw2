from django.contrib import admin
from .models import Categoria, Fornecedor, Produto, Lote, Venda, ItemVenda

class LoteInline(admin.TabularInline):
    model = Lote
    extra = 1

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'telefone', 'email')
    search_fields = ('razao_social', 'cnpj')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'fornecedor', 'preco_venda', 'unidade_medida')
    list_filter = ('categoria', 'unidade_medida')
    search_fields = ('nome',)
    inlines = [LoteInline]

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('numero_lote', 'produto', 'quantidade', 'data_validade', 'data_entrada')
    list_filter = ('data_validade', 'produto')
    search_fields = ('numero_lote', 'produto__nome')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_venda', 'valor_total')
    inlines = [ItemVendaInline]
