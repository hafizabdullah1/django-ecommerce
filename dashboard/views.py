from django.shortcuts import render, redirect, get_object_or_404
from products.models import *
from .forms import *

# Create your views here.

def products_page(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'products.html', context)
    

def categories_page(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request,'categories.html', context)
    

# =============================PRODUCTS RELATED VIEWS=============================

def update_product(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product }
    return render(request,"product_update.html", context)


def create_product(request):
    categories = Categorie.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_products')            
    else:
        form = ProductForm()
    context = { 'categories': categories }
    return render(request, "product_create.html", context)


def update_product(request, id):
    categories = Categorie.objects.all()
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("dashboard_products")
    else:
        form = ProductForm(instance=product)
    context = {'form': form, 'categories': categories}
    return render(request, "product_update.html", context)


def delete_product(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.delete()
        return redirect("dashboard_products")
    context = {'product': product}
    return render(request,"product_delete.html", context)


# ==================================CATEGORY RELATED VIEWS===========================

# Create new category
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is not valid')
            form.save()
            return redirect('dashboard_categories')  
        else:
            print('form is not valid')          
    else:
        form = CategoryForm()
    return render(request, "category_create.html")


# Update category
def update_category(request, id):
    category = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("dashboard_categories")
    else:
        form = CategoryForm(instance=category)
    context = {'form': form}
    return render(request, "category_update.html", context)

# Delete category
def delete_category(request, id):
    category = Categorie.objects.get(id = id)
    if request.method == 'POST':
        category.delete()
        return redirect("dashboard_categories")
    context = {'category': category}
    return render(request,"category_delete.html", context)