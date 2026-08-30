from django.shortcuts import render, redirect
from .models import Fornecedor
from .forms import FornecedorForm

def fornecedor_list_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:lista_criar')
    else:
        form = FornecedorForm()

    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/fornecedor_list.html', {
        'fornecedores': fornecedores,
        'form': form
    })