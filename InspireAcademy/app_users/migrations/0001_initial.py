# Generated by Django 4.0 on 2021-12-17 18:19

import app_users.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture')),
                ('Parent_Agreement', models.FileField(default='Upload here', upload_to=app_users.models.papath_and_rename, verbose_name='Parent Agreement')),
                ('user_type', models.CharField(choices=[('Junior: Grade 6-7', 'Junior: Grade 6-7'), ('Senior: Grade 8-12', 'Senior: Grade 8-12')], default='Junior: Grade 6-7', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
