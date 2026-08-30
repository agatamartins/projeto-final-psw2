from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} (CPF: {self.cpf})"