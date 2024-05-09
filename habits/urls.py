from django.urls import path

from config.urls import schema_view
from habits.apps import HabitsConfig
from habits.views.habits import HabitsListView, HabitsCreateView, HabitsDeleteView, HabitsUpdateView, HabitsDetailView
from habits.views.API_habits import HabitsListAPIView, HabitsDetailAPIView, HabitsCreateAPIView, HabitsUpdateAPIView, \
    HabitsDeleteAPIView, HabitsPublicListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    # CRUD Habits
    path('', HabitsListView.as_view(), name='home'),
    path('view/<int:pk>', HabitsDetailView.as_view(), name='view'),
    path('create/', HabitsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', HabitsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', HabitsDeleteView.as_view(), name='delete'),

    # API Habits
    path('API/public/', HabitsPublicListAPIView.as_view()),
    path('API/', HabitsListAPIView.as_view()),
    path('API/<int:pk>/', HabitsDetailAPIView.as_view()),
    path('API/create/', HabitsCreateAPIView.as_view()),
    path('API/update/<int:pk>/', HabitsUpdateAPIView.as_view()),
    path('API/delete/<int:pk>/', HabitsDeleteAPIView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
