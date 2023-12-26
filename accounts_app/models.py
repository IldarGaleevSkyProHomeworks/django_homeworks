from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

from utils.const import MF_NULL
from utils.hash_storage import user_logo_images, HashStorage


class User(AbstractUser):
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    user_logo = models.ImageField(upload_to=user_logo_images, storage=HashStorage(),
                                  verbose_name='Лого профиля', **MF_NULL)
    country = CountryField()
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
