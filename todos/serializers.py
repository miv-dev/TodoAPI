from rest_framework import serializers

from todos.models import TodoList, TodoItem


class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['url', 'title', 'description', 'created_at', 'due_date']


class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    todo_items = TodoItemSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ['title', 'description', 'created_at', 'user', 'todo_items']

    def create(self, validated_data):
        todo_items = validated_data.pop('todo_items')
        todo_list = TodoList.objects.create(**validated_data)
        for item in todo_items:
            TodoItem.objects.create(todo_list=todo_list, **item)
        return todo_list
