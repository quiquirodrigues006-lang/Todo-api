from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer

def index(request):
    return render(request, 'index.html')

@api_view(['POST']) #Processa requisição POST com os campos para criar o usuário.
@permission_classes([permissions.AllowAny]) #Processa requisição sem autenticação
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Retornar dados públicos do usuário criado
        output = UserSerializer(user)
        return Response(output.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) #Requisições HTTP com o verbo GET
@permission_classes([permissions.IsAuthenticated])#Apenas para usuários autenticados.
def current_user_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)