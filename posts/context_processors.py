from posts.models import Post, Category
from django.contrib.auth.models import User
from random import sample
from django.db.models import Count


def slider(request):
    posts = Post.objects.all()
    if posts.count() >= 5:
        random_posts = sample(list(posts), 5)
        return {'random_posts': random_posts}
    else:
        return {'random_posts': posts}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def latest_posts(request):
    return {'latest_posts': Post.objects.all().order_by('-date_posted')[:3]}


def most_liked_posts(request):
    return {'most_liked_posts': Post.objects.all().order_by('-likes')[:3]}


def most_commented_posts(request):
    return {
        "most_commented_posts": Post.objects.all().annotate(num_comments=Count('comment')).order_by('-num_comments')[
                                :3]}


def admin_profile(request):
    return {'about_me': User.objects.get(id=1)}
