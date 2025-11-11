from django.shortcuts import render
from .models import Product, Category, Tag
from django.db.models import Q

# Create your views here.
def product_list(request):
    # get parameters from GET request
    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()
    tag_ids = request.GET.getlist('tags')

    products = Product.objects.all()

    # Filtering:
    if query:
        products = products.filter(
            Q(description__icontains=query) | Q(name__icontains=query)
        )
    
    # Filter by category if provided
    if category_id:
        products = products.filter(category__id=category_id)
    
    # Filter by tags if provided
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()
    
    # Fetch all categories and tags for filter options
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "current_query": query,
        "current_category": category_id,
        "current_tags": [int(t) for t in tag_ids] if tag_ids else [], # Convert to int list
    }

    # Render the product list template with context
    return render(request, 'catalog/product_list.html', context)