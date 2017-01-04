# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161012_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='author_pages', to='common.Person', verbose_name='Author'),
        ),
    ]
