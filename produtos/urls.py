from django.urls import path
from . import views

app_name = 'produtos'
urlpatterns = [
    path('categorias/', views.categoria_list_create, name='categoria_lista_criar'),
    path('', views.produto_list_create, name='produto_lista_criar'),
]