from pprint import pprint

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static

from main.forms import ProductForm
from main.models import Product, Contact
from main.apps import MainConfig


# Create your views here.
def index(request: WSGIRequest):
    # pprint(Product.objects.all().order_by('-id')[:5][::-1])
    return render(request, 'main/index.html', {'title': 'Главная'})


def catalog(request: WSGIRequest):
    products = Product.objects.order_by('id').all()
    paginator = Paginator(products, MainConfig.catalog_per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'title': 'Каталог',
        'page': page,
        'form': ProductForm()
    }

    return render(
        request,
        'main/catalog.html',
        context=context
    )


def product_info(request, product_id):
    product = Product.objects.filter(id=product_id).first()

    if product:
        context = {
            'title': product.name,
            'product': product
        }

        return render(
            request,
            'main/product_info.html',
            context=context
        )
    return redirect(catalog, permanent=True)


def contacts(request: WSGIRequest):
    contact_list = [{
        'name': contact.name,
        'phones': [phone.strip() for phone in contact.phones.split(',')],
        'address': contact.address
    } for contact in Contact.objects.all()]

    return render(
        request,
        'main/contacts.html',
        {
            'title': 'Контакты',
            'contacts': contact_list
        })


def api(request: WSGIRequest):
    return JsonResponse({'status': 'ok'})


def create_product(request: WSGIRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            return JsonResponse({
                'status': 'ok',
                'id': new_product.id,
                'name': new_product.name,
                'price': new_product.price,
                'description': new_product.description,
                'image': new_product.preview_image.url if new_product.preview_image else static('/img/hnh_logo.png')
            })

    return JsonResponse({'status': 'fail'})
