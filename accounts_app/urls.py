from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from accounts_app.apps import AccountsAppConfig
from accounts_app.views import (UserDetailView, UserCreateView, UserEmailVerify,
                                VerifyMailAgain, UserResetPassword, UserEditView)

app_name = AccountsAppConfig.name

urlpatterns = [
    path('profile/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('registration/email_verify/<uidb64>/<token>/', UserEmailVerify.as_view(), name='email_verify'),
    path('registration/email_verify/resend', VerifyMailAgain.as_view(), name='email_verify_again'),
    path('reset_password/', UserResetPassword.as_view(), name='reset_password'),
    path('edit/', UserEditView.as_view(), name='user_edit'),

    path('login/', LoginView.as_view(
        template_name='accounts_app/login.html',
        extra_context={'title': 'Вход'}
    ),
         name='login',
         ),

    path('registration/email_verify/', TemplateView.as_view(
        template_name='accounts_app/user_email_verify.html',
        extra_context={'title': 'Подтвердите вашу почту'}
    ),
         name='email_verify_alert'
         ),

    path('registration/email_verify_failed/', TemplateView.as_view(
        template_name='accounts_app/user_email_verify_failed.html',
        extra_context={'title': 'Не удалось подтвердить адрес почты'}
    ),
         name='email_verify_failed'
         ),

    path('reset_password/success', TemplateView.as_view(
        template_name='accounts_app/reset_password_success.html',
        extra_context={'title': 'Пароль сброшен'}
    ),
         name='reset_password_alert'
         ),

]
