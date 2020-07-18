from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def about(request):
    latest_posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'posts/about.html', {"latest_posts": latest_posts})


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


def posts_by_categories(request, slug):
    category = Category.objects.get(slug=slug)
    posts_by_cat = Post.objects.filter(category=category)

    return render(request, 'posts/category_posts.html', {'posts_by_cat': posts_by_cat})


def post_detail_with_comment_form(request, slug):
    post = Post.objects.get(slug=slug)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect("post-detail", slug=post.slug)
    else:
        comment_form = CommentForm()

    context = {'post': post,
               'comment_form': comment_form}
    return render(request, 'posts/post_detail.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'posts/categories.html'
    context_object_name = 'categories'
    ordering = 'name'


def like_view(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_like'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[slug]))
