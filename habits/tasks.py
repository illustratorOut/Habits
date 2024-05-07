from celery import shared_task
from django.utils import timezone

from habits.models import Habits
from habits.services import MyBot


@shared_task
def send_telegram():
    '''Отправка сообщения в телеграм о напоминании привычки'''
    habits = Habits.objects.select_related('user').filter(is_pleasant=False, user__id_telegram__isnull=False).all()

    for habit in habits:
        if timezone.now() >= habit.last_notification:
            massage = f"Напоминание:\n - необходимо выполнить привычку '{habit.action}' за {habit.execute_time} секунд в {habit.place}"

            periodic = timezone.timedelta(habit.periodic)
            habit.last_notification = timezone.now() + periodic
            habit.save()

            my_bot = MyBot()
            my_bot.send_message(massage)
