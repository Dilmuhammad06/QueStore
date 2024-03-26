from .cart import Cart

def cart(request):
    return {'cart_len': Cart(request).__len__()}