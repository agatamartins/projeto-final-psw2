from django.urls import path
from . import views

app_name = 'vendas'
urlpatterns = [
    path('', views.venda_list_create, name='lista_criar'),
]