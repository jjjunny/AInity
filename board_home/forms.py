# board_home/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('student_id', 'name', 'password1', 'password2', 'role')  # role 포함


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
