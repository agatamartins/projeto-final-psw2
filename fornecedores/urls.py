from django.urls import path
from . import views

app_name = 'fornecedores'
urlpatterns = [
    path('', views.fornecedor_list_create, name='lista_criar'),
]