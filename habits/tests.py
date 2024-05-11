import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin')
        data = {
            'user': self.user,
            'place': 'Работа',
            'time': datetime.datetime.now().time(),
            'action': 'Подготавливать отчет',
            'periodic': 7,
            'reward': 'Зарплата',
            'execute_time': 120
        }
        self.habits = Habits.objects.create(**data)

    def test_API_list_habits(self):
        """Тестирование просмотра привычек"""
        response = self.client.get(
            '/API/public/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_API_get_habits(self):
        """Тестирование просмотра привычки"""
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/API/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_API_create_habits(self):
        """Тестирование создание привычки"""
        self.client.force_authenticate(user=self.user)

        data = {
            'place': 'Работа',
            'time': datetime.datetime.now().time(),
            'action': 'Подготавливать отчет',
            'periodic': 7,
            'reward': 'Зарплата',
            'execute_time': 120
        }

        response = self.client.post(
            '/API/create/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_API_update_habits(self):
        """Тестирование обновление привычки"""
        self.client.force_authenticate(user=self.user)
        data = {
            'place': 'Работа',
            'time': datetime.datetime.now().time(),
            'action': 'Подготавливать отчет',
            'periodic': 3,
            'reward': 'Зарплата',
            'execute_time': 120
        }

        response = self.client.put(
            f'/API/update/{self.habits.pk}/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_API_delete_habits(self):
        """Тестирование удаление привычки"""
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/API/delete/{self.habits.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
