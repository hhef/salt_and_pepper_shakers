from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default='default-cat.jpg', upload_to='category_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/"


class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)
    likes = models.ManyToManyField(User, related_name='post_likes')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='comment_likes')

    def __str__(self):
        return f"Comment in {self.post} by {self.author}"


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics', null=True, blank=True)