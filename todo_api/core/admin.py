# Arquivo: core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class ListUser(admin.ModelAdmin): 
    list_display = ('id', 'cpf','first_name', 'email', 'is_staff') 
    list_display_links = ('id','first_name', 'email') 
    search_fields = ('cpf', 'email', 'is_staff') 
    list_per_page = 10 

admin.site.register(User, ListUser)
