from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def main_land(request):
    return render(request, 'main/index.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug = slug)
    return render(request, 'product/detail.html', {'product': product})

def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category=category)
    return render(request, 'category/university.html', {'category': category,
                                                        'categories': categories,
                                                        'products': products,
                                                        'slug_url': category_slug})