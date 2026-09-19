# Arquivo: tasks/models.py

from django.db import models
from django.conf import settings

class Task(models.Model):
    # ... (classes Status e Priority permanecem as mesmas) ...
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        COMPLETED = 'COMPLETED', 'Concluída'
    class Priority(models.IntegerChoices):
        LOW = 1, 'Baixa'
        MEDIUM = 2, 'Média'
        HIGH = 3, 'Alta'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title