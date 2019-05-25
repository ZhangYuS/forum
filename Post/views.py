from django.views.generic import ListView, DetailView, FormView
from .models import Post, Reply
from User.models import User
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy

class PostsList(ListView, FormView):
    model = Post
    template_name = 'Posts/PostsList.html'
    context_object_name = 'postsList'
    form_class = PostForm
    pk = 0

    def form_valid(self, form):
        pk = form.create()
        return redirect(reverse_lazy('Post:PostDetail', kwargs={'pk':pk}))


class PostDetail(DetailView):
    model = Post
    template_name = 'Posts/PostDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replys'] = Reply.objects.filter(postId=self.kwargs['pk'])
        return context
