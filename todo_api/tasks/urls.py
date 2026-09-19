# Arquivo: tasks/urls.py

from django.urls import path
from .views import * 

urlpatterns = [
    # URL para listar e criar tarefas
    path('tasks/', task_list_create_view, name='task-list-create'),
    # URL para ver, atualizar ou deletar uma tarefa específica
    path('tasks/<int:pk>', task_detail_view, name='task-detail'),
]




















