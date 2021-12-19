from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
import os
# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]

def papath_and_rename(instance, filename):
    upload_to = 'Parent_Agreements/'
    ext = filename.split('.')[-1]

    if instance.user.username:
        filename = 'Profile_pic/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank = True)

    Parent_Agreement = models.FileField(upload_to=papath_and_rename, verbose_name="Parent Agreement", blank = False, default='Upload here')

    Junior = 'Junior: Grade 6-7'
    Senior = 'Senior: Grade 8-12'
    user_types = [
        (Junior, 'Junior: Grade 6-7'),
        (Senior, 'Senior: Grade 8-12'),
    ] 
    user_type = models.CharField(max_length=50, choices=user_types, default=Junior) 
 
    ICT_Junior = 'Junior ICT'
    Math_Junior = 'Junior Mathematics'
    ICT_Senior = 'Senior ICT'
    Math_Senior = 'Senior Mathematics'
    Physics = 'Physics'
    Accounting = 'Accounting'

    Courses = [
        (ICT_Junior,'Junior ICT'),
        (Math_Junior,'Junior Mathematics'),
        (ICT_Senior, 'Senior ICT'),
        (Math_Senior,'Senior Mathematics'),
        (Physics, 'Physics'),
        (Accounting, 'Accounting')

    ]
    Courses = models.CharField(max_length=500, choices=Courses, default='Junior ICT')
    

    def __str__(self):
        return self.user.username

    