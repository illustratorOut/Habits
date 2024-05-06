import datetime

from django import forms

from habits.models import Habits
from users.forms import StyleFormMixin


class HabitsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Habits
        # fields = '__all__'
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
                    'max': 120,
                    'value': 120,
                }
            )

        }
