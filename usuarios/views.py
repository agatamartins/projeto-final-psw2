from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def usuario_list_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Cria o usuário criptografando a senha
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('usuarios:lista_criar')
    else:
        form = UsuarioForm()

    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuario_list.html', {
        'usuarios': usuarios,
        'form': form
    })