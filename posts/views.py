from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.db.models import Q


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'posts/home.html', context)


def about(request):
    return render(request, 'posts/about.html')


def contact(request):
    return render(request, 'posts/contact.html')


class SearchListView(ListView):
    model = Post
    template_name = 'posts/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset_list = Post.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()
        return queryset_list.order_by('-date_posted')
