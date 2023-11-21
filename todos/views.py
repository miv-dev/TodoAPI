from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from todos.models import TodoList
from todos.serializers import TodoListSerializer


# Create your views here.
class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    
    
    