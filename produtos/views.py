from django.shortcuts import render, redirect
from .models import Categoria, Produto
from .forms import CategoriaForm, ProdutoForm

def categoria_list_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:categoria_lista_criar')
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    return render(request, 'produtos/categoria_list.html', {
        'categorias': categorias,
        'form': form
    })

def produto_list_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:produto_lista_criar')
    else:
        form = ProdutoForm()

    produtos = Produto.objects.all()
    return render(request, 'produtos/produto_list.html', {
        'produtos': produtos,
        'form': form
    })