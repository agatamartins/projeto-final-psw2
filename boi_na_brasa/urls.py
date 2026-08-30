from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('produtos/', include('produtos.urls')),
    path('vendas/', include('vendas.urls')),
]