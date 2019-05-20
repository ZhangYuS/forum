from django.urls import path
from django import forms

from . import views

app_name = 'User'

urlpatterns = [
    path('login', views.MyLoginView.as_view(), name='Login'),
]