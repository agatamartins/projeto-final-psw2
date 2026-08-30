from django.shortcuts import render, redirect
from .models import Venda, ItemVenda
from .forms import ItemVendaForm

def venda_list_create(request):
    if request.method == 'POST':
        form_item = ItemVendaForm(request.POST)
        if form_item.is_valid():
            # 1. Cria a Venda vinculando o usuário logado
            venda = Venda.objects.create(
                usuario=request.user,
                valor_total=0
            )
            # 2. Salva o item relacionado
            item = form_item.save(commit=False)
            item.venda = venda
            item.save()

            # 3. Atualiza o total
            venda.valor_total = item.quantidade * item.preco_unitario
            venda.save()

            return redirect('vendas:lista_criar')
    else:
        form_item = ItemVendaForm()

    vendas = Venda.objects.all()
    return render(request, 'vendas/venda_list.html', {
        'vendas': vendas,
        'form_item': form_item
    })