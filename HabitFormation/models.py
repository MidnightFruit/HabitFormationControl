from django.db import models

from Users.models import User


class Habit(models.Model):
    owner = models.ForeignKey(to=User, verbose_name='владелец', on_delete=models.CASCADE)
    place = models.CharField(max_length=256, verbose_name='место, в котором необходимо выполнять привычку')
    date_time = models.DateTimeField(verbose_name='время, когда необходимо выполнять привычку')
    habit_to_do = models.CharField(max_length=1024, verbose_name='действие, которое представляет собой привычка')
    frequency =  models.IntegerField(default=1, verbose_name='периодичность, в днях')
    award = models.CharField(max_length=1024, verbose_name='награда за успешное выполнение')
    time_to_do = models.TimeField(default=10)

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = "привычки"
