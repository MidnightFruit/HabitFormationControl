from dataclasses import field

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from HabitFormation.models import Habit
from HabitFormation.validators import LinkedHabitValidator, FrequencyValidator, TimeToDoValidator, AwardValidator, \
    PleasantValidator


class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentUserDefault())
    validators = [
        LinkedHabitValidator(field='linked_habit'), FrequencyValidator(field='frequency'),
        TimeToDoValidator(field='time_to_do'), AwardValidator(award_field='award', linked_habit='linked_habit'),
        PleasantValidator(is_pleasant_field='is_pleasant', linked_habit_field='linked_habit', award_field='award'),
    ]


    class Meta:
        model = Habit
        fields = '__all__'