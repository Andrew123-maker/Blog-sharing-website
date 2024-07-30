# Generated by Django 5.0.2 on 2024-07-29 16:50

import blog.models
import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.user_directory_path)),
                ('follows', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.user_directory_path)),
                ('title', models.CharField(max_length=200)),
                ('text', django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Text')),
                ('published_date', models.DateTimeField(auto_now=True, null=True)),
                ('connect', models.ManyToManyField(blank=True, related_name='posts_group', to='blog.connect')),
                ('liked', models.ManyToManyField(related_name='liked', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(related_name='tag', to='blog.tag')),
            ],
        ),
        migrations.AddField(
            model_name='connect',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='group_posts', to='blog.post'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to=blog.models.user_directory_path)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('follow', models.ManyToManyField(related_name='follow', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='connect',
            name='question',
            field=models.ManyToManyField(default=None, to='blog.question'),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('published_date', models.DateTimeField(auto_now=True, null=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
