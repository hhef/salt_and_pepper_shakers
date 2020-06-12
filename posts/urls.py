from django.urls import path
from .views import about, contact, SearchListView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home-page"),
    path("about/", about, name="about-page"),
    path("contact/", contact, name="contact-page"),
    path('search/', SearchListView.as_view(), name='search')
]
