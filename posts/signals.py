from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post, Category
import string
import random


@receiver(pre_save, sender=Post)
def create_post_slug(sender, instance, *args, **kwargs):
    random_string = string.ascii_lowercase + string.digits
    after_slug = ''.join(random.choice(random_string) for _ in range(4))
    instance.slug = f"{slugify(instance.name)}-{after_slug}"


@receiver(pre_save, sender=Category)
def create_category_slug(sender, instance, *args, **kwargs):
    instance.slug = f"{slugify(instance.name)}-{instance.id}"
