from django.contrib.auth.forms import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name=forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
