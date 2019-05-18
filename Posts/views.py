from django.views.generic import ListView
from .models import Posts

class PostsList(ListView):
    model = Posts
    template_name = 'Posts/Posts.html'
    context_object_name = 'postsList'