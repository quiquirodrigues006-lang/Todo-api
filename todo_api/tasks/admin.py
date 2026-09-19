# Arquivo: tasks/admin.py
from django.contrib import admin
from .models import Task

class ListTask(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'priority', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'user__username', 'status')
    list_per_page = 10

admin.site.register(Task, ListTask)

