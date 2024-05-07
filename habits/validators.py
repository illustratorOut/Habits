from rest_framework.exceptions import ValidationError

from habits.models import Habits


class ExecuteTimeValidator:
    '''Проверка поля execute_time на пораметр время выполнения должно быть не больше 120 секунд'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        execute_time = value.get('execute_time')

        if 0 == execute_time:
            raise ValidationError('Время выполнения не может равняться нулю')
        elif execute_time >= 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')


class RewardorRelatedHabitValidator:
    ''' '''

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        reward = value.get(self.field1)
        related_habit = value.get(self.field2)

        if reward and related_habit:
            raise ValidationError('Выберите что то одно связанную привычку или вознаграждение.')


class RelatedHabitIsPublicValidator:
    ''' '''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_id = value.get('id')
        habit = Habits.objects.filter(pk=habit_id, is_pleasant=True)
        if not habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class PleasantHabitNotRewardValidator:
    '''Валидатор у (приятной привычки) не может быть вознаграждения или связанной привычки'''

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        is_pleasant = value.get(self.field1)
        reward = value.get(self.field2)

        if is_pleasant and reward:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class PeriodValidator:
    '''Валидатор периодичности выполнения'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = value.get('periodic')

        if period > 7 or period < 1:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
