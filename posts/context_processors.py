from posts.models import Post
from random import sample


def slider(request):
    random_posts = Post.objects.filter(name='Elvis')
    return {'random_posts': random_posts}
