from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitsListView, MailingCreateView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitsListView.as_view(), name='home'),
    path('create', MailingCreateView.as_view(), name='create'),
]
