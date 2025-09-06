from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag(takes_context=True)
def dark_mode(context):
    request = context['request']
    dark_mode = request.COOKIES.get('dark_mode', 'off')
    return dark_mode
