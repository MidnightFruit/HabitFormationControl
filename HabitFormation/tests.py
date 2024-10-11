from datetime import datetime

from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from HabitFormation.models import Habit

User = get_user_model()


class HabitTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User(email='test@mail.com',
                         first_name='Tester',
                         last_name='Tester',
                         )
        self.user.set_password('321')
        self.user.save()

        self.habit = Habit.objects.create(
            owner=self.user,
            place='home',
            date_time = datetime.now(),
            habit_to_do='nothing',
            is_pleasant=False,
            linked_habit=None,
            frequency=1,
            award='nothing',
            time_to_do=120
        )
        self.habit2 = Habit.objects.create(
            owner=self.user,
            place='home',
            date_time=datetime.now(),
            habit_to_do='nothing',
            is_pleasant=False,
            linked_habit=None,
            frequency=1,
            award='nothing',
            is_public=True,
            time_to_do=1
        )

    def test_create_habit(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'owner': self.user,
            'place': 'home12',
            'habit_to_do': 'nothing',
            'is_pleasant': False,
            'frequency': 1,
            'award': 'nothing',
            'is_public':True
        }
        response = self.client.post(
            reverse('habits:create_habit'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_retrieve_habit(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(
            path='/habits/habit/', args=[self.habit.id]
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_public_habit(self):
        response = self.client.get(reverse('habits:public_habits'))

        data = response.data

        is_all_public = True
        print(data)
        for habit in data:
            if not habit['is_public']:
                is_all_public = False
                break

        self.assertTrue(is_all_public)
