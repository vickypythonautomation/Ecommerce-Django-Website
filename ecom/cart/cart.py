
class Cart:
    def __init__(self, request):
        self.session = request.session

        # get session key if exists
        cart = self.session.get('session_key')

        # if there is no session key, create an empty cart and save it in the session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # to make sure the cart is always available in the session of all pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price_or_sale())}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    