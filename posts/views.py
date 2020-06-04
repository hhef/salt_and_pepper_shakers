from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'posts/home.html', context)


def about(request):
    return render(request, 'posts/about.html')


def contact(request):
    return render(request, 'posts/contact.html')
