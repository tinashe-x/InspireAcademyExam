# Generated by Django 4.0 on 2021-12-14 14:25

import curriculum.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=curriculum.models.save_subject_image, verbose_name='Subject Image')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='curriculum.standard')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Chapter no.')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=curriculum.models.save_lesson_files, verbose_name='video')),
                ('ppt', models.FileField(blank=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Presentation')),
                ('Notes', models.FileField(blank=True, upload_to=curriculum.models.save_lesson_files, verbose_name='Notes')),
                ('Standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='curriculum.subject')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
