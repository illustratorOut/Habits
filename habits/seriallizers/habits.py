from rest_framework import serializers

from habits.models import Habits
from habits.validators import ExecuteTimeValidator, RewardorRelatedHabitValidator, RelatedHabitIsPublicValidator, \
    PeriodValidator, PleasantHabitNotRewardValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        # fields = '__all__'
        exclude = ('user',)


class HabitsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'
        validators = [
            ExecuteTimeValidator(field='execute_time'),
            RewardorRelatedHabitValidator(field1='reward', field2='related_habit'),
            RelatedHabitIsPublicValidator(field='related_habit'),
            PleasantHabitNotRewardValidator(field1='is_pleasant', field2='reward'),
            PeriodValidator(field='periodic'),
        ]
