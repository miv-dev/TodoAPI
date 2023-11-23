from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from todos.filters import IsOwnerFilterBackend
from todos.models import TodoList, TodoItem
from todos.serializers import TodoListSerializer, TodoItemSerializer


# Create your views here.
class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()


class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()

    def get_queryset(self):
        queryset = TodoItem.objects.all()

        todo_id = self.kwargs['pk']
        item = queryset.filter(pk=todo_id)
        return item
