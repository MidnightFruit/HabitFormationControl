from django.db import models
from datetime import time

from users.models import User


class Habit(models.Model):
    owner = models.ForeignKey(to=User, verbose_name='владелец', on_delete=models.CASCADE)
    place = models.CharField(max_length=256, verbose_name='место, в котором необходимо выполнять привычку')
    date_time = models.DateTimeField(verbose_name='время, когда необходимо выполнять привычку')
    habit_to_do = models.CharField(max_length=1024, verbose_name='действие, которое представляет собой привычка')
    frequency =  models.IntegerField(default=1, verbose_name='периодичность, в днях')
    award = models.CharField(max_length=1024, verbose_name='награда за успешное выполнение')
    time_to_do = models.TimeField(default=time(0, 10, 0), verbose_name='время требуемое на выполнение задачи')
    is_public = models.BooleanField(default=False, verbose_name='публичный/непубличный')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = "привычки"
