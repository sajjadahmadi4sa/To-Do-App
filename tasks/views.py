from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import TaskForm


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'index.html'
    form_class = TaskForm
    success_url = '/task_list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListTaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class DoneTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['status']
    success_url = '/task_list/'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = True
        task.save()
        return redirect(self.success_url)


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/task_list/'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)