# Arquivo: tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        # Define os campos que serão expostos na API.
        fields = [
            'id', 
            'user', 
            'title', 
            'description', 
            'status', 
            'priority', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


'''
    "user":2, 
    "title":"", 
    "description":"", 
    "status":"PENDING", 
    "priority":3
'''