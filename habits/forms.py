import datetime

from django import forms
from django.core.exceptions import ValidationError

from habits.models import Habits
from users.forms import StyleFormMixin


class HabitsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Habits
        exclude = ('user',)

        widgets = {
            'time': forms.TimeInput(
                format='%H:%M:%S',
                attrs={
                    'type': 'time',
                    'value': datetime.datetime.today().strftime('%H:%M'),
                }),

            'is_public': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'type': 'checkbox',
                    'id': 'flexSwitchCheckDefault',
                }),

            'execute_time': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 120,
                    'value': 120,
                }),

            'periodic': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 7,
                    'value': 7,
                }
            )

        }

    def clean_execute_time(self):
        execute_time = super().clean().get('execute_time')

        if execute_time is not None:
            if execute_time <= 0 or execute_time > 120:
                raise ValidationError('Время на выполнение не может равняться нулю и не должно привышать 120 секунд')
            return execute_time

    def clean_periodic(self):
        periodic = super().clean().get('periodic')

        if periodic is not None:
            if periodic > 7 or periodic < 1:
                raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
            return periodic

    def clean(self):
        cleaned_data = super().clean()
        is_pleasant = cleaned_data.get('is_pleasant')
        reward = cleaned_data.get('reward')
        related_habit = cleaned_data.get('related_habit')

        if is_pleasant is not None or reward is not None:
            if is_pleasant is not None or reward is not None:
                if is_pleasant and reward:
                    raise ValidationError(
                        'С признаком приятной привычки выберите что-то одно вознаграждение или связанную привычку')

        if reward is not None or related_habit is not None:
            if reward and related_habit:
                raise ValidationError('Выберите что то одно связанную привычку или вознаграждение.')
