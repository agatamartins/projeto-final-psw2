from django.shortcuts import render


def inicio(request):
    """Renderiza a página inicial pública do sistema."""
    return render(request, 'home.html')
