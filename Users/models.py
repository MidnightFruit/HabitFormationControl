from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Почта', null=False, blank=False)
    telegram_id = models.CharField(max_length=32, verbose_name='ID телеграмма')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'