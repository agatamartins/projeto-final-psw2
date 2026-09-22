from django.urls import path
from . import views

app_name = 'fornecedores'

urlpatterns = [
    path('', views.fornecedor_list, name='fornecedor_list'),
    path('criar/', views.fornecedor_create, name='fornecedor_create'),
    path('<int:id>/', views.fornecedor_detail, name='fornecedor_detail'),
    path('<int:id>/editar/', views.fornecedor_update, name='fornecedor_update'),
    path('<int:id>/excluir/', views.fornecedor_delete, name='fornecedor_delete'),
]