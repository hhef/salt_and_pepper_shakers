from posts.models import Post, Category
from django.contrib.auth.models import User
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


def most_liked_posts(request):
    return {'most_liked_posts': Post.objects.all().order_by('-likes')[:3]}


def admin_profile(request):
    return {'about_me': User.objects.get(id=1)}
