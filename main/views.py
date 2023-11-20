from pprint import pprint

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from main.models import Product, Contact
from main.apps import MainConfig


# Create your views here.
def index(request: WSGIRequest):
    pprint(Product.objects.all().order_by('-id')[:5][::-1])
    return render(request, 'main/index.html', {'title': 'Главная'})


def catalog(request: WSGIRequest):

    products = Product.objects.all()
    paginator = Paginator(products, MainConfig.catalog_per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'title': 'Каталог',
        'page': page
    }

    return render(
        request,
        'main/catalog.html',
        context=context
    )


in_memory_db = []


def contacts(request: WSGIRequest):
    if request.method == 'POST':
        new_item = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),
        }
        in_memory_db.append(new_item)
        pprint(new_item)

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
            'feedback': [{'name': f'{item["name"][0]}***', 'message': item["message"]} for item in in_memory_db[-3:]],
            'contacts': contact_list
        })


def api(request: WSGIRequest):
    return JsonResponse({'status': 'ok'})
