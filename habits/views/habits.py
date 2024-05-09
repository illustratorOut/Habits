from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from habits.forms import HabitsForm
from habits.models import Habits


class HabitsDetailView(DetailView):
    """Класс просмотра 1 привычки"""
    model = Habits


class HabitsListView(ListView):
    """Класс отображения привычек"""
    model = Habits


class HabitsCreateView(LoginRequiredMixin, CreateView):
    """Класс создания привычек"""
    model = Habits
    form_class = HabitsForm
    success_url = reverse_lazy('habits:home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["related_habit"].queryset = Habits.objects.filter(is_pleasant=True)
        return form

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class HabitsUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования привычек"""
    model = Habits
    form_class = HabitsForm
    success_url = reverse_lazy('habits:home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["related_habit"].queryset = Habits.objects.filter(is_pleasant=True)
        return form


class HabitsDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления привычек"""
    model = Habits
    success_url = reverse_lazy('habits:home')
