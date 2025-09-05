from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, verbose_name=_("Descripción"))
    is_active = models.BooleanField(default=True, verbose_name=_("¿Activo?"))

    class Meta:
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Nombre del color"))

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colores")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, verbose_name=_("Descripción"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Precio"))
    stock = models.PositiveIntegerField(default=0, verbose_name=_("Stock"))
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name=_("Imagen"))
    is_active = models.BooleanField(default=True, verbose_name=_("¿Activo?"))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Categoría"))
    colors = models.ManyToManyField(Color, blank=True, verbose_name=_("Colores"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Fecha de actualización"))

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")

    def __str__(self):
        return self.name

class Promotion(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Nombre"))
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Descuento (%)"))
    start_date = models.DateField(verbose_name=_("Fecha de inicio"))
    end_date = models.DateField(verbose_name=_("Fecha de fin"))
    is_active = models.BooleanField(default=True, verbose_name=_("¿Activo?"))

    class Meta:
        verbose_name = _("Promoción")
        verbose_name_plural = _("Promociones")

    def __str__(self):
        return f"{self.name} ({self.discount_percent}%)"