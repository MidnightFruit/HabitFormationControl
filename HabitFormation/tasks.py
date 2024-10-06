from datetime import datetime, timedelta

from celery import shared_task

from HabitFormation.models import Habit
from HabitFormation.services import send_tg_message


@shared_task
def send_notifications():
    habits = Habit.objects.all()
    for habit in habits:
        if habit.date_time is datetime.now():
            text = f"я буду {habit.habit_to_do} в {habit.time_to_do} в {habit.place}\n"
            send_tg_message(text, habit.owner.telegram_id)
            habit.date_time += timedelta(days=habit.frequency)
