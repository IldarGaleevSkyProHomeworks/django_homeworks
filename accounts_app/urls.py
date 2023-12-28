from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts_app.apps import AccountsAppConfig
from accounts_app.views import UserDetailView, UserCreateView

app_name = AccountsAppConfig.name

urlpatterns = [
    path('profile/', UserDetailView.as_view(), name='user_detail'),
    path('login/', LoginView.as_view(template_name='accounts_app/login.html', extra_context={'title': 'Вход'}),
         name='login',
         ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserCreateView.as_view(), name='registration'),
]
