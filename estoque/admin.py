from django.contrib import admin
from .models import Categoria, Fornecedor, Produto, Usuario, Venda, ItemVenda

# Configuração para exibir os itens dentro da tela de Venda no Admin
class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_venda', 'valor_total')
    inlines = [ItemVendaInline]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_venda', 'estoque_minimo', 'categoria', 'fornecedor')
    list_filter = ('categoria', 'fornecedor')
    search_fields = ('nome',)

# Registro dos demais modelos
admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Usuario)