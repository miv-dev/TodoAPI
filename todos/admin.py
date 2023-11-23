from django.contrib import admin

from todos.models import TodoList, TodoItem


# Register your models here.
@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    pass


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    pass
