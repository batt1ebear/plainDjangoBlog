# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2020-01-11 06:55
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191021_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
