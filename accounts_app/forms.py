from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts_app.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'password1', 'password2')


class UserResetPasswordForm(forms.Form):
    user_email = forms.EmailField()
    captcha = CaptchaField()

    def clean_user_email(self):
        # TODO: if captcha invalid raise exception
        email = self.cleaned_data.get('user_email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователя с таким email не найдено!')
        return email
