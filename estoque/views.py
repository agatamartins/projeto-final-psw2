from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm

# 1. READ (Listagem)
@login_required
def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/produto_list.html', {'produtos': produtos})

# 2. DETAIL VIEW (Detalhes) - Requisito do edital
@login_required
def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    lotes = produto.lotes.all() # Histórico de lotes deste produto
    return render(request, 'estoque/produto_detail.html', {'produto': produto, 'lotes': lotes})

# 3. CREATE (Criação)
@login_required
def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/produto_form.html', {'form': form, 'titulo': 'Cadastrar Produto'})

# 4. UPDATE (Edição)
@login_required
def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/produto_form.html', {'form': form, 'titulo': 'Editar Produto'})

# 5. DELETE (Exclusão)
@login_required
def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto removido com sucesso!')
        return redirect('produto_list')
    return render(request, 'estoque/produto_confirm_delete.html', {'produto': produto})