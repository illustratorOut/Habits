from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.seriallizers.user import UserSerializer, UserDetailSerializer, UserCreateSerializer


class RegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    """Профиль пользователя"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


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
