# Generated by Django 4.0 on 2021-12-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='Courses',
            field=models.CharField(choices=[('Junior ICT', 'Junior ICT'), ('Junior Mathematics', 'Junior Mathematics'), ('Senior ICT', 'Senior ICT'), ('Senior Mathematics', 'Senior Mathematics'), ('Physics', 'Physics'), ('Accounting', 'Accounting')], default='Junior ICT', max_length=500),
        ),
    ]
