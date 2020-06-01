from django.shortcuts import render
from .models import Post
from random import sample


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)


def about(request):
    return render(request, 'posts/about.html')


def contact(request):
    return render(request, 'posts/contact.html')


def base(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/base.html', context)
