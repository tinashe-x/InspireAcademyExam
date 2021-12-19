from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from django.forms.widgets import CheckboxInput
from app_users.models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField
    
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

        labels = {
            'password1' : 'Password',
            'password1' : 'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    full_time = 'Registered at School(Full-time)'
    supp_exam = 'Preparing for Supplementary/Deferred Exam'
    neither = 'None'

    Juniors = 'Junior: Grade 6-7'
    Seniors = 'Senior: Grade 8-12'

    Bisho_1 = 'Bisho 1'
    Bisho_2 = 'Bisho 2'
    King_Williams_Town = 'King Williams Town'
    Soweto = 'Soweto'

    ICT_Junior = 'Junior ICT'
    Math_Junior = 'Junior Mathematics'
    ICT_Senior = 'Senior ICT'
    Math_Senior = 'Senior Mathematics'
    Physics = 'Senior Physics'
    Accounting = 'Senior Accounting'
    
    Are_You = [
        (full_time, 'Registered at School(Full-time)'),
        (supp_exam, 'Preparing for Supplementary/Deferred Exam'),
    ]
    Are_You = forms.ChoiceField(required=True, choices=Are_You)
        

    Centers = [
        (Bisho_1, 'Bisho 1'),
        (Bisho_2, 'Bisho 2'),
        (King_Williams_Town, 'King Williams Town'),
        (Soweto, 'Soweto'),
    ]
    Centers = forms.ChoiceField(required=True, choices=Centers)
    

    user_types = [
        (Juniors, 'Junior: Grade 6-7'),
        (Seniors, 'Senior: Grade 8-12')
    ]
    user_types = forms.ChoiceField(required=True, choices=user_types)

    Courses = [
        (ICT_Junior,'Junior ICT'),
        (Math_Junior,'Junior Mathematics'),
        (ICT_Senior, 'Senior ICT'),
        (Math_Senior,'Senior Mathematics'),
        (Physics, 'Senior Physics'),
        (Accounting, 'Senior Accounting')

    ]
    Select_a_Maximum_of_3_Courses_to_Register = forms.MultipleChoiceField(required=True, choices=Courses)

    class Meta():
        model = user_profile
        fields = ('profile_pic','Parent_Agreement')
