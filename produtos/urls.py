from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    # Categorias
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/criar/', views.categoria_create, name='categoria_create'),
    path('categorias/<int:id>/', views.categoria_detail, name='categoria_detail'),
    path('categorias/<int:id>/editar/', views.categoria_update, name='categoria_update'),
    path('categorias/<int:id>/excluir/', views.categoria_delete, name='categoria_delete'),

    # Produtos
    path('', views.produto_list, name='produto_list'),
    path('criar/', views.produto_create, name='produto_create'),
    path('<int:id>/', views.produto_detail, name='produto_detail'),
    path('<int:id>/editar/', views.produto_update, name='produto_update'),
    path('<int:id>/excluir/', views.produto_delete, name='produto_delete'),
]