from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    photo = models.ImageField(upload_to='users', verbose_name='Фотография', **NULLABLE)
    id_telegram = models.CharField(max_length=35, verbose_name='ID телеграм канала', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
