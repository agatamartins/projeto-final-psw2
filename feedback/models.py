from django.db import models

from usuarios.models import Usuario


class Feedback(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    opiniao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ['-data_criacao']

    def __str__(self):
        return f'Feedback de {self.usuario.username}'
