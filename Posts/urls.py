from django.urls import path
from django import forms

from . import views

app_name = 'Posts'

urlpatterns = [
    path('', views.PostsList.as_view(), name='Posts'),
    path('<int:pk>', views.PostDetail.as_view(), name='PostDetail'),
]