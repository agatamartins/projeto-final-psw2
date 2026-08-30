from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.db import transaction

# Importe os modelos do seu app estoque
from .models import Categoria, Fornecedor, Produto, Venda, ItemVenda, Usuario
# Importe os formulários que criou no forms.py
from .forms import CategoriaForm, FornecedorForm, ProdutoForm


# ==========================================
# 1. CRUD CATEGORIA
# ==========================================
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('categoria_list')


# ==========================================
# 2. CRUD FORNECEDOR
# ==========================================
class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedor_list.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedor_list')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedor_list')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('fornecedor_list')


# ==========================================
# 3. CRUD PRODUTO
# ==========================================
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('produto_list')


# ==========================================
# 4. REGISTRO DE VENDA
# ==========================================
@login_required
def realizar_venda(request):
    produtos = Produto.objects.all()

    if request.method == 'POST':
        usuario_logado = Usuario.objects.get(user=request.user)

        produtos_ids = request.POST.getlist('produto_id')
        quantidades = request.POST.getlist('quantidade')

        if produtos_ids and quantidades:
            with transaction.atomic():
                venda = Venda.objects.create(
                    usuario=usuario_logado,
                    valor_total=0
                )

                total_venda = 0

                for p_id, qtd in zip(produtos_ids, quantidades):
                    if int(qtd) > 0:
                        prod = Produto.objects.get(id=p_id)
                        subtotal = prod.preco_venda * int(qtd)
                        total_venda += subtotal

                        ItemVenda.objects.create(
                            venda=venda,
                            produto=prod,
                            quantidade=int(qtd),
                            preco_unitario=prod.preco_venda
                        )

                venda.valor_total = total_venda
                venda.save()

                return redirect('produto_list')

    return render(request, 'venda_form.html', {'produtos': produtos})