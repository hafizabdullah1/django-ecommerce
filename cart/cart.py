from products.models import Product



class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # get the current session key if it exists.
        cart = self.session.get('session_key')
        
        # If the user is new, no session key available! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        # Make sure cart is available on all pages.
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        
        # logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        self.session.modified = True
            
            
    def __len__(self):
        return len(self.cart)
    
    
    def get_products(self):
        # get ids from cart
        product_ids = self.cart.keys()

        # use ids to lookup products
        products = Product.objects.filter(id__in = product_ids)
        
        # return the lookup products
        return products
    
    
    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
