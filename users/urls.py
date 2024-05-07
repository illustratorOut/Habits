from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserDeleteView, UserUpdateView, UserCreateView, UserDetailView, \
    UserListView

app_name = UsersConfig.name

urlpatterns = [
    # User
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('delete/<int:pk>/', UserDeleteView.as_view()),

    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
