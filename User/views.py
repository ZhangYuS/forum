from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, FormView
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy

class MyLoginView(LoginView):
    template_name = 'User/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('Post:Post')



class RegisterView(FormView):
    template_name = 'User/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.create()
        login(self.request, user)
        return redirect(reverse_lazy('Post:Post'))