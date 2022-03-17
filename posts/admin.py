from django.contrib import admin

from posts.models import CategoryModel, PostModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_descriptions', 'image', 'category', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
