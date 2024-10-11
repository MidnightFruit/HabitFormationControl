from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, verbose_name='Почта', null=False, blank=False)
    telegram_id = models.CharField(max_length=32, verbose_name='ID телеграмма')
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'