from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = 'Create a new user.'

    def handle(self, *args, **kwargs):
        # user = User(name='Grisha', email='grisha@example.com', password='secret', age=25)
        user = User(name='Jhon', email='Jhon@example.com', password='secret', age=58)
        # user = User(name='Neo', email='Neo@example.com', password='secret', age=60)
        user.save()
        self.stdout.write(f'{user}')
