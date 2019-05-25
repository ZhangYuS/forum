from django.views.generic import ListView, DetailView
from .models import Post
from .models import Reply
from django.utils import timezone

class PostsList(ListView):
    model = Post
    template_name = 'Posts/PostsList.html'
    context_object_name = 'postsList'

class PostDetail(DetailView):
    model = Post
    template_name = 'Posts/PostDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replys'] = Reply.objects.filter(postId=self.kwargs['pk'])
        return context
