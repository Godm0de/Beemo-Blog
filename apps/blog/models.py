from django.db import models
from django.db.models.signals import pre_save
from tinymce import models as tinymce_models

from .utils import unique_slug_generator


# Create your models here.

# Category model
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.CharField(max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    activate = models.BooleanField('Activate', default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

# Posts model

class Post(models.Model):

    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.CharField(max_length=200, null=True, blank=True, unique=True)
    image = models.URLField(blank=True)  # max_length by default is 200
    text = tinymce_models.HTMLField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activate = models.BooleanField('Activate', default=False)
    visits = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

# Functions

# Slug generator

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# Instance for slug pre_save.connect(slug_generator, sender=Model)
pre_save.connect(slug_generator, sender=Category)
pre_save.connect(slug_generator, sender=Post)
