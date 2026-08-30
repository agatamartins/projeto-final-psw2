from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.usuario_list_create, name='lista_criar'),
]