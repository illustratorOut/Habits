from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.seriallizers.user import UserSerializer, UserDetailSerializer, UserCreateSerializer


class UserDetailView(RetrieveAPIView):
    '''Отображение однго пользователя'''
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]


class UserListView(ListAPIView):
    '''Отображение списка пользователей'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(CreateAPIView):
    '''Создание пользователя'''
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserUpdateView(UpdateAPIView):
    '''Редактирование пользователя'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDeleteView(DestroyAPIView):
    '''Удаление пользователя'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
