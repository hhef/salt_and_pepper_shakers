from django.urls import path
from .views import about, contact, SearchListView, PostListView, PostCreateView, PostDetailView, PostUpdateView, \
    PostDeleteView, CategoryCreateView, posts_by_categories

urlpatterns = [
    path("", PostListView.as_view(), name="home-page"),
    path("about/", about, name="about-page"),
    path("contact/", contact, name="contact-page"),
    path('search/', SearchListView.as_view(), name='search'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('categories/<slug:slug>/', posts_by_categories, name='categories'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),

]
