from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from usuarios.models import Usuario

from .forms import VendaForm, ItemVendaForm
from .models import Venda


@login_required
@permission_required('vendas.view_venda', raise_exception=True)
def venda_list(request):
    vendas = Venda.objects.select_related(
        'usuario'
    ).prefetch_related(
        'itens__produto'
    )

    return render(
        request,
        'vendas/venda_list.html',
        {
            'vendas': vendas,
        }
    )


@login_required
@permission_required('vendas.add_venda', raise_exception=True)
def venda_create(request):

    if request.method == 'POST':
        form_item = ItemVendaForm(request.POST)

        if form_item.is_valid():

            usuario = get_object_or_404(
                Usuario,
                pk=request.user.pk
            )

            venda = Venda.objects.create(
                usuario=usuario,
                valor_total=0
            )

            item = form_item.save(commit=False)
            item.venda = venda
            item.save()

            venda.valor_total = (
                item.quantidade *
                item.preco_unitario
            )

            venda.save()

            messages.success(
                request,
                f'Venda #{venda.id} registrada com sucesso!'
            )

            return redirect('vendas:venda_list')

    else:
        form_item = ItemVendaForm()

    return render(
        request,
        'vendas/venda_form.html',
        {
            'form_item': form_item,
        }
    )


@login_required
@permission_required('vendas.view_venda', raise_exception=True)
def venda_detail(request, id):

    venda = get_object_or_404(
        Venda.objects.select_related(
            'usuario'
        ).prefetch_related(
            'itens__produto'
        ),
        id=id
    )

    return render(
        request,
        'vendas/venda_detail.html',
        {
            'venda': venda,
        }
    )


@login_required
@permission_required('vendas.change_venda', raise_exception=True)
def venda_update(request, id):

    venda = get_object_or_404(Venda, id=id)

    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                f'Venda #{venda.id} atualizada com sucesso!'
            )

            return redirect(
                'vendas:venda_detail',
                id=venda.id
            )

    else:
        form = VendaForm(instance=venda)

    return render(
        request,
        'vendas/venda_form.html',
        {
            'form': form,
            'venda': venda,
        }
    )


@login_required
@permission_required('vendas.delete_venda', raise_exception=True)
def venda_delete(request, id):

    venda = get_object_or_404(Venda, id=id)

    if request.method == 'POST':
        venda_id = venda.id
        venda.delete()

        messages.success(
            request,
            f'Venda #{venda_id} excluída com sucesso!'
        )

        return redirect('vendas:venda_list')

    return render(
        request,
        'vendas/venda_confirm_delete.html',
        {
            'venda': venda,
        }
    )