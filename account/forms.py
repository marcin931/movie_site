from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate

from .models import User



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', "password")



class LoginForm(forms.Form):
        email = forms.EmailField()
        password = forms.CharField(widget = forms.PasswordInput())


