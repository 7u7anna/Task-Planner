from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Habits, Task
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'planner/front.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['task_list'] = context['task_list'].filter(user=self.request.user)

        user_input = self.request.GET.get('search-area') or ''
        if user_input:
            context['task_list'] = context['task_list'].filter(title__icontains=user_input)
        return context

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'priority', 'date_due']
    template_name = 'planner/task_create.html'
    success_url = reverse_lazy('front')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'priority', 'date_due']
    context_object_name = 'task'
    template_name = 'planner/task_update.html'
    success_url = reverse_lazy('front')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'planner/task_confirm_delete.html'
    context_object_name = 'task'
    success_url = '/'

# Habits List

class HabitsListView(LoginRequiredMixin, ListView):
    model = Habits
    context_object_name = 'habits_list'
    template_name = 'planner/habits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habits_list'] = context['habits_list'].filter(user=self.request.user)

        user_input = self.request.GET.get('search-area') or ''
        if user_input:
            context['habits_list'] = context['habits_list'].filter(name__icontains=user_input)

        return context 

class HabitCreateView(LoginRequiredMixin, CreateView):
    model = Habits
    context_object_name = 'habit'
    fields = ['habit']
    template_name = 'planner/habit_create.html'
    success_url = reverse_lazy('habits')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HabitDeleteView(DeleteView):
    model = Habits
    context_object_name = 'habit'
    template_name = 'planner/habit_confirm_delete.html'
    success_url = reverse_lazy('habits')

# function based 

def about(request):
    return render(request, 'planner/about.html')




