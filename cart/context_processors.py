from .cart import Cart

# Create context processor so our cart work on all pages

def cart(request):
    # return the default data from our cart
    return {'cart': Cart(request)}