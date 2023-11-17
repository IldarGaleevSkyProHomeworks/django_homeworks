from pprint import pprint

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render

from main.models import Product, Contact


# Create your views here.
def index(request: WSGIRequest):
    pprint(Product.objects.all().order_by('-id')[:5][::-1])
    return render(request, 'main/index.html', {'title': 'Главная'})


def catalog(request: WSGIRequest):
    count = request.GET.get('count')
    count = int(count) if count else 6
    items = [
        {
            'id': n + 1,
            'title': f'Пенгвинчег {n + 1}',
            'description': f'Пенгвинчег {n + 1} самый лучший, среди {count} пенгвинчегов'
        }
        for n in range(count)
    ]

    return render(request, 'main/catalog.html', {'title': 'Каталог', 'items': items})


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
