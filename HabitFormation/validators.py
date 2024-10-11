from rest_framework import serializers


class LinkedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        linked_habit = data.get(self.field)

        if linked_habit is not None and not linked_habit.is_pleasant:
            raise serializers.ValidationError("Linked habit must be pleasant!")


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        frequency = data.get(self.field)

        if frequency > 7:
            raise  serializers.ValidationError("Frequency must be less then 7!")

        if frequency <= 0:
            raise serializers.ValidationError("Frequency must be more then 0!")


class TimeToDoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        time_to_do = data.get(self.field)
        if time_to_do > 120:
            raise serializers.ValidationError("The time to do a habit should not be more than 120 seconds!")


class AwardValidator:
    def __init__(self, award_field, linked_habit):
        self.award_field = award_field
        self.linked_habit = linked_habit

    def __call__(self, data):
        award = data.get(self.award_field)
        linked_habit = data.get(self.linked_habit)

        if award is not None and linked_habit is not None:
            raise serializers.ValidationError("Only one thing should be selected: award or linked_habit")


class PleasantValidator:
    def __init__(self, is_pleasant_field, linked_habit_field, award_field):
        self.is_pleasant_field = is_pleasant_field
        self.linked_habit_field = linked_habit_field
        self.award_field = award_field

    def __call__(self, data):
        is_pleasant = data.get(self.is_pleasant_field)
        linked_habit = data.get(self.linked_habit_field)
        award = data.get(self.award_field)

        if is_pleasant and (linked_habit is not None or award is not None):
            raise serializers.ValidationError("Pleasant habit can't have linked habit or award")