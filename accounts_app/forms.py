from django.contrib.auth.forms import UserCreationForm
from accounts_app.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'country', 'password1', 'password2')
