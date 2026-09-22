from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('', views.venda_list, name='venda_list'),
    path('criar/', views.venda_create, name='venda_create'),
    path('<int:id>/', views.venda_detail, name='venda_detail'),
    path('<int:id>/editar/', views.venda_update, name='venda_update'),
    path('<int:id>/excluir/', views.venda_delete, name='venda_delete'),
]