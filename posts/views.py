from django.shortcuts import render
from .models import Post, Category
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = '-date_posted'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['name', 'description', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['name', 'description', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser


class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['name', 'image']
    template_name = 'posts/create_category.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class CategoryListView(ListView):
    model = Category
    template_name = 'posts/category.html'
    context_object_name = 'categories'


# def posts_by_categories(request, slug):
#     category = Category.objects.get(slug=slug)
#     posts_by_cat = Post.objects.filter(category=category)
#
#     return render(request, 'posts/category.html', {'posts_by_cat': posts_by_cat})
