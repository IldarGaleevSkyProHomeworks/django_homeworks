from django import template

register = template.Library()


@register.inclusion_tag('main/share/_product_card.html', name='product_card')
def footer(obj=None):
    if not obj:
        obj = {
            'preview_image': '${data.image}',
            'name': '${data.name}',
            'description': '${data.description}',
            'price': '${data.price}'
        }

    return {'object': obj}
