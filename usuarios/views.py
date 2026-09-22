from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import UsuarioForm
from .models import Usuario


# ==========================================================
# LOGIN
# ==========================================================

def login_view(request):

    if request.user.is_authenticated:
        return redirect('produtos:produto_list')

    form = AuthenticationForm(
        request,
        data=request.POST or None
    )

    # Estilização Bootstrap
    form.fields['username'].widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Digite seu usuário',
    })

    form.fields['password'].widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Digite sua senha',
    })

    if request.method == 'POST':

        if form.is_valid():

            usuario = form.get_user()

            login(request, usuario)

            messages.success(
                request,
                f'Bem-vindo(a), {usuario.username}!'
            )

            proxima_url = (
                request.POST.get('next')
                or request.GET.get('next')
            )

            if proxima_url and url_has_allowed_host_and_scheme(
                proxima_url,
                allowed_hosts={request.get_host()}
            ):
                return redirect(proxima_url)

            return redirect('produtos:produto_list')

        messages.error(
            request,
            'Usuário ou senha inválidos.'
        )

    return render(
        request,
        'login.html',
        {
            'form': form,
            'next': request.GET.get('next', ''),
        }
    )


# ==========================================================
# LOGOUT
# ==========================================================

@login_required
def logout_view(request):

    if request.method == 'POST':

        logout(request)

        messages.success(
            request,
            'Você saiu do sistema com sucesso.'
        )

        return redirect('login')

    return render(
        request,
        'usuarios/logout_confirm.html'
    )


# ==========================================================
# LISTAR USUÁRIOS
# ==========================================================

@login_required
@permission_required(
    'usuarios.view_usuario',
    raise_exception=True
)
def usuario_list(request):

    usuarios = Usuario.objects.all()

    return render(
        request,
        'usuarios/usuario_list.html',
        {
            'usuarios': usuarios,
        }
    )


# ==========================================================
# CRIAR USUÁRIO
# ==========================================================

@login_required
@permission_required(
    'usuarios.add_usuario',
    raise_exception=True
)
def usuario_create(request):

    if request.method == 'POST':

        form = UsuarioForm(request.POST)

        if form.is_valid():

            usuario = form.save(commit=False)

            usuario.set_password(
                form.cleaned_data['password']
            )

            usuario.save()

            messages.success(
                request,
                'Usuário cadastrado com sucesso!'
            )

            return redirect(
                'usuarios:usuario_list'
            )

    else:

        form = UsuarioForm()

    return render(
        request,
        'usuarios/usuario_form.html',
        {
            'form': form,
            'titulo': 'Cadastrar usuário',
        }
    )


# ==========================================================
# DETALHES DO USUÁRIO
# ==========================================================

@login_required
@permission_required(
    'usuarios.view_usuario',
    raise_exception=True
)
def usuario_detail(request, id):

    usuario = get_object_or_404(
        Usuario,
        id=id
    )

    return render(
        request,
        'usuarios/usuario_detail.html',
        {
            'usuario': usuario,
        }
    )


# ==========================================================
# EDITAR USUÁRIO
# ==========================================================

@login_required
@permission_required(
    'usuarios.change_usuario',
    raise_exception=True
)
def usuario_update(request, id):

    usuario = get_object_or_404(
        Usuario,
        id=id
    )

    if request.method == 'POST':

        form = UsuarioForm(
            request.POST,
            instance=usuario
        )

        if form.is_valid():

            usuario = form.save(commit=False)

            usuario.set_password(
                form.cleaned_data['password']
            )

            usuario.save()

            messages.success(
                request,
                'Usuário atualizado com sucesso!'
            )

            return redirect(
                'usuarios:usuario_detail',
                id=usuario.id
            )

    else:

        form = UsuarioForm(instance=usuario)

    return render(
        request,
        'usuarios/usuario_form.html',
        {
            'form': form,
            'titulo': 'Editar usuário',
            'usuario': usuario,
        }
    )


# ==========================================================
# EXCLUIR USUÁRIO
# ==========================================================

@login_required
@permission_required(
    'usuarios.delete_usuario',
    raise_exception=True
)
def usuario_delete(request, id):

    usuario = get_object_or_404(
        Usuario,
        id=id
    )

    if request.method == 'POST':

        usuario.delete()

        messages.success(
            request,
            'Usuário excluído com sucesso!'
        )

        return redirect(
            'usuarios:usuario_list'
        )

    return render(
        request,
        'usuarios/usuario_confirm_delete.html',
        {
            'usuario': usuario,
        }
    )