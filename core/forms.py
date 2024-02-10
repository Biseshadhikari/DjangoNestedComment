from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment



class LoginForm(AuthenticationForm):
    class Meta:
        fields = '__all__'

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
