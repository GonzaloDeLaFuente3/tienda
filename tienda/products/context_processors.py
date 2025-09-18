from .cart import Cart

def cart_context(request):
    """Context processor para hacer disponible el carrito en todas las plantillas"""
    cart = Cart(request)
    return {
        'cart_count': len(cart),
        'cart_total': cart.get_total_price() if cart else 0
    }