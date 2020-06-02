from posts.models import Post, Category
from random import sample


def slider(request):
    random_posts = Post.objects.filter(name='Elvis')
    return {'random_posts': random_posts}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
