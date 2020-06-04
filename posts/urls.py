from django.urls import path
from .views import home, about, contact, SearchListView

urlpatterns = [
    path("", home, name="home-page"),
    path("about/", about, name="about-page"),
    path("contact/", contact, name="contact-page"),
    path('search/', SearchListView.as_view(), name='search')
]
