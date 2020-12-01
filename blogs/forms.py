from .models import Comments, Post

from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'text']
