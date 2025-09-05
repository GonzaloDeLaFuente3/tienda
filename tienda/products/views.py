from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Product
from .cart import Cart
from django.contrib import messages

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_active=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Asegúrate de que solo se muestren los colores disponibles
        context['colors'] = self.object.colors.all()
        return context

class CartView(TemplateView):
    template_name = 'products/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    color_id = request.GET.get('color')
    
    # Si el producto tiene colores, validamos que se haya seleccionado uno
    if product.colors.exists() and not color_id:
        messages.error(request, 'Por favor selecciona un color')
        return redirect('product_detail', pk=product_id)
    
    cart = Cart(request)
    cart.add(product, color_id=color_id)
    messages.success(request, 'Producto agregado al carrito')
    return redirect('product_list')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'El carrito ha sido vaciado.')
    return redirect('cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    color_id = request.GET.get('color')
    cart = Cart(request)
    cart.remove(product, color_id=color_id)
    return redirect('cart')
