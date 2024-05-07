from django.urls import path

from config.urls import schema_view
from habits.apps import HabitsConfig
from habits.views import HabitsDetailView, HabitsCreateView, HabitsListView, HabitsDeleteView, HabitsUpdateView, \
    HabitsPublicListView

app_name = HabitsConfig.name

urlpatterns = [
    path('public', HabitsPublicListView.as_view()),

    # Habits
    path('', HabitsListView.as_view()),
    path('<int:pk>/', HabitsDetailView.as_view()),
    path('create/', HabitsCreateView.as_view()),
    path('update/<int:pk>/', HabitsUpdateView.as_view()),
    path('delete/<int:pk>/', HabitsDeleteView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
