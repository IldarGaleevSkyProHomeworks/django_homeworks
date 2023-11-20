from django import template
from django.templatetags.static import static

register = template.Library()


@register.filter(name="product_image")
def product_image(value, arg=None):
    if value:
        return value.url
    return static('/img/hnh_logo.png')
