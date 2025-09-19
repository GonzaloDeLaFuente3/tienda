from .models import SiteConfig

def site_config_context(request):
    """Context processor para hacer disponible la configuración del sitio"""
    config = SiteConfig.get_active_config()
    
    return {
        'site_config': config,
    }