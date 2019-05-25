from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'content']

    def create(self):
        instance = self.save(commit=False)
        instance.author_id = 1
        instance.save()

        return instance.pk
