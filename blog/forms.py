from django import forms
from django.forms import ModelForm
from blog.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created_on']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
