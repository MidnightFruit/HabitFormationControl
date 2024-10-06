from django.urls import path

from HabitFormation.views import HabitListAPIView, PersonalHabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitRetrieveAPIView
from HabitFormation.apps import HabitformationConfig


app_name = HabitformationConfig.name


urlpatterns = [
    path('PublicHabits/', HabitListAPIView.as_view(), name='public_habits'),
    path('PersonalHabits/', PersonalHabitListAPIView.as_view(), name='personal_habits'),
    path('create_habit/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('update_habit/<int:pk>', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('delete_habit/<int:pk>', HabitDestroyAPIView.as_view(), name='delete_habit'),
    path('habit/<int:pk>', HabitRetrieveAPIView.as_view(), name='read_habit')
]