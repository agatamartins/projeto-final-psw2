from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm, ProdutoForm
from .models import Categoria, Produto


# ==========================================================
# CATEGORIAS
# ==========================================================

@login_required
@permission_required(
    'produtos.view_categoria',
    raise_exception=True
)
def categoria_list(request):

    categorias = Categoria.objects.all()

    return render(
        request,
        'produtos/categoria_list.html',
        {
            'categorias': categorias,
        }
    )


@login_required
@permission_required(
    'produtos.add_categoria',
    raise_exception=True
)
def categoria_create(request):

    if request.method == 'POST':

        form = CategoriaForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Categoria cadastrada com sucesso!'
            )

            return redirect(
                'produtos:categoria_list'
            )

    else:

        form = CategoriaForm()

    return render(
        request,
        'produtos/categoria_form.html',
        {
            'form': form,
            'titulo': 'Cadastrar categoria',
        }
    )


@login_required
@permission_required(
    'produtos.view_categoria',
    raise_exception=True
)
def categoria_detail(request, id):

    categoria = get_object_or_404(
        Categoria,
        id=id
    )

    return render(
        request,
        'produtos/categoria_detail.html',
        {
            'categoria': categoria,
        }
    )


@login_required
@permission_required(
    'produtos.change_categoria',
    raise_exception=True
)
def categoria_update(request, id):

    categoria = get_object_or_404(
        Categoria,
        id=id
    )

    if request.method == 'POST':

        form = CategoriaForm(
            request.POST,
            instance=categoria
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Categoria atualizada com sucesso!'
            )

            return redirect(
                'produtos:categoria_detail',
                id=categoria.id
            )

    else:

        form = CategoriaForm(
            instance=categoria
        )

    return render(
        request,
        'produtos/categoria_form.html',
        {
            'form': form,
            'titulo': 'Editar categoria',
            'categoria': categoria,
        }
    )


@login_required
@permission_required(
    'produtos.delete_categoria',
    raise_exception=True
)
def categoria_delete(request, id):

    categoria = get_object_or_404(
        Categoria,
        id=id
    )

    if request.method == 'POST':

        categoria.delete()

        messages.success(
            request,
            'Categoria excluída com sucesso!'
        )

        return redirect(
            'produtos:categoria_list'
        )

    return render(
        request,
        'produtos/categoria_confirm_delete.html',
        {
            'categoria': categoria,
        }
    )


# ==========================================================
# PRODUTOS
# ==========================================================

@login_required
@permission_required(
    'produtos.view_produto',
    raise_exception=True
)
def produto_list(request):

    produtos = Produto.objects.select_related(
        'categoria',
        'fornecedor'
    )

    return render(
        request,
        'produtos/produto_list.html',
        {
            'produtos': produtos,
        }
    )


@login_required
@permission_required(
    'produtos.add_produto',
    raise_exception=True
)
def produto_create(request):

    if request.method == 'POST':

        form = ProdutoForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Produto cadastrado com sucesso!'
            )

            return redirect(
                'produtos:produto_list'
            )

    else:

        form = ProdutoForm()

    return render(
        request,
        'produtos/produto_form.html',
        {
            'form': form,
            'titulo': 'Cadastrar produto',
        }
    )


@login_required
@permission_required(
    'produtos.view_produto',
    raise_exception=True
)
def produto_detail(request, id):

    produto = get_object_or_404(
        Produto.objects.select_related(
            'categoria',
            'fornecedor'
        ),
        id=id
    )

    return render(
        request,
        'produtos/produto_detail.html',
        {
            'produto': produto,
        }
    )


@login_required
@permission_required(
    'produtos.change_produto',
    raise_exception=True
)
def produto_update(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    if request.method == 'POST':

        form = ProdutoForm(
            request.POST,
            instance=produto
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Produto atualizado com sucesso!'
            )

            return redirect(
                'produtos:produto_detail',
                id=produto.id
            )

    else:

        form = ProdutoForm(
            instance=produto
        )

    return render(
        request,
        'produtos/produto_form.html',
        {
            'form': form,
            'titulo': 'Editar produto',
            'produto': produto,
        }
    )


@login_required
@permission_required(
    'produtos.delete_produto',
    raise_exception=True
)
def produto_delete(request, id):

    produto = get_object_or_404(
        Produto,
        id=id
    )

    if request.method == 'POST':

        produto.delete()

        messages.success(
            request,
            'Produto excluído com sucesso!'
        )

        return redirect(
            'produtos:produto_list'
        )

    return render(
        request,
        'produtos/produto_confirm_delete.html',
        {
            'produto': produto,
        }
    )