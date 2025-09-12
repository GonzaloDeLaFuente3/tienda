from django.urls import path
from .views import ProductListView, ProductDetailView, CartView, add_to_cart, remove_from_cart, clear_cart, WhatsAppView, debug_cloudinary, debug_images

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('whatsapp/', WhatsAppView.as_view(), name='whatsapp'),
    path('debug-cloudinary/', debug_cloudinary, name='debug_cloudinary'),
    path('debug-images/', debug_images, name='debug_images'),
]