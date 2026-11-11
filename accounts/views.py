from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import FormView
from .forms import RegisterForm
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,)
# Create your views here.


class RegisterView(FormView):

    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = '/task_list/'

    def form_valid(self, form):
        user = form.save()

        login(self.request, user)

        return super().form_valid(form)


class CustomTokenObtainPairView(TokenObtainPairView):
    pass


class CustomTokenRefreshView(TokenRefreshView):
    pass


class CustomTokenVerifyView(TokenVerifyView):
    pass