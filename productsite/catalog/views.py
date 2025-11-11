from django.shortcuts import render
from .models import Product, Category, Tag
from django.db.models import Q

# Create your views here.
def product_list(request):
    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()
    tag_ids = request.GET.getlist('tags')

    products = Product.objects.all()

    # Filtering:
    if query:
        products = products.filter(
            Q(description__icontains=query) | Q(name__icontains=query)
        )
    
    if category_id:
        products = products.filter(category__id=category_id)
    
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()
    
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "current_query": query,
        "current_category": category_id,
        "current_tags": [int(t) for t in tag_ids] if tag_ids else [],
    }

    return render(request, 'catalog/product_list.html', context)