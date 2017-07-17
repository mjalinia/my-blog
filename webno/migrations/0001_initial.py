# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-03 20:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='post title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='post content')),
                ('createtime', models.DateTimeField(auto_now=True, verbose_name='createtime')),
                ('updatetime', models.DateTimeField(auto_now_add=True, verbose_name='updatetime')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'verbose_name': 'Post',
            },
        ),
    ]
