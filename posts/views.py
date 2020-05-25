from django.shortcuts import render


def home(request):
    return render(request, 'posts/home.html')


def about(request):
    return render(request, 'posts/about.html')


def contact(request):
    return render(request, 'posts/contact.html')
