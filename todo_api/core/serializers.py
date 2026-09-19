# Arquivo: core/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'email', 'last_name', 'cpf', 'endereco')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
