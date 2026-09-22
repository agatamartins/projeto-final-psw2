from django.contrib import admin
from django.urls import path, include

from . import views
from usuarios import views as usuarios_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),

    # Autenticação
    path('login/', usuarios_views.login_view, name='login'),
    path('logout/', usuarios_views.logout_view, name='logout'),

    # Aplicações
    path('usuarios/', include('usuarios.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('produtos/', include('produtos.urls')),
    path('vendas/', include('vendas.urls')),
    path('feedback/', include('feedback.urls')),
]