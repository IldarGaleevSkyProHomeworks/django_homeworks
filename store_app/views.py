from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse
from django.views.generic import DetailView, ListView

from store_app.forms import ProductForm
from store_app.models import Product, Contact
from store_app.apps import StoreAppConfig


# Create your views here.
def index(request: WSGIRequest):
    # pprint(Product.objects.all().order_by('-id')[:5][::-1])
    return render(request, 'store_app/index.html', {'title': 'Главная'})


def catalog(request: WSGIRequest):
    products = Product.objects.order_by('id').all()
    paginator = Paginator(products, StoreAppConfig.catalog_per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'title': 'Каталог',
        'page': page,
        'form': ProductForm()
    }

    return render(
        request,
        'store_app/catalog.html',
        context=context
    )


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx

    def get(self, request, *args, **kwargs):
        try:
            obj = super().get(request, *args, **kwargs)
            return obj
        except Http404:
            return redirect(reverse('store_app:catalog'))


class ContactListView(ListView):
    model = Contact

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['object_list'] = [{
            'name': contact.name,
            'phones': [phone.strip() for phone in contact.phones.split(',')],
            'address': contact.address
        } for contact in ctx['object_list']]

        ctx['title'] = 'Контакты'
        return ctx


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
