from django.contrib import admin
from .models import SiteConfig

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_subtitle', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('site_name',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('site_name', 'site_subtitle', 'logo', 'is_active'),
            'description': 'Configuración básica del sitio web'
        }),
        ('Información de Contacto', {
            'fields': ('phone', 'email'),
            'classes': ('collapse',),
            'description': 'Datos de contacto que aparecerán en el sitio'
        }),
        ('Redes Sociales', {
            'fields': ('instagram_url', 'facebook_url', 'whatsapp_number'),
            'classes': ('collapse',),
            'description': 'Enlaces a redes sociales'
        }),
    )
    
    def has_delete_permission(self, request, obj=None):
        # Prevenir eliminación si es la única configuración
        if SiteConfig.objects.count() <= 1:
            return False
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        # Permitir solo una configuración activa
        if SiteConfig.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)