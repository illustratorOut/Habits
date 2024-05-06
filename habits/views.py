from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from habits.forms import HabitsForm
from habits.models import Habits


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Класс создания привычек"""
    model = Habits
    form_class = HabitsForm
    success_url = reverse_lazy('habits:home')

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     if not self.request.user.is_superuser:
    #         # Отключить поле status
    #         form.fields["status"].disabled = True
    #     return form
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     MailingFormset = inlineformset_factory(Mailing, MessageMailing, form=MessageMailingForm, extra=1,
    #                                            can_delete=False)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = MailingFormset(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = MailingFormset(instance=self.object)
    #     return context_data
    #
    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class HabitsListView(ListView):
    """Класс отображения привычек"""
    model = Habits
