from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteConfig(models.Model):
    site_name = models.CharField(max_length=100, verbose_name=_("Nombre del sitio"), default="Velour")
    site_subtitle = models.CharField(max_length=200, verbose_name=_("Subtítulo"), default="Tienda Online", blank=True)
    logo = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name=_("Logo"))
    
    # Información de contacto
    phone = models.CharField(max_length=20, verbose_name=_("Teléfono"), blank=True)
    email = models.EmailField(verbose_name=_("Email"), blank=True)
    
    # Redes sociales
    instagram_url = models.URLField(verbose_name=_("Instagram"), blank=True)
    facebook_url = models.URLField(verbose_name=_("Facebook"), blank=True)
    whatsapp_number = models.CharField(max_length=20, verbose_name=_("WhatsApp"), default="+543834653289")
    
    # Configuraciones adicionales
    is_active = models.BooleanField(default=True, verbose_name=_("¿Activo?"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Fecha de actualización"))

    class Meta:
        verbose_name = _("Configuración del Sitio")
        verbose_name_plural = _("Configuraciones del Sitio")

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        # Asegurar que solo haya una configuración activa
        if self.is_active:
            SiteConfig.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active_config(cls):
        """Obtener la configuración activa"""
        return cls.objects.filter(is_active=True).first()


