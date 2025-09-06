from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Product
from .cart import Cart
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import CustomerForm 
import urllib.parse

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

class WhatsAppView(FormView):
    template_name = 'products/whatsapp_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        # Validación: Si el carrito está vacío, redirige con un mensaje de error
        if not cart:
            messages.error(self.request, "El carrito está vacío. Agrega productos antes de enviar.")
            return redirect('cart')

        customer_name = form.cleaned_data['name']
        customer_phone = form.cleaned_data['phone']
        message = self._generate_whatsapp_message(cart, customer_name, customer_phone)
        whatsapp_url = f"https://wa.me/543834025848?text={message}"
        return redirect(whatsapp_url)

    def _generate_whatsapp_message(self, cart, customer_name, customer_phone):
        message = f"Nuevo Pedido de {customer_name}\n"
        message += f"Teléfono: {customer_phone}\n"
        message += "_" * 20 + "\n"
        message += "*Detalle del Pedido*\n\n"

        for item in cart:
            product_name = item['name']
            color_info = f" ({item['color_name']})" if item.get('color_name') else ""
            message += f"- {item['quantity']} x {product_name}{color_info} "
            message += f"→ *${item['price']} c/u* = *${item['total_price']}*\n"

        message += "\n" + "_" * 20 + "\n"
        message += f"*Total a pagar: ${cart.get_total_price()}*\n"
        message += "_" * 20 + "\n"
        message += "*¡Gracias por comunicarse!*\n"
        message += "*En breve nos pondremos en contacto con usted!.*"

        return urllib.parse.quote(message)