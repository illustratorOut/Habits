from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Habits(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=120, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=120, verbose_name='Действие')
    is_pleasant = models.BooleanField(verbose_name='Признак приятной привычки', **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    periodic = models.PositiveSmallIntegerField(verbose_name='Периодичность')
    reward = models.CharField(max_length=120, verbose_name='Вознаграждение')
    execute_time = models.PositiveSmallIntegerField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='Признак публичности', **NULLABLE)