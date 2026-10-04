from django.shortcuts import render
from django.views.generic import TemplateView , ListView , CreateView, UpdateView,DeleteView
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateTaskView (LoginRequiredMixin,CreateView):
    template_name = 'index.html'
    form_class = TaskForm
    success_url = '/task_list/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    
class ListTaskView (LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    

class DoneTaskView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['status']
    success_url = '/task_list/'

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = True
        task.save()
        return redirect(self.success_url)
    
class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = '/task_list/'
# Create your views here.
