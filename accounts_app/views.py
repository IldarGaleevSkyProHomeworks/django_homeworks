from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from accounts_app.models import User
from accounts_app.forms import UserRegisterForm


class UserDetailView(DetailView, LoginRequiredMixin):
    model = User

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Информация об аккаунте'
        return ctx

    def get_object(self, queryset=None):
        return self.request.user


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'accounts_app/register.html'
    success_url = reverse_lazy('accounts:login')
