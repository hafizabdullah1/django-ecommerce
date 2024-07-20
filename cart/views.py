from django.shortcuts import render, get_object_or_404
from .cart import Cart
from products.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request): 
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_products
    
    context = {'cart_products': cart_products}
    return render(request, "cart_summary.html", context)
    
    
def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        # lookup product in the DB
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product)
        
        # get cart qty
        cart_qty = cart.__len__()

        # return response
        response = JsonResponse({
            'qty': cart_qty,
        })
        return response
    # context = {}
    # return render(request, "cart_add.html", context)
    
    
    
def cart_update(request):
    context = {}
    return render(request, "cart_update.html", context)
    
    
def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)
        
        response = JsonResponse({
            'product': product_id,
        })
        return response
