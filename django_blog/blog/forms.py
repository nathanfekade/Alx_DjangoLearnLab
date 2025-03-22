from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagField
from taggit.managers import TaggableManager

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit = True):
        user = super().save(commit= False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    tags = TagField(required=False, help_text="Enter tags separated by commas (e.g., tech, python, blog)")
    class Meta:
        model = Post
        fields = ['title', 'content']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Write your comment here' }),
        }
    
