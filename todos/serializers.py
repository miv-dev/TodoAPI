from rest_framework import serializers

from todos.models import TodoList


class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ['title', 'description', 'created_at', 'user']
        