from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = 'Get posts by author id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')
