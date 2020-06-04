from posts.models import Post, Category
from random import sample


def slider(request):
    posts = Post.objects.all()
    random_posts = sample(list(posts), 3)
    return {'random_posts': random_posts}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def latest_posts(request):
    return {'latest_posts': Post.objects.all().order_by('-date_posted')[:3]}
