# Arquivo: core/urls.py

from django.contrib import admin
from django.urls import path
from .views import index, register_view, current_user_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('user-auth/', current_user_view, name='current-user')

]

#esses paths sao tipo um menu, e o urls e o garçom, o views e o chef