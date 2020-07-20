import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salt_and_pepper_shakers.settings')
django.setup()

from django.contrib.auth.models import User
from posts.models import Post, Category, Comment
from faker import Faker
import random


def create_superuser():
    superuser = User.objects.create_superuser('admin', 'admin@admin.com', 'password')
    superuser.save()


def create_users():
    faker = Faker()
    for _ in range(10):
        name = faker.first_name() + faker.last_name()
        email = faker.email()
        password = 'password'
        user = User.objects.create_user(name, email, password)
        user.save()


def create_category():
    faker = Faker()
    for _ in range(10):
        name = faker.word()
        category = Category(name=name)
        category.save()


def create_posts():
    faker = Faker()
    for _ in range(40):
        author_id = 1
        name = faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        description = faker.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
        cat = str(random.randint(1, 10))
        post = Post.objects.create(name=name, description=description, author_id=author_id)
        post.category.add(cat)
        post.save()


def create_comments_and_likes():
    faker = Faker()
    for _ in range(100):
        author_id = str(random.randint(1, 10))
        post = str(random.randint(1, 40))
        text = faker.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)
        comment = Comment(author_id=author_id, post_id=post, text=text)
        comment.save()
        post_like = Post.objects.get(id=str(random.randint(1, 40)))
        post_like.likes.add(str(random.randint(1, 10)))
    for _ in range(200):
        comment_like = Comment.objects.get(id=str(random.randint(1, 100)))
        comment_like.likes.add(str(random.randint(1, 10)))


create_superuser()
create_users()
create_category()
create_posts()
create_comments_and_likes()
