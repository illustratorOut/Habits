from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habits
from habits.paginators import CustomPagination
from habits.permissions import IsOwner
from habits.seriallizers.habits import HabitsCreateSerializer, HabitsSerializer


class HabitsPublicListView(ListAPIView):
    '''Отображение списка привычек'''
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitsSerializer
    permission_classes = [AllowAny]


class HabitsDetailView(RetrieveAPIView):
    '''Отображение привычки'''
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsListView(ListAPIView):
    '''Отображение списка привычек'''
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class HabitsCreateView(CreateAPIView):
    '''Создание привычки'''
    queryset = Habits.objects.all()
    serializer_class = HabitsCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''При создании привычки присваиваем автора(user)'''
        habits_ = serializer.save()
        habits_.user = self.request.user
        habits_.save()


class HabitsUpdateView(UpdateAPIView):
    '''Редактирование (обновление) привычки'''
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner, IsOwner]


class HabitsDeleteView(DestroyAPIView):
    '''Удаление сущности'''
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]
