from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse
from django.views.generic import DetailView, ListView

from store_app.forms import ProductForm
from store_app.models import Product
from store_app.apps import StoreAppConfig


class ProductListView(ListView):
    model = Product
    paginate_by = StoreAppConfig.catalog_per_page

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = ProductForm()
        ctx['title'] = 'Каталог'
        return ctx


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
