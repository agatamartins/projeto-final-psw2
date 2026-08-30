from django.db import models

class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.razao_social