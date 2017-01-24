from django.forms import ModelForm
from django import forms

from forum.models import Comment, Post, Avatar


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_text','post_name']
