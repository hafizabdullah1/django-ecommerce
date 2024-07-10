from django.shortcuts import render
from .models import *

# Create your views here.

def categories_page(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'products/categories.html', context)


def get_products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {'products': products}
    return render(request, "products/products.html", context)


def get_product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)