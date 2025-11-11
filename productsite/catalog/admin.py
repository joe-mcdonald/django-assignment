from django.contrib import admin
from .models import Category, Tag, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # display name, category, and price in admin list view
    list_display = ('name', 'category', 'price')

    # filter by category and tags
    list_filter = ('category', 'tags')

    # include name and description in search
    search_fields = ('name', 'description')

    # use a horizontal filter widget for tags
    filter_horizontal = ('tags',)