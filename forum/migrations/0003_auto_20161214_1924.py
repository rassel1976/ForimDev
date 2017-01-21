# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-14 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20161214_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_name',
            field=models.CharField(max_length=255, verbose_name='Название поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(verbose_name='Текст комментария'),
        ),
    ]