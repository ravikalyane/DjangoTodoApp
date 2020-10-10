from django import forms
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddTask(forms.ModelForm):
    name = forms.CharField(label='', max_length=200,
                           widget=forms.TextInput(attrs={'placeholder': 'Add a new task & press enter.'}))

    class Meta:
        model = Task
        exclude = ('author',)
        fields = "__all__"


class RegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'username', 'email', 'password1', 'password2'
