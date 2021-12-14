from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
import os
# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]

    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank = True)

    junior = 'junior'
    senior = 'senior'
    user_types = [
        (junior, 'junior'),
        (senior, 'senior'),
    ] 
    user_type = models.CharField(max_length=10, choices=user_types, default=junior) 

    def __str__(self):
        return self.user.username
