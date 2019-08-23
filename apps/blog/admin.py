from django.contrib import admin
from .models import Category, Post, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'activate']
    list_display = ('title', 'slug', 'activate')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','pk')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'text', 'categories', 'tags', 'activate']
    list_display = ('title', 'visits', 'created', 'updated', 'activate')


