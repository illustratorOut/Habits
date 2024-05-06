from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    # Авторизации и регистрации
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Token
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
