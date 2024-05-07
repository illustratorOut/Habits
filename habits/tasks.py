from celery import shared_task

from habits.models import Habits
from habits.services import MyBot


@shared_task
def send_telegram():
    '''Отправка сообщения в телеграм напоминание о привычке'''
    habits = Habits.objects.select_related('user').filter(is_pleasant=False, user__id_telegram__isnull=False).all()

    my_bot = MyBot()
    my_bot.send_message('sdfsdf')
