from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Listar usuários
    path(
        '',
        views.usuario_list,
        name='usuario_list'
    ),

    # Cadastrar usuário
    path(
        'criar/',
        views.usuario_create,
        name='usuario_create'
    ),

    # Detalhes do usuário
    path(
        '<int:id>/',
        views.usuario_detail,
        name='usuario_detail'
    ),

    # Editar usuário
    path(
        '<int:id>/editar/',
        views.usuario_update,
        name='usuario_update'
    ),

    # Excluir usuário
    path(
        '<int:id>/excluir/',
        views.usuario_delete,
        name='usuario_delete'
    ),
]