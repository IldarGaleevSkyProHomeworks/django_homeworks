from django import template

register = template.Library()


@register.inclusion_tag('main/share/_product_card.html', name='product_card')
def footer(obj=None):
    if not obj:
        obj = {
            'preview_image': '${img_url}',
            'name': '${product_name}',
            'description': '${description}',
            'price': '${price}'
        }

    return {'object': obj}
