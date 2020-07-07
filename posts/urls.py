from django.urls import path
from .views import about, contact, SearchListView, PostListView, PostCreateView, PostUpdateView, \
    PostDeleteView, CategoryCreateView, posts_by_categories, post_detail_with_comment_form, CategoryListView

urlpatterns = [
    path("", PostListView.as_view(), name="home-page"),
    path("about/", about, name="about-page"),
    path("contact/", contact, name="contact-page"),
    path('search/', SearchListView.as_view(), name='search'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', post_detail_with_comment_form, name='post-detail'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('categories/<slug:slug>/', posts_by_categories, name='categories-posts'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/', CategoryListView.as_view(), name='categories')

]
