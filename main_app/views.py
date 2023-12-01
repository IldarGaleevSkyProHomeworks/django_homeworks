from django.views.generic import TemplateView, ListView

from main_app.models import Contact


class IndexView(TemplateView):
    template_name = 'main_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


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
