from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def task_list_create_view(request):
    """
    View para listar todas as tarefas do usuário logado (GET)
    ou criar uma nova tarefa (POST).
    """
    
    if request.method == 'GET':
        # 1. Busca apenas as tarefas do usuário que fez a requisição
        tasks = Task.objects.filter(user=request.user).order_by('-created_at')
        
        # 2. Serializa a lista de tarefas
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # 1. Cria um serializador com os dados enviados
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            # 2. Salva a tarefa, injetando o usuário logado (lógica do perform_create)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 3. Retorna erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------------------------------------------------------

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def task_detail_view(request, pk):
    """
    View para ver, atualizar ou deletar uma tarefa específica (pelo 'pk').
    """
    # 1. Tenta buscar a tarefa pelo PK
    #PK e uma priary key (chave primaria)
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(
            {'detail': 'Tarefa não encontrada.'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    # 2. !! IMPORTANTE: Verifica se o usuário logado é o dono da tarefa
    if task.user != request.user: 
        return Response(
            {'detail': 'Você não tem permissão para esta ação.'}, 
            status=status.HTTP_403_FORBIDDEN
        )

    # --- Se o usuário for o dono, prossiga ---
    if request.method == 'GET':
        # 3. Retorna os detalhes da tarefa
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method in ['PUT', 'PATCH']:
        # 4. Atualiza a tarefa
        # 'partial=True' permite a atualização parcial (PATCH)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # 5. Deleta a tarefa
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
