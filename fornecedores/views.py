from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FornecedorForm
from .models import Fornecedor


# ==========================================================
# LISTAR FORNECEDORES
# ==========================================================

@login_required
@permission_required(
    'fornecedores.view_fornecedor',
    raise_exception=True
)
def fornecedor_list(request):

    fornecedores = Fornecedor.objects.all()

    return render(
        request,
        'fornecedores/fornecedor_list.html',
        {
            'fornecedores': fornecedores,
        }
    )


# ==========================================================
# CRIAR FORNECEDOR
# ==========================================================

@login_required
@permission_required(
    'fornecedores.add_fornecedor',
    raise_exception=True
)
def fornecedor_create(request):

    if request.method == 'POST':

        form = FornecedorForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Fornecedor cadastrado com sucesso!'
            )

            return redirect(
                'fornecedores:fornecedor_list'
            )

    else:

        form = FornecedorForm()

    return render(
        request,
        'fornecedores/fornecedor_form.html',
        {
            'form': form,
            'titulo': 'Cadastrar fornecedor',
        }
    )


# ==========================================================
# DETALHES DO FORNECEDOR
# ==========================================================

@login_required
@permission_required(
    'fornecedores.view_fornecedor',
    raise_exception=True
)
def fornecedor_detail(request, id):

    fornecedor = get_object_or_404(
        Fornecedor,
        id=id
    )

    return render(
        request,
        'fornecedores/fornecedor_detail.html',
        {
            'fornecedor': fornecedor,
        }
    )


# ==========================================================
# EDITAR FORNECEDOR
# ==========================================================

@login_required
@permission_required(
    'fornecedores.change_fornecedor',
    raise_exception=True
)
def fornecedor_update(request, id):

    fornecedor = get_object_or_404(
        Fornecedor,
        id=id
    )

    if request.method == 'POST':

        form = FornecedorForm(
            request.POST,
            instance=fornecedor
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Fornecedor atualizado com sucesso!'
            )

            return redirect(
                'fornecedores:fornecedor_detail',
                id=fornecedor.id
            )

    else:

        form = FornecedorForm(
            instance=fornecedor
        )

    return render(
        request,
        'fornecedores/fornecedor_form.html',
        {
            'form': form,
            'titulo': 'Editar fornecedor',
            'fornecedor': fornecedor,
        }
    )


# ==========================================================
# EXCLUIR FORNECEDOR
# ==========================================================

@login_required
@permission_required(
    'fornecedores.delete_fornecedor',
    raise_exception=True
)
def fornecedor_delete(request, id):

    fornecedor = get_object_or_404(
        Fornecedor,
        id=id
    )

    if request.method == 'POST':

        fornecedor.delete()

        messages.success(
            request,
            'Fornecedor excluído com sucesso!'
        )

        return redirect(
            'fornecedores:fornecedor_list'
        )

    return render(
        request,
        'fornecedores/fornecedor_confirm_delete.html',
        {
            'fornecedor': fornecedor,
        }
    )