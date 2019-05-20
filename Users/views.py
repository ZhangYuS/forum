from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, FormView

class MyLoginView(LoginView):
    template_name = 'User/login.html'
