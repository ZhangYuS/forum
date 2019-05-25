from django.urls import path
from django import forms

from . import views

app_name = 'Post'

urlpatterns = [
    path('', views.PostsList.as_view(), name='Post'),
    path('<int:pk>', views.PostDetail.as_view(), name='PostDetail'),
]