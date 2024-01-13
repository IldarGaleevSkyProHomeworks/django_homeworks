from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse, Http404
from django.shortcuts import redirect
from django.templatetags.static import static
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from store_app.forms import ProductForm, ProductVersionFormset, ManagerForm
from store_app.models import Product
from store_app.apps import StoreAppConfig


class IsOwner(Permission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ProductListView(ListView):
    model = Product
    paginate_by = StoreAppConfig.catalog_per_page

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True).order_by('-create_date')

        return qs

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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def _is_ajax(self):
        return self.request.headers.get('x-requested-with') == 'XMLHttpRequest'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Создание продукта'

        if self.request.method == 'POST':
            ctx['formset'] = ProductVersionFormset(self.request.POST)
        else:
            ctx['formset'] = ProductVersionFormset()

        return ctx

    def form_valid(self, form):
        def create_product():
            new_product = form.save(commit=False)
            new_product.seller = self.request.user
            new_product.save()
            return new_product

        formset: ProductVersionFormset = self.get_context_data()['formset']
        formset_errors = None

        if len(formset):
            if formset.is_valid():
                new_product = create_product()

                formset.instance = new_product
                formset.save()
            else:
                formset_errors = formset.errors
                new_product = None
        else:
            new_product = create_product()

        if self._is_ajax():
            if formset_errors:
                return JsonResponse({
                    'status': 'fail',
                    'errors': formset_errors
                })

            return JsonResponse({
                'status': 'ok',
                'id': new_product.id,
                'name': new_product.name,
                'price': new_product.price,
                'description': new_product.description,
                'image': new_product.preview_image.url if new_product.preview_image else static('/img/hnh_logo.png')
            })
        else:
            if formset_errors:
                return self.render_to_response(self.get_context_data(form=form))
            return redirect(reverse('store_app:product', kwargs={'pk': new_product.id}))

    def form_invalid(self, form):
        if self._is_ajax():
            return JsonResponse({'status': 'fail', 'errors': form.errors})
        else:
            return super().form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product

    def test_func(self):
        curr_user = self.request.user
        return (self.get_object().seller == self.request.user or
                any([
                    curr_user.has_perm('store_app.change_product'),
                    curr_user.has_perm('store_app.can_unpublished_product'),
                    curr_user.has_perm('store_app.can_change_product_name'),
                    curr_user.has_perm('store_app.can_change_product_description'),
                    curr_user.has_perm('store_app.can_change_product_category'),
                ])
                )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = f'Редактирование: "{self.object.name}"'

        if self.request.user.has_perm('catalog_app.changed_product') or self.get_object().seller == self.request.user:
            if self.request.method == 'POST':
                ctx['formset'] = ProductVersionFormset(self.request.POST, instance=self.object)
            else:
                ctx['formset'] = ProductVersionFormset(instance=self.object)

        return ctx

    def form_valid(self, form):
        self.object = form.save()
        if self.request.user.has_perm('catalog_app.changed_product') or self.get_object().seller == self.request.user:
            formset: ProductVersionFormset = self.get_context_data()['formset']

            if formset.is_valid():
                formset.instance = self.object
                formset.save()
                return redirect(reverse('store_app:product', kwargs={'pk': self.object.id}))
            return self.render_to_response(self.get_context_data(form=form))
        else:
            return redirect(reverse('store_app:product', kwargs={'pk': self.object.id}))

    def get_form_class(self):
        if self.request.user.has_perm('catalog_app.changed_product') or self.get_object().seller == self.request.user:
            return ProductForm
        return ManagerForm
    def form_invalid(self, form):
        pass