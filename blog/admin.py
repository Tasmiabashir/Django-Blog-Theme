from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')
    search_fields = ('category_name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_featured', 'is_published', 'created_at')
    list_filter = ('category', 'is_featured', 'is_published')
    search_fields = ('title',)

