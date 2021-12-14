from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from app_users.models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        labels = {
            'password1' : 'Password',
            'password1' : 'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    juniors = 'juniors'
    seniors = 'seniors'

    user_types = [
        (juniors, 'juniors'),
        (seniors, 'senior')
    ]
    user_types = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = user_profile
        fields = ('profile_pic', 'user_type')
