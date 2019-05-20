from django.shortcuts import render
from django.views.generic import DetailView
from .models import Reply

# Create your views here.

class PostDetail(DetailView):
    model = Reply

