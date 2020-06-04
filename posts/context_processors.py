from posts.models import Post, Category
from random import sample


def slider(request):
    random_posts = Post.objects.filter(name='Elvis')
    return {'random_posts': random_posts}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def latest_posts(request):
    return {'latest_posts': Post.objects.all().order_by('-id')[:3]}
