from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'cpf', 'rg', 'is_staff')
    search_fields = ('username', 'email', 'cpf', 'rg')