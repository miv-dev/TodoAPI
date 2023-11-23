from django.core.management import BaseCommand, CommandError

from todos.models import TodoItem, TodoList
from users.models import User


class Command(BaseCommand):
    help = "Close all finished todos for current user ()"

    def add_arguments(self, parser):
        parser.add_argument("username", nargs="+", type=str)

    def handle(self, *args, **options):
        username = options["username"]
        if username != "":
            try:
                user = User.objects.get(username=username)
                todo_lists = TodoList.objects.filter(user=user)
                if len(todo_lists) > 0:
                    for todo_list in todo_lists:
                        todos = TodoItem.objects.filter(todo_list=todo_list, is_complete=True)
                        todos.delete()
                else:
                    raise CommandError('This user doesn\'t have todo lists')

            except User.DoesNotExist:
                raise CommandError(f'User {username} doesn\'t exist')
