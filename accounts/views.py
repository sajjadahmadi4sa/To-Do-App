from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import FormView
from .forms import RegisterForm
# Create your views here.


class RegisterView(FormView):

    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/task_list/'

    def form_valid(self, form):
        user = form.save()

        login(self.request, user)

        return super().form_valid(form)