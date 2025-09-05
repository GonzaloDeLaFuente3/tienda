from decimal import Decimal
from .models import Color, Product


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, color_id=None, quantity=1, update_quantity=False):
        # Usamos una combinación de product_id y color_id como clave
        product_id = str(product.id)
        if color_id:
            key = f"{product_id}_{color_id}"
            color = Color.objects.get(id=color_id)
            color_name = color.name
        else:
            key = product_id
            color_name = None

        if key not in self.cart:
            self.cart[key] = {
                'quantity': 0,
                'price': str(product.price),
                'name': product.name,
                'image': product.image.url if product.image else '',
                'color_id': color_id,
                'color_name': color_name,
                'product_id': product_id
            }
        if update_quantity:
            self.cart[key]['quantity'] = quantity
        else:
            self.cart[key]['quantity'] += quantity
        self.save()

    def remove(self, product, color_id=None):
        product_id = str(product.id)
        if color_id:
            key = f"{product_id}_{color_id}"
        else:
            key = product_id
            
        if key in self.cart:
            del self.cart[key]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        del self.session['cart']
        self.save()

    def __iter__(self):
    # Obtener todos los IDs de productos (removiendo el color_id si existe)
        product_ids = set()
        for key in self.cart.keys():
            product_id = key.split('_')[0]  # Obtiene el ID del producto sin el color
            product_ids.add(product_id)
        
        # Obtener los productos de la base de datos
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        # Agregar los productos al carrito
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
