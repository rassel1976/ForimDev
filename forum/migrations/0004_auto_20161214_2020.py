# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-14 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20161214_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(verbose_name='Текс Поста'),
        ),
    ]
