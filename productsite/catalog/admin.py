from django.contrib import admin
from .models import Category, Tag, Product

# Register your models here.

# register Category model with admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # display name in admin list view
    search_fields = ('name',) # enable search by name

# register Tag model with admin
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',) # display name in admin list view
    search_fields = ('name',) # enable search by name

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