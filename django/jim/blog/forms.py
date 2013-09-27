from django.forms import ModelForm
from blog.models import Post, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text','email','name','post_id')